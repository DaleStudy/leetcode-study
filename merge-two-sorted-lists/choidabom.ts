/**
 * Runtime: 0ms, Memory: 52.30MB
 *
 * 접근
 * 핵심은 두 리스트를 비교하면서 작은 값부터 정렬되도록 리스트를 만드는 것이다.
 * 두 연결 리스트 중 하나가 null이 될 때까지 현재 노드 값을 비교하여 더 작은 값을 새로운 리스트트 추가하고, 남은 리스트를 추가한다.
 *
 * 평소 접하는 배열이 아닌 링크드 리스트로 풀어야 했기에 접근 방식이 와닿지 않았다.
 * 처음에는 list1, list2가 하나의 노드라고 생각하여 헷갈렸지만, 실제로는 각 노드가 next를 통해 연결된 연결 리스트임이 중요하다.
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

function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null
): ListNode | null {
  let dummy = new ListNode(-1);
  let current = dummy;

  while (list1 !== null && list2 !== null) {
    if (list1.val < list2.val) {
      current.next = list1;
      list1 = list1.next;
    } else {
      current.next = list2;
      list2 = list2.next;
    }
    current = current.next;
  }

  current.next = list1 || list2;

  return dummy.next;
}
