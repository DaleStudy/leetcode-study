package climbing_stairs

import (
	"fmt"
)

func climbStairs(n int) int {
	return fibo(n)
}

func fibo(n int) int {
	ret := []int{0, 1}

	for i := 2; i <= n; i++ {
		ret = append(ret, ret[i-1]+ret[i-2])
	}

	ret = ret[len(ret)-2:]
	fmt.Printf("ret=%v\n", ret)
	sum := 0
	for _, n := range ret {
		sum += n
	}
	return sum
}
