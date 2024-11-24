/*
풀이 1
- lists를 순회하면서 순서대로 링크드리스트 두 개를 짝 지어 병합하는 방식으로 풀이할 수 있습니다

Big O
- K: 배열 lists의 길이
- N: 모든 링크드리스트의 노드 개수의 합
- n_i: i번 인덱스 링크드리스트의 노드의 개수
- Time complexity: O(KN)
  - K-1 번의 병합을 진행합니다
  - i번째 병합 때, 병합하는 두 링크드리스트는 각각 𝚺(n_(i-1)), n_i입니다
    이 때 𝚺(n_(i-1))의 상한을 고려한다면 두 링크드리스트의 병합에 걸리는 시간복잡도는 O(N)입니다
  - O((K-1)N) = O(KN)
  - 풀이 2로 시간복잡도를 O((logK)N)으로 최적화할 수 있습니다
- Space complexity: O(1)
  - res, dummy, curr 등의 추가적인 포인터를 생성하긴 하지만 기존에 주어져 있던 ListNode의 Next만 조작하므로 K, N과 상관 없이 공간복잡도는 상수값을 가집니다
*/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func mergeKLists(lists []*ListNode) *ListNode {
	n := len(lists)

	if n == 0 {
		return nil
	}

	res := lists[0]
	for i := 1; i < n; i++ {
		res = mergeTwoLists(res, lists[i])
	}
	return res
}

func mergeTwoLists(first *ListNode, second *ListNode) *ListNode {
	dummy := &ListNode{}
	curr := dummy

	for first != nil && second != nil {
		if first.Val < second.Val {
			curr.Next = first
			first = first.Next
		} else {
			curr.Next = second
			second = second.Next
		}
		curr = curr.Next
	}

	if first != nil {
		curr.Next = first
	}
	if second != nil {
		curr.Next = second
	}

	return dummy.Next
}


/*
풀이 2
- Divide and Conquer 방식으로 시간복잡도를 최적화할 수 있습니다
- 하지만 공간복잡도 측면에서는 trade-off가 있습니다

Big O
- K: 배열 lists의 길이
- N: 모든 링크드리스트의 노드 개수의 합
- Time complexity: O((logK)N)
  - lists를 반으로 쪼개 가면서 재귀호출을 진행하므로 재귀호출은 logK 레벨에 걸쳐 이루어집니다 -> O(logK)
  - 각 계층마다 우리는 모든 노드를 최대 한 번씩 조회합니다 -> O(N)
- Space complexity: O(logK)
  - 풀이 1과 비슷하지만 재귀호출 스택을 고려해야 합니다
*/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func mergeKLists(lists []*ListNode) *ListNode {
	n := len(lists)

	if n == 0 {
		return nil
	}
	if n == 1 {
		return lists[0]
	}

	left := mergeKLists(lists[:n/2])
	right := mergeKLists(lists[n/2:])

	return mergeTwoLists(left, right)
}

func mergeTwoLists(first *ListNode, second *ListNode) *ListNode {
	dummy := &ListNode{}
	curr := dummy

	for first != nil && second != nil {
		if first.Val < second.Val {
			curr.Next = first
			first = first.Next
		} else {
			curr.Next = second
			second = second.Next
		}
		curr = curr.Next
	}

	if first != nil {
		curr.Next = first
	}
	if second != nil {
		curr.Next = second
	}

	return dummy.Next
}
