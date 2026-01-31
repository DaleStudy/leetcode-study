class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        int[] answer = new int[k];
        int n = nums.length;
        List<Data> result = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int key = nums[i];
            if (map.get(key) == null) {
                map.put(key, 1);
            } else {
                map.put(key, map.get(key) + 1);
            }
        }
        for (int key: map.keySet()) {
            result.add(new Data(key, map.get(key)));
        }
        result.sort((a, b) -> b.count() - a.count());

        for (int i = 0; i < k; i++) {
            answer[i] = result.get(i).key();
        }

        return answer;

    }
    record Data(
            int key,
            int count
    ){}
}


