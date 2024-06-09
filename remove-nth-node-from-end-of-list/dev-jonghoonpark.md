- 문제: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
- time complexity : O(n)
- space complexity : O(1)
- 블로그 링크 : https://algorithm.jonghoonpark.com/2024/06/10/leetcode-19

```java
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode current = head;
        int length = 0;
        while(current != null) {
            length++;
            current = current.next;
        }

        if (length == 1) {
            return null;
        }

        if (length == n) {
            return head.next;
        }

        int removeIndex = length - n;
        int pointer = 0;
        current = head;
        while (pointer < removeIndex - 1) {
            current = current.next;
            pointer++;
        }
        current.next = current.next.next;
        return head;
    }
}
```
