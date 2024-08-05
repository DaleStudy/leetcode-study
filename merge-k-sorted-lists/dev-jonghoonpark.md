- 문제: https://leetcode.com/problems/merge-k-sorted-lists/
- 풀이: https://algorithm.jonghoonpark.com/2024/02/19/leetcode-23

## 풀이 1

lists를 순회하면서 가장 작은 수를 가진 노드를 찾고, 그 노드를 mergedList 에 추가한다.

```java
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode mergedList = new ListNode();

        ListNode current = mergedList;

        while (true) {
            int minIndex = -1;
            int currentMin = Integer.MAX_VALUE;

            for (int i = 0; i < lists.length; i++) {
                ListNode node = lists[i];
                if (node != null && node.val < currentMin) {
                    minIndex = i;
                    currentMin = node.val;
                }
            }

            if (minIndex == -1) {
                break;
            }

            current.next = lists[minIndex];
            lists[minIndex] = lists[minIndex].next;

            current = current.next;
        }

        return mergedList.next;
    }
}
```

### TC, SC

문제에서 다음과 같이 정의가 되어있다.

```
k == lists.length
```

추가적으로 n을 list 들의 item 수의 총합 이라고 정의하였을 때

시간복잡도는 `O(n * k)`, 공간복잡도는 `O(n)` 이다.

## 풀이 2: stream 사용해서 풀기

우선 다 하나의 리스트에 합친 후 정렬한다.

```java
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        List<ListNode> mergedListNode = new ArrayList<>();
        for (ListNode listNode : lists) {
            ListNode current = listNode;
            while (current != null) {
                mergedListNode.add(current);
                current = current.next;
            }
        }

        ListNode listNode = new ListNode();
        final ListNode[] current = {listNode};
        mergedListNode.stream().sorted(Comparator.comparingInt(node -> node.val))
                .forEach(node -> {
                    current[0].next = node;
                    current[0] = current[0].next;
                });

        return listNode.next;
    }
}
```

예상과는 다르게 오히려 이 방식이 더 적은 실행시간으로 완료되었다.

### TC, SC

n을 list 들의 item 수의 총합 이라고 정의하였을 때, 시간복잡도는 `O(nlogn)`, 공간복잡도는 `O(n)` 이다.
