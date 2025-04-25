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
  // 가짜(head 역할을 할) 임시 노드 생성
  // 실제 결과 리스트는 dummy.next부터 시작됨
  let dummy = new ListNode(-1);

  // 현재 노드를 가리킬 포인터. 처음엔 dummy에서 시작
  let current = dummy;

  // 두 리스트 모두 null이 아닐 동안 반복 (비교 가능한 노드가 있을 때까지)
  while (list1 !== null && list2 !== null) {
    // list1의 현재 값이 더 작으면 list1 노드를 current.next에 붙임
    if (list1.val < list2.val) {
      current.next = list1; // current 뒤에 list1 노드 연결
      list1 = list1.next; // list1 포인터를 다음 노드로 이동
    } else {
      current.next = list2; // current 뒤에 list2 노드 연결
      list2 = list2.next; // list2 포인터를 다음 노드로 이동
    }
    current = current.next; // current 포인터도 다음 노드로 이동 (리스트를 계속 이어가기 위해)
  }

  // 위 반복문을 빠져나오면, 둘 중 하나는 null이 됨
  // 나머지 하나는 아직 정렬된 상태이므로 그대로 뒤에 붙여줌
  current.next = list1 !== null ? list1 : list2;

  // dummy는 첫 번째 노드를 가리키는 용도였으니, 실제 결과 리스트는 dummy.next부터 시작
  return dummy.next;
};
// 시간 복잡도: O(n + m) (n: list1의 길이, m: list2의 길이)
// 공간 복잡도: O(1) (추가적인 공간 사용 없음)
