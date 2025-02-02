/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
    if (!head?.next) {
        return false;
    }

    let current = head;

    const set = new Set();

    while (current.next) {
        if (set.has(current)) {
            return true;
        }

        set.add(current);
        current = current.next;
    }

    return false;
};

// 시간복잡도 O(n) -> 최대 리스트의 노드 수 만큼 while문이 반복되므로
// 공간복잡도 O(n) -> set에 최대 리스트의 노드 수 만큼 size가 증가되므로
