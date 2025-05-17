class Solution {
    public:
        vector<vector<string>> groupAnagrams(vector<string>& strs) {
            unordered_map<string, vector<string>> map;
            vector<vector<string>> result;
    
            for(const string& s : strs){
                string key = s;
                sort(key.begin(), key.end());
    
                map[key].push_back(s);
            }
    
            for(auto& pair : map){
                result.push_back(pair.second);
            }
    
            return result;
        }
    };
