package top_k_frequent_elements

//package main

import (
	"container/heap"
	"slices"
)

/*
 1. 문제
    nums 에서 가장 많이 나온 숫자들 k 개를 반환.

 2. 풀이
    map 에 빈도를 기록하여 내림차순 정렬한 후 k개 뽑기

3. 분석

  - 시간 복잡도: O(N + M logM) --> O(N logN)
    빈도맵핑을 위한 nums 순회: O(N)
    오름차순정렬: O(M logM)

  - 공간 복잡도: O(N)
    주어진 배열 nums: O(N)
    빈도맵핑용 map: O(N)
*/
type Kvp struct {
	k int
	v int
}

func topKFrequent(nums []int, k int) []int {
	freq := map[int]int{}

	// 빈도를 기록
	for _, n := range nums {
		if _, ok := freq[n]; !ok {
			freq[n] = 1
		} else {
			freq[n]++
		}
	}

	// map->array
	tmp := make([]Kvp, 0, len(freq))
	for key, v := range freq {
		tmp = append(tmp, Kvp{key, v})
	}

	// 내림차순 정렬 (time O(M logM)
	slices.SortFunc(tmp, func(a, b Kvp) int { return b.v - a.v })

	// []int 로 변환
	res := make([]int, 0, len(tmp))
	for _, kvp := range tmp {
		res = append(res, kvp.k)
	}

	// k 개 뽑기
	return res[:k]
}

func topKElements_HeapBasedApproach(nums []int, k int) []int {
	freq := map[int]int{}
	for _, n := range nums {
		freq[n]++
	}

	h := &IntHeap{}
	heap.Init(h)

	for k, v := range freq {
		heap.Push(h, Kvp{k, v})
		if h.Len() > k {
			heap.Pop(h)
		}
	}

	res := make([]int, k)
	for i := k - 1; i >= 0; i-- {
		res[i] = heap.Pop(h).(Kvp).k
	}

	return res
}

type IntHeap []Kvp

func (h *IntHeap) Len() int           { return len(*h) }
func (h *IntHeap) Less(i, j int) bool { return (*h)[i].v < (*h)[j].v }
func (h *IntHeap) Swap(i, j int)      { (*h)[i], (*h)[j] = (*h)[j], (*h)[i] }
func (h *IntHeap) Push(x interface{}) { *h = append(*h, x.(Kvp)) }
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func topKFrequentElements_BucketSort(nums []int, k int) []int {
	freq := map[int]int{}
	for _, n := range nums {
		freq[n]++
	}

	buc := make([][]int, len(nums)+1)
	for k, v := range freq {
		buc[v] = append(buc[v], k)
	}

	res := []int{}
	for i := len(buc) - 1; i >= 0 && len(res) < k; i-- {
		res = append(res, buc[i]...)
	}

	return res[:k]
}

//
//func main() {
//	r1 := topKFrequent([]int{1, 1, 1, 2, 2, 3}, 2)
//	fmt.Println(r1)
//
//	r2 := topKFrequent([]int{1}, 1)
//	fmt.Println(r2)
//}
