# Intuition (DFS, Recursion)
<!-- Describe your first thoughts on how to solve this problem. -->
Recursion is natural method to iterate trees. (Particularly, multiple trees!)
# Approach
<!-- Describe your approach to solving the problem. -->
1. Child nodes(i.e. Left and Right) are compared eqaulity with their subtrees.
2. Parent nodes check their own values (`Val`) and their children's comparisions.

(Tip: Comparing the values of nodes before recursion is more efficient. due to **short circuit**, which stops further evaluation(`isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)`) when the outcome is already determined by comparing `p.Val == q.Val`)
# Complexity
- Time complexity: $$O(n+m)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(h_n + h_m)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

(n and m are number of nodes in trees p and q. $$h_n$$ and $$h_m$$ are their heights.)
# Code
```
func isSameTree(p *TreeNode, q *TreeNode) bool {
    if p == nil || q == nil {
        return p == nil && q == nil
    }

    return p.Val == q.Val && isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
}
```
- - -
# BFS
# Approach
<!-- Describe your approach to solving the problem. -->
1. Like a typical BFS solution, Create Queue and iterate through the tree. However, in this case, mulitple queues are required.
2. While Iterating, Check equality two nodes in p and q.
# Complexity
- Time complexity: $$O(n+m)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n + m)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

(n and m are number of nodes in trees p and q.)
# Code
```
func updateQueue(node *TreeNode, queue []*TreeNode) []*TreeNode {
	queue = append(queue, node.Left)
	queue = append(queue, node.Right)

	return queue
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil || q == nil {
		return p == nil && q == nil
	}
	pQueue := []*TreeNode{p}
	qQueue := []*TreeNode{q}

	for len(pQueue) != 0 {
        pCurr := pQueue[0]
        qCurr := qQueue[0]

        pQueue = pQueue[1:]
        qQueue = qQueue[1:]

        if pCurr == nil && qCurr == nil {
            continue
        }

        if (pCurr == nil || qCurr == nil) || (pCurr.Val != qCurr.Val) {
            return false
        }
        pQueue = updateQueue(pCurr, pQueue)
        qQueue = updateQueue(qCurr, qQueue)
	}

	return true
}
```

# What I learned
- Short circuit In Go.
- Function couldn't update original value (like `updateQueue()'s queue`)