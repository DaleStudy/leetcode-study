# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Use DFS, referencing the property of a tree (i.e. child node is the root node of a subtree.)
# Approach
<!-- Describe your approach to solving the problem. -->
1. Visit the root node.
2. If visited node is `nil`, return `nil`
3. Swap left and right nodes.
4. Visit Swapped left and right nodes.
5. Repeat Step 2 ~ 4.
# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
func invertTree(root *TreeNode) *TreeNode {
    if root == nil {
        return nil
    }
    root.Left, root.Right = invertTree(root.Right), invertTree(root.Left)
    return root
}
```
- - -
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Visit, But Use BFS. (`for loop`)
# Approach
<!-- Describe your approach to solving the problem. -->
1. Create Queue and push root node to it.
2. If the queue is empty, return the `root` node.
3. Otherwise, pop the top node.
4. Swap the left and right children of the removed node.
5. Push swapped children.
4. Repeat Step
# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
type Queue[T any] struct {
    Index int
    Nodes []T
}

func NewQueue[T any]() Queue[T] {
    return Queue[T]{Nodes: make([]T, 0)}
}

func (q *Queue[T]) Push(node T) {
    q.Nodes = append(q.Nodes, node)    
}

func (q *Queue[T]) Pop() T {
    ret := q.Nodes[q.Index]
    q.Index++
    return ret
}

func (q *Queue[T]) IsEmpty() bool {
    return q.Index == len(q.Nodes)
}

func invertTree(root *TreeNode) *TreeNode {
    q := NewQueue[*TreeNode]()
    q.Push(root)
    for !q.IsEmpty() {
        t := q.Pop()
        if t == nil {
            continue
        }
        t.Left, t.Right = t.Right, t.Left
        
        q.Push(t.Left)
        q.Push(t.Right)
    }
    return root
}
```

# Learned
- 고언어에서 `a, b = b, a` 처럼 간결한 코딩이 가능하다.
- 포인터 타입과 일반 타입의 차이 (고언어에서는 일반 타입을 넘길 시 무조건 복사한다.)