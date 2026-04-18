# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode | None = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        current_node = head
        reversed_node = None

        while current_node:
            next_node = current_node.next
            current_node.next = reversed_node

            if next_node is None:
                return current_node

            reversed_node = current_node
            current_node = next_node


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
