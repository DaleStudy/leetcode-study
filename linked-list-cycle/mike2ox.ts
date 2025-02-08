/**
 * Source: https://leetcode.com/problems/linked-list-cycle/
 * 풀이방법: Set을 이용하여 방문한 노드를 저장하고 순회하면서 중복된 노드가 있는지 확인
 *
 * 시간복잡도: O(n)
 * 공간복잡도: O(n)
 */

// class ListNode {
//   val: number;
//   next: ListNode | null;
//   constructor(val?: number, next?: ListNode | null) {
//     this.val = val === undefined ? 0 : val;
//     this.next = next === undefined ? null : next;
//   }
// }

function hasCycle(head: ListNode | null): boolean {
  if (head === null) return false;

  // 방문한 노드들을 저장할 Set
  const addr = new Set<ListNode>();

  // 첫 노드 추가
  addr.add(head);
  head = head.next;

  // 리스트 순회
  while (head !== null) {
    // 이미 방문한 노드인 경우 cycle 존재
    if (addr.has(head)) return true;

    // 새로운 노드 추가
    addr.add(head);
    head = head.next;
  }

  return false;
}
