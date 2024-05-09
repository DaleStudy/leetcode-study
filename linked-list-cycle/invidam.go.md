# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Makr elements as visited by setting a dirty bit.
Check Dirty bit to visited nodes.
# Approach
<!-- Describe your approach to solving the problem. -->
1. Initiate a constant value named `visited` over the input range. (In my case `-10001`.)
2. Start Visitng node. by head.
3. Check if the current node is `nil` or its value matches the visited value (Initially, the head node should not be visited value)
4. If node is valid(i.e. not `nil` and not `visited`), set the node's value as the visited value. 
5. Move to the next node and repeat step 3.

# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->


- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
(n = list's size)
# Code
```
const visited = -10001
func hasCycle(head *ListNode) bool {
    if head == nil {
        return false;
    }
    if head.Val == visited {
        return true;
    }
    head.Val = visited
    return hasCycle(head.Next)
}
```

- - -
# Institution
Use "The tortoise and hare" Algorithom.
# Approach
<!-- Describe your approach to solving the problem. -->
1. Designate two node to move at differnt speeds. One node should move faster (referred to as `fast`), and the other should move slower (`slow`)
2. Allow both nodes to iterate through the graph, with each node moving at its designated speed.
3. If the `fast` node catches up to the `slow` node (i.e. both node points to the same node at same point), the the graph contains a cycle.is cycle.
# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
# Code
```
func hasCycle(head *ListNode) bool {
    if head == nil || head.Next == nil {
        return false
    }
    for slow, fast := head, head.Next; fast != nil && fast.Next != nil; slow, fast = slow.Next, fast.Next.Next{
        if slow == fast {
            return true
        }
    }
    return false
}

```
# Learned
- 약한 부분이었던 투포인터 알고리즘에 대해 좀 더 생각해보았다.
- 반복문을 깔끔하게 작성하는 법을 고민해보았다.