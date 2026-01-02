// 문제에서 주어진 ListNode
class ListNode {
    val: number
    next: ListNode | null

    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

function reverseList(head: ListNode | null): ListNode | null {
    let current = null;

    // 매번 새로운 노드를 생성하고, 지금까지 순회한 모든 결과를 이 새로운 노드의 next로 연결
    while (head !== null) {
        const newNode = new ListNode(head.val);
        newNode.next = current;
        current = newNode;
        head = head.next;
    }

    return current;
};
