function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

// 첫 번째 시도
// 시간복잡도: O(n)
// 공간복잡도: O(n)
/**
 * 단방향 연결 리스트를 reverse하여 반환하는 함수
 * @param {ListNode} head
 * @return {ListNode}
 */
const reverseList = function (head) {
    const newHead = new ListNode();

    function _reverseList(head) {
        if (!head) {
            return newHead;
        }

        const reversedHead = _reverseList(head.next);
        reversedHead.next = new ListNode(head.val, null);

        return reversedHead.next;
    }

    _reverseList(head);
    return newHead.next;
};


// 두 번째 시도
// 시간복잡도: O(n)
// 공간복잡도: O(1)
const reverseList = function (head) {
    let current = head;
    let prev = null;

    while (current) {
        const next = current.next;
        current.next = prev;
        prev = current;
        current = next;
    }

    return prev;
};
