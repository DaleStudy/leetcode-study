#include <iostream>
#include <vector>
#include <set>

using namespace std;

/*
    TC: O(nlogn)
        - 정렬된 벡터 s 생성: O(nlogn) ... std::set은 이진 검색 트리를 기반으로 한다
        - s의 순회: O(n)
        => 전체 시간 복잡도: O(nlogn)
    SC: O(n)

    풀이 방법: nums에 대한 정렬된 벡터 s의 루프를 돌면서
             연속되는 다음 값을 변수 i로 두고 i값과 비교해서 연속되지 않는다면 다시 1부터 최장길이를 센다.
*/

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> s(nums.begin(), nums.end()); // set은 정렬된 벡터이다
        int cnt;
        int max = 0;

        int i = *s.begin(); // 초기 비교값은 테이블의 첫번째 값으로 둔다
        for (set<int>::iterator iter = s.begin(); iter != s.end(); iter++)
        {
            if (*iter != i) // 테이블의 현재 값이 연속되어야 하는 값이 아닌 경우
            {
                cnt = 1;
                i = *iter + 1;
                continue;
            }
            cnt++;
            i++;
            if (cnt > max)
                max = cnt;
        }
        return (max);
    }
};
