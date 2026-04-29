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
리스트 노드를 저장하는 Map을 생성, 노드를 탐색하며 해당 Map에 노드를 저장하고 이미 있는 노드일 경우 true 리턴

시간복잡도 : O(N) - N은 리스트의 개수
공간복잡도 : O(N) - Map 객체
*/

function hasCycle(head: ListNode | null): boolean {
  const nodeMap = new Map<ListNode, boolean>()

  while (head) {
    if (nodeMap.get(head) === true) {
      return true
    }
    nodeMap.set(head, true)
    head = head.next
  }

  return false
}
