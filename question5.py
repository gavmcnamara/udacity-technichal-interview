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
    def push(self, new_value):
        new_node = Element(new_value)
        new_node.next = self.head
        self.head = new_node

    def question5(ll, m):

        current = ll.head
        count = 0

        while (current):
            if (count == m):
                return current.value
            count += 1
            current = current.next
        return None
        return 0;

# Since the push function adds a node to the
# beginning of the ll, then thechnically the first node
# that is inserted will be the last in the length of ll

# Execution of the code
# Should return 67 as its value
if __name__=='__main__':

    ll = LinkedList()

    # Push function to add nodes
    # 5->67->3->123->6
    ll.push(5);
    ll.push(67);
    ll.push(3);
    ll.push(123);
    ll.push(6);

    m = 3
    print ("Element at index 2 is :", ll.question5(m))

# Should return 21323353 as its value
if __name__=='__main__':

    ll = LinkedList()

    # Push function to add nodes
    # 5->67->3->123->6
    ll.push(21323353);
    ll.push(21356456);
    ll.push(06453436);
    ll.push(12314325);
    ll.push(63253534);

    m = 4
    print ("Element at index 4 is :", ll.question5(m))

# This will check for a value below the length
# of ll and should return None as its value
if __name__=='__main__':

    ll = LinkedList()

    # Push function to add nodes
    # 5->67->3->123->6
    ll.push(0);
    ll.push(14);
    ll.push(345);
    ll.push(12546);
    ll.push(6325353);

    m = -1
    print ("Element at index -1 is :", ll.question5(m))

# This will check for a value above the length
# of ll and should return None as its value
if __name__=='__main__':

    ll = LinkedList()

    # Push function to add nodes
    # 5->67->3->123->6
    ll.push(0);
    ll.push(14);
    ll.push(345);
    ll.push(12546);
    ll.push(6325353);

    m = 10
    print ("Element at index 10 is :", ll.question5(m))
# Time Complexity: O(n) because it visits all the nodes
# then finds the node at position m

# Code Design: This algorithm initializes count = 0 and then
# loops through the link listand if count is equal to
# m then it will return the current node and increment
# the count. Then will change the current point
# to the next current.