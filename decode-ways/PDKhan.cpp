class Solution {
    public:
        int numDecodings(string s) {
            int n = s.length();
    
            if(n == 0 || s[0] == '0')
                return 0;
            
            int next = 1;
            int nextnext = 1;
            int curr = 0;
    
            for(int i = n - 1; i >= 0; i--){
                if(s[i] == '0')
                    curr = 0;
                else{
                    curr = next;
                    if(i < n - 1 && (s[i] == '1' || (s[i] == '2' && s[i+1] >= '0' && s[i+1] <= '6')))
                        curr += nextnext;
                }
    
                nextnext = next;
                next = curr;
            }
    
            return curr;
        }
    };
