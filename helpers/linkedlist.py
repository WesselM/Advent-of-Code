from importlib.machinery import FrozenImporter


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")

        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def get_length(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next

        return count

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.data == target_node_data:
            return self.add_first(new_node)
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)


def main():
    llist = LinkedList(["a", "b", "c", "d"])
    print("Create new list LinkedList(['a', 'b', 'c', 'd'])\n", llist)

    llist.add_first(Node("0"))
    llist.add_last(Node("e"))
    print("\nadd_first(Node('0')) and add_last(Node('e'))\n", llist)

    llist.add_after("a", Node("f"))
    llist.add_before("c", Node("g"))
    print("\nadd_after('a', Node('f')) and add_before('c', Node('g'))\n", llist)

    llist.remove_node("d")
    print("\nremove_node('d')\n", llist)

    print("\nllist.get_length()\n", llist.get_length())

    print("\nIterate over LinkedList")
    for node in llist:
        print(node, "is connected to", node.next)

if __name__ == "__main__":
    main()
