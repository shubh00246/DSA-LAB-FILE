class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    
    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        print("Circular Linked List:", end=" ")
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

        print(f"\nAfter inserting {data} at the beginning:")
        self.display()

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

        print(f"\nAfter inserting {data} at the end:")
        self.display()


if __name__ == "__main__":
    cll = CircularLinkedList()

    cll.insert_at_end(10)
    cll.insert_at_end(20)
    cll.insert_at_beginning(5)
    cll.insert_at_end(30)
    cll.insert_at_beginning(2)
