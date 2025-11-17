type MedianFinder struct {
    lq Heap
    rq Heap
}

type Heap []int // S(n) = O(n)

func (pq Heap) Len() int {return len(pq)}
func (pq Heap) Less(i, j int) bool {return pq[i] < pq[j]}
func (pq Heap) Swap(i, j int) {pq[i], pq[j] = pq[j], pq[i]}
func (pq *Heap) Push(x any) {*pq = append(*pq, x.(int))}
func (pq *Heap) Pop() any {
    x := (*pq)[len(*pq) - 1]
    *pq = (*pq)[: len(*pq) - 1]
    return x
}


func Constructor() MedianFinder {
    return MedianFinder{}
}


func (this *MedianFinder) AddNum(num int)  { // T(n) = O(logn)
    if len(this.rq) != 0 && this.rq[0] <= num {
        heap.Push(&this.rq, num)
        if len(this.lq) == len(this.rq) - 1 {
            heap.Push(&this.lq, - heap.Pop(&this.rq).(int))
        }
        return
    }
    heap.Push(&this.lq, - num)
    if len(this.lq) == len(this.rq) + 2 {
        heap.Push(&this.rq, - heap.Pop(&this.lq).(int))
    }
}


func (this *MedianFinder) FindMedian() float64 { // T(n) = O(1)
    if len(this.lq) > len(this.rq) {
        return float64(- this.lq[0])
    }
    return float64(- this.lq[0] + this.rq[0]) / 2
}


/**
 * Your MedianFinder object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(num);
 * param_2 := obj.FindMedian();
 */
