/*
    풀이 :
        strs의 각 str에 대해 정렬을 통해 아나그램을 동일한 판별할 수 있도록 하고 
        해시테이블 unordered_map에 ans 중 어느 인덱스에 속하는 아나그램인지 판별하도록 한다
        
        이전에 저장되지 않은 아나그램일 경우 새로운 vector<string>을 ans에 추가하고
        unordered_map에 추가해준다

    strs의 개수 N, 평균 길이 L

    TC : O(N * L log(L))
        strs의 개수(N)만큼 반복문을 실시하고 sort는 L log(L)의 시간복잡도를 가져서

    SC : O(N * L)
        해시테이블 lookup의 크기는 최대 개수 * 평균길이 만큼 할당될 수 있으므로 (다 안겹칠 경우우)
*/

#include <vector>
#include <string>
using namespace std;

class Solution {
    public:
        vector<vector<string>> groupAnagrams(vector<string>& strs) {
            int index = 0;
            unordered_map<string, int>  lookup;
            vector<vector<string>>  ans;

            for (string& str : strs)
            {
                string sorted = str;
                sort(sorted.begin(), sorted.end());
                if(lookup.count(sorted))
                    ans[lookup[sorted]].push_back(str);
                else
                {
                    lookup[sorted] = index;
                    index++;
                    ans.push_back(vector<string>{str});
                }
            }
            return ans;
        }
    };
