/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
  // 리스트가 비어 있거나 노드가 하나뿐이면 사이클이 있을 수 없음
  if (!head || !head.next) return false;

  // 두 포인터 초기화: slow는 한 칸씩, fast는 두 칸씩 이동
  let slow = head;
  let fast = head.next;

  // fast와 slow가 만날 때까지 반복
  while (fast !== slow) {
    // fast가 끝에 도달하면 사이클이 없음
    if (!fast || !fast.next) return false;

    // slow는 한 칸 이동
    slow = slow.next;
    // fast는 두 칸 이동
    fast = fast.next.next;
  }

  // fast와 slow가 만났다면 사이클이 있음
  return true;
};
