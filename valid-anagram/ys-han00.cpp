// class Solution {
// public:
//     bool isAnagram(string s, string t) {
//         map<char, int> counter;

//         for(int i = 0; i < s.size(); i++)
//             counter[s[i] - 'a']++;
//         for(int i = 0; i < t.size(); i++)
//             counter[t[i] - 'a']--;
        
//         for(auto const& iter : counter)
//             if(iter.second != 0)
//                 return false;
        
//         return true;
//     }
// };

class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> counter(26, 0);

        for(int i = 0; i < s.size(); i++)
            counter[s[i] - 'a']++;
        for(int i = 0; i < t.size(); i++)
            counter[t[i] - 'a']--;

        for(int i = 0; i < 26; i++)
            if(counter[i] != 0)
                return false;
        
        return true;
    }
};

