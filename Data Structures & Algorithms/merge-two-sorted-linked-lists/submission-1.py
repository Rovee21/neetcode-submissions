# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #1->2->4
        #1->3->5
        #0->1->1->2->3->4->5->None
        tracker = ListNode()
        dummy = tracker
        while(list1 and list2):
            if(list1.val < list2.val):
                tracker.next = list1
                list1 = list1.next
            else:
                tracker.next = list2
                list2 = list2.next
            tracker = tracker.next
        if(list1):
            tracker.next = list1
        if(list2):
            tracker.next = list2
        
        return dummy.next

        