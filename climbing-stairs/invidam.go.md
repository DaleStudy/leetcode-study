# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
This problem is a typical dynamic programming (DP) problem. (keyword: `Fibonacci`)

DP has two methods: tabulation and memoization. I'll introduce both methods.
# Approach (tabulation)
<!-- Describe your approach to solving the problem. -->
1. Create an array to store the results.
2. Initiate default values for the base cases `0` and `1`.
3. While iterating through the array, fill in the values using this formula $$f(n) = f(n-1) + f(n-2)$$
# Complexity
## Complexity (V1)
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
# Complexity (V2)
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

(n is value of `n`)
# Code
```go
func climbStairsV1(n int) int {
	climbData := make([]int, n+2, n+2)
	climbData[0], climbData[1] = 1, 1
	for s := 0; s < n; s++ {
		climbData[s+2] = climbData[s] + climbData[s+1]
	}

	return climbData[n]
}

func climbStairsV2(n int) int {
	prev, curr := 1, 1
	for s := 1; s < n; s++ {
		prev, curr = curr, prev+curr
	}

	return curr
}
```

> As you can see in `V2`, it can be optimized. Remove the array and maintain only the `prev` and `curr` values. In Golang, `Multiple Assignment` prodives syntatic sugar.

- - -

# Approach (memoization)
<!-- Describe your approach to solving the problem. -->
1. Create an hash map (or array) to **cache** the results.
2. Initialize default values to indicate unvisited nodes. (`-1`).
3. Call the recursion using this formula $$f(n) = f(n-1) + f(n-2)$$.
4. If there are cached results, return it.
5. Pay attension to the **base case**, and always update the cache.

# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
(n is value of `n`)
# Code
```go
var cache map[int]int = map[int]int{}
func climbStairs(n int) int {
	if n == 0 || n == 1 {
		return 1
	} else if n < 0 {
		return 0
	} else if val, ok := cache[n]; ok {
		return val
	}

	ret := climbStairs(n-1) + climbStairs(n-2)
	cache[n] = ret
	return ret
}
```