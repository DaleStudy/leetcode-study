class Solution {
  public int[] topKFrequent(int[] nums, int k) {
    int[] answer = new int[k];
    Map<Integer, Integer> count = new HashMap<>();

    for(int i = 0; i < nums.length; i++) {
      count.put(nums[i], count.getOrDefault(nums[i], 0) + 1);
    }

    PriorityQueue<int[]> queue = new PriorityQueue<>((a, b) -> b[1] - a[1]);

    for(int key : count.keySet()) {
      queue.offer(new int[]{key, count.get(key)});
    }

    for(int i = 0; i < k; i++) {
      int[] num = queue.poll();

      answer[i] = num[0];
    }

    return answer;
  }
}
