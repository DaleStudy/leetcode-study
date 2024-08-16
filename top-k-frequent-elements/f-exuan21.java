
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

// n : nums의 길이
// m : nums에서 서로 다른 숫자의 개수

// time : O(n) + O(m*logm) + O(k*logm) = O(n + m*logm + k*logm)
// 최악의 경우, nums 가 다 unique 하기 때문에 n == m == k 가 됨
// 따라서, O(n*logn)

// space : O(m) + O(m) + O(k) = O(m + k)
// 최악의 경우 n == m == k 가 됨
// 따라서, O(n)



