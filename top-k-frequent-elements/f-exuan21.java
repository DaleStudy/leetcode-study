
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        
        PriorityQueue<Map.Entry<Integer, Integer>> queue = new PriorityQueue<>(
            (a, b) -> Integer.compare(b.getValue(), a.getValue())
        );

        for(Map.Entry<Integer, Integer> entry : map.entrySet()) {
            queue.offer(entry);
        }

        int[] res = new int[k];

        for(int i = 0; i < k; i++) {
            res[i] = queue.poll().getKey();
        }

        return res;
    }
}

// time : O(n) + O(m log m) + O(k log m) = O(n + m*logm + k*logm)
// 
// 최악의 경우 n log n 이 될 수 있음
// space : O(m) + O(m) + O(k) = O(m + k)
// 최악의 경우 n + k 가 될 수 있음

// n : nums의 길이
// m : nums에서 서로 다른 숫자의 개수

