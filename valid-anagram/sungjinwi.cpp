/*
    풀이 :
        해시테이블에 string을 순회하며 문자 : 빈도로 값 저장 후 두 데이터가 같은 지 비교
    
    TC : O(S + T)
    SC : O(S + T)
*/

#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> s_map;
        unordered_map<char, int> t_map;

        for (char c : s)
            s_map[c]++;
        for (char c : t)
            t_map[c]++;

        return (s_map == t_map);
    }
};
