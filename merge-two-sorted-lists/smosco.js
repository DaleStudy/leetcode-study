/**
 * Merge Two Sorted Lists
 *
 * 핵심 아이디어:
 * - 두 정렬된 리스트를 비교하며 작은 값부터 새로운 리스트에 연결
 * - 더미 노드를 사용해 head 처리를 간단하게 만듦
 * - 한쪽 리스트가 끝나면 나머지를 그대로 연결
 *
 * 시간 복잡도: O(n + m) - 두 리스트의 모든 노드를 한 번씩 방문
 * 공간 복잡도: O(1) - 새 노드를 만들지 않고 기존 노드만 재배치
 */
const mergeTwoLists = (list1, list2) => {
  // 더미 노드: head 처리를 쉽게 하기 위한 임시 시작점
  const dummy = { val: 0, next: null };
  let current = dummy;

  // 두 리스트 모두 남아있는 동안 비교하며 병합
  while (list1 !== null && list2 !== null) {
    if (list1.val <= list2.val) {
      current.next = list1; // 더 작은 노드 연결
      list1 = list1.next; // list1 포인터 이동
    } else {
      current.next = list2;
      list2 = list2.next;
    }
    current = current.next; // 결과 리스트 포인터 이동
  }

  // 남은 노드들을 그대로 연결 (이미 정렬되어 있음)
  current.next = list1 !== null ? list1 : list2;

  return dummy.next; // 더미 노드 다음부터가 실제 결과
};
