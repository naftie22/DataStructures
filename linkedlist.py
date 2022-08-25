class Node:
    def __init__(self, content):
        self.content = content
        self.succ = None

class List:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def is_empty(self):
        match self.head:
            case None: return True
            case _: return False

    def add_head(self, data):
        node = Node(data)
        match self.head:
            case None: self.head = node; self.length += 1
            case _:
                node.succ = self.head
                self.head = node
                self.length += 1
    
    def append(self, data):
        match self.head:
            case None: self.add_head(data); self.length += 1
            case _:
                node = Node(data)
                current = self.head
                while current.succ is not None:
                    current = current.succ
                current.succ = node
                self.length += 1

    def print_it(self):
        match self.head:
            case None: pass
            case _:
                current = self.head
                while current is not None:
                    print(current.content, end=' ')
                    current = current.succ

    def print_rec(self):
        def prnt(head):
            match head:
                case None: pass
                case _:
                    print(head.content, end= ' ')  
                    prnt(head.succ)
                    
                    
        prnt(self.head)

    def length_it(self):
        match self.head:
            case None: return 0
            case _:
                count = 0
                current = self.head
                while current is not None:
                    count += 1
                    current = current.succ
                return count
    
    def length_rec(self):
        def len(head):
            match head:
                case None: return 0
                case _: return 1 + len(head.succ)
        return len(self.head)

    def __str__(self):
        match self.head:
            case None: return '[]'
            case _:
                rep = '['
                current = self.head
                while current.succ is not None:
                    rep += f'{current.content}, '
                    current = current.succ
                rep += f'{current.content}'
                rep += ']'
                return rep
    
    def __len__(self):
        return self.length_it()

    def insert_at(self, index, data):
        if 0 <= index <= len(self):
            node = Node(data)
            if index == 0:
                self.add_head(data)
                self.length += 1
            else:
                counter = 0
                current = self.head
                while counter < index - 1:
                    current = current.succ
                    counter += 1
                node.succ = current.succ
                current.succ = node
                self.length += 1

    def get_at(self, index):
        match self.head:
            case None: pass
            case _: 
                if 0 <= index <= len(self):
                    count = 0
                    current = self.head
                    while count != index:
                        count += 1
                        current = current.succ
                    return current.content

    def __getitem__(self, index):
        return self.get_at(index)

    def __setitem__(self, index, data):
        self.insert_at(index, data)

    def length_const(self):
        return self.length

    def search_it(self, key):
        current = self.head
        while current is not None:
            if current.content == key:
                return True
            current = current.succ
        return False

    def search_rec(self, key):
        def inner(head):
            match head:
                case None: return False
                case _: return head.content == key or inner(head.succ)
        return inner(self.head)



