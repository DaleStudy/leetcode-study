
/**
 * 정수 배열 nums와 정수 k가 주어질 때 자주 반복되는 값을 K개 반환
 * */
import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;

public class Solution {

    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }

        int[][] arr = map.entrySet().stream()
                .map((e) -> new int[]{e.getKey(), e.getValue()})
                .toArray(int[][]::new);

        Arrays.sort(arr, (f1, f2) -> f2[1] - f1[1]);

        int[] frequency = new int[k];
        for (int i = 0; i < k; i++) {
            frequency[i] = arr[i][0];
        }

        return frequency;

    }

}


