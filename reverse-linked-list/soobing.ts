/**
 * 문제 설명
 * - 링크드 리스트를 뒤집는 문제
 *
 * 아이디어
 * - 노드를 순회하면서 다음 노드를 미리 기억해두고, 화살표를 반대로 돌린 후 한칸씩 이동한다.
 * - prev, head(current) 두 가지 포인터가 필요
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

interface ListNode {
  val: number;
  next: ListNode | null;
}

function reverseList(head: ListNode | null): ListNode | null {
  let prev: ListNode | null = null;

  while (head) {
    const next = head.next;
    head.next = prev;
    prev = head;
    head = next;
  }

  return prev;
}
