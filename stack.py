
class Node:
    def __init__ (self,content):
        self.content = content
        self.next = None

class Client():
    def __init__(self):
        self.tail = None
        self.length = 0

    def is_empty(self):
        return self.tail == None

    def push(self, content):
        node = Node(content)
        match self.tail:
            case None:
                self.tail = node
                self.length += 1
            case _:
                node.next = self.tail
                self.tail = node
                self.length += 1

    def peek(self):
        match self.tail:
            case None: raise Exception()
            case _: return self.tail.content

    def pop(self):
        match self.tail:
            case None: raise Exception()
            case _:
                data = self.tail.content
                self.tail = self.tail.next
                self.length -= 1
                return data

    def count(self):
        return self.length




        

