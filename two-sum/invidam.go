type NumAndIdx struct {
	Num int
	Idx int
}

func twoSum(nums []int, target int) []int {
	numAndIdxs := make([]NumAndIdx, 0, len(nums))
	for i, n := range nums {
		numAndIdxs = append(numAndIdxs, NumAndIdx{Num: n, Idx: i})
	}

	sort.Slice(numAndIdxs, func(i, j int) bool {
		return numAndIdxs[i].Num < numAndIdxs[j].Num
	})

	ldx, rdx := 0, len(numAndIdxs)-1

	for ldx < rdx {
		l := numAndIdxs[ldx]
		r := numAndIdxs[rdx]
		if sum := l.Num + r.Num; sum > target {
			rdx--
		} else if sum < target {
			ldx++
		} else {
			return []int{l.Idx, r.Idx}
		}
	}

	return nil
}
