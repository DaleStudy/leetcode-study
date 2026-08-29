// 문제 풀이 흐름 1
// 먼저, 알파벳이 아닌 글자는 다 쳐내는 작업이 필요
// 그 다음 알파벳으로만 만들어진 문자열에 대해 팰린드롬 확인
// 길이 확인 후
// 맨처음에서부터 중간까지, 대칭 값이 맞는지 확인

// n = s의 길이라 할때
// 시간복잡도 : O(n)
// 공간복잡도 : O(n) - 어쩔수없이 trimming한 문자열은 저장해야하므로

// 문제 풀이 흐름 2

// 문자열 그대로 팰린드롬 확인 스타트
// 맨 앞과 뒤의 인덱스에서 시작해서
//  알파벳이 아닌 다른 문자라면 skip
//  알파벳이라면 비교

// n = s의 길이라 할때
// 시간복잡도 : O(n)
// 공간복잡도 : O(1)


class Solution {
	public boolean isPalindrome(String s) {
		int rightIdx = s.length() - 1;

		for (int leftIdx = 0 ; leftIdx <= rightIdx ; leftIdx ++) {
			if (!isValid(s.charAt(leftIdx))) continue;

			// rightIdx 조절
			while (leftIdx <= rightIdx && !isValid(s.charAt(rightIdx))) {
				rightIdx--;
			}

			if (!isSameChar(s.charAt(leftIdx), s.charAt(rightIdx))) {
				return false;
			}
			rightIdx-- ;
		}

		return true;
	}

	private boolean isValid(char c) {
		return 'a' <= c && c <= 'z' || 'A' <= c && c <= 'Z' || '0' <= c && c <= '9';
	}

	private boolean isSameChar(char a, char b) {
		return Character.toLowerCase(a) == Character.toLowerCase(b);
	}
}
