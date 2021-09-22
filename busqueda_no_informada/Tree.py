class Node:
    def __init__(self, data, child=None):
        self.data = data
        self.child = None
        self.fathr = None
        self.cost = None
        self.set_child(child)

    def set_child(self, child):
        self.child = child
        if self.child is not None:
            for ch in self.child:
                ch.fathr = self

    def get_child(self):
        return self.child

    def get_fathr(self):
        return self.fathr

    def set_fathr(self, fathr):
        self.fathr = fathr

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_cost(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost

    def equal(self, node):
        if self.get_data() == node.get_data():
            return True
        else:
            return False

    def on_list(self, node_list):
        listed = False
        for n in node_list:
            if self.equal(n):
                listed = True
        return listed

    def __str__(self):
        return str(self.get_data())
