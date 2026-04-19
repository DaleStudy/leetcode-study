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

/*
직전 노드를 담는 변수 before과 다음 노드를 담는 변수 next, 순회중인 노드 head 변수와 함께 list를 순회
head의 next에 before을 넣고, head를 next로 변환하며 head가 null이 아닐 때까지 반복한다

시간복잡도 : O(N) - 1번 순회
공간복잡도 : O(1) - before, next 변수

*/
function reverseList(head: ListNode | null): ListNode | null {
  if (!head) return head
  let originNext = head.next
  let before = null

  while (head !== null) {
    originNext = head.next
    head.next = before
    before = head
    head = originNext
  }

  return before
}
