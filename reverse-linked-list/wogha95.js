/**
 * 2차
 * Tony님 풀이 참고해서 SC 개선
 *
 * TC: O(N)
 * SC: O(1)
 * 순회동안 노드 생성하지 않으므로 공간복잡도가 상수다.
 *
 * N: linked-list length
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {
  let pointer = null;

  while (head !== null) {
    let temp = head.next;
    head.next = pointer;
    pointer = head;
    head = temp;
  }

  return pointer;
};

/**
 * 1차
 * TC: O(N)
 * linked-list 길이 만큼 순회
 *
 * SC: O(N)
 * linked-list 길이만큼 생성
 *
 * N: linked-list length
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {
  let pointer = null;

  while (head) {
    // 1. 정답 리스트의 맨 앞에 새로운 노드를 추가
    pointer = new ListNode(head.val, pointer);
    // 2. head는 다음 노드로 이동
    head = head.next;
  }

  return pointer;
};
