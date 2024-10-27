/**
 * TC: O(N)
 * 1번에서 절반 길이만큼 순회
 * 2번에서 절반 길이만큼 순회
 * 3번에서 절반 길이만큼 순회
 *
 * SC: O(1)
 * linked list의 node를 가리키는 포인터를 가지고 활용하므로 linked list의 길이와 무관한 공간 복잡도를 갖습니다.
 *
 * N: linked list length
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
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function (head) {
  // 1. linked list 절반 위치 구하기
  let slow = head;
  let fast = head;

  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  // 2. 후반 linked list 순서 뒤집기
  let halfStartTemp = slow.next;
  let halfStart = null;
  // 절반을 기준으로 linked list 끊기
  slow.next = null;

  while (halfStartTemp) {
    const temp = halfStartTemp.next;
    halfStartTemp.next = halfStart;
    halfStart = halfStartTemp;
    halfStartTemp = temp;
  }

  // 3. 두 리스트 합치기
  while (head && halfStart) {
    const headTemp = head.next;
    const halfStartTemp = halfStart.next;
    head.next = halfStart;
    halfStart.next = headTemp;
    head = headTemp;
    halfStart = halfStartTemp;
  }
};
