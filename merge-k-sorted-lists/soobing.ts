/**
 * 문제 설명
 * - k개의 정렬된 링크드 리스트 병합하기
 *
 * 아이디어
 * 1) 병합정렬 -> 대표적인 분할 정복(Divide and Conquer) 문제
 * - 두 리스트를 병합할 수 있는 함수를 계속해서 적용한다.
 * - 두 링크드 리스트 병합하는 예제
 *  ㄴ @link https://leetcode.com/problems/merge-two-sorted-lists/description/
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

function mergeList(list1: ListNode | null, list2: ListNode | null) {
  const dummy = new ListNode(0);
  let current = dummy;

  while (list1 && list2) {
    if (list1.val <= list2.val) {
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

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
  return lists.reduce((acc, current) => {
    return mergeList(acc, current);
  }, null);
}
