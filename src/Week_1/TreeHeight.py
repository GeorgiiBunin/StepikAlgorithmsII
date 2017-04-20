import sys
sys.setrecursionlimit(50000)
class Tree():
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def get_tree(self):
        return self.__graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def get_children(self, vertex):
        return list(self.__graph_dict[vertex])

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_child(self, vertex, child):
        self.add_vertex(vertex)
        self.__graph_dict[vertex].append(child)
        self.add_vertex(child)


def Height(tr, r):
    global heights
    height = 1
    for child in tr.get_children(r):
        if child not in heights:
            height = max(height, 1 + Height(tr, child))
            heights[child]=[]
            heights[child].append(height)
        else:
            height = heights[child]
    return height


n = int(input())
tree_list = [int(x) for x in (input().split())]
tree = Tree()
heights = {}
for i in range(n):
    if tree_list[i] == -1:
        tree.add_child('root', i)
    else:
        tree.add_child(tree_list[i], i)

print(Height(tree, tree.get_children('root')[0]))

# print(tree.get_children(4))
