from typing import Optional
list1=[1,2,4]
list2=[1,3,4]
list3=list1+list2

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node11 = ListNode(val=1)
node12 = ListNode(val=2)
node13 = ListNode(val=4)

node21 = ListNode(val=1)
node22 = ListNode(val=3)
node23 = ListNode(val=4)

node11.next = node12
node12.next = node13

node21.next = node22
node22.next = node23
    
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

    def compareAndCreate (node1:Optional[ListNode], node2:Optional[ListNode]):
        node = None
        if not node1 and not node2:
            return node

        if not node1 and node2:
            node = node2
            next = compareAndCreate(None, node2.next)
        elif not node2 and node1:
            node = node1
            next = compareAndCreate(node1.next, None)
        elif (node1.val <= node2.val):
            node = node1
            next = compareAndCreate(node1.next, node2)
        else:
            node = node2
            next = compareAndCreate(node1, node2.next)

        node.next = next

        return node
    return compareAndCreate(list1, list2)

head = mergeTwoLists(node11, node21)

print ('Result')

while (head.next):
    print(head.val)
    head = head.next
print(head.val)