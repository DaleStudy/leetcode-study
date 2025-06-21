class Solution {
    public:
        string minWindow(string s, string t) {
            unordered_map<char, int> t_map;
            unordered_map<char, int> window;
            int need = 0, match = 0;
            int min_len = INT_MAX;
            int min_low = 0;
            int l = 0;
    
            for(char ch : t){
                if(t_map[ch] == 0)
                    need++;
    
                t_map[ch]++;
            }
    
            for(int h = 0; h < s.length(); h++){
                window[s[h]]++;
    
                if(window[s[h]] == t_map[s[h]])
                    match++;
                
                while(need == match){
                    if(h - l + 1 < min_len){
                        min_len = h - l + 1;
                        min_low = l;
                    }
    
                    window[s[l]]--;
    
                    if(window[s[l]] < t_map[s[l]])
                        match--;
                    
                    l++;
                }            
            }
    
            if(min_len == INT_MAX)
                return "";
            
            return s.substr(min_low, min_len);
        }
    };
