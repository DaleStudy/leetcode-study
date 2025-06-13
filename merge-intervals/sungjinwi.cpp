/*
    풀이 :
        시작시간으로 interval을 정렬한 뒤에 첫번째 interval을 ans에 넣는다(.back() 메서드의 에러 방지)
        ans 배열의 마지막 interval과 시간이 겹치면 interval을 통합시키고
        겹치지 않으면 ans에 현재 interval을 넣고 반복

    interval 개수 : N

    TC : O (N logN)
        sort로 정렬

    SC : O (1)
        ans외에 추가적인 메모리 할당은 상수
*/

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
    public:
        vector<vector<int>> merge(vector<vector<int>>& intervals) {
            vector<vector<int>> ans;

            sort(intervals.begin(), intervals.end());
            ans.push_back(intervals[0]);

            for (int i = 1; i < intervals.size(); i++) {
                vector<int>& lastInterval = ans.back();

                if (intervals[i][0] <= lastInterval[1])
                    lastInterval[1] = max(lastInterval[1], intervals[i][1]);
                else
                    ans.push_back(intervals[i]);
            }
            return ans;
        }
    };
