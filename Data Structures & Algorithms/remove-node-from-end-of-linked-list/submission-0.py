# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def get_length(self,head):
        itr=head
        cnt=0
        while itr:
            cnt+=1
            itr=itr.next
        return cnt    


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        itr=head
        index=self.get_length(head)-n
        if index==0:
            return head.next
        count=0


        while itr:
            if count==index-1:
                itr.next=itr.next.next
            itr=itr.next
            count+=1
        return head             