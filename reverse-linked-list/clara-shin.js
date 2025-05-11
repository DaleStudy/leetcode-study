/**
 * 단일 연결리스트(Singly Linked List)의 노드 순서를 반대로 뒤집어서 리턴하기
 * follow-up: 연결리스트는 반복적(Iterative) 또는 재귀적(Recursive)으로 뒤집을 수 있는데, 두 가지 방법 다 가능?
 *
 * 반복문(Iterative) 방식 (✅ 실무에서 더 많이 사용한다고 함)
 * 포인터 세 개(prev, curr, next)를 사용, 리스트를 한 번 순회하며 역방향으로 연결을 바꿈
 * 시간복잡도: O(n), 공간복잡도: O(1)
 *
 * 재귀(Recursive) 방식
 * 재귀적으로 끝까지 들어간 뒤, 각 노드의 next를 역방향으로 연결
 * 시간복잡도: O(n), 공간복잡도: O(n) (재귀 콜스택)
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
// 반복문(Iterative) 방식
var reverseList = function (head) {
  let prev = null;
  let curr = head;
  while (curr) {
    const next = curr.next; // 다음 노드 저장
    curr.next = prev; // 현재 노드의 next를 prev로 변경
    prev = curr; // prev를 현재 노드로 이동
    curr = next; // curr를 다음 노드로 이동
  }
  return prev;
};

// 재귀(Recursive) 방식
var reverseList = function (head) {
  if (!head || !head.next) return head; // 빈 리스트 또는 마지막 노드인 경우, 빠른 리턴

  const reversed = reverseList(head.next); // 나머지 리스트 역순
  head.next.next = head; // 다음 노드의 next를 현재 노드로
  head.next = null; // 현재 노드의 next를 null로
  return reversed;
};
