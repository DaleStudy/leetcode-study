# Intuition
정렬된 문자열을 통해 그룹 여부를 쉽게 확인한다.
# Approach
1. `{정렬된 문자열, 그 문자열의 인덱스}`를 유지하는 배열을 선언한다.
2. 원본 배열을 순회하며 정렬한 결과, 인덱스를 struct로 하여 배열에 삽입한다.
   - 인덱스를 유지하는 이유는 원본 배열의 문자열 값을 확인하기 위함이다. (정렬을 했기에 이렇지 않으면 확인이 어렵다.)
3. 모든 struct가 삽입된 배열을 문자열을 기준으로 정렬한다.
4. 반복문을 순회하며 `이전 문자열과 같은지` 여부를 그룹을 판단하여 인덱스들을 그루핑해 모아놓는다.
5. 그루핑한 인덱스들을 문자열(원본 문자열을 참조해서)로 치환하여 최종적으로 반환한다.
# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(nklog(n))$$ -->
: 배열의 길이 `n`, 문자열의 길이 `k`. 문자열을 기준으로 정렬할 때 발생하는 비용이다.
- Space complexity: $$O(nk)$$

: 주어진 배열의 길이 `n`, 배열이 가지는 문자열의 길이 `k`, (코드로 생성하는 배열의 길이, 문자열의 크기 모두 `n`, `k`이다.)
  <!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```go
type StrAndIdx struct {
	Str string
	Idx int
}

func sortSring(s string) string {
	runes := []rune(s)

	sort.Slice(runes, func(i, j int) bool {
		return runes[i] < runes[j]
	})

	return string(runes)
}

func groupAnagrams(strs []string) [][]string {

	strAndIdxs := make([]StrAndIdx, 0, len(strs)+5)

	for i, s := range strs {
		strAndIdxs = append(strAndIdxs, StrAndIdx{sortSring(s), i})
	}

	sort.Slice(strAndIdxs, func(i, j int) bool {
		return strAndIdxs[i].Str < strAndIdxs[j].Str
	})

	groupedIdxs := make([][]int, 0, len(strAndIdxs)/4)

	group := make([]int, 0)
	defaultString := "NOT_EXIST_STRING"
	prev := defaultString
	for _, sAI := range strAndIdxs {
		curr := sAI.Str
		idx := sAI.Idx
		if prev == curr {
			group = append(group, idx)
		} else {
			if prev != defaultString {
				groupedIdxs = append(groupedIdxs, group)
			}
			group = []int{idx}
		}
		prev = curr
	}

	if len(group) != 0 {
		groupedIdxs = append(groupedIdxs, group)
	}

	groupedStrs := make([][]string, 0, len(groupedIdxs))
	for _, idxs := range groupedIdxs {

		groupStr := make([]string, 0, len(idxs))
		for _, idx := range idxs {
			groupStr = append(groupStr, strs[idx])
		}
		groupedStrs = append(groupedStrs, groupStr)
	}

	return groupedStrs
}
```

# **To** Learn
- GoLang에서 문자열을 어떻게 비교하는지.
- 해당 문제 해결에 있어서 삽질한 것은 무엇이었는지. 앞으로 어떻게 해야 안할 수 있는지.