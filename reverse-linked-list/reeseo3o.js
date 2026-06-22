// Time Complexity: O(n) - 노드를 한 번만 순회
// Space Complexity: O(1) - 변수 3개(prev, current, next)만 사용
const reverseList = (head) => {
    let prev = null;
    let current = head;

    while (current !== null) {
        const next = current.next;
        current.next = prev;
        prev = current;
        current = next;
    }

    return prev;
};

// Time Complexity: O(n) - 노드 수만큼 재귀 호출
// Space Complexity: O(n) - 콜 스택이 노드 수만큼 쌓임
const reverseListRecursive = (head) => {
    if (head === null || head.next === null) return head;

    const newHead = reverseListRecursive(head.next);

    head.next.next = head;
    head.next = null;     

    return newHead;
};
