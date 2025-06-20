/*
    풀이 :
        종료시간을 오름차순으로 정렬
        intervals를 순회하면서 시간이 겹치면 현재의 interval을 삭제 (종료시간이 큰 interval이 삭제되는게 더 최소한으로 삭제할 수 있으므로)
        겹치지 않으면 lastEnd를 현재 interval의 end로 업데이트

    TC : O (N log N)
        sort에 n log n의 시간복잡도

    SC : O (1)
*/

#include <vector>
#include <algorithm>
#include <limits.h>

using namespace std;

class Solution {
    public:
        int eraseOverlapIntervals(vector<vector<int>>& intervals) {

            sort(intervals.begin(), intervals.end(), [] (vector<int>& a, vector<int>& b){ return a[1] < b[1]; });
    
            int cnt = 0;
            int lastEnd = INT_MIN;

            for (auto& interval : intervals) {
                if (interval[0] < lastEnd)
                    cnt++;
                else
                    lastEnd = interval[1];
            }

            return cnt;
        }
    };
