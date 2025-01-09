/**
 * source: https://leetcode.com/problems/merge-two-sorted-lists/
 * 풀이방법: 두 리스트를 비교하면서 작은 값을 결과 리스트에 추가
 *
 * 시간복잡도: O(n + m) (n: list1의 길이, m: list2의 길이)
 * 공간복잡도: O(1) (상수 공간만 사용)
 *
 */

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null
): ListNode | null {
  const result = new ListNode();
  let current = result;
  while (list1 !== null && list2 !== null) {
    if (list1.val <= list2.val) {
      current.next = list1;
      list1 = list1.next;
      current = current.next;
    } else {
      current.next = list2;
      list2 = list2.next;
      current = current.next;
    }
  }
  if (list1 !== null) {
    current.next = list1;
  }
  if (list2 !== null) {
    current.next = list2;
  }
  return result.next; // 처음에 추가한 더미 노드 제외
}
