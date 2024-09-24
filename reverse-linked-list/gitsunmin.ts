/**
 * https://leetcode.com/problems/reverse-linked-list
 * time complexity : O(n)
 * space complexity : O(1)
 */

class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

/** Not used in real problem */
const arrayToListNode = (arr: number[]): ListNode | null => {
    if (arr.length === 0) return null;
    let head = new ListNode(arr[0]);
    let curr = head;
    for (let i = 1; i < arr.length; i++) {
        curr.next = new ListNode(arr[i]);
        curr = curr.next;
    }
    return head;
}

/* Main function */
function reverseList(head: ListNode | null): ListNode | null {
    let prev: ListNode | null = null;
    let current = head;

    while (current !== null) {
        const next = current.next;
        current.next = prev;
        prev = current;
        current = next;
    }

    return prev;
};

/* Examples */
const input1 = [1, 2, 3, 4, 5];
const input2 = [1, 2];
const input3 = [];

console.log('output1:', reverseList(arrayToListNode(input1)));
console.log('output2:', reverseList(arrayToListNode(input2)));
console.log('output3:', reverseList(arrayToListNode(input3)));
