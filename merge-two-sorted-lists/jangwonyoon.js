/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */

/*
* 시간 복잡도(TC): O(n + m)
- n: list1의 길이, m: list2의 길이

* 공간 복잡도(SC): O(n + m)
- 재귀 호출 시 스택 메모리가 최대 n+m 깊이까지 쌓일 수 있음
*/

var mergeTwoLists = function(list1, list2) {
    // 예외처리 - 둘 중 하나라도 리스트가 비어있으면, 그냥 다른 리스트를 반환.
    if (!list1) return list2;
    if (!list2) return list1;

    // 현재 노드 값 비교
    if (list1.val <= list2.val) {
        // list1의 값이 더 작거나 같으면
        // list1의 결과 리스트의 head로 선택
        // list1.next는 남은 list1.next와 list2를 병합한 결과로 연결
        list1.next = mergeTwoLists(list1.next, list2);
        return list1;
    } else {
        // list2의 값이 더 작으면
        // list2의 결과를 리스트의 head로 선택
        // list2.next는 list1과 list2.next를 병합한 결과로 연결
        list2.next = mergeTwoLists(list1, list2.next);
        return list2;
    }
};
