package youngDaLee

import "sort"

func topKFrequent(nums []int, k int) []int {
	frequencyMap := make(map[int]int)
	for _, num := range nums {
		frequencyMap[num]++
	}

	type freqPair struct {
		num   int
		count int
	}

	freqPairs := make([]freqPair, 0, len(frequencyMap))
	for num, count := range frequencyMap {
		freqPairs = append(freqPairs, freqPair{num, count})
	}

	sort.Slice(freqPairs, func(i, j int) bool {
		return freqPairs[i].count > freqPairs[j].count
	})

	result := make([]int, k)
	for i := 0; i < k; i++ {
		result[i] = freqPairs[i].num
	}

	return result
}
