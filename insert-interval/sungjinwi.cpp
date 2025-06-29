/*
    풀이 :
        기존 배열 중 start가 newInterval보다 빠르면서 newInterval과 겹치지 않는 요소들 result에 push
        겹치는 요소들은 newInterval에 통합 후 result에 push
        그 후 나머지 겹치지 않는 부분 result에 push

    intervals 개수 : N

    TC : O (N)
    
    SC : O (1)
        리턴하는 배열 외에 추가 공간 사용 X
*/

#include <vector>
using namespace std;

class Solution {
    public:
        vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
            vector<vector<int>> result;
            int i = 0;
            int n = intervals.size();
    
            while (i < n && intervals[i][1] < newInterval[0]) {
                result.push_back(intervals[i]);
                i++;
            }
    
            while (i < n && intervals[i][0] <= newInterval[1]) {
                newInterval[0] = min(intervals[i][0], newInterval[0]);
                newInterval[1] = max(intervals[i][1], newInterval[1]);
                i++;
            }
            result.push_back(newInterval);
    
            while (i < n) {
                result.push_back(intervals[i]);
                i++;
            }
            return result;
        }
    };
