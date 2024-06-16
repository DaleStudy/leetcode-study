# Intuition
n번 째를 알기 위해 정보(몇 번째에 어떤 요소가 있는지)를 알아야 한다.
# Approach
1. 배열에 링크드 리스트 정보를 모두 넣는다.
2. 맨 앞 요소를 제거해야하는 경우 (`len(nodes) == n`) 헤드의 다음을 반환한다.
3. 뒤에서 `n`번째 요소(`len(nodes)-n`)의 앞과 뒤를 이어붙여 `n`번째 요소를 제거한다.
# Complexity
- Time complexity: $O(n)$
  - 링크드 리스트의 길이 `n`에 대하여, 이를 순회하는 비용이 발생한다.
- Space complexity: $O(n)$
  - 링크드 리스트의 길이 `n`에 대하여, 배열의 크기 `n`이 발생한다.

# Code
## Array
```go
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	nodes := make([]*ListNode, 0, 100)

	for curr := head; curr != nil; curr = curr.Next {
		nodes = append(nodes, curr)
	}

	if len(nodes) == n {
		return head.Next
	}

	nodes[len(nodes)-n-1].Next = nodes[len(nodes)-n].Next
	return head
}

```
# Intuition
배열의 모든 원소를 저장할 필요는 없어 보였다. 공간 복잡도를 줄일 방법을 알아보았다.
# Approach
모든 원소가 아니라, `n`번째의 이전(`prev`), 이후 (`next`)만을 저장하게 하였다.
# Complexity
- Time complexity: $O(n)$
    - 링크드 리스트의 길이 `n`에 대하여, 이를 순회하는 비용이 발생한다.
- Space complexity: $O(1)$
    - 2개의 요소만 유지하므로, `O(1)`이다.

# Code
## Two Pointer
```go
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	len := 0
	for curr := head; curr != nil; curr = curr.Next {
		len++
	}

	if len == n {
		return head.Next
	}

	var prev, curr, next *ListNode
	curr = head
	next = head.Next
	for i := 0; i+n < len; i++ {
		prev = curr
		curr = next
		next = next.Next
	}

	prev.Next = next
	return head
}

```