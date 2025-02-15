/**
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 * 풀이방법: Sliding Window
 * 
 * 공간 복잡도: O(1)
 * 시간 복잡도: O(n)
 */

#include <vector>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int answer = 0;
        vector<int> visit(256, -1);
        int i, j;
        
        for (i = 0, j = 0; i < s.size(); i++){
            if (visit[s[i]] != -1 && visit[s[i]] >= j && visit[s[i]] < i) {
                j = visit[s[i]] + 1;
            }
            answer = max(answer, i - j + 1);
            visit[s[i]] = i;
        }
        return answer;
    }
};
