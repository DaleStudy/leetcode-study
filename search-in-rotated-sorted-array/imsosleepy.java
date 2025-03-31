// O(log n)의 시간복잡도를 문제에서 요구하고 있다.
// O(log n)의 시간복잡도를 갖는 탐색 문제는 대부분 바이너리 서치로 해결된다.
// 주어진 배열이 정렬되어있다는 점에서 이진탐색을 이용하면 된다는 것을 알 수 있다.
class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target) {
                return mid;
            }

            // 왼쪽이 정렬된 경우
            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;  
                } else {
                    left = mid + 1;
                }
            }
            // 오른쪽이 정렬된 경우
            else {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        
        return -1;
    }
}
