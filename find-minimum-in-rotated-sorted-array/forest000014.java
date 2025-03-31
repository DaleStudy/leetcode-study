/*
# Time Complexity: O(logn)
# Space Complexity: O(1)

binary search를 사용해 접근했습니다.
sorted array인 경우는 while문 시작 전, 예외 체크를 했습니다.
binary search를 진행하면, 각각의 loop의 mid 원소는 아래 4가지 경우 중 하나입니다.
maximum / minimum / 앞쪽 수열의 원소 중 하나 / 뒤쪽 수열의 원소 중 하나
maximum이거나 minimum인 경우는 더 이상 탐색할 필요 없이 종료합니다.
앞쪽 수열인 경우, 우리가 원하는 minimum은 왼쪽에는 없으므로, left 포인터를 mid의 오른쪽으로 옮기고 다음 loop를 진행하고,
뒤쪽 수열인 경우, 우리가 원하는 minimum은 오른쪽에는 없으므로, rigth 포인터를 mid의 왼쪽으로 옮기고 다음 loop를 진행합니다.

 */
class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int r = nums.length - 1;

        if (nums[l] <= nums[r]) { // sorted array인 경우 (size가 1인 경우도 포함)
            return nums[l];
        }

        while (l <= r) {
            int m = (r - l) / 2 + l; // 만약 문제 조건상 l, r의 합이 int 범위를 넘어가서 overflow가 생길 수 있는 경우에, 이런 식으로 overflow를 방지할 수 있다고 알고 있습니다. 이 문제는 overflow 걱정은 없지만, 나중에 실전에서 나오면 잊지 않으려고 이렇게 구현해보았습니다.
            if (m > 0 && nums[m - 1] > nums[m]) {
                return nums[m];
            } else if (m < nums.length - 1 && nums[m] > nums[m + 1]) {
                return nums[m + 1];
            } else if (nums[m] > nums[l]) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        return -1;
    }
}
