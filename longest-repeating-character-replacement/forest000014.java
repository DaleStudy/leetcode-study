/*
Time Complexity: O(n)
Space Complexity: O(1)

투 포인터 방식으로 접근했습니다.
현재 상태에서, 두 포인터 사이의 가장 많은 문자를 제외한 나머지 문자의 개수가 k개 이하면 right를 오른쪽으로 1칸,
k개 초과면 left를 오른쪽으로 1칸씩 이동합니다.

다만, 개인적으로 에너지가 고갈된 상태에서 풀다보니,
현재 상태에서 가장 많은 문자를 카운트하는 방식을 counts[26] 배열을 순회하는 식으로 단순하게 짰습니다.
PQ를 사용하면 조금 더 시간이 개선될 것 같습니다.
*/
class Solution {
    public int characterReplacement(String s, int k) {
        int[] counts = new int[26];

        int l = 0;
        int r = 0;
        int mostCount = 1;

        counts[s.charAt(0) - 'A'] = 1;
        int ans = 0;

        while (r < s.length()) {
            mostCount = 0;
            for (int i = 0; i < 26; i++) {
                if (counts[i] > mostCount) {
                    mostCount = counts[i];
                }
            }

            if (r - l + 1 - mostCount <= k) {
                if (r - l + 1 > ans) {
                    ans = r - l + 1;
                }

                r++;
                if (r == s.length()) {
                    break;
                }
                counts[s.charAt(r) - 'A']++;
            } else {
                counts[s.charAt(l) - 'A']--;
                l++;
            }
        }

        return ans;
    }
}
