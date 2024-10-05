/**
 * 풀이
 * - 주어진 s로 만들 수 있는 가장 긴 valid substring의 길이를 찾는 문제입니다
 *   - valid substring: 최대 k개의 문자를 바꿔서, 모든 문자가 같게 만들 수 있는 substring
 * 
 * - 두 단계로 나누어 풀이에 대해 생각할 수 있습니다
 * 
 * - 1. 특정 길이의 valid substring을 만들 수 있는지 확인
 *   - 함수 bool can_make_valid_substring(string const s, int substr_length, int k)
 *   - 특정 길이의 substring에 대해서, 등장 빈도가 가장 높은 문자의 빈도수를 저장합니다 (max_freq)
 *     만약 해당 substring이 valid substring이라면, max_freq + k >= substr_length 이어야 합니다
 * 
 * - 2. 최대 길이의 valid substring을 찾는다
 *   - 이진탐색을 통해 최대 길이를 찾는다
 *   - 함수 int characterReplacement(string s, int k)
 *   - 주어진 문자열 s로 만들 수 있는 substring의 길이는 1이상 s.size() 이하입니다
 *     이진 탐색의 범위를 위에서 언급한 대로 설정하고, 현재 탐색하려는 길이 (mid)에 대해서
 *     can_make_valid_substring 함수를 호출하여 현재 길이로 valid substring을 만들 수 있는지 확인합니다
 *     이진 탐색 알고리즘의 전개 및 결과에 대한 설명은 https://github.com/DaleStudy/leetcode-study/discussions/332를 참고해주세요 :)
 * 
 * Big O
 * - N: 주어진 문자열 s의 길이
 * - K: 주어진 정수 k
 * 
 * - Time complexity: O(N * logN)
 * - Space complexity: O(1)
 */

class Solution {
public:
    bool can_make_valid_substring(string const s, int substr_length, int k) {
        // 문자의 빈도수를 저장하는 배열입니다
        array<int, 26> freq;
        freq.fill(0);

        // 최대 빈도수를 저장하는 변수입니다
        int max_freq = 0;

        int window_start = 0;

        for (int window_end = 0; window_end < s.size(); ++window_end) {
            ++freq[s[window_end] - 'A'];

            int curr_size = window_end - window_start + 1;
            if (curr_size > substr_length) {
                --freq[s[window_start] - 'A'];
                ++window_start;
            }

            max_freq = max(max_freq, freq[s[window_end] - 'A']);
            if (max_freq + k >= substr_length) return true;
        }

        return false;
    }

    int characterReplacement(string s, int k) {
        int lo = 1;
        int hi = s.size() + 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;

            if (can_make_valid_substring(s, mid, k)) lo = mid + 1;
            else hi = mid;
        }

        // 이진탐색이 종료되면 lo는 최대 길이보다 1 큰 값이 된다.
        // EX:      hi lo
        // T  T  T  T  F  F  F  F
        // 따라서 최대 길이는 lo - 1이 된다
        return lo - 1;
    }
};
