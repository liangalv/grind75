# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = ListNode()
        if not list1 or not list2:
            return list1 if list1 else list2 if list2 else None
        head, prior_node = merged_list, merged_list
        while list1 and list2:
            #case1: when list1 has smaller value
            if list1.val <= list2.val:
                #set and generate next ListNode
                merged_list.val = list1.val
                list1 = list1.next
            else:
                merged_list.val = list2.val
                list2 = list2.next
            prior_node = merged_list
            merged_list.next = ListNode()
            merged_list = merged_list.next
        merged_list = prior_node 
        merged_list.next = list1 if list1 else list2 if list2 else None
        return head 



        