/**
 * 풀이
 * - Floyd's Tortoise and Hare Algorithm을 이용한 풀이입니다.
 *   참고: https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare
 *
 * Big O
 * - N: 노드의 개수
 * - L: 루프 구간에 속하는 노드의 개수
 *
 * Time Complexity: O(N)
 * - 루프가 없는 경우:
 *   - fast 포인터가 링크드리스트의 끝까지 이동하면 종료합니다.
 *   - 이 때 fast 포인터의 탐색 시간 복잡도는 다음과 같습니다:
 *     O(N / 2) = O(N)
 * - 루프가 있는 경우:
 *   - slow 포인터와 fast 포인터가 루프 안에서 만나면 종료합니다.
 *   - 이 때 slow 포인터의 탐색 시간 복잡도는 다음과 같습니다:
 *     O((N - L) + L * c)  (c는 slow가 fast를 만날 때까지 루프를 반복한 횟수)
 *     = O(r + (N - r) * c)  (L은 0 <= r <= N인 r에 대해 N - r로 표현할 수 있습니다)
 *     = O(N)
 *
 * Space Complexity: O(1)
 * - 노드의 개수에 상관없이 일정한 공간을 사용합니다.
 */

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func hasCycle(head *ListNode) bool {
    if head == nil {
        return false
    }

    slow := head
    fast := head

    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next

        if slow == fast {
            return true
        }
    }

    return false
}
