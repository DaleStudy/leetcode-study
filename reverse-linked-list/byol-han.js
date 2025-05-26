/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * https://leetcode.com/problems/reverse-linked-list/
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {
  let prev = null;
  let current = head;

  while (current) {
    const next = current.next; // 다음 노드 기억
    current.next = prev; // 현재 노드가 이전 노드를 가리키도록 변경
    prev = current; // prev를 현재 노드로 이동
    current = next; // current를 다음 노드로 이동
  }

  return prev; // prev는 새로운 head
};

/* 
*** linked list ***
리스트의 각 노드가 다음 노드를 가리키는 포인터를 가지고 있는 자료구조

리스트의 첫 번째 노드를 head라고 하고, head.next는 두 번째 노드, head.next.next는 세 번째 노드...
이런식으로 노드들을 순차적으로 접근할 수 있는 자료구조를 '연결 리스트(linked list)'라고 함

reverseList(head)에서 head는 리스트 전체의 진입점.
head 하나만 알고 있어도, .next를 따라가면서 전체 노드들을 순차적으로 접근할 수 있기 때문에 리스트 전체를 다룰 수 있음

// 노드 구조 정의
function ListNode(val, next = null) {
  this.val = val;
  this.next = next;
}

// 리스트 만들기
const node3 = new ListNode(3);              // 마지막 노드
const node2 = new ListNode(2, node3);       // node2 → node3
const head  = new ListNode(1, node2);       // head → node2 → node3

// 확인
console.log(head.val);         // 1
console.log(head.next.val);    // 2
console.log(head.next.next.val); // 3
 */
