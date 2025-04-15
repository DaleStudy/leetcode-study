/*
    풀이 :
        nums 배열을 정렬시킨 후 반복되는 값을 건너뛰며 두 포인터 기법을 사용한다
        i포인터와 left, right 포인터의 값의 합이 0보다 작으면 left++, 크면 right--
        0이면 ans에 저장하고 left++, right--하는 로직을 left < right인 동안 반복한다
    
    nums의 길이 N

    TC : O(N^2)
        외부 반복문 N * 내부 반복문 N
    
    SC : O(1) (ans 제외)
        left, right, threeSum 3개의 변수만 사용한다
*/

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        int left;
        int right;
        int threeSum;

        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 2; i++)
        {
            // i포인터 중복 제거
            if (i > 0 && nums[i] == nums[i - 1])
                continue ;

            left = i + 1;
            right = nums.size() - 1;
            while (left < right)
            {
                threeSum = nums[i] + nums[left] + nums[right];
                if (threeSum < 0)
                    left++;
                else if(threeSum > 0)
                    right--;
                else
                {
                    ans.push_back({nums[i], nums[left], nums[right]});
                    // left포인터 중복 제거
                    while (left < right && nums[left] == nums[left + 1])
                        left++;
                    // right 포인터 중복 제거
                    while (left < right && nums[right] == nums[right - 1])
                        right--;
                    left++;
                    right--;
                }
            }
        }
        return ans;
    }
};
