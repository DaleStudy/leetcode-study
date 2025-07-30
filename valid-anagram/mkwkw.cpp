//map: key:alphabet, value:count
//if t is an anagram of s
// 1. same length
// 2. same content of map
class Solution {
public:
    bool isAnagram(string s, string t) {
        
        //1. different length -> false
        if(s.length()!=t.length())
        {
            return false;
        }

        //2. different map -> false
        map<char, int> sMap, tMap;
        for(int i=0; i<s.length(); i++)
        {
            sMap[s[i]]++;
            tMap[t[i]]++;
        }

        for(auto c : sMap)
        {
            if(tMap.find(c.first)==tMap.end())
            {
                return false;
            }
            if(tMap[c.first] != c.second)
            {
                return false;
            }
        }

        return true;
    }
};
