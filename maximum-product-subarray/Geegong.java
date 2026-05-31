public class Geegong {

    /**
     * kadane's algorithm 으로 풀이
     * 위 알고리즘은 contiguous array 에 대한 문제를 풀이할 때 자주 쓰임
     * time complexity : O(N)
     * space complexity : O(1)
     * @param nums
     * @return
     */
    public int maxProduct(int[] nums) {
        int currMaxProd = nums[0];
        int currMinProd = nums[0];
        int max = nums[0];

        for (int idx=1; idx<nums.length; idx++) {
            int num = nums[idx];

            // currMaxProd 가 변경되고 난 후에 currMinProd 를 구하기 때문에 currMinprod 를 구하기 위해 임시 저장
            int tempMaxProd = currMaxProd;
            currMaxProd = Math.max(num, Math.max(currMaxProd * num, currMinProd * num));
            currMinProd = Math.min(num, Math.min(currMinProd * num, tempMaxProd * num));

            max = Math.max(currMaxProd, max);
        }

        return max;
    }
}
