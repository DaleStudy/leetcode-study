/**
 * 길이가 n인 오름차순으로 정렬된 숫자 배열이 1 ~ n번 회전했다. 회전된 배열에서 가장 작은 수를 찾아서 반환하시오.
 */
class Solution {

    // 이진 탐색: 시간복잡도: O(log n)
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return nums[left];
    }


// 1차는 단순하게 앞뒤 배열 요소 비교로 풀어봄: O(n^2)
// Submission은 되었지만 시간 복잡도 기준을 못 맞춘 것 같아서 이진 탐색으로 재풀이 진행
//    public int findMin(int[] nums) {
//        int rotate = 0;
//        for (int i = 0; i < nums.length - 1; i++) {
//            int idx = (i + rotate) < nums.length ? (i + rotate) : (i + rotate) - nums.length;
//            int nextIdx = idx + 1 < nums.length ? idx + 1 : nums.length - (idx + 1);
//            if (nums[idx] > nums[nextIdx]) {
//                rotate++;
//                i = -1;
//            }
//        }
//        return nums[rotate];
//    }

}

