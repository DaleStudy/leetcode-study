// class Solution {
// public:
//     vector<vector<string>> groupAnagrams(vector<string>& strs) {
//         map<string, vector<string>> anagram;
//         vector<vector<string>> ans;

//         for(int i = 0; i < strs.size(); i++) {
//             string now = strs[i];
//             sort(now.begin(), now.end());

//             if(anagram.find(now) == anagram.end()) 
//                 anagram[now] = vector<string> ({strs[i]});
//             else
//                 anagram[now].push_back(strs[i]);
//         }

//         for(map<string, vector<string>>::iterator iter = anagram.begin(); iter != anagram.end(); iter++)
//             ans.push_back(iter->second);

//         return ans;
//     }
// };

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        vector<vector<string>> ans;

        for(string &s : strs) {
            string key = s;
            sort(key.begin(), key.end());
            mp[key].push_back(s);
        }

        for(auto &element : mp)
            ans.push_back(element.second);

        return ans;
    }
};

