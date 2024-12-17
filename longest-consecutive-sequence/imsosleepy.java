// 중복여부만 제거하고 포함여부로 판단 O(N)
class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }

        int maxLength = 0;

        for (int num : set) {
            if (!set.contains(num - 1)) {
                int currentNum = num;
                int count = 1;
                while (set.contains(currentNum + 1)) {
                    currentNum++;
                    count++;
                }

                maxLength = Math.max(maxLength, count);
            }
        }

        return maxLength;
    }
}
// 정렬이 들어가면 O(nlogn) 아래로 줄일 수 없음
class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length == 0) return 0;
        TreeSet<Integer> set = new TreeSet<>();
        for (int num : nums) {
            set.add(num);
        }
        int max = 1;
        int consecutiveCount = 1;
        int prev = set.pollFirst();
        while(!set.isEmpty()) {
            int next = set.pollFirst();
            if (next - prev == 1) {
                consecutiveCount++;
            } else {
                max = Math.max(consecutiveCount, max);
                consecutiveCount = 1;
            }
            prev = next;
        }
        return Math.max(max, consecutiveCount);
    }
}
// 이중 변환 필요 없음
class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length == 0) return 0;
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>(set);
        int max = 1;
        int consecutiveCount = 1;
        int prev = pq.poll();
        while(!pq.isEmpty()) {
            int next = pq.poll();
            if (next - prev == 1) {
                 consecutiveCount++;
             } else {
                max = Math.max(consecutiveCount, max);
                consecutiveCount = 1;
            }
            prev = next;
        }
        return Math.max(max, consecutiveCount);
    }
}
