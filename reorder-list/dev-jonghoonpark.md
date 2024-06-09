- 문제 : https://leetcode.com/problems/reorder-list/
- 블로그 링크 : https://algorithm.jonghoonpark.com/2024/06/10/leetcode-143

## 방법 1 (list 사용)

- time complexity : O(n)
- space complexity : O(n)

```java
class Solution {
    public void reorderList(ListNode head) {
        List<ListNode> list = new ArrayList<>();

        ListNode current = head;
        while (current.next != null) {
            list.add(current);
            current = current.next;
        }
        list.add(current);

        ListNode reordered = head;
        for (int i = 1; i < list.size(); i++) {
            if (i % 2 == 0) {
                reordered.next = list.get(i / 2);
            } else {
                reordered.next = list.get(list.size() - ((i / 2) + 1));
            }
            reordered = reordered.next;
        }
        reordered.next = null;
    }
}
```

## 방법 2 (pointer 사용)

- time complexity : O(n)
- space complexity : O(1)

```java
class Solution {
    public void reorderList(ListNode head) {
        ListNode prev = null;
        ListNode slow = head;
        ListNode fast = head;

        while(slow != null && fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }

        if (prev == null) {
            return;
        }

        prev.next = null;

        ListNode current = head;
        ListNode reversed = reverse(slow);
        while(true) {
            ListNode temp = current.next;

            if (reversed != null) {
                current.next = reversed;
                reversed = reversed.next;
                current = current.next;
            }

            if (temp != null) {
                current.next = temp;
                current = current.next;
            } else {
                current.next = reversed;
                break;
            }
        }
    }

    public ListNode reverse(ListNode treeNode) {
        ListNode current = treeNode;
        ListNode prev = null;
        while(current != null) {
            ListNode temp = current.next;
            current.next = prev;
            prev = current;
            current = temp;
        }
        return prev;
    }
}
```
