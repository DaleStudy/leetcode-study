/**
 * Source: https://leetcode.com/problems/reorder-list/
 * 풀이방법: 임시 배열을 사용해서 투포인트 전략으로 풂
 * 시간복잡도: O(n)
 * 공간복잡도: O(n)
 *
 * 추가 풀이
 * - node를 가리키는 두 인자만 사용해서 투포인트 전략이 가능(but, 구현 x)
/

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

/**
 Do not return anything, modify head in-place instead.
 */
function reorderList(head: ListNode | null): void {
  if (!head || !head.next) return;

  // 1. 모든 노드를 배열에 저장
  const nodes: ListNode[] = [];
  let current: ListNode | null = head;
  while (current) {
    nodes.push(current);
    current = current.next;
  }

  // 2. 배열의 양끝에서 시작하여 리스트 재구성
  let left = 0;
  let right = nodes.length - 1;

  while (left < right) {
    // 현재 왼쪽 노드의 다음을 저장
    nodes[left].next = nodes[right];
    left++;

    if (left === right) break;

    // 현재 오른쪽 노드를 다음 왼쪽 노드에 연결
    nodes[right].next = nodes[left];
    right--;
  }

  // 마지막 노드의 next를 null로 설정
  nodes[left].next = null;
}
