var reverseList = function (head) {
  let prev = null;
  let current = head;

  while (current !== null) {
    let nextTemp = current.next; // 1. 다음 노드 기억해둠
    current.next = prev; // 2. 포인터 방향 뒤집기
    prev = current; // 3. prev 이동
    current = nextTemp; // 4. current 이동
  }

  return prev; // prev가 새로운 head
};
