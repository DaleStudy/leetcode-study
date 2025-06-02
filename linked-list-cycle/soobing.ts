/**
 * 문제 설명
 * - 링크드리스트 내에 cycle이 존재하는지 확인하는 문제
 *
 * 아이디어
 * - 링크드리스트를 끝까지 순회하면서 방문한 노드를 저장하고, 방문한 노드가 존재하면 cycle이 존재하는 것으로 판단
 * - 시간복잡도: O(n), 공간복잡도 O(n)
 *
 */

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function hasCycle(head: ListNode | null): boolean {
  const visited = new Set<ListNode>();

  while (head) {
    if (visited.has(head)) {
      return true;
    } else {
      visited.add(head);
      head = head.next;
    }
  }
  return false;
}

/**
 * 공간복잡도 O(1) 로도 풀 수 있음.
 */

// function hasCycle(head: ListNode | null): boolean {
//   let slow = head;
//   let fast = head;

//   while (fast && fast.next) {
//     slow = slow!.next;
//     fast = fast.next.next!;

//     if (slow === fast) {
//       return true;
//     }
//   }

//   return false;
// }
