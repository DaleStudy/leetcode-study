// 문제 풀이 흐름
// DP[i] = i - 1 번째 인덱스 char를 끝으로 하는 조합
// 문제는 case를 다 분리할 수 밖에 없는건가?
// 7~9 이면 앞자리가 1인지 확인 -> 있으면 두가지 합해야함 / 아니면 한가지만
// 0이면 앞자리가 반드시 1,2 이어야함 -> 무조건 한가지
// 1~6이면 앞자리가 1,2인지 확인 -> 있으면 두가지 합해야함 / 아니면 한가지만
// 이러면 너무 더러운 느낌?
//      if () {
//           if ()
//       } else if () {
//           if ()
//       } else {
//       }

// 추가적으로 고려하지 못한 사항 : 01, 001 과 같은 경우

// n = s의 길이
// 시간복잡도 : O(n)
// 공간복잡도 : O(n)


class Solution {

	String s;
	int length;
	int[] DP;

	public int numDecodings(String s) {

		this.s = s;
		this.length = s.length();
		this.DP = new int[this.length + 1];

		DP[0] = 1;

		for (int i = 1 ; i < this.length + 1; i ++) {

			if (canDecodeSingle(i)) {
				DP[i] += DP[i - 1];
			}

			if (i >= 2 && canDecodePair(i)) {
				DP[i] += DP[i - 2];
			}
		}

		return DP[this.length];
	}

	private boolean canDecodeSingle(int currentIdx) {
		return s.charAt(currentIdx - 1) != '0';
	}

	private boolean canDecodePair(int currentIdx) {
		char currentChar = s.charAt(currentIdx - 1);
		char prevChar = s.charAt(currentIdx - 2);
		return prevChar == '1'
				|| (prevChar == '2' && currentChar <= '6');
	}
}
