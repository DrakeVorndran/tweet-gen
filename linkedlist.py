#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.len = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(1) length is a property on the object that is updated every time the length is changed"""
        # TODO: Loop through all nodes and count one for each
        return self.len

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) all constant time opperations"""
        self.len += 1
        node = Node(item) 
        if not self.head :
            self.head = node
        if self.tail :
            self.tail.next = node
        self.tail = node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) All constant time opperations"""
        
        self.len += 1
        node = Node(item)
        if self.head :
            node.next = self.head
        if not self.tail :
            self.tail = node
        self.head = node
        

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) when node is first node?
        Worst case running time: O(n) when node is not in list
        Where n is the number of items in the list"""
        node = self.head
        while node: # O(n) step through every element of the list
            if(quality(node.data)):
                return node.data # can end before end of list
            node = node.next
        return None # nothing satisfied quality

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) element to delete is the first element?
        Worst case running time: O(n) element is either not in the list or the last element
        where n is the number of nodes in the list"""
        node = self.head
        last = None
        looking = True
        while looking: # O(n) step through every element, can end early
            if node is None:
                raise ValueError('Item not found: {}'.format(item))
            if(item == node.data):
                looking = False
            else:
                last = node
                node = node.next
        self.len -= 1
        if node.next is None:
            if(last):
                self.tail = last
            else:
                self.tail = None
        if(last):
            last.next = node.next
            
        else:
            self.head = node.next


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.prepend(item)
        print('list: {}'.format(ll))
    # for item in ['D', 'E', 'F']:
    #     print('append({!r})'.format(item))
    #     ll.append(item)
    #     print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))
    print(ll.find(lambda item: item == 'B'))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
