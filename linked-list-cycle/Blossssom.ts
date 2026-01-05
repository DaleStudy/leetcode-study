class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

/**
 * @param head - linked list node
 * @returns - 순환되는 리스트인지?
 * @description
 * - 풀이 1. - 단순 순회 및 조회로 판단, 결국 visit에 다시 돌아온다면 순환
 * - 풀이 2. - 1칸, 2칸 포인터를 나눠 결국 순환이라면 돌고 돌아 만나는 과정을 통한 메모리 O(1)의 풀이
 */

// function hasCycle(head: ListNode | null): boolean {
//   const visit = new Set();
//   let current = head;

//   while (current) {
//     if (visit.has(current)) {
//       return true;
//     }

//     visit.add(current);
//     current = current.next;
//   }

//   return false;
// }

function hasCycle(head: ListNode | null): boolean {
  if (!head || !head.next) {
    return false;
  }

  let slow: ListNode | null = head;
  let fast: ListNode | null = head;

  while (fast && fast.next) {
    slow = slow!.next;
    fast = fast.next.next;

    if (slow === fast) {
      return true;
    }
  }
  return false;
}


