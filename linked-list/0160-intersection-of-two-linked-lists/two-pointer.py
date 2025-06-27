# Suppose:
# - List A has length a + c
# - List B has length b + c
# (where c is the length of the shared tail)

# After both pointers traverse a + b + c steps:
# - If there is an intersection, they will meet at the start of the shared part (length c)
# - If there is no intersection, both will reach the end (None) at the same time

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA, pB = headA, headB
        
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
            
        return pA
        
# At the end of traversal:
# If the lists intersect: pA == pB == intersection node
# If the lists do not intersect: pA == pB == None
