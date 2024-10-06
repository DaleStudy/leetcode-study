/**
 * TC: O(List1 + List2)
 * List1, List2 전체 순회 1번씩 합니다.
 *
 * SC: O(1)
 * List1, List2의 길이와 무관한 고정된 데이터 공간을 사용합니다. (head, pointer 변수들)
 *
 * List1: list1.length, List2.length;
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
  // 1. 둘 중 하나의 list가 없는 경우 반대편의 list를 반환
  if (!list1) {
    return list2;
  }
  if (!list2) {
    return list1;
  }

  // 2. 정답을 반환할 시작점(head)와 list 순회시 필요한 pointer
  const head = new ListNode();
  let headPointer = head;
  let list1Pointer = list1;
  let list2Pointer = list2;

  // 3. 두 list 모두 노드를 가진 경우
  while (list1Pointer && list2Pointer) {
    if (list1Pointer.val < list2Pointer.val) {
      list1Pointer = connectHeadAndListPointer(list1Pointer);
    } else {
      list2Pointer = connectHeadAndListPointer(list2Pointer);
    }
  }

  // 4. 한쪽 list의 남은 노드 연결
  while (list1Pointer) {
    list1Pointer = connectHeadAndListPointer(list1Pointer);
  }

  while (list2Pointer) {
    list2Pointer = connectHeadAndListPointer(list2Pointer);
  }

  return head.next;

  // 5. head의 list로 연결 후 다음 노드로 pointer 이동
  function connectHeadAndListPointer(listPointer) {
    headPointer.next = listPointer;
    listPointer = listPointer.next;
    headPointer = headPointer.next;

    return listPointer;
  }
};
