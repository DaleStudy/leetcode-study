/**
[문제풀이]
time: O(N + M), space: O(N + M)
- list1과 list2를 비교해서 list2의 수가 작으면 list1을 list2로 교체하자.
- 이때 list1은 list2의 자리에 들어갈 것이다.

[회고]
주어진 메서드를 dfs로 활용할 수도 있구나!
 */

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null || list2 == null) {
            return list1 == null ? list2 : list1;
        }

        if (list1.val > list2.val) {
            ListNode temp = list1;
            list1 = list2;
            list2 = temp;
        }

        list1.next = mergeTwoLists(list1.next, list2);
        return list1;
    }
}

