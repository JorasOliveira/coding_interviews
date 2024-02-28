from Node import Node

def find_intersection(head1: Node, head2: Node) -> Node:

    if (head1 is None) or (head2 is None):
        return None
    
    while head1 is not None and head2 is not None:
        if head1 == head2:
            return head2
        head1 = head1.next
        head2 = head2.next

    return None
