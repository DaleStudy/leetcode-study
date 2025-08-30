import java.util.Arrays;

public class Geegong {

    /**
     * case 1. binarySearch 를 이용, 범위를 1개의 원소부터 시작해서 점차 늘릴 수 있는 LIS 를 별도 변수에서 관리
     * 그리고 정렬이 되어가는 배열을 따로 저장하는 배열도 필요
     * Patience Sorting 아이디어 (?) -> 찾아보자
     * time complexity :
     * O(log n) - binary search 이고
     * 위 bs 를 각 원소별로 진행하기 때문에 o(n log n)
     * space complexity : O(n)
     *
     * case 2. DP
     * dp[i] => nums 의 i 번째 인덱스까지의 LIS 최장 길이를 의미
     * time complexity : O(n^2)
     * space complexity : O(n)
     *
     * @param nums
     * @return
     */
//    public static int lengthOfLIS(int[] nums) {
//        int n = nums.length;
//        int[] tails = new int[n];
//        int size = 0;
//
//        for (int x : nums) {
//            // 0 ~ size 안에서 이분탐색으로 넣을 수 있는 자리가 있으면 그 자리의 index 리턴 (따라서 tc 는 o(n log n)
//            // 넣을 수 없으면 음수값을 리턴하는데 ret = - (insertionPosition - 1)
//            // (0~size) 안에서 x 가 들어갈 수 있는 index는?=> insertionPosition = - (ret + 1) 이렇게 획득
//            int i = Arrays.binarySearch(tails, 0, size, x);
//            if (i < 0) i = -(i + 1); // lower_bound
//            tails[i] = x;
//            // size 는 nums 안에 원소들을 하나씩 훑어가면서 지금까지 LIS의 최장 길이
//            if (i == size) size++;
//        }
//        return size;
//    }

    public static int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length + 1];
        int maxLIS = 0;

        for (int index=0; index<nums.length; index++) {
            dp[index] = 1; // 첫번쨰 인덱스부터 LIS 는 1이라고 보자
            for (int innerIndex=0; innerIndex<index; innerIndex++) {
                // ex) {10,9,2,5,3,7,101,18};
                if (nums[innerIndex] < nums[index]) {
                    //dp[index] = dp[index] + 1; => 맨 처음에는 이렇게 생각했으나
                    dp[index] = Math.max(dp[index], dp[innerIndex] + 1);
                    // dp[innerIndex] + 1 에서 +1을 한 이유는 innerIndex의 값과 index의 값까지가 LIS가 될 것이기 때문에 더해진 것
                }
            }

            maxLIS = Math.max(maxLIS, dp[index]);
        }

        return maxLIS;
    }


}

