class Solution {
public:
    string toLowerCase(string s) {
        for (std::size_t i = 0; i < s.size(); i++) {
            if (std::isupper(s[i])){
                s[i] = std::tolower(s[i]);
            }
        }
        return s;
    }
};

