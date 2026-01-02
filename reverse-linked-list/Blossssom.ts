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
 * @param head - ListNode 구조체
 * @returns - 역순 head
 * @description
 * - 1차 시도: 단순 val 추출 후 역순으로 재 배치
 * - 2차 시도: head를 순회하며 스와핑, prev에 재 배치 하며 진행
 */

// function reverseList(head: ListNode | null): ListNode | null {
//   if (!head) {
//     return head;
//   }

//   let currentNode: ListNode | null = head;
//   let reversed: ListNode = new ListNode();
//   const saveArr = [];
//   while (currentNode?.val !== undefined) {
//     saveArr.push(currentNode.val);
//     currentNode = currentNode.next;
//   }

//   let check = reversed;
//   for (let i = saveArr.length; i > 0; i--) {
//     check.val = saveArr[i - 1];
//     if (i - 1) {
//       check.next = new ListNode();
//       check = check.next;
//     }
//   }

//   return reversed;
// }

function reverseList(head: ListNode | null): ListNode | null {
  if (!head) {
    return null;
  }

  let prevNode: ListNode | null = null;
  let nextNode: ListNode | null = null;

  console.log(head);
  while (head) {
    nextNode = head.next;
    head.next = prevNode;
    prevNode = head;
    head = nextNode;
    console.log(head, nextNode, prevNode);
  }

  return prevNode;
}

const head = new ListNode(
  0,
  new ListNode(1, new ListNode(4, new ListNode(-2)))
);

reverseList(head);


