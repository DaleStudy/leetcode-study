/**
 * 연결 리스트를 뒤집는 알고리즘
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n)
 * - 공간 복잡도: O(n)
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
function reverseList(head: ListNode | null): ListNode | null {
  // console.log(head)
  if (head === null || head.next === null) {
    return head
  }

  // 마지막 노드에 도달할 때까지 계속 재귀 호출
  const newHead = reverseList(head.next)

  // 백트래킹 과정
  head.next.next = head
  head.next = null

  return newHead
}
