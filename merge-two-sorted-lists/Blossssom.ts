class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

/**
 * @param linked_list list1
 * @param linked_list list2
 * @returns 정렬된 linked_list
 * @description
 * - 연결리스트로 각 단계를 탐색하려니 접근 방법이 떠오르지 않음
 * - 해당 유형의 문제를 더 풀어볼 예정
 */

function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null
): ListNode | null {
  if (!list1 && !list2) {
    return null;
  }

  const temp = new ListNode();
  let current = temp;

  while (list1 && list2) {
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

  return temp.next;
}

const list1 = new ListNode(1, new ListNode(2, new ListNode(4)));
const list2 = new ListNode(1, new ListNode(3, new ListNode(4)));

mergeTwoLists(list1, list2);

