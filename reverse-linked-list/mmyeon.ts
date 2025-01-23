class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

/**
 *
 * @link https://leetcode.com/problems/reverse-linked-list/
 *
 * 접근 방법 :
 *  - 리스트 순회하면서 새로운 노드를 생성하고 기존 reversed 리스트의 head를 연결
 *
 * 시간복잡도 : O(n)
 *  - 리스트 노드 1회 순회하니까
 *
 * 공간복잡도 : O(n)
 *  - reversed 된 링크드 리스트 새로 만드니까
 */

function reverseList(head: ListNode | null): ListNode | null {
  if (head === null) return head;

  let headNode: ListNode | null = null;
  let currentNode: ListNode | null = head;

  while (currentNode !== null) {
    const newNode = new ListNode(currentNode.val, headNode);
    headNode = newNode;
    currentNode = currentNode.next;
  }

  return headNode;
}
