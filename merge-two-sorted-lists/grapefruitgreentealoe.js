//두개의 정렬된 링크드 리스트 list1, list2의 Head를 받았다.(리스트가 아니라, 연결리스트의 헤드)
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
function mergeTwoLists(
  list1,
  list2,
) {
  if (!(list1 && list2)) return list1 || list2;
  if (list1.val < list2.val) {
    list1.next = mergeTwoLists(list1.next, list2);
    return list1;
  } else {
    list2.next = mergeTwoLists(list1, list2.next);
    return list2;
  }
}

/*
list1.val이 list2.val보다 작으면
list1.next 다음에 list2.val이 온다. 
만약 아니라면, list2.next 다음에 list1의 Head를 붙여준다.
이렇게 next만 바꿔주면서 연결지어주는 것이다.

시간 복잡도: O(log n)
공간 복잡도: O(h)
*/
