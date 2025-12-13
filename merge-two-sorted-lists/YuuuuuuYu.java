/**
 * Runtime: 0ms
 * Time Complexity: O(n)
 * - list1.length + list2.length
 *
 * Memory: 44.28MB
 * Space Complexity: O(1)
 *
 * Approach: 빈 node를 만들고 list1, list2의 현재 값을 비교하여 더 작은 값을 추가
 *
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) return list2;
        else if (list2 == null) return list1;

        ListNode result = new ListNode();
        ListNode currentNode = result;
        while (list1 != null && list2 != null) {
            if (list1.val > list2.val) {
                currentNode.next = list2;
                list2 = list2.next;
            } else {
                currentNode.next = list1;
                list1 = list1.next;
            }

            currentNode = currentNode.next;
        }

        currentNode.next = list1 != null ? list1 : list2;
        return result.next;
    }
}
