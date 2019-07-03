# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def helper(self, p, dummy, cur, carry):
        while p:
            if carry == 0:
                cur.next = p
                return dummy.next
            
            sumBit = p.val + carry 
            if sumBit > 9:
                sumBit, carry = sumBit % 10, 1
            else:
                cur.next = ListNode(sumBit)
                cur.next.next = p.next
                return dummy.next
            cur.next = ListNode(sumBit)
            p, cur = p.next, cur.next
        if carry == 1:
            cur.next = ListNode(1)
            return dummy.next
    
    def addTwoNumbers(self, l1, l2):
        if not l1 and not l2:
            return None
        if not l1 or not l2:
            return l1 if not l1 else l2
        
        dummy = ListNode(-1)
        cur = dummy
        p1, p2 = l1, l2
        carry, sumBit = 0, 0
        
        import pdb; pdb.set_trace()
        while p1 and p2:
            sumBit = p1.val + p2.val + carry
            if sumBit > 9:
                sumBit, carry = sumBit % 10, 1
            else:
                carry = 0
            
            cur.next = ListNode(sumBit)
            cur = cur.next
            p1, p2 = p1.next, p2.next
            
          
        if p1:
            return self.helper(p1, dummy, cur, carry)
        if p2:
            return self.helper(p2, dummy, cur, carry)
        if carry:
            cur.next = ListNode(1)
        return dummy.next




s = Solution()
l1 = ListNode(9)
l1.next = ListNode(9)
# l1.next.next = ListNode(3)            
l2 = ListNode(1)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)  
node = s.addTwoNumbers(l1, l2)
while node:
    print(node.val)
    node = node.next
