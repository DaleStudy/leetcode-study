- https://leetcode.com/problems/merge-two-sorted-lists/
- time complexity : O(n)
- space complexity : O(n)
- https://algorithm.jonghoonpark.com/2024/05/01/leetcode-21

```java
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head = null;
        ListNode tail = null;

        while(!(list1 == null && list2 == null)) {
            ListNode selected;
            if (list1 == null) {
                selected = list2;
                list2 = list2.next;
            } else if (list2 == null) {
                selected = list1;
                list1 = list1.next;
            } else if (list1.val < list2.val) {
                selected = list1;
                list1 = list1.next;
            } else {
                selected = list2;
                list2 = list2.next;
            }

            ListNode newNode = new ListNode(selected.val);
            if(head == null) {
                head = newNode;
            } else {
                tail.next = newNode;
            }

            tail = newNode;
        }

        return head;
    }
}
```
