class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

/**
 * @link https://leetcode.com/problems/linked-list-cycle/description/
 *
 * 접근 방법 :
 *  - 노드 순회하면서 방문한 노드에 저장
 *  - 방문할 노드가 이미 방문한 노드에 있으면 순환 구조 이므로 true 리턴
 *
 * 시간복잡도 : O(n)
 *  - 순환 이전 노드의 개수 n만큼 순회하면서 순환 여부 확인
 *
 * 공간복잡도 : O(n)
 *  - visited set에 순환되기 이전 노드 n개 저장
 */
function hasCycle(head: ListNode | null): boolean {
  const visited = new Set<ListNode>();
  let current = head;

  while (current !== null) {
    if (visited.has(current)) return true;

    visited.add(current);
    current = current.next;
  }

  return false;
}

/*
 * 접근 방법 :
 *  - 공간복잡도 O(1)로 풀이
 *  - 사이클이 있으면 두 포인터가 결국 같은 노드를 가리키게 되므로 투 포인터 사용
 *  - 사이클이 없는 경우를 위해서 tail노드의 null체크를 해야함
 *
 * 시간복잡도 : O(n)
 *  - 순환 이전 노드의 개수 n만큼 순회하면서 순환 여부 확인
 *
 * 공간복잡도 : O(1)
 *  - 추가 메모리없이 slow, fast 포인터만 사용하므로 O(1)
 */
function hasCycle(head: ListNode | null): boolean {
  let slow = head;
  let fast = head;

  while (fast !== null && fast.next !== null) {
    slow = slow.next;
    fast = fast.next.next;

    if (slow === fast) return true;
  }

  return false;
}
