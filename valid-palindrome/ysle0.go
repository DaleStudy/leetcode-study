package valid_palindrome

import (
	"regexp"
	"strings"
)

/*
 1. 문제
    회문. 주어진 문자열 s 를 모두 소문자로 바꾸고, alphanumeric 이 아닌 문자를 제외할 때,
    앞으로 읽으나 뒤로 읽으나 같은 문자열인지 체크 (회문)

 2. 풀이
    - 주어진 문자열 s 에서 alphanumeric character 만 남기고 제거.
    - 모두 소문자로 변환
    - 앞, 뒤로 인덱스 위치를 기록하는 cursor 를 정의
    커서 둘을 앞, 뒤로 전진하며 같지않은 문자가 나오면 false 를 반환, 그렇지 않고 회문이면 true 를 반환.

3. 분석
  - 시간 복잡도: O(N)
    regex.ReplaceAllString(): O(n)
    모든 문자열을 돌며 regex 검사 후 대체
    strings.ToLower(str): O(n)
    모든 문자열을 돌며 소문자로 변환
    palindrome 문자열 체크 loop
    앞 커서 < 뒤 커서 의 조건으로 O(n/2) ---> O(n)
  - 공간 복잡도: O(1)
    새로운 저장공간은 없으며 주어진 문자열 s 하나뿐
*/
var nonAlphanumericRegex = regexp.MustCompile(`[^a-zA-Z0-9]+`)

func isPalindrome(s string) bool {
	s = nonAlphanumericRegex.ReplaceAllString(s, "")
	s = strings.ToLower(s)
	// 앞, 뒤 커서
	front, rear := 0, len(s)-1

	for front < rear {
		frontCh := s[front]
		readCh := s[rear]

		// 선택한 두 문자가 다르면 실패!
		if frontCh != readCh {
			return false
		}

		front++
		rear--
	}

	return true
}

/*
1. 개선점
  - regex 오버헤드 제거
*/
func isPalindrome_Optimized(s string) bool {
	front, rear := 0, len(s)-1

	for front < rear {
		for front < rear && !isAlphanumeric(s[front]) {
			front++
		}

		for front < rear && !isAlphanumeric(s[rear]) {
			rear--
		}

		if toLower(s[front]) != toLower(s[rear]) {
			return false
		}

		front++
		rear--
	}

	return true
}

func isAlphanumeric(ch byte) bool {
	return (ch >= 'a' && ch <= 'z') ||
		(ch >= 'A' && ch <= 'Z') ||
		(ch >= '0' && ch <= '9')
}

func toLower(ch byte) byte {
	if ch >= 'A' && ch <= 'Z' {
		return ch + 32
	}
	return ch
}
