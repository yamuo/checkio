import numpy as np

class Friends:
    def __init__(self, connections):
        print(connections)
        self.connections = connections

    def add(self, connection):
        connections_list = list(self.connections)
        if connection not in connections_list :
            connections_list.append(connection)
            self.connections = tuple(connections_list)
            return True
        return False
                
    def remove(self, connection):
        connections_list = list(self.connections)
        if connection in connections_list :
            connections_list.remove(connection)
            self.connections = tuple(connections_list)
            return True
        return False

    def names(self):
        ret = set()
        for i in self.connections:
            ret = ret.union(i)
        return ret

    def connected(self, name):
        ret = set()
        for i in self.connections:
            if {name} <= i :
                ret = ret.union(i - {name})
        return ret


f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))
print(f.connected("nikola"))

"""
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
"""