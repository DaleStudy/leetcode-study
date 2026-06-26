
/**
 * 
 * 시간 복잡도: O(n log n)
 * 공간 복잡도: O(n)
 */
class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        Map<Integer, Integer> counter = new HashMap<>();

        for (int num : nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }

        List<Integer> list = new ArrayList<>(counter.keySet());

        // 빈도수 내림차순 정렬
        list.sort((a, b) -> Integer.compare(counter.get(b), counter.get(a)));

        int[] result = new int[k];

        for (int i = 0; i < k; i++) {
            result[i] = list.get(i);
        }

        return result;
    }
}
