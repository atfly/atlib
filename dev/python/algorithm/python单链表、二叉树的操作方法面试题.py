
class Node:
    """Base Node type"""
    Value = None

    def __init__(self, value):
        self.Value = value

    def __str__(self):
        return "Value = %s" % self.Value


class Snode(Node):
    """Node type in a singly link"""
    Next = None


class Tnode(Node):
    """Node type in a binary tree"""
    Lchild = None
    Rchild = None

    def __str__(self):
        return str(self.Value)

def sprint(head):
    """Print the Singly link consist by Snode instance"""
    while head != None:
        print(head)
        head = head.Next

def Reverse(head):
    """Reverse a single list"""
    newHead = None
    while head != None:
        temp = head
        head = head.next
        temp.next = newHead
        newHead = temp
    return newHead

def createSinglyLink(start, end):
    """Create a singly link, start from 'start', end with 'end'"""
    head = p = Snode(start)
    for i in range(start + 1, end):
        p.Next = Snode(i)
        p = p.Next
    return head

def InOrderTraverse(head):
    """Inorder to traverse a binary tree"""
    p = head
    stack = []
    while p != None or len(stack) > 0:
        if p != None:
            stack.append(p)
            p = p.Lchild
        else:
            p = stack.pop()
            print(p)
            p = p.Rchild

def PreOrderTraverse(head):
    """Preorder to traverse a binary tree"""
    p = head
    stack = []
    while p != None or len(stack) > 0:
        if p != None:
            print(p)
            stack.append(p)
            p = p.Lchild
        else:
            p = stack.pop()
            p = p.Rchild

def PostOrderTraverse(head):
    """Postorder to traverse a binary tree"""
    p = head
    stack = []
    while p != None or len(stack) > 0:
        if p != None:
            stack.append(p)
            p = p.Lchild
        else:
            while len(stack) > 0 and p == stack[-1].Rchild:
                p = stack.pop()
                print(p)
            if len(stack) > 0:
                p = stack[-1].Rchild
            else:
                p = None   

def LevelTraverse(head):
    """Level traverse a binary tree"""
    stack = [head]
    while len(stack) > 0:
        p = stack.pop(0)
        print(p)
        if p.Lchild != None:
            stack.append(p.Lchild)
        if p.Rchild != None:
            stack.append(p.Rchild)
            
def CreateBinaryTree():
    head = Tnode("-")
    head.Lchild = Tnode("+")
    head.Lchild.Lchild = Tnode("a")
    head.Lchild.Rchild = Tnode("*")
    head.Lchild.Rchild.Lchild = Tnode("b")
    head.Lchild.Rchild.Rchild = Tnode("-")
    head.Lchild.Rchild.Rchild.Lchild = Tnode("c")
    head.Lchild.Rchild.Rchild.Rchild = Tnode("d")
    head.Rchild = Tnode("/")
    head.Rchild.Lchild = Tnode("e")
    head.Rchild.Rchild = Tnode("f")
    return head

def CreateTree():
    head = Tnode(1)
    head.Lchild = Tnode(2)
    head.Rchild = Tnode(3)
    head.Lchild.Lchild = Tnode(4)
    head.Lchild.Rchild = Tnode(5)
    head.Rchild.Lchild = Tnode(6)
    head.Rchild.Rchild = Tnode(7)
    head.Lchild.Lchild.Lchild = Tnode(8)
    head.Lchild.Lchild.Rchild = Tnode(9)
    head.Rchild.Lchild.Lchild = Tnode(10)
    head.Rchild.Lchild.Rchild = Tnode(11)
    return head
    
if __name__ == '__main__':
    head = CreateTree()
    print('Pre traverse:')
    PreOrderTraverse(head)
    print('InOrderTraverse:')
    InOrderTraverse(head)
    print('Post Order Tranverse')
    PostOrderTraverse(head)
    print('level traverse:')
    LevelTraverse(head)