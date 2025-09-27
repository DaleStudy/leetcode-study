/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type Heap []*ListNode

func (pq Heap) Len() int {return len(pq)}
func (pq Heap) Less(i, j int) bool {
    return pq[i].Val < pq[j].Val
}
func (pq Heap) Swap(i, j int) {pq[i], pq[j] = pq[j], pq[i]}
func (pq *Heap) Push(x any) {*pq = append(*pq, x.(*ListNode))}
func (pq *Heap) Pop() any {
    x := (*pq)[len(*pq) - 1]
    *pq = (*pq)[:len(*pq) - 1]
    return x
}

func mergeKLists(lists []*ListNode) *ListNode {
    h := Heap{}
    for _, l := range lists {
        if l != nil {
            h = append(h, l)
        }
    }
    heap.Init(&h)
    ans := ListNode{}
    u := &ans
    for len(h) > 0 { // T(n) = S(n) = O(nlogn)
        u.Next = heap.Pop(&h).(*ListNode)
        u = u.Next
        if u.Next != nil {
            heap.Push(&h, u.Next)
        }
    }
    return ans.Next
}
