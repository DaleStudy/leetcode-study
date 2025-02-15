/**
 * Source: https://leetcode.com/problems/merge-k-sorted-lists/
 * 풀이방법: 모든 리스트들을 한곳에 넣고 재배치
 *
 * 시간복잡도: O(NlogN) - 모든 리스트를 순회(N), 정렬(NlogN) 하는데 드는 시간 고려
 * 공간복잡도: O(N) - 기존 배열을 저장할 공간만 필요
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

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
  if (!lists?.length) return null;
  let merged = [];

  for (let i = 0; i < lists.length; i++) {
    let cursor = lists[i];
    while (cursor != null) {
      merged.push(cursor.val);
      cursor = cursor.next;
    }
  }
  let sorted = merged.sort((a, b) => (a < b ? -1 : 1));
  let head = null;
  let tail = null;

  for (let i = 0; i < sorted.length; i++) {
    const node = new ListNode(sorted[i], null);
    if (head === null) {
      head = node;
      tail = node;
    } else {
      tail.next = node;
      tail = node;
    }
  }

  return head;
}
