import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {


    // priority queue 로 풀어보기
    public int[] topKFrequent(int[] nums, int k) {

        // 빈도수를 셈
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        // 갯수만큼 배열 생성 (빈도수를 인덱스로 가지는)
        List<Integer>[] bucket = new List[nums.length + 1]; // freq는 최대 nums.length
        for (int i = 0; i < bucket.length; i++) {
            bucket[i] = new ArrayList<>();
        }

        for (Map.Entry<Integer, Integer> entry : freqMap.entrySet()) {
            int num = entry.getKey();
            int freq = entry.getValue();
            bucket[freq].add(num);
        }

        // 빈도수가 높은 뒤에서부터 넣어줌
        List<Integer> result = new ArrayList<>();
        for (int i = bucket.length - 1; i >= 0 && result.size() < k; i--) {
            if (!bucket[i].isEmpty()) {
                result.addAll(bucket[i]);
            }
        }

        // k개만 반환
        return result.subList(0, k).stream().mapToInt(i -> i).toArray();
    }
}