# Find the element in a singly linked list that's m elements
# from the end. For example, if a linked list has 5 elements,
# the 3rd element from the end is the 3rd element.
# The function definition should look like question5(ll, m),
# where ll is the first node of a linked list and m is the
# "mth number from the end". You should copy/paste the Node
# class below to use as a representation of a node in the
# linked list. Return the value of the node at that position.

# An Element has some value associated with it
# and it has a variable that points to the next element
# in the linked list.
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

# This function is in LinkedList class. It inserts
    # a new node at the beginning of Linked List.
    def push(self, new_data):

        # 1 & 2: Allocate the Element &
        #     Put in the data
        new_node = Element(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    def question5(ll, m):
        current = ll.head
        count = 0

        while (current):
            if (count == m):
                return current.value
            count += 1
            current = current.next
        assert(false)
        return 0;


# Code execution starts here
if __name__=='__main__':

    llist = LinkedList()

    # Use push() to construct below list
    # 1->12->1->4->1
    llist.push(1);
    llist.push(4);
    llist.push(1);
    llist.push(12);
    llist.push(1);

    n = 3
    print ("Element at index 3 is :", llist.question5(n))


# Time Complexity: O(n)