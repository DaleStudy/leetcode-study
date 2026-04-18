# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode | None = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        reversed_node = None

        while head:
            reversed_node = ListNode(head.val, next=reversed_node)

            if not head.next:
                return reversed_node

            else:
                head = head.next


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
    ]

    solution = Solution()

    for idx, (inp, expected) in enumerate(test_cases, start=1):
        head = None
        for value in reversed(inp):
            head = ListNode(value, head)

        result = solution.reverseList(head)

        result_list = []
        while result is not None:
            result_list.append(result.val)
            result = result.next

        assert (
            result_list == expected
        ), f"Test Case {idx} Failed: Expected {expected}, Got {result_list}"

    print("All test cases passed.")
