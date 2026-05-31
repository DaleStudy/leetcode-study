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
새 mergeList를 만들고 list1, list2를 순회하며 더 작은 값을 mergeList에 넣는다.
두 리스트의 next가 비게 되면 mergeList의 head를 리턴한다.

시간복잡도 : O(N+K) (N은 list1의 길이, K는 list2의 길이)

*/

function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null,
): ListNode | null {
  let now = null
  let head = null

  while (list1 || list2) {
    if (!list2 || (list1 && list1.val <= list2.val)) {
      if (!now) {
        now = list1
        head = now
      } else {
        now.next = list1
        now = now.next
      }
      list1 = list1.next
    } else {
      if (!now) {
        now = list2
        head = now
      } else {
        now.next = list2
        now = now.next
      }
      list2 = list2.next
    }
  }

  return head
}
