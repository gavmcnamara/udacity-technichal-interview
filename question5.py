# Find the element in a singly linked list that's m elements
# from the end. For example, if a linked list has 5 elements,
# the 3rd element from the end is the 3rd element.
# The function definition should look like question5(ll, m),
# where ll is the first node of a linked list and m is the
# "mth number from the end". You should copy/paste the Node
# class below to use as a representation of a node in the
# linked list. Return the value of the node at that position.

# An Element has some value associated with it (which could
# be anything—a number, a string, a character, et cetera),
# and it has a variable that points to the next element
# in the linked list.
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def append(self, new_element):
        current = self.head
        # If the LinkedList already has a head, iterate through
        # the next reference in every Element until you reach
        # the end of the list.
        if self.head:
            while current.next:
                current = current.next
            #Set next for the end of the list to be the new_element
            current.next = new_element
        else:
            # if there is no head already, you should just assign
            # new_element to it and do nothing else.
            self.head = new_element