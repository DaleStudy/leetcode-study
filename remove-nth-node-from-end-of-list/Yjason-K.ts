/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number;
 *     next: ListNode | null;
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val === undefined ? 0 : val);
 *         this.next = (next === undefined ? null : next);
 *     }
 * }
 */

/**
 * 주어진 단일 연결 리스트에서 뒤에서 N번째 노드를 제거하는 함수
 * @param {ListNode | null} head - 연결 리스트의 시작 노드
 * @param {number} n - 뒤에서 n번째 노드
 * @returns {ListNode | null} - n번째 노드가 제거된 새로운 연결 리스트의 시작 노드
 * 
 * 시간 복잡도: O(N)
 * - 연결 리스트를 한 번 순회하여 길이를 찾고, 다시 한 번 순회하여 노드를 삭제 (2N)
 * 공간 복잡도: O(1)
 * - 추가적인 데이터 구조를 사용하지 않으며, 포인터만 사용하여 처리
 */
function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    let headlength = 0, cur = head;

    // 전체 길이 구하기
    while (cur) {
        headlength++;
        cur = cur.next;
    }

    // 삭제할 노드 위치 계산 (length - n)
    let dummy = new ListNode(0, head);
    cur = dummy;
    for (let i = 0; i < headlength - n; i++) {
        cur = cur.next;
    }

    // 노드 삭제 (n번째 노드 제거)
    cur.next = cur.next?.next || null;

    return dummy.next;
}

