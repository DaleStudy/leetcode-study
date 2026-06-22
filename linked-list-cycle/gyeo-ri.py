"""
[결과 요약]
# 시도한 로직 수: 2
    1. Set을 사용하여 이전 노드를 저장하기(O(n) / O(n))
        - 메모리를 많이 사용함
    2. 포인터를 사용하여 메모리 사용량 줄이기(O(n) / O(1)
        - set 방식과 시간 복잡도(O(n))은 동일하나, 실제 성능은 개선됨
            - set은 이전 노드 비교를 위해 해시 탐색이 필요하여 상대적으로 성능 저하
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode | None = next


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        node_1_step, node_2_steps = head, head

        # 1. 2 steps를 더 이상 탐색할 수 없을 때까지(node is None or node.next is None) 반복
        while node_2_steps is not None and node_2_steps.next is not None:
            node_1_step = node_1_step.next
            node_2_steps = node_2_steps.next.next

            # 2. 계속 돌렸을 때 node 1과 node 2가 만나면 순회가 있는 것
            # 일치 비교이므로 is 사용
            if node_1_step is node_2_steps:
                return True

        return False


if __name__ == "__main__":
    test_cases = [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([1, 2], -1, False),
        ([], -1, False),
    ]

    solution = Solution()

    for idx, (inp, pos, expected) in enumerate(test_cases, start=1):
        head = None
        nodes = []

        for value in reversed(inp):
            head = ListNode(value, head)

        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        if pos != -1 and nodes:
            nodes[-1].next = nodes[pos]

        result = solution.hasCycle(head)

        assert (
            result == expected
        ), f"Test Case {idx} Failed: Expected {expected}, Got {result}"

    print("All test cases passed.")
