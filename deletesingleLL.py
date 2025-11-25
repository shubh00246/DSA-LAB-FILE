
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class SinglyLinkedList:
    def __init__(self):
        self.head = None

   
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node


    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        print(f"Deleting node from beginning: {self.head.data}")
        self.head = self.head.next

    def delete_from_end(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        if self.head.next is None:
            print(f"Deleting node from end: {self.head.data}")
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next
        print(f"Deleting node from end: {temp.next.data}")
        temp.next = None


    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")



if __name__ == "__main__":
    llist = SinglyLinkedList()
    llist.insert(10)
    llist.insert(20)
    llist.insert(30)
    llist.insert(40)

    print("Original List:")
    llist.display()

    llist.delete_from_beginning()
    llist.display()

    llist.delete_from_end()
    llist.display()
