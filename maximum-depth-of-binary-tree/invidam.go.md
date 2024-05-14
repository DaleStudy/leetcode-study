# Intuition
Recursuib is a natural method for iterating trees.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Child function can calculate the depth of its subtrees automatically.
2. Parent function only select the maximum of the two depths and return +1. (i.e. `+1` means parent's depth.)

# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity
    - $$O(logN)$$ (best case for balanced tree)
    - $$O(N)$$ (worst case for  skewed tree)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
(N: size of node.)
# Code
```
func maxDepth(root *TreeNode) int {
    if root == nil {
        return 0
    }
    return max(maxDepth(root.Left), maxDepth(root.Right)) + 1
}
```
- - -
# Intuition
Implement Stack can be troublesome, but it is effective to problem that require tracking depths or levels.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->
1. Maintain Element belonging to the same level in the stack.
2. While Iterating through the stack, remove the current level and save the next level.
- In GoLang, `range for loop` capture only first once. So We can maintain current level's easily.
3. increase depth while iterationg through all elements until the end.
# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity
    - $$O(logN)$$ (best case for balanced tree)
    - $$O(N)$$ (worst case for  skewed tree)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
(N: size of node.)

# Code
```
func maxDepth(root *TreeNode) int {
    if root == nil {
        return 0
    }
    depth := 0
    currLevel := []*TreeNode{root}
    
    for len(currLevel) != 0 {
        depth++
        for _, curr := range currLevel {
            if curr.Left != nil {
                currLevel = append(currLevel, curr.Left)
            }
            if curr.Right != nil {
                currLevel = append(currLevel, curr.Right)
            }
            currLevel = currLevel[1:]
        }
    }

    return depth
}
```