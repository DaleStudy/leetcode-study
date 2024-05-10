# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
링크드리스트 --> 반복문 or 재귀호출이 떠올랐다.
# Approach
<!-- Describe your approach to solving the problem. -->
- 재귀 호출과 반복문 사이에서 고민하였다.
- 새로운 노드를 만들고, 작은 노드들을 이어 붙였다. (V1_1, V2_1)
- 새로운 노드의 생성 없이, 기존 노드들을 연결하여 해결할 수도 있었다. (V1_2, V2_2)
# Complexity
- Time complexity: $$O(N+M)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(N+M)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

(N,M은 각각 두 링크드리스트의 길이)
# Code
```
func mergeTwoListsV1(list1 *ListNode, list2 *ListNode) *ListNode {
	if list1 == nil && list2 == nil {
		return nil
	} else if list1 != nil {
		return list1
	} else if list2 != nil {
		return list2
	}
	// assert list1, list2 is not nil
	var val int
	if list1.Val < list2.Val {
		val = list1.Val
		list1 = list1.Next
	} else {
		val = list2.Val
		list2 = list2.Next
	}

	return &ListNode{Val: val, Next: mergeTwoListsV1(list1, list2)}
}

func mergeTwoListsV1_2(list1 *ListNode, list2 *ListNode) *ListNode {
	if list1 == nil {
		return list2
	} else if list2 == nil {
		return list1
	}

	if list1.Val < list2.Val {
		list1.Next = mergeTwoListsV1_2(list1.Next, list2)
		return list1
	} else {
		list2.Next = mergeTwoListsV1_2(list1, list2.Next)
		return list2
	}
}

func mergeTwoListsV2_1(list1 *ListNode, list2 *ListNode) *ListNode {
	var head = &ListNode{}
	curr := head

	for list1 != nil && list2 != nil {
		if list1.Val < list2.Val {
			curr.Next = list1
			list1 = list1.Next
		} else {
			curr.Next = list2
			list2 = list2.Next
		}
		curr = curr.Next
	}

	if list1 != nil {
		curr.Next = list1
	} else if list2 != nil {
		curr.Next = list2
	}

	return head.Next
}

func mergeTwoListsV2_2(list1 *ListNode, list2 *ListNode) *ListNode {
	if list1 == nil {
		return list2
	} else if list2 == nil {
		return list1
	}

	head := list1
	if list1.Val > list2.Val {
		head = list2
		list2 = list2.Next
	} else {
		list1 = list1.Next
	}
	curr := head

	for list1 != nil && list2 != nil {
		if list1.Val < list2.Val {
			curr.Next = list1
			list1 = list1.Next
		} else {
			curr.Next = list2
			list2 = list2.Next
		}
		curr = curr.Next
	}

	if list1 != nil {
		curr.Next = list1
	} else if list2 != nil {
		curr.Next = list2
	}

	return head
}

```