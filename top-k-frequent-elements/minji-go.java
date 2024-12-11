class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        for(int num : nums){
            count.put(num, count.getOrDefault(num, 0)+1);
        }
        List<Integer> tops = count.keySet().stream()
                .sorted((i1, i2) -> count.get(i2)-count.get(i1))
                .limit(k)
                .toList();

        int[] answer = new int[k];
        for(int i=0; i<k; i++) {
            answer[i] = tops.get(i);
        }
        return answer;
    }
}
