// package _sum
package main

import (
	"slices"
	"strconv"
)

/*
 * 첫 번째 수 n1
 * 두 번째 수 n2
 * 세 번째 수 n3 일때,
 * 2sum 문제와 동일하게 map에 모든 수를 맵핑하여
 * 두가지 수를 계산하여 얻을 수 있는 세가지 수가 map에 있는지를 확인하여
 * 중복되지 않도록 결과를 map에 저장 -> [][]int로 반환
 * 시간 복잡도: O(N^2)
 * 공간 복잡도: O(N)
 */
func threeSum(nums []int) [][]int {
	triplets := make(map[string][]int)
	for i, n1 := range nums[:len(nums)-2] {
		seen := make(map[int]int)
		for _, n2 := range nums[i+1:] {
			target := -n1 - n2
			if _, ok := seen[target]; ok {
				item := []int{n1, n2, target}
				slices.Sort(item)
				key := strconv.Itoa(item[0]) + strconv.Itoa(item[1]) + strconv.Itoa(item[2])
				triplets[key] = item
			}
			seen[n2] = n2
		}
	}

	ret := make([][]int, 0)
	for _, t := range triplets {
		ret = append(ret, t)
	}
	return ret
}

/*
 * 따로 맵핑하여 첫 번째 수를 고정 후, 2,3 번째 수를 순회하며 도는 첫 번째 방식과 동일하게 O(N^2) 비용은 유지
 * 되지만, 공간 복잡도 면에서 O(N) -> O(1)로 개선이 됨.
 */
func threeSum2(nums []int) [][]int {
	slices.Sort(nums)
	triplets := make(map[string][]int, 0)

	for i := 0; i < len(nums); i++ {
		l, h := i+1, len(nums)-1
		for l < h {
			sum := nums[l] + nums[h] + nums[i]
			if sum < 0 {
				l++
			} else if sum > 0 {
				h--
			} else {
				k := strconv.Itoa(nums[l]) + strconv.Itoa(nums[h]) + strconv.Itoa(nums[i])
				nums := []int{nums[i], nums[l], nums[h]}
				triplets[k] = nums
				l++
				h--
			}
		}
	}
	ret := make([][]int, 0)
	for _, t := range triplets {
		ret = append(ret, t)
	}
	return ret
}
