from pygraphviz import AGraph
import base64
import tempfile
from simpleai.search import SearchProblem


class BadInputGraph(Exception):
    pass


class DotGraphSearchProblem(SearchProblem):
    """
    Playground for stuff in the library... eats a .dot graph and allows you
    to try it with the search methods.
    """
    def __init__(self, filename):
        self.G = AGraph(filename)
        xs = [(nodo, nodo.attr.get("estado_inicial", None))
              for nodo in self.G.iternodes()]
        xs = [x for x in xs if x[1]]
        if len(xs) == 0:
            raise BadInputGraph("Missing 'estado_inicial' node")
        elif len(xs) > 1:
            raise BadInputGraph("Cannot have two estado_inicial nodes")
        if not any(nodo.attr.get("estado_objetivo", None) for nodo in self.G.iternodes()):
            raise BadInputGraph("Missing a estado_objetivo estado '[estado_objetivo=\"1\"]'")
        super(DotGraphSearchProblem, self).__init__(xs[0][0])
        self.initial_state.attr["shape"] = "doublecircle"
        for node in self.G.iternodes():
            if self.es_objetivo(node):
                node.attr["shape"] = "hexagon"
                node.attr["color"] = "blue"
        self.seen = set()
        self.visit(self.initial_state)
        for edge in self.G.iteredges():
            edge.attr["style"] = "dotted"
            x = edge.attr.get("weight", None)
            if x:
                x = int(x)
            else:
                x = 1
            edge.attr["weight"] = x
            edge.attr["label"] = x

    def acciones(self, estado):
        assert estado in self.G
        if self.G.is_directed():
            return self.G.itersucc(estado)
        else:
            assert self.G.is_undirected()
            return self.G.iterneighbors(estado)

    def resultado(self, estado, accion):
        assert estado in self.G and accion in self.G
        self.visit(estado)
        return accion

    def costo(self, state1, accion, state2):
        assert state1 in self.G and accion in self.G and accion == state2
        x = self.G.get_edge(state1, state2).attr["weight"]
        if float(x) == int(x):
            return int(x)
        else:
            return float(x)

    def visit(self, estado):
        if estado in self.seen:
            return
        self.seen.add(estado)
        attr = self.G.get_node(estado).attr
        attr["color"] = "firebrick"

    def es_objetivo(self, estado):
        return bool(estado.attr.get("estado_objetivo", False))

    def value(self, estado):
        assert estado in self.G
        value = self.G.get_node(estado).attr.get("value", None)
        if not value:
            return 0
        return float(value)


def run_algorithm(algorithm, filename):
    problem = DotGraphSearchProblem(filename)
    estado_objetivo = algorithm(problem)
    if estado_objetivo:
        problem.visit(estado_objetivo.estado)
        prev = None
        for _, estado in estado_objetivo.path():
            if prev:
                edge = problem.G.get_edge(prev, estado)
                edge.attr["style"] = "solid"
            prev = estado
        return problem.G, estado_objetivo.estado, estado_objetivo.costo, problem.value(estado_objetivo.estado), \
               len(problem.seen)
    return problem.G, None, None, None, len(problem.seen)


HTML_TEMPLATE = """
<html><body>
<table style="border:0" align="center">
    <tr><td colspan="2"><h2 style="text-align: center">{graph}</h2></td></tr>
    <tr><td colspan="2"><hr /></td></tr>
    {rows}
</table>
</body></html>
"""

RUN_TEMPLATE = """
<tr>
    <td>
      <b style="text-align: center"> {algorithm} </b> <br /> <br />
      Nodes expanded(or 'visited') = {visited}
      <br /> Path costo = {costo}
      <br /> Final node value = {value} </td>
    {image_column}
</tr>
<tr>
    <td colspan="2"><hr /></td>
</tr>
"""

IMAGE_TEMPLATE = """<td style="padding-left: 50px">
<img src="data:image/png;base64,{image}" /> </td>"""

#
#  Credits to Gonzalo Garcia Berrotaran (j0hn) for the clever way of putting
#  this into HTML.
#


def report(infile=None, algorithms=None, outfile="report.html",
           with_images=True):
    assert infile and algorithms
    rows = []
    for algorithm in algorithms:
        G, estado_objetivo, costo, value, visited = run_algorithm(algorithm, infile)
        image = ""
        if with_images:
            out = tempfile.NamedTemporaryFile(delete=False)
            G.draw(out, format="png", prog="dot")
            out.seek(0)
            image = base64.b64encode(out.read())
            out.close()
            image = IMAGE_TEMPLATE.format(image=image)
        s = RUN_TEMPLATE.format(algorithm=algorithm.__name__,
                                visited=visited, costo=costo, value=value,
                                image_column=image, )
        rows.append(s)
    s = HTML_TEMPLATE.format(graph=infile, rows="".join(rows))
    open(outfile, "w").write(s)
