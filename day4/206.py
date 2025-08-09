class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        pre=None
        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        return pre