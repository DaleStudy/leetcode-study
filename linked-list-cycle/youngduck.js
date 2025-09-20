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
  // 순환탐지 기법
  // 1. 플로이드 토끼와 거북이 (포인터2개)
  // 2. 집합을 통한 중복검사

  ////////풀이///////

  // 노드 0개 1개면 순환불가

  if (!head || !head.next) {
    return false;
  }

  // 토끼, 거북이 설정
  let slow = head;
  let fast = head.next;

  while (slow !== fast) {
    // 두칸전진시 노드 존재 체크
    if (!fast || !fast.next) {
      return false;
    }

    slow = slow.next;
    fast = fast.next.next;
  }

  return true;
};

// 시간복잡도 O(n) -> 최대 리스트의 노드 수 만큼 while문이 반복되므로
// 공간복잡도 O(1) -> 토끼, 거북이 포인터 2개만 사용하므로
