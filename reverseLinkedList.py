#Time Complexity: O(n)
#Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
       
       if (head == None):
           return None

       if(head.next == None):
           return head

       prev = None
       curr = head
       fast = curr.next

       while(fast != None):
           curr.next = prev  
           prev = curr
           curr = fast
           fast = fast.next

       curr.next = prev

       return curr 