class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

/**
 * @psuedocode
 * - 배열 내 노드를 정리
 * - 문제의 정의인 n 값으로 접근
 * @param head
 */

function reorderList(head: ListNode | null): void {
  const nodeArr = [];

  let current: ListNode | null = head;
  while (current) {
    nodeArr.push(current);
    current = current?.next;
  }

  let left = 0;
  let right = nodeArr.length - 1;

  while (left < right) {
    nodeArr[left].next = nodeArr[right];
    left++;

    if (left === right) {
      break;
    }

    nodeArr[right].next = nodeArr[left];
    right--;
  }

  nodeArr[left].next = null;
}

const head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));

reorderList(head);



