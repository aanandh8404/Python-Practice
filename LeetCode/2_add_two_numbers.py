# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.


# l1 = list(map(int,input("Enter l1 values :").split()))
# l2 = list(map(int,input("Enter l2 values :").split()))

# s1 = ''.join(str(i) for i in l1[::-1])
# s2 = ''.join(str(i) for i in l2[::-1])

# sum = int(s1) + int(s2)

# result = list(map(int,(str(sum)[::-1])))
# print(result)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
    
def build_linked_list(nums):
    dummy = ListNode(0)
    curr = dummy
    for n in nums:
        curr.next = ListNode(n)
        curr = curr.next
    return dummy.next

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

l1 = build_linked_list([2, 4, 3])
l2 = build_linked_list([5, 6, 4])

sol = Solution()
result = sol.addTwoNumbers(l1, l2)

print(linked_list_to_list(result))
