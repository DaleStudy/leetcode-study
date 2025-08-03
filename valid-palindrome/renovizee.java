

// tag renovizee 3week
// https://github.com/DaleStudy/leetcode-study/issues/220
// https://leetcode.com/problems/valid-palindrome/ #125 #Easy
class Solution {
    // Solv1 :
    // 시간복잡도 : O(n)
    // 공간복잡도 : O(n)
    public boolean isPalindrome(String s) {
//        replaceAll(...): 문자열 전체를 한 번 순회 → O(n)
//        trim(): 공백을 양쪽 끝에서만 탐색 → O(n) 이라고 보지만 보통 무시 가능한 수준
//        toLowerCase(): 모든 문자를 소문자로 바꿈 → O(n)
        String cleanString = s.replaceAll("[^a-zA-Z0-9]", "").trim().toLowerCase();

        int left = 0;
        int right = cleanString.length() - 1;

        //O(n)
        while (left < right) {
            if (cleanString.charAt(left) != cleanString.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;

    }
}

//-------------------------------------------------------------------------------------------------------------
// Java 문법 피드백
// 1) char[] 대문자 Char 가 아니고 소줌ㄴ자
// 2) ~.equals는 char에서 제공되지 않음
//-------------------------------------------------------------------------------------------------------------
