"""
[결과 요약]
# 시도한 로직 수: 3
    1. 반복문을 사용한 풀이: 코드는 짧고 성능은 좋지만 (새로운 노드 객체 정의를 위해) 불필요한 메모리 사용이 있어 (2)에서 개선함
        - 시간복잡도 O(n) / 공간복잡도 O(n)
    2. 반복문 풀이와 메모리 개선: 기존 노드(ListNode)의 연결 관계(next)를 직접 바꾸는 방식)
        - 시간복잡도 O(n) / 공간복잡도 O(1)
    3. 재귀 풀이: 반복문과 시간복잡도는 동일하나 실제 실행 속도가 약간 느리고, 공간복잡도에서는 불리함
        - 재귀는 기본적으로 공간의 깊이에 비례하여 O(1)의 공간복잡도가 나오기는 어려움
        - 시간복잡도 O(n) / 공간복잡도 O(n)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode | None = next


# 재귀를 사용한 최종 풀이
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # 1. 리스트가 비었거나(head is None) 마지막 노드일 때(head.next is None)는 종료
        if head is None or head.next is None:
            return head

        # 2. 현재 노드(=head)를 제외하고, 다음 노드(next_node)부터 끝까지를 재귀 호출(뒤쪽 리스트를 뒤집기)
        next_node = head.next
        reversed_node = self.reverseList(next_node)

        # 3. 현재 노드를 뒤집힌 이전 노드(reversed_node)의 뒤에 붙이기
        # reversed_node의 가장 끝은 head.next이므로, head를 next_node 뒤에 붙인 다음 마지막 노드로 표시(head.next = None)
        next_node.next = head
        head.next = None

        # 4. 최종 노드를 반환
        # 2의 reversed_node는 head(=마지막 노드)가 빠진 상태였지만 3에서 next_node -> head를 연결하면서 완성됨
        return reversed_node


"""
# 반복문을 사용한 풀이
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
"""


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
