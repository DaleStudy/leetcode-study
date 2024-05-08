- https://leetcode.com/problems/merge-two-sorted-lists/
- time complexity : O(n)
- space complexity : O(n)
- https://algorithm.jonghoonpark.com/2024/05/01/leetcode-21

```java
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head = new ListNode(0);
        ListNode tail = head;

        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                tail.next = list1;
                list1 = list1.next;
            } else {
                tail.next = list2;
                list2 = list2.next;
            }
            tail = tail.next;
        }

        if (list1 != null) {
            tail.next = list1;
        } else {
            tail.next = list2;
        }

        return head.next;
    }
}
```
