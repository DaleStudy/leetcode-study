# Intuition
높이가 양 끝 라인에 의해 결정된다는 것을 응용하여 투포인터 해결법을 고안했다.

# Approach
1. 높이(`h`)를 0 ~ 최대까지 순회한다.
2. 높이를 초과하는 선까지 양 끝(`l`, `r`)을 조절한다.
3. 조절한 양 끝을 최댓값 갱신에 이용한다.

# Complexity
- Time complexity: $O(n)$
    - 배열의 크기 `n`에 대하여, 반복문이 배열의 인덱스를 모두 순회하면 종료되기에 (`l < r`이 깨질 때) 이에 따라 시간복잡도가 결정된다.
- Space complexity: $O(n), inline$
    - 배열의 크기 `n`에 대하여, 입력값으로 배열을 받으니 inline인 n이 소요된다.

# Code
## Two Pointer
```go
func maxArea(height []int) int {
	l, r := 0, len(height)-1
	var maxArea int
	for l < r {
		minH := min(height[l], height[r])
		maxArea = max(minH*(r-l), maxArea)

		if minH == height[l] {
			l++
		} else {
			r--
		}
	}

	return maxArea
}

```
: 원래는 deque를 이용해 해결했는데, 솔루션의 투포인터를 이용한 것과 동일한 방식이어서 깔끔한 후자로 수정했다.

## Deque
```go
type Deque struct {
	Nodes []int
}

func NewDeque(arr []int) Deque {
	return Deque{Nodes: arr}
}

func (dq *Deque) PushFront(node int) {
	dq.Nodes = append([]int{node}, dq.Nodes...)
}

func (dq *Deque) PushBack(node int) {
	dq.Nodes = append(dq.Nodes, node)
}
func (dq *Deque) Front() int {
	return dq.Nodes[0]
}

func (dq *Deque) Back() int {
	return dq.Nodes[len(dq.Nodes)-1]
}

func (dq *Deque) PopFront() int {
	ret := dq.Front()

	dq.Nodes = dq.Nodes[1:]

	return ret
}

func (dq *Deque) PopBack() int {
	ret := dq.Back()

	dq.Nodes = dq.Nodes[0 : len(dq.Nodes)-1]

	return ret
}

func (dq *Deque) Size() int {
	return len(dq.Nodes)
}

func maxArea(height []int) int {
	dq := NewDeque(height)

	var max int
	for h := 0; dq.Size() > 1; h++ {
		for dq.Size() != 0 && dq.Front() < h {
			dq.PopFront()
		}
		for dq.Size() != 0 && dq.Back() < h {
			dq.PopBack()
		}

		area := h * (dq.Size() - 1)

		if area > max {
			max = area
		}
	}

	return max
}

```