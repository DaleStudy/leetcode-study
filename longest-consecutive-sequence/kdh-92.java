/**
 * Constraints:
 * - 0 <= nums.length <= 105
 * - -109 <= nums[i] <= 109
 *
 * Output
 * - 가장 긴 길이
 *
 * 풀이 특이점
 * - 둘다 시간복잡도는 O(N)으로 생각되는데 Runtime의 결과 차이가 꽤 크게 나온 점
 */

class Solution {
    public int longestConsecutive(int[] nums) {
        // (1) Set & num -1
        // 시간복잡도 : O(N)
        // Runtime : 1267ms Beats 5.15%
        // Memory : 63.30MB Beats 62.58%
        // Set<Integer> uniqueNums = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        // int result = 0;

        // for (int num : nums) {
        //     if (uniqueNums.contains(num - 1)) continue;
        //     int length = 1;
        //     while (uniqueNums.contains(num + length)) length += 1;
        //     result = Math.max(length, result);
        // }

        // return result;

        // (2) HashMap
        // 시간복잡도 : O(N)
        // Runtime : 38ms Beats 46.54%
        // Memory : 66.45MB Beats 51.28%
        HashMap<Integer, Boolean> hm = new HashMap<>();

        for(int i=0; i<nums.length; i++){
            hm.put(nums[i], false);
        }

        for(int key : hm.keySet()){
            if(hm.containsKey(key - 1)){
                hm.put(key, true);
            }
        }

        int max = 0;
        for(int key : hm.keySet()){
            int k =1;
            if(hm.get(key)){
                while(hm.containsKey(key + k)){
                    k++;
                }
            }

            max = Math.max(max, k);
        }

        return max;
    }
}
