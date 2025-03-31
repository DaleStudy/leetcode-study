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
 * n번째 노드 제거하기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n)
 * - 공간 복잡도: O(n)
 * @param head
 * @param n
 */
function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
  let stack: ListNode[] = [];
  let node = head;

  while (node) {
    stack.push(node);
    node = node.next;
  }

  // 첫 번째 노드를 제거하는 경우 추가
  if (stack.length - n - 1 < 0) {
    return head?.next || null;
  }

  const prevNode = stack[stack.length - n - 1];
  prevNode.next = prevNode.next?.next || null;

  return head;
}
