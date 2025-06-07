/*
    풀이 :
        mid를 기준으로 왼쪽이 정렬된 경우, 오른쪽이 정렬된 경우를 나누고
        정렬된 숫자 범위에 target값이 존재하느냐에 따라 범위를 이분 탐색으로 좁혀나간다

    - 이분탐색 시 종료조건 및 비교조건에서 등호를 포함시킬지 여부 고려 필요
        while (left <= right) -> 탐색 범위에 양 끝 인덱스 포함
            -> left = mid + 1 또는 right = mid - 1 로 새로운 범위 업데이트

        while (left < right) -> 탐색 범위에 오른쪽 끝 인덱스는 제외
            -> left = mid + 1 또는 right = mid 로 새로운 범위 업데이트

    nums 개수 N

    TC : O(logN)
        이분 탐색으로 찾아서 log2N의 복잡도를 갖는다
    
    SC : O(1)
*/

#include <vector>
using namespace std;

class Solution {
    public:
        int search(vector<int>& nums, int target) {
            int left = 0, right = nums.size() - 1;
    
            while (left <= right)
            {
                int mid = left + (right - left) / 2;
    
                if (nums[mid] == target)
                    return mid;
    
                if (nums[left] <= nums[mid]) {
                    if (nums[left] <= target && target < nums[mid])
                        right = mid -1;
                    else
                        left = mid + 1;
                }
                else {
                    if (nums[mid] < target && target <= nums[right])
                        left = mid + 1;
                    else
                        right = mid - 1;
                }
            }
            return -1;
        }
    };
