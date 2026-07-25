/**
 * [풀이 개요]
 * - 시간복잡도 : O(n+m)
 * - 공간복잡도 : O(1)
 */
class Solution {
    /**
     * [문제 풀이 아이디어]
     * - 노드를 돌면서 더 작은 수를 다음으로 넣고, 커서를 다음으로 옮김
     * - ListNode 중 하나라도 비면 비지 않은 것을 죽 이어 붙임
     * - 이 경우 시간 복잡도는 두 노드의 길이의 합만큼 반복하게 되어 각 길이를 n, m 이라 했을 때 n+m이 됨
     * - 별도의 유의미한 공간 할당을 하지 않으므로 O(1)의 공간복잡도를 가짐.
     */
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        ListNode merged = new ListNode();
        ListNode cursor = merged;

        while(list1 != null && list2 != null) {
            if(list1.val <= list2.val) {
                cursor.next = list1;
                list1 = list1.next;
            } else {
                cursor.next = list2;
                list2 = list2.next;
            }
            cursor = cursor.next;
        }

        if(list1 != null) {
            cursor.next = list1;
        } else {
            cursor.next = list2;
        }
        return merged.next;
    }
}
