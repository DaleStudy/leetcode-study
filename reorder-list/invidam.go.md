# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
재귀함수를 이용한 풀이를 생각하였으나, 맨 뒤에 있는 요소가 2번째 까지 장거리 이동해야 하므로 맨 뒤를 `O(1)`에 접근하기 위한 방법(배열을 떠올림)이 필요할 것이다.
<!-- Describe your approach to solving the problem. -->
1. Deque안에 모든 노드들을 삽입한다. 
    - 코드에서는 배열(`nodes`)와 두 인덱스(`i`, `j`)가 `Deque`의 역할을 대신한다.
2. 맨 앞, 맨 뒤에서 하나씩을 뺀다. (`f`, `b`)
3. 맨 앞 요소 뒤에 맨 뒤 요소를 넣는다. (`f` --> `b` -- (기존) `f.Next`)
3. reorder이후 맨 마지막 요소에 `nil`을 추가해 종료 지점을 만든다.
# Complexity
- Time complexity: $O(n)$
  - 링크드 리스트의 길이 `n`에 대하여, 링크드리스트 순회와 배열 순회 비용 `n`이 발생한다.
- Space complexity: $O(n)$
  - 링크드 리스트의 길이 `n`에 대하여, 배열(`nodes`) 생성에 비용 `n`이 발생한다.
# Code
## Two Pointer(Deque)
```go
func reorderListv1(head *ListNode) {
	nodes := make([]*ListNode, 0, 25)
	for curr := head; curr != nil; curr = curr.Next {
		nodes = append(nodes, curr)
	}

	i, j := 0, len(nodes)-1
	for i < j {
		nodes[j].Next = nodes[i].Next
		nodes[i].Next = nodes[j]

		i++
		j--
	}
	nodes[i].Next = nil
}

```

## 다른 풀이
: 솔루션을 보며 뒤쪽 절반을 `reverse()`하여 해결하는 솔루션이 더욱 직관적으로 느껴졌다.

```go
func reverse(node *ListNode) *ListNode {
	var prev *ListNode
	curr := node
	for curr != nil {
		next := curr.Next
		curr.Next = prev
		prev = curr

		curr = next
	}
	return prev
}

func reorderList(head *ListNode) {
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
	}

	curr, rCurr := head, reverse(slow.Next)
	slow.Next = nil
	for curr != nil && rCurr != nil {
		next, rNext := curr.Next, rCurr.Next

		rCurr.Next = next
		curr.Next = rCurr

		curr, rCurr = next, rNext
	}
}

```
: 인덱스 조절하는 게 꽤나 어려워서 솔루션을 참고했다...