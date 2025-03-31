// 정렬을 하고하면 O(nlogn)이 나온다.
// 정렬이 되어있다 가정할 수 있으니 배열을 모두 탐색해서 편차가 가장 큰걸 찾으면 O(n)
// 위 두 방법은 속도가 너무 느리게 나와서 다른 방법을 찾아보니
// 가장 빠른 방법은 최소값만 찾으면 되니 이진 탐색으로 찾으면 O(logn)
class Solution {
    public int findMin(int[] nums) {
        int left = 0, right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2; // 중간 인덱스

            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return nums[left];
    }
}
