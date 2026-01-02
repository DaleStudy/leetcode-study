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

/**
  * list는 오름 차순으로 정렬되어 있기 때문에 두 개의 리스트의 head가 더 작은 값이 listNode의 next에 순서대로 들어오게 하면 됩니다.
  * list 둘 중하나가 없는 경우에는 나머지 다른 하나의 리스트를 반환합니다.
  * 두 헤드 중에서 더 작은 값의 next에 재귀적으로 다음 링크드 리스트를 넘겨주면서 비교하는 방법으로 문제를 해결했습니다
  *
*/

var mergeTwoLists = function(list1, list2) {
    if(!list1 || !list2) return list1 || list2

    if(list1.val < list2.val){
        list1.next = mergeTwoLists(list1.next,list2)
        return list1
    }

    list2.next = mergeTwoLists(list2.next,list1);

    return list2;
};
