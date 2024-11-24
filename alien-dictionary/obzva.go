/*
풀이
- 두 단어를 알파벳 하나씩 차례대로 비교했을 때, 첫번째 차이가 발생하는 지점에서 alien dictionary의 order를 찾을 수 있습니다
- 첫번째 단어부터 바로 그 다음 단어와 두 단어씩 짝지어서 비교하면 앞에서 말한 일련의 order를 찾아낼 수 있습니다
  알파벳 x가 알파벳 y보다 alien dictionary order에서 앞서는 관계, 즉 x->y인 관계를 찾아서 x: {y1, y2, y3, ...}인 집합의 map을 만들겠습니다
  그리고 이를 nextLetters라고 명명하였습니다
- 만약 특정 알파벳 x에 대해, z->x인 알파벳 z가 없다면 x는 우리가 정답으로 제출할 result string의 어느 위치에든 자유롭게 끼워넣을 수 있습니다
  (* If there are multiple solutions, return any of them.)
  우리는 이런 알파벳 x를 찾아낼 때마다 바로바로 result string res에 추가하겠습니다
- z->x인 알파벳 z가 현재 있는지 없는지에 대한 상태관리를 하기 위해서 prevLetterCounts라는 map을 만들겠습니다
  prevLetterCounts[x]: z->x인 z의 개수
- nextLetters, prevLetterCounts를 잘 생성한 후에는 prevLetterCount가 0인 알파벳부터 queue에 등록시킨 후 BFS를 실행합니다
  BFS를 실행하며 prevLetterCount가 0인 알파벳이 새로 발견될 경우 queue에 등록시킵니다
- 엣지케이스가 두 경우 발생하는데,
  첫번째는 nextLetters를 생성하는 반복문에서 발견됩니다
    두번째 단어가 첫번째 단어의 prefix인 경우는 애초부터 잘못된 dictionary order인 경우입니다
	위 경우는 단순 알파벳 비교로는 발견하기 어려우므로 flag를 사용하였습니다
  두번째는 result string의 길이가 input으로 주어진 단어들에 등장한 알파벳의 개수보다 적은 경우입니다
    이 경우는 nextLetters에 순환이 발생한 경우이므로 dictionary order가 잘못되었다고 판단할 수 있습니다
Big O
- N: 주어진 배열 words의 길이
- S(W): 배열 words에 속한 모든 string의 길이의 총합
- Time complexity: O(N + S(W))
  - prevLetterCounts와 nextLetters 생성 -> O(N)
  - nextLetters에 들어갈 알파벳 전후관계 찾기 -> O(S(W))
  - 알파벳 소문자의 수는 제한되어 있기 때문에 BFS의 시간 복잡도 상한선은 정해져 있습니다 -> O(26 * 26) = O(1)
- Space complexity: O(1)
  - 알파벳 소문자의 수는 제한되어 있기 때문에 공간 복잡도의 상한선은 정해져 있습니다
    prevLetterCounts -> O(26) = O(1)
	nextLetters -> O(26 * 26) = O(1)
	queue -> O(26) = O(1)
*/

import "strings"

func alienOrder(words []string) string {
	n := len(words)
	// prevLetterCounts[x] = count of letters y that are in relation of y->x
	prevLetterCounts := make(map[string]int)
	// nextLetters[x] = set of letters y that are in relation of x->y
	nextLetters := make(map[string]map[string]bool)
	for _, word := range words {
		for _, c := range word {
			if _, ok := prevLetterCounts[string(c)]; !ok {
				prevLetterCounts[string(c)] = 0
				nextLetters[string(c)] = make(map[string]bool)
			}
		}
	}

	for i := 0; i < n-1; i++ {
		currWord := words[i]
		nextWord := words[i+1]
		// flag for edge case below
		diff := false
		for j := 0; j < len(currWord) && j < len(nextWord); j++ {
			if currWord[j] != nextWord[j] {
				diff = true
				if _, ok := nextLetters[string(currWord[j])][string(nextWord[j])]; !ok {
					prevLetterCounts[string(nextWord[j])]++
					nextLetters[string(currWord[j])][string(nextWord[j])] = true
				}
				break
			}
		}
		// tricky edge case!!!
		// if nextWord is prefix of currWord, then the provided dictionary order is invalid
		if !diff && len(currWord) > len(nextWord) {
			return ""
		}
	}
	// BFS
	queue := make([]string, 0, len(prevLetterCounts))
	for letter := range prevLetterCounts {
		// we can arrange letters whose prevLetterCount is zero as we wish
		if prevLetterCounts[letter] == 0 {
			queue = append(queue, letter)
		}
	}
	// in Go, using strings.Builder is the most efficient way to build strings
	var sb strings.Builder
	for len(queue) > 0 {
		// pop the letter from the queue and append it to the result string
		popped := queue[0]
		queue = queue[1:]
		sb.WriteString(popped)

		for nextLetter := range nextLetters[popped] {
			prevLetterCounts[nextLetter]--
			// if prevLetterCount for nextLetter becomes zero, we can add it to the queue
			// append to the result string (order) in the next iteration
			if prevLetterCounts[nextLetter] == 0 {
				queue = append(queue, nextLetter)
			}
		}
	}
	// res is result string
	res := sb.String()
	// this case means that there was a cycle
	if len(res) != len(prevLetterCounts) {
		return ""
	}
	// else return res
	return res
}
