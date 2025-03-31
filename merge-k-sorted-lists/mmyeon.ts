class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

/**
 * @link https://leetcode.com/problems/merge-k-sorted-lists/description/
 *
 * 접근 방법 :
 *  - 리스트를 배열에 넣고, 최소값을 가진 노드 찾기
 *  - 최소값 노드를 더미 노드에 연결한 뒤 제거하고, 최소값 노드의 다음 노드를 다시 배열에 추가하기
 *  - 배열 길이가 0이 될 때까지 반복하기
 *
 * 시간복잡도 : O(n * k)
 *  - n = 총 노드의 개수
 *  - k = 리스트의 개수
 *  - 최소값 찾고, 최소값 제거하는 로직: O(k)
 *  - 위의 연산을 총 n번 실행
 *
 * 공간복잡도 : O(k)
 * - k = 리스트 개수
 * - minList 배열의 크기가 최대 K개까지 유지
 *
 */

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
  const minList: ListNode[] = [];

  for (const list of lists) {
    if (list !== null) minList.push(list);
  }

  const dummy = new ListNode();
  let tail = dummy;

  while (minList.length > 0) {
    const minIndex = getMinIndex(minList);
    const minNode = minList.splice(minIndex, 1)[0];

    tail.next = minNode;
    tail = tail.next;

    if (minNode.next) minList.push(minNode.next);
  }

  return dummy.next;
}

function getMinIndex(nodes: ListNode[]): number {
  let minIndex = 0;

  for (let i = 1; i < nodes.length; i++) {
    if (nodes[i].val < nodes[minIndex].val) minIndex = i;
  }

  return minIndex;
}
