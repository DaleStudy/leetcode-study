# Complexity
- Time complexity: $O(N^t)$
  - `target`의 크기 t와 `candiates`의 크기 N에 대하여, t만큼의 재귀호출이 연속적으로 일어날 수 있고 각 함수에서 배열 순회 비용 N이 발생할 수 있다.

- Space complexity: $O(N^t)$
  - `target`의 크기 t와 `candiates`의 크기 N에 대하여, 백트래킹에서 만들 수 있는 모든 경우의 수 만큼 `ret`이 적재될 수 있다.

# Code
```go
func combinationSum(candidates []int, target int) [][]int {
	sort.Ints(candidates)

	var combination func(candidates []int, target int) [][]int
	combination = func(candidates []int, target int) [][]int {
		if target < 0 {
			return nil
		}
		if target == 0 {
			return [][]int{{}}
		}

		ret := make([][]int, 0)
		for i, c := range candidates {
			items := combination(candidates[i:], target-c)
			for _, item := range items {
				ret = append(ret, append(item, c))
			}
		}
		return ret
	}

	return combination(candidates, target)
}

```