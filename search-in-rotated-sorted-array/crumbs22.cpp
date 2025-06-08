class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        while(left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target)
                return (mid);

            // 왼쪽 구간이 정렬된 상태일 때
            if (nums[left] <= nums[mid]) {
                // 왼쪽 구간에 있으면 right를 좁히면서 target을 탐색
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                }
                // 왼쪽 구간에 없다면 오른쪽 구간으로 이동
                else
                    left = mid + 1;
            }
            // 오른쪽 구간이 정렬된 상태
            else {
                // 오른쪽 구간에 target이 있으면 left를 좁히면서 target 탐색
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                }
                // 오른쪽 구간에 없다면 왼쪽 구간으로 이동
                else
                    right = mid - 1;
            }
        }
        return (-1);
    }
};
