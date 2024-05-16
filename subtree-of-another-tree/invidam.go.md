# Intuition (DFS & BFS)
<!-- Describe your first thoughts on how to solve this problem. -->
We need two main function: one to check the equality of nodes and the subtrees, and another to iterate through the main tree.

We will use both DFS and BFS methods to solve this problem.

Reference. [Same Tree](ttps://leetcode.com/problems/same-tree/solutions/5159658/go-simple-solution)

# Approach
<!-- Describe your approach to solving the problem. -->
1. Create a function that, while iterating using DFS(Recursion) or BFS(Queue),checks if the two trees are equal.
2. First, check if the two trees are equal. If not, iterate through the children of main tree. (`root.Left`, `root.Right`)
# Complexity (DFS)
- Time complexity: $$O(n * m)$$
  (This complexity is $$O(n * m)$$. because the `isSubtree()` iterates throuth all modes while **simultaneously** calling the `isEqualtree()` for each node.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O({h_n} + {h_m})$$
  (This complexity is determined. because the maximun depth of the call stack, which doesn't exceed the sum of heights of both trees.)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
func isEqualTree(root *TreeNode, subRoot *TreeNode) bool {
    if (root == nil) || (subRoot == nil) {
        return root == subRoot
    }

    return (root.Val == subRoot.Val) && isEqualTree(root.Left, subRoot.Left) && isEqualTree(root.Right, subRoot.Right)
}

func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
    if root == nil {
        //assert subRoot != nil
        return false
    }
    
    return isEqualTree(root, subRoot) || isSubtree(root.Left, subRoot) || isSubtree(root.Right, subRoot)
}
```
- - -
# Complexity (BFS)
- Time complexity: $$O(n * m)$$
  (This complexity is $$O(n * m)$$. because the `isSubtree()` iterates throuth all modes while **simultaneously** calling the `isEqualtree()` for each node.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O({h_n} + {h_m})$$
  (This complexity is determined. because the maximun sizes of the queues (`q`, `q1`, `q2`), which doesn't exceed the sum of sizes of both trees.)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
# Code
```
func isEqualTree(root *TreeNode, subRoot *TreeNode) bool {
    q1 := []*TreeNode{root}
    q2 := []*TreeNode{subRoot}

    for len(q1) != 0 {
        f1 := q1[0]
        f2 := q2[0]

        q1 = q1[1:]
        q2 = q2[1:]

        if (f1 == nil) && (f2 == nil) {
            continue
        }
        if (f1 == nil) || (f2 == nil) || (f1.Val != f2.Val) {
            return false
        }

        q1 = append(q1, f1.Left)
        q1 = append(q1, f1.Right)

        q2 = append(q2, f2.Left)
        q2 = append(q2, f2.Right)
    }
    
    return true
}

func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
    if root == nil {
        //assert subRoot != nil
        return false
    }

    q := []*TreeNode{root}

    for len(q) != 0 {
        node := q[0]
        q = q[1:]

        if node == nil {
            continue
        }
        if isEqualTree(node, subRoot) {
            return true
        }

        q = append(q, node.Left)
        q = append(q, node.Right)
    }

    return false
}
```