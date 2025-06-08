/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * 연결 리스트의 사이클 여부를 반환하는 함수
 * 시간복잡도: O(n)
 * 공간복잡도: O(1)
 * @param {ListNode} head
 * @return {boolean}
 */
const hasCycle = function(head) {
    let node = head;

    while (node?.next) {
        if (node.val === null) {
            return true;
        }
        node.val = null;
        node = node.next;
    }

    return false;
};

// 거북이와 토끼 알고리즘
// 시간복잡도: O(n)
// 공간복잡도: O(1)
const hasCycle = function(head) {
    let slow = head; // 한 번에 한 노드씩
    let fast = head; // 한 번에 두 노드씩

    while (fast?.next) {
        slow = slow.next;
        fast = fast.next.next;

        // 한 번에 두 노드씩 가는 fast가
        // 자신보다 느린 slow랑 같은 경우가 생긴다면
        // 사이클이 있다는 뜻
        if (slow === fast) {
            return true;
        }
    }

    return false;
};
