# Intuition
두 변수간의 Swap이 떠올랐다.

# Approach
<!-- Describe your approach to solving the problem. -->
- 링크드 리스트의 "언제나 자신의 값과 다음 노드의 주소를 유지한다"는 특성이 재귀 함수를 유용하게 쓸 수 있다고 판단했다.
# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

(N은 링크드리스트의 길이)
*/

# Code
- V1은 재귀호출, V2는 반복문 활용을 한 경우이다.
- V3은 V1을 개선하여, 하나의 함수만으로 간결하게 해결했다.
```

func reverseListV3(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	newHead := reverseList(head.Next)

	head.Next.Next = head
	head.Next = nil

	return newHead
}

func reverseListV2(head *ListNode) *ListNode {
	var prev *ListNode
	curr := head
	for curr != nil {
		next := curr.Next
		curr.Next = prev
		prev = curr
		curr = next
	}
	return prev
}

func reverseNodeAllV1(head *ListNode, prev *ListNode) *ListNode {
	if head == nil {
		return prev
	}
	next := head.Next
	head.Next = prev
	return reverseNodeAllV1(next, head)
}
func reverseListV1(head *ListNode) *ListNode {
	return reverseNodeAllV1(head, nil)
}
```

# Remind
재귀 함수의 특성(자기 자신을 호출한 이후 이전의 코드를 실행할 수 있다는 점)을 활용해 간결한 코딩이 가능하다.