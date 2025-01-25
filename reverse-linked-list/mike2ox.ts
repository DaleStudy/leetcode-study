/**
 * https://leetcode.com/problems/reverse-linked-list/
 * 풀이방법: 스택을 사용하여 역순으로 노드를 생성
 *
 * 시간복잡도: O(n) (n: 리스트의 길이)
 * 공간복잡도: O(n) (스택에 모든 노드를 저장)
 */

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

function reverseList(head: ListNode | null): ListNode | null {
  if (!head) return null;

  const stack: number[] = [];
  let result: ListNode | null = null;
  let lastNode: ListNode;
  while (head) {
    stack.push(head.val);
    head = head.next;
  }
  for (let i = stack.length - 1; i >= 0; i--) {
    if (!result) {
      result = new ListNode(stack[i]);
      lastNode = result;
      continue;
    }
    lastNode.next = new ListNode(stack[i]);
    lastNode = lastNode.next;
  }
  return result;
}
