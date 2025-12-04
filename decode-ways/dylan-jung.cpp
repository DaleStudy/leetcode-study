class Solution {
public:
    int mem[100];
    string str;

    bool isValid(string s) {
        if(s.size() == 1) {
            return '1' <= s[0] && s[0] <= '9';
        }
        else if(s.size() == 2) {
            if(s[0] == '1') return '0' <= s[1] && s[1] <= '9';
            else if(s[0] == '2') return '0' <= s[1] && s[1] <= '6';
        }
        return false;
    }

    int dfs(int idx) {
        if(idx >= str.size()) return 1;

        int& ret = mem[idx];
        if(ret != -1) return ret;
        ret = 0;

        if (isValid(str.substr(idx, 1))){
            ret += dfs(idx+1);
        }
        if (idx < str.size() - 1 && isValid(str.substr(idx, 2))){
            ret += dfs(idx+2);
        }
        return ret;
    }

    int numDecodings(string s) {
        str = s;
        fill(mem, mem+100, -1);
        return dfs(0);
    }
};
