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
  const answer = new ListNode();
  let temp = answer; // answer은 head를 가지고 있어야함

  // list1, list2 중 하나라도 끝까지 도달할 때 까지 루프 돌리기
  while (list1 && list2) {
    // 더 작은수를 가진 리스트를 연결
    if (list1.val < list2.val) {
      temp.next = list1;
      list1 = list1.next;
    } else {
      temp.next = list2;
      list2 = list2.next;
    }
    temp = temp.next;
  }

  // list1, list2 중 어떤게 끝까지 갔는지 몰라서 둘 다 체크
  // 남은건 그냥 뒤에 가져다가 붙이기
  temp.next = list1 || list2;
  return answer.next;
};
