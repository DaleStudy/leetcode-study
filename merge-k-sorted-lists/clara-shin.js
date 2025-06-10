/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
// 최적화된 K개 연결 리스트 병합 - 재귀 분할 정복
var mergeKLists = function (lists) {
  if (!lists || lists.length === 0) return null;
  if (lists.length === 1) return lists[0];

  return mergeListsRange(lists, 0, lists.length - 1);
};

// 범위 내의 리스트들을 재귀적으로 병합
function mergeListsRange(lists, start, end) {
  // 기저 조건: 하나의 리스트만 남은 경우
  if (start === end) {
    return lists[start];
  }

  // 두 개의 리스트만 남은 경우
  if (start + 1 === end) {
    return mergeTwoLists(lists[start], lists[end]);
  }

  // 중간점을 기준으로 분할
  let mid = Math.floor((start + end) / 2);
  let left = mergeListsRange(lists, start, mid);
  let right = mergeListsRange(lists, mid + 1, end);

  return mergeTwoLists(left, right);
}

// 두 개의 정렬된 연결 리스트를 병합 (최적화)
function mergeTwoLists(l1, l2) {
  // null 체크를 먼저 수행하여 불필요한 연산 방지
  if (!l1) return l2;
  if (!l2) return l1;

  // 더 작은 값을 가진 노드를 선택하고 재귀 호출
  if (l1.val <= l2.val) {
    l1.next = mergeTwoLists(l1.next, l2);
    return l1;
  } else {
    l2.next = mergeTwoLists(l1, l2.next);
    return l2;
  }
}
