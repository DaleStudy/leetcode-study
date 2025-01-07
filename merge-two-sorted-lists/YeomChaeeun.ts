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
 * 두개의 리스트 정렬 - 재귀 알고리즘으로 접근
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n+m) - 모든 노드를 한 번씩 들르기 때문
 * - 공간 복잡도: O(n+m) - 함수 호출 스택이 재귀 호출로 인해 사용하기 때문
 * @param list1
 * @param list2
 */
function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    if(!(list1 && list2)) return list1 || list2
    if(list1.val < list2.val) {
        list1.next = mergeTwoLists(list1.next, list2);
        return list1
    } else {
        list2.next = mergeTwoLists(list2.next, list1);
        return list2
    }
}
