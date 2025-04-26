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

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
  // 더미 헤드 노드를 생성하여 결과 리스트의 시작점으로 사용
  const dummy = new ListNode(0);
  let current = dummy;
  
  // 두 리스트를 순회하면서 더 작은 값을 가진 노드를 결과 리스트에 연결
  while (list1 !== null && list2 !== null) {
      if (list1.val <= list2.val) {
          current.next = list1;
          list1 = list1.next;
      } else {
          current.next = list2;
          list2 = list2.next;
      }
      current = current.next;
  }
  
  // 남은 노드들을 결과 리스트에 연결
  current.next = list1 === null ? list2 : list1;
  
  // 더미 노드의 다음 노드가 실제 병합된 리스트의 헤드
  return dummy.next;
}
