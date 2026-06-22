type MedianFinder struct {
	small *MaxHeap // lower half
	large *MinHeap // upper half
}

func Constructor() MedianFinder {
	small := &MaxHeap{}
	large := &MinHeap{}
	heap.Init(small)
	heap.Init(large)

	return MedianFinder{
		small: small,
		large: large,
	}
}

// SC: O(n)
// TC: O(m * log n)
func (this *MedianFinder) AddNum(num int) {
	if this.small.Len() == 0 || num <= (*this.small)[0] {
		heap.Push(this.small, num)
	} else {
		heap.Push(this.large, num)
	}

	// rebalance
	if this.small.Len() > this.large.Len()+1 {
		v := heap.Pop(this.small).(int)
		heap.Push(this.large, v)
	}

	if this.large.Len() > this.small.Len() {
		v := heap.Pop(this.large).(int)
		heap.Push(this.small, v)
	}
}

// TC: O(m)
func (this *MedianFinder) FindMedian() float64 {
	if this.small.Len() > this.large.Len() {
		return float64((*this.small)[0])
	}

	return float64((*this.small)[0]+(*this.large)[0]) / 2.0
}

type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type MaxHeap []int

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] } // reverse
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MaxHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}
