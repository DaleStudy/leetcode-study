# Intuition
빈도수 계산, 정렬을 활용하면 가능하다고 생각했다. (깔끔하진 않아 해결될지는 의문이었다.)
# Approach
1. 빈도 수를 저장한다.
2. 원소들을 빈도수(내림차순)대로 정렬한다.
3. 정렬된 원소 중 앞에서부터 k개를 반환한다.
# Complexity
- Time complexity: $$O(nlog(n))$$
  - 배열의 길이 n에 대하여, 정렬비용으로 소모된다.

- Space complexity: $$O(n+m)$$
  - 배열의 길이 n과 원소의 범위 k에 대하여, 빈도수 저장을 위해 선언하는 비용 `k`와 정렬된 원소를 저장하는 비용 `n`이 소모된다.

# Code
```go
type NumAndFreq struct {
	Num  int
	Freq int
}

func topKFrequent(nums []int, k int) []int {
	freq := make(map[int]int, 20000)

	for _, num := range nums {
		freq[num]++
	}

	numAndFreqs := make([]NumAndFreq, 0, len(freq))
	for n, f := range freq {
		numAndFreqs = append(numAndFreqs, NumAndFreq{Num: n, Freq: f})
	}

	sort.Slice(numAndFreqs, func(i, j int) bool {
		return numAndFreqs[i].Freq > numAndFreqs[j].Freq
	})

	numsSortedByFreqDesc := make([]int, 0, len(nums))
	for _, e := range numAndFreqs {
		numsSortedByFreqDesc = append(numsSortedByFreqDesc, e.Num)
	}

	return numsSortedByFreqDesc[0:k]
}

```

# 여담
- 타 솔루션들을 보며 정렬을 하지 않고 빈도수별로 원소들을 모아놨다가 배열을 만드는 방법도 확인했다. 직관적이진 않다고 느꼈다.
- 문제 해결 도중 `map`, `filter`와 같은 함수형 프로그래밍을 활용하면 좋겠다는 생각이 들어 golang에서도 이를 제공하나 찾아봤다. [링크1](https://stackoverflow.com/questions/71624828/is-there-a-way-to-map-an-array-of-objects-in-go)과 [링크2](https://github.com/golang/go/issues/45955)를 통해 다양한 논의가 있었으나, 여러 이유로 도입하지 않음을 알게되었다. 