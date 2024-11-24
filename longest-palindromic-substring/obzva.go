/*
풀이
- 슬라이딩 윈도우 기법을 이용하면 풀이할 수 있습니다
Big O
- N: 주어진 문자열 s의 길이
- Time complexity: O(N^2)
  - window 함수가 O(N)의 시간복잡도를 가지므로
    각 반복문은 O(N * N) = O(N^2)의 시간복잡도를 가진다고 볼 수 있습니다
- Space complexity: O(1)
  - 별도의 추가적인 공간 복잡도를 고려하지 않아도 됩니다
*/

func longestPalindrome(s string) string {
	n := len(s)
	maxStart := 0
	maxEnd := 0
	// for odd lengths
	for i := 0; i < n; i++ {
		window(&s, &maxStart, &maxEnd, i, false)
	}
	// for even lengths
	for i := 0; i < n-1; i++ {
		window(&s, &maxStart, &maxEnd, i, true)
	}

	return s[maxStart : maxEnd+1]
}

/*
helper function for searching palindromic substring
from the pivotal index `i`
*/
func window(s *string, maxStart *int, maxEnd *int, i int, isEven bool) {
	n := len(*s)
	start := i
	end := i
	if isEven {
		end++
	}
	for 0 <= start && end < n {
		if (*s)[start] != (*s)[end] {
			break
		}

		// if new palindromic substring is longer than the previously found one,
		// update the start and end index
		if *maxEnd-*maxStart < end-start {
			*maxStart = start
			*maxEnd = end
		}
		start--
		end++
	}
}
