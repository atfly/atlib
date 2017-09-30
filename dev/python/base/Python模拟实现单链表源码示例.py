
#coding:utf-8

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class NodeList(object):
    def __init__(self, node):
        self.head = node
        self.head.next = None
        self.end = self.head

    def add_node(self, node):
        self.end.next = node
        self.end = self.end.next

    def length(self):
        node = self.head
        count = 1
        while node.next is not None:
            count += 1
            node = node.next
        return count

    # delete node and return it's value
    def delete_node(self, index):
        if index+1 > self.length():
            raise IndexError('index out of bounds')
        i = 0

        node = self.head

        while True:
            if i==index-1:
                break
            node = node.next
            i += 1

        tmp_node = node.next

        node.next = node.next.next

        return tmp_node.data

    def show(self):
        node = self.head
        node_str = ''

        while node is not None:
            if node.next is not None:
                node_str += str(node.data) + '->'
            else:
                node_str += str(node.data)
            node = node.next

        print node_str

    # Modify the original position value and return the old value
    def change(self, index, data):
        if index+1 > self.length():
            raise IndexError('index out of bounds')
        i = 0
        node = self.head

        while True:
            if i == index:
                break
            node = node.next
            i += 1
        tmp_data = node.data

        node.data = data

        return tmp_data

    # To find the location of index value

    def find(self, index):
        if index+1 > self.length():
            raise IndexError('index out of bounds')
        i = 0

        node = self.head

        while True:
            if i == index:
                break
            node = node.next
            i += 1

        return node.data

#www.iplaypy.com
#test case
n1 = Node(0)
n2 = Node(1)
n3 = Node(2)
n4 = Node(3)
n5 = Node(4)
node_list = NodeList(n1)
node_list.add_node(n2)
node_list.add_node(n3)
node_list.add_node(n4)
node_list.add_node(n5)
#node = node_list.delete_node(3)
#print node
#d = node_list.change(0,88)
data = node_list.find(5)
print data
node_list.show()
