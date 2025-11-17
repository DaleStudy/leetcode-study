import java.util.HashMap;
import java.util.Map;

public class Geegong {

    /**
     * top-down + memoization 방식으로 풀이
     * memoization (memo 변수) 없이 풀이하면 Time Limit Exceeded 발생
     * time complexity : O(N) -> memo 가 있어서 이미 연산이 된건 패스함
     * space complexity : O(N) -> index 만큼의 연산 결과가 있음
     * @param nums
     * @return
     */
    public int rob(int[] nums) {
        // memoization 하지 않으면 Time Limit Exceeded.
        Map<Integer, Integer> memo = new HashMap<>();

        int maxAmount = 0;
        for (int idx=0; idx<nums.length; idx++) {
            int currAmount = Math.max(
                    nums[idx] + rob(nums, idx+2, memo), rob(nums, idx+1, memo));
            maxAmount = Math.max(currAmount, maxAmount);
        }

        return maxAmount;
    }


    public int rob(int[] origin, int currIdx, Map<Integer, Integer> memo) {
        if (currIdx == origin.length - 1) {
            return origin[currIdx];
        } else if (currIdx >= origin.length) { // when out of bounds
            return 0;
        }

        if (memo.containsKey(currIdx)) {
            return memo.get(currIdx);
        }

        int currentVal = origin[currIdx];

        int maxAmount = Math.max(
                currentVal + rob(origin, currIdx + 2, memo), rob(origin, currIdx+1, memo));

        memo.put(currIdx, maxAmount);

        return maxAmount;
    }


}

