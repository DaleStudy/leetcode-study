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

/**
 * 리스트 재정렬 하기 (0 -> n -> 1 -> n-1 -> ...) 
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n)
 * - 공간 복잡도: O(n)
 * @param head
 */
function reorderList(head: ListNode | null): void {
  if (!head || !head.next) return;

  const stack: ListNode[] = [];
  let node = head;
  while (node) {
    stack.push(node);
    node = node.next;
  }

  let left = 0;
  let right = stack.length - 1;

  while (left < right) {
    // 현재 노드의 다음에 마지막 노드 연결
    stack[left].next = stack[right];
    left++;

    // 남은 노드가 있으면 마지막 노드의 다음에 다음 왼쪽 노드 연결
    if (left < right) {
      stack[right].next = stack[left];
      right--;
    }
  }

  // 마지막 노드의 next를 null로 설정
  stack[left].next = null;
}
