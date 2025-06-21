/**
 * 0 ~ n까지 고유한 숫자들로 이루어진 배열 nums가 주어질 때 해당 범위 내에서 없어진 숫자를 찾으세요.
 */
class Solution {

    // 시간복잡도: O(n), 공간복잡도: O(n)
    public int missingNumber(int[] nums) {

        boolean[] visitNum = new boolean[nums.length + 1];

        for (int i = 0; i < nums.length; i++) {
            visitNum[nums[i]] = true;
        }

        for (int i = 0; i < visitNum.length; i++) {
            if (!visitNum[i]) {
                return i;
            }
        }

        return 0;
    }
}

