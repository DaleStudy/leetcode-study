/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * 문제: 리스트 뒤집기
 * 
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(n)
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
  // 노드 값을 선언
  let node = null;

  // head가 없을 때 까지 반복
  while(head) {
      const temp = head.next; // head 의 다음 값을 temp에 저장
      head.next = node;       // 기존 head의 다음값을 node에 저장
      node = head;            // 현재 node의 값을 head에 저장
      head = temp;            // 현재 head값에 temp 저장
  }
  
  return node;                // node 출력
};
