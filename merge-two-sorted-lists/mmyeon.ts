class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

/**
 *
 * 접근 방법 :
 * - 2개의 정렬된 링크드 리스트가 주어지니까 각 리스트 값 비교하면서 작은 값을 새로운 링크드 리스트에 추가
 * - 링크드 리스트 head에 접근해야하니까 더미노드와 포인터 변수 분리해서 사용
 * - 포인터 변수 사용해서 노드 연결하기
 * - 두 링크드 리스트가 있는 동안 반복하고, 한 쪽이 끝나면 나머지 노드를 그대로 새로운 링크드 리스트에 추가
 *
 * 시간복잡도 : O(n+k)
 *  - n은 list1 길이, k는 list2 길이 => 두 리스트 모두 반복하니까 O(n+k)
 *
 * 공간복잡도 : O(1)
 *  - 기존 노드 연결해서 재사용하니까 O(1)
 */

function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null
): ListNode | null {
  const dummyNode = new ListNode();
  let current = dummyNode;

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
  current.next = list1 !== null ? list1 : list2;

  return dummyNode.next;
}
