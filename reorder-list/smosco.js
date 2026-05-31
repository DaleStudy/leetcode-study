/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

/**
 * 방법 1: 반으로 나누기 + 뒤집기 + 합치기
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(1)
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function (head) {
  if (!head || !head.next) return;

  // 1. 중간 지점 찾기 (slow-fast pointer)
  let slow = head,
    fast = head;
  while (fast.next && fast.next.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  // 2. 뒷부분 리스트 분리 및 뒤집기
  let second = slow.next;
  slow.next = null;

  let prev = null;
  while (second) {
    let temp = second.next;
    second.next = prev;
    prev = second;
    second = temp;
  }

  // 3. 두 리스트 합치기
  let first = head;
  second = prev;
  while (second) {
    let temp1 = first.next;
    let temp2 = second.next;
    first.next = second;
    second.next = temp1;
    first = temp1;
    second = temp2;
  }
};

/**
 * 방법 2: Stack 사용
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(n)
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderListStack = function (head) {
  if (!head || !head.next) return;

  // 모든 노드를 스택에 저장
  let stack = [];
  let curr = head;
  while (curr) {
    stack.push(curr);
    curr = curr.next;
  }

  // 앞에서부터, 뒤에서부터 번갈아 연결
  let len = stack.length;
  curr = head;
  for (let i = 0; i < Math.floor(len / 2); i++) {
    let last = stack.pop();
    let temp = curr.next;
    curr.next = last;
    last.next = temp;
    curr = temp;
  }
  curr.next = null; // 마지막 노드 처리
};
