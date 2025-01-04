/*
time complexity: O(n^2)
space complexity: O(1)

모든 가능한 조합(O(n^2))에 대해 palindrome 여부를 검사(O(n))하는 brute force는 O(n^3).
i번째 문자에서 시작하여, 앞/뒤로 한 글자씩 늘려가면서 탐색하되, 한번이라도 앞/뒤 글자가 서로 다르다면 그 이후는 탐색하지 않을 수 있음. 이 경우는 O(n^2).
*/
class Solution {
    public int countSubstrings(String s) {
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            int head = i, tail = i;
            while (head >= 0 && tail < s.length()) {
                if (s.charAt(head) == s.charAt(tail)) {
                    ans++;
                } else {
                    break;
                }
                head--;
                tail++;
            }

            head = i;
            tail = i + 1;
            while (head >= 0 && tail < s.length()) {
                if (s.charAt(head) == s.charAt(tail)) {
                    ans++;
                } else {
                    break;
                }
                head--;
                tail++;
            }
        }

        return ans;
    }
}
