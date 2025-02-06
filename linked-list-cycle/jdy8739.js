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
var hasCycle = function(head) {
    if (!head?.next) {
        return false;
    }

    let turtle = head;
    let rabbit = head;

    while (turtle.next && rabbit.next) {
        if (turtle === rabbit) {
            return true;
        }

        turtle = turtle.next;
        rabbit = rabbit.next.next;
    }

    return false;
};

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
    if (!head?.next || !head?.next.next) {
        return false;
    }

    let turtle = head;
    let rabbit = head;

    while (turtle && rabbit?.next) {
        turtle = turtle.next;
        rabbit = rabbit.next.next;

        if (turtle === rabbit) {
            return true;
        }
    }

    return false;
};

// 시간복잡도 O(n) -> 최대 리스트의 노드 수 만큼 while문이 반복되므로
// 공간복잡도 O(1) -> 고정된 두 변수 turtle, rabbit을 사용하기때문에 (거북이와 토끼 알고리즘 사용)
