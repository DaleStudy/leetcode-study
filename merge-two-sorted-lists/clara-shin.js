/**
 * 문제 정의
 * 입력: 두 개의 정렬된 연결 리스트의 헤드 노드 list1과 list2
 * 출력: 두 리스트를 병합한 정렬된 연결 리스트의 헤드 노드
 * 조건: 두 리스트는 이미 오름차순으로 정렬되어 있음
 *
 * 접근 방법
 * 1. 더미 헤드 노드를 생성하여 결과 리스트의 시작점을 설정
 * 2. 두 리스트를 순회하며 작은 값을 가진 노드를 결과 리스트에 추가
 * 3. 한 리스트가 끝나면 다른 리스트의 남은 노드를 결과 리스트에 연결
 * 4. 더미 헤드의 다음 노드를 반환하여 결과 리스트를 반환
 * 5. 시간 복잡도: O(n + m) (n: list1의 길이, m: list2의 길이)
 *    공간 복잡도: O(1) (추가적인 공간 사용 없음)
 *
 * 재귀적으로 구현할 수도 있지만, 공간복잡도는 재귀호출 스택 때문에 O(n + m)이 됨
 * 따라서, 반복적(iterative) 방법을 사용하여 공간복잡도를 O(1)로 유지하는 것이 좋음
 */

/**
 * @param {ListNode} list1 - 첫 번째 정렬된 연결 리스트의 헤드
 * @param {ListNode} list2 - 두 번째 정렬된 연결 리스트의 헤드
 * @return {ListNode} - 병합된 정렬 리스트의 헤드
 */
var mergeTwoLists = function (list1, list2) {
  let dummy = new ListNode(-1); // 더미 헤드 노드 생성 (결과 리스트의 시작점)

  let current = dummy; // 현재 결과 리스트의 위치를 추적하는 포인터

  while (list1 !== null && list2 !== null) {
    if (list1.val <= list2.val) {
      current.next = list1;
      list1 = list1.next;
    } else {
      current.next = list2;
      list2 = list2.next;
    }
    // 결과 리스트의 포인터 이동ㄱㄱ
    current = current.next;
  }

  // 남아있는 노드들을 결과 리스트에 연결 (list1이나 list2 중 하나는 이미 null일 테니까)
  current.next = list1 !== null ? list1 : list2;

  // 더미 헤드 다음 노드가 실제 결과의 시작 노드가 됨
  return dummy.next;
};
