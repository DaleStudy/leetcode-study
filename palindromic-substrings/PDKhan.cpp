class Solution {
    public:
        int countSubstrings(string s) {
            int cnt = 0;
    
            for(int i = 0; i < s.length(); i++){
                int start = i;
                int end = i;
    
                while(0 <= start && end < s.length() && s[start] == s[end]){
                    cnt++;
                    start--;
                    end++;
                }
    
                start = i;
                end = i + 1;
    
                while(0 <= start && end < s.length() && s[start] == s[end]){
                    cnt++;
                    start--;
                    end++;
                }
            }
    
            return cnt;
        }
    };
