class Solution {
    public:
        int characterReplacement(string s, int k) {
            int start = 0;
            int max_len = 0;
            int max_cnt = 0;
            int map[26] = {0};
    
            for(int end = 0; end < s.length(); end++){
                map[s[end] - 'A']++;
    
                max_cnt = max(max_cnt, map[s[end] - 'A']);
    
                while(end - start + 1 - max_cnt > k){
                    map[s[start] - 'A']--;
                    start++;
                }
    
                max_len = max(max_len, end - start + 1);
            }
    
            return max_len;
        }
    };
