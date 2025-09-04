class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head=ListNode(next=head)
        current=dummy_head
        while current.next:
            if current.next.val==val:
                current.next=current.next.next
            else:
                current=current.next
        return dummy_head.next