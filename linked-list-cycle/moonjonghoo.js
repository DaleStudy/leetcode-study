// ## 🔗 문제 링크
// https://leetcode.com/problems/linked-list-cycle/

// ## ✨ 문제 요약
// 연결 리스트에 사이클이 있는지 여부를 판별하는 문제입니다.

// ## ✅ 풀이 방법
// ### 1. HashSet 사용
// - 방문한 노드를 저장하고 중복 방문 시 true
// - 시간복잡도: O(n), 공간복잡도: O(n)

var hasCycle = function (head) {
  let visited = new Set();
  let current = head;

  while (current !== null) {
    if (visited.has(current)) {
      return true; // 이미 방문한 노드를 다시 방문 => 사이클 존재
    }
    visited.add(current);
    current = current.next;
  }

  return false; // 끝까지 갔다면 사이클 없음
};

// ### 2. Two Pointer 방식 (Floyd's Algorithm)
// - slow, fast 포인터 이용
// - 만날 경우 → 사이클 존재
// - 끝까지 도달 → 사이클 없음
// - 시간복잡도: O(n), 공간복잡도: O(1)

var hasCycle = function (head) {
  let slow = head;
  let fast = head;

  while (fast !== null && fast.next !== null) {
    slow = slow.next; // 한 칸 이동
    fast = fast.next.next; // 두 칸 이동

    if (slow === fast) {
      return true; // 만났다면 사이클 존재!
    }
  }

  return false; // 끝까지 갔다면 사이클 없음
};
