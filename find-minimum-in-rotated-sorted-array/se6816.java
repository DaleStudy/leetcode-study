/**
    for문 순회를 통해 최소값 찾기
    nums의 길이 -> N
    시간 복잡도 : O(N)
    공간 복잡도 : O(1)
 */
class Solution {
    public int findMin(int[] nums) {
        int result = Integer.MAX_VALUE;
        for(int num : nums) {
            result = Math.min(result, num);
        }
        return result;
    }
}
