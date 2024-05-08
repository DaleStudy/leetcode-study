- https://leetcode.com/problems/linked-list-cycle
- time complexity : O(n)
- space complexity : O(1)
- https://algorithm.jonghoonpark.com/2024/02/15/leetcode-141

```java
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null) {
            return false;
        }

        ListNode p1 = head;
        ListNode p2 = head;
        while(p2 != null && p2.next != null) {
            p1 = p1.next;
            p2 = p2.next.next;

            if (p1 == p2) {
                return true;
            }
        }

        return false;
    }
}
```
