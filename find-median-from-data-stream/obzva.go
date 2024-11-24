/*
풀이
- 이진탐색을 이용합니다
Big O
- N: 현재 MedianFinder.nums의 크기
- AddNum
  - Time complexity: O(N)
    - bisect -> O(logN)
	- slices.Insert -> O(N)
  - Space complexity: O(1)
- FindMedian
  - Time complexity: O(1)
  - Space complexity: O(1)
*/

import "slices"

type MedianFinder struct {
	nums []int
}

func Constructor() MedianFinder {
	mf := MedianFinder{}
	mf.nums = make([]int, 0)
	return mf
}

func (this *MedianFinder) AddNum(num int) {
	n := len(this.nums)
	if n == 0 {
		this.nums = append(this.nums, num)
	} else {
		idx := bisectLeft(this.nums, num)
		this.nums = slices.Insert(this.nums, idx, num)
	}
}

func (this *MedianFinder) FindMedian() float64 {
	n := len(this.nums)
	if n%2 == 0 {
		return (float64(this.nums[n/2-1]) + float64(this.nums[n/2])) / 2
	} else {
		return float64(this.nums[n/2])
	}
}

// ----- Helper -----
func bisectLeft(arr []int, x int) int {
	lo := 0
	hi := len(arr)
	for lo < hi {
		mid := lo + (hi-lo)/2
		if arr[mid] < x {
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	return lo
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(num);
 * param_2 := obj.FindMedian();
 */
