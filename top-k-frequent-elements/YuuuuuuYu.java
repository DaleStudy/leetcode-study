/**
 * Runtime: 15ms
 * Time Complexity: O(n log n)
 * - 빈도 계산: O(n)
 * - 정렬: O(u log u) ≤ O(n log n)
 * - k개 추출: O(k)
 *
 * Memory: 47.73MB
 * Space Complexity: O(n)
 * - HashMap: O(u) ≤ O(n)
 * - List: O(u) ≤ O(n)
 *
 * Approach: HashMap으로 빈도 계산 후 정렬하여 top k 추출
 * - 배열 순회하여 각 원소의 빈도 계산
 * - 빈도 기준 내림차순 정렬
 * - 상위 k개 원소 추출
 */
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> frequentMap = new HashMap<>();
        for (int num: nums) {
            frequentMap.put(num, frequentMap.getOrDefault(num, 0)+1);
        }

        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(frequentMap.entrySet());
        list.sort((a, b) -> b.getValue() - a.getValue());

        int[] result = new int[k];
        for (int i=0; i<k; i++) {
            result[i] = list.get(i).getKey();
        }

        return result;
    }
}
