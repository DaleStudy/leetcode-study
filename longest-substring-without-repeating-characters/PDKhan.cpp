class Solution {
    public:
        int lengthOfLongestSubstring(string s) {
            int result = 0;
            int start = 0;
            unordered_map<char, int> map;
    
            for(int end = 0; end < s.length(); end++){
                char ch = s[end];
    
                if(map.count(ch) && map[ch] >= start)
                    start = map[ch] + 1;
                
                map[ch] = end;
                result = max(result, end - start + 1);
            }
    
            return result;
        }
    };