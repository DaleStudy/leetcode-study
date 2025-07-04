// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

function reverseList(head: ListNode | null): ListNode | null {
    let prev: ListNode | null = null;
    let current = head;
    let next = null;

    while (current !== null) {
        const next = current.next;  // 1. 다음 노드를 기억해두고
        current.next = prev;        // 2. 현재 노드가 이전 노드를 가리키도록
        prev = current;             // 3. 이전 노드를 지금 노드로 업데이트
        current = next;             // 4. 현재 노드를 다음 노드로 이동
    }


    return prev;
};