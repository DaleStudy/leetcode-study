/**
 * 문제 설명
 * - 연결 리스트의 "끝"에서 n번째 노드를 제거하는 문제
 *
 * 아이디어
 * 1) 투 포인터 기법 ⚠️
 *   - fast, slow 포인터간의 간격을 n + 1만큼 벌리면 fast 포인터가 끝에 도달했을 경우, slow 포인터를 활용하여 제거 가능하다.
 *   - 주의할점은 노드가 하나만 존재하는 케이스를 대응하기 위해 더미 노드를 사용한다.
 *
 */
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
  let dummy = new ListNode(0, head);
  let fast: ListNode | null = dummy;
  let slow: ListNode | null = dummy;

  for (let i = 0; i < n + 1; i++) {
    fast = fast!.next;
  }

  while (fast) {
    fast = fast.next;
    slow = slow!.next;
  }

  slow!.next = slow!.next!.next;
  return dummy.next;
}
