/**
 * 풀이
 * - 주어진 배열 `nums`로 set `s`를 만듭니다
 * - `nums`를 조회하는데, 현재 조회 중인 `num`에 대하여 `num - 1`이 `s`에 포함되지 않는 경우만 while문을 실행하여 subsequence의 길이를 측정합니다
 * - `num - 1`이 `s`에 포함되지 않는다는 것은 `num`이 해당 subsequence의 첫 수임을 뜻합니다
 * 
 * Big-O
 * - N: 주어진 배열 `nums`의 길이
 * 
 * - Time complexity: O(N)
 *   - 이중 반복문의 구조를 가졌지만, 조건문때문에 각 원소를 한 번씩만 조회합니다
 * 
 * - Space complexity: O(N)
 *   - `nums`를 구성하는 원소가 모두 고유한 정수일 경우, `s`의 크기가 `nums`만큼 커질 수 있습니다
 */

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        
        int res = 0;
        for (int num : nums) {
            if (s.find(num - 1) != s.end()) continue;
            
            int curr = num;
            int streak = 1;
            while (s.find(curr + 1) != s.end()) {
                ++curr;
                ++streak;
            }
            res = max(res, streak);
        }

        return res;
    }
};
