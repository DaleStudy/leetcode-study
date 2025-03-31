/**
 * Source: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
 * Solution: 두 개의 포인터를 이용해 n번째 노드를 찾아 삭제
 *
 * 시간복잡도: O(N) - 두 개의 포인터가 한번씩 순회
 * 공간복잡도: O(1) - 상수만큼의 공간 사용
 */

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
  if (!head) return null;

  const dummy = new ListNode(0, head);
  let slow: ListNode | null = dummy;
  let fast: ListNode | null = dummy;

  for (let i = 0; i <= n; i++) {
    if (!fast) return head;
    fast = fast.next;
  }

  while (fast) {
    slow = slow!.next;
    fast = fast.next;
  }

  if (slow && slow.next) {
    slow.next = slow.next.next;
  }

  return dummy.next;
}
