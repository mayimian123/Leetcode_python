class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA=self.getlength(headA)
        lenB=self.getlength(headB)
        
        if lenA<lenB: # bigger one move forward
            headB=self.move(headB,lenB-lenA)
        else:
            headA=self.move(headA,lenA-lenB)

        while headA and headB:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next

        return None

    def getlength(self,head:ListNode)->int:
        length=0
        while head:
            length+=1
            head=head.next
        return length
    def move(self,head:ListNode, dis:int)->Optional[ListNode]:
        while dis>0:
            head=head.next
            dis-=1
        return head