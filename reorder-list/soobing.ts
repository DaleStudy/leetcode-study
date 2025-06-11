class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

/**
 Do not return anything, modify head in-place instead.
 */

function reverseList(head: ListNode | null) {
  let prev: ListNode | null = null;
  let cur: ListNode | null = head;

  while (cur) {
    const next = cur.next;
    cur.next = prev;
    prev = cur;
    cur = next;
  }

  return prev;
}

function reorderList(head: ListNode | null): void {
  if (!head || !head.next) return;

  // 1. 중간 지점 찾기
  let slow: ListNode | null = head;
  let fast: ListNode | null = head;

  while (fast && fast.next) {
    slow = slow!.next;
    fast = fast.next.next;
  }

  // 2. 리스트 절단
  const secondHead = slow!.next;
  slow!.next = null;

  // 3. 뒤쪽 리스트 뒤집기
  let second: ListNode | null = reverseList(secondHead);

  // 4. 병합
  let first: ListNode | null = head;

  while (second) {
    let tmp1 = first!.next;
    let tmp2 = second.next;

    first!.next = second;
    second.next = tmp1;

    first = tmp1;
    second = tmp2;
  }
}
