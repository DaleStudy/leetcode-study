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
    /*
     * [풀이]
     * 1) 두 리스트가 이미 정렬된 상태 → 맨 앞에서부터 둘 중 더 작은 노드를 결과 리스트 rs에 이어 붙인다.
     * 2) 하나의 리스트가 끝날 때까지 반복한다. → 남은 리스트의 노드는 그대로 rs에 붙인다.  
     * 3) rs 헤드 노드의 next부터 반환한다.
     * [T.C]
     * 각 노드를 한 번씩 비교 → 연결(또는 연결만)하므로,
     * T.C = O(n+m) (n = list1의 길이, m = list2의 길이)
     * [S.C]
     * list1과 list2의 노드를 다시 연결하는 것이므로 추가적인 공간은 거의 필요하지 않으므로(rs의 head 정도?),
     * S.C = O(1)
     */

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode rs = new ListNode(0);
        ListNode rsNext = rs;
        // step 1
        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                rsNext.next = list1;
                list1 = list1.next;
            }
            else {
                rsNext.next = list2;
                list2 = list2.next;
            }
            rsNext = rsNext.next;
        }
        // step 2
        if (list1 != null) rsNext.next = list1;
        if (list2 != null) rsNext.next = list2;
        // step3
        return rs.next;
    }
}
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
    /*
     * [풀이]
     * 1) 두 리스트가 이미 정렬된 상태 → 맨 앞에서부터 둘 중 더 작은 노드를 결과 리스트 rs에 이어 붙인다.
     * 2) 하나의 리스트가 끝날 때까지 반복한다. → 남은 리스트의 노드는 그대로 rs에 붙인다.  
     * 3) rs 헤드 노드의 next부터 반환한다.
     * [T.C]
     * 각 노드를 한 번씩 비교 → 연결(또는 연결만)하므로,
     * T.C = O(n+m) (n = list1의 길이, m = list2의 길이)
     * [S.C]
     * list1과 list2의 노드를 다시 연결하는 것이므로 추가적인 공간은 거의 필요하지 않으므로(rs의 head 정도?),
     * S.C = O(1)
     */

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode rs = new ListNode(0);
        ListNode rsNext = rs;
        // step 1
        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                rsNext.next = list1;
                list1 = list1.next;
            }
            else {
                rsNext.next = list2;
                list2 = list2.next;
            }
            rsNext = rsNext.next;
        }
        // step 2
        if (list1 != null) rsNext.next = list1;
        if (list2 != null) rsNext.next = list2;
        // step3
        return rs.next;
    }
}

