// 주어진 연결 리스트에서 사이클이 있는지 판단하는 문제
// 사이클: 연결 리스트의 어떤 노드가, 이전에 방문했던 노드를 다시 가리키는 경우

// 문제접근:
// 1) hashset : 직관적
// 2) two pointers : 플로이드의 사이클 탐지 알고리즘(토끼와 거북이 알고리즘)

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/** two pointers로 접근
 * 시간복잡도: O(n)
 * 공간복잡도: O(1) - ✅ follow-up 고려
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
  if (!head || !head.next) return false;

  let slow = head; // 거북이: 한 칸씩
  let fast = head; // 토끼: 두 칸씩

  while (fast && fast.next) {
    slow = slow.next; // 한 칸 이동
    fast = fast.next.next; // 두 칸 이동

    // 두 포인터가 만나면 사이클 존재한다
    if (slow === fast) {
      return true;
    }
  }

  return false;
};

/**
 * hashset으로 접근
 * 시간복잡도: O(n)
 * 공간복잡도: O(n)
 */
var hasCycle2 = function (head) {
  if (!head) return false;

  const visited = new Set();
  let current = head;

  while (current) {
    // 이미 방문한 노드라면 사이클 존재한다
    if (visited.has(current)) {
      return true;
    }

    // 현재 노드를 방문 기록에 추가
    visited.add(current);
    current = current.next;
  }

  return false;
};
