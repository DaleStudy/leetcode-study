- https://leetcode.com/problems/reverse-linked-list/
- time complexity : O(n)
- space complexity : O(1)
- https://algorithm.jonghoonpark.com/2024/02/15/leetcode-206

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null) {
            return null;
        }

        ListNode p1 = head;
        ListNode p2 = head.next;
        p1.next = null;

        while (p2 != null) {
            ListNode temp = p2.next;
            p2.next = p1;
            p1 = p2;
            p2 = temp;
        }

        return p1;
    }
}
```
