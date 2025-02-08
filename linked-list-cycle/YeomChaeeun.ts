/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */
/**
 * 순환되는 링크드 리스트 찾기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n)
 * - 공간 복잡도: O(1)
 * @param head
 */
function hasCycle(head: ListNode | null): boolean {
    // 1. set을 이용한 풀이
    // 시간 복잡도: O(n) , 공간 복잡도: O(n)
    // let set = new Set();
    // while(head !== null) {
    //     // set에 이미 존재하는지 확인
    //     if(set.has(head)) return true
    //     set.add(head)
    //     head = head.next
    // }

    // 2. 토끼와 거북이 알고리즘
    // 포인터를 2개 이동하는 방법
    let slow = head
    let fast = head

    while (fast?.next) {
        slow = slow.next
        fast = fast.next.next

        if(slow === fast) {
            return true
        }
    }

    return false
}
