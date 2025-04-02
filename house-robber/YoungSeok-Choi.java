import java.util.HashMap;
import java.util.Map;

// 시간복잡도: O(n)
// TODO: DP 방식으로 풀어보기
class Solution {
    public Map<Integer, Integer> robMap = new HashMap<>();
    public int rob(int[] nums) {
        return dfs(nums, 0);
    }

    public int dfs(int[] nums, int index) {
        if(nums.length == 0) {
            return 0;
        }

        if(index >= nums.length) {
            return 0;
        }

        // 이미 털었던 집이라면, 해
        if(robMap.containsKey(index)) {
            return robMap.get(index);
        }

        // 이번 집을 털게되는 경우
        int robThis = nums[index] + dfs(nums, index + 2);

        // 이번 집을 털지않고 건너뛰는 경우,.
        int skipThis = dfs(nums, index + 1);

        robMap.put(index, Math.max(robThis, skipThis));

        return robMap.get(index);
    }
}

// TODO: 비효율적으로 작성한 알고리즘의 동작 방식을 도식화 해서 그려보기.
// NOTE: dfs를 사용한 완전탐색
// 탐색 방식이 매우 비효율적이라, 정답은 맞추지만 N이 커지면 시간초과
// 시간복잡도: O(2^n) + alpha(중복탐색)
class WrongSolution {
    public boolean[] visit;
    public int mx = -987654321;
    public int curSum = 0;

    public int rob(int[] nums) {
        if(nums.length == 1) {
            return nums[0];
        }

        visit = new boolean[nums.length];
        dfs(nums, 0);
        dfs(nums, 1);

        return mx;
    }

    public void dfs(int[] arr, int idx) {
        int len = arr.length;
        int prevIdx = idx - 1;
        int nextIdx = idx + 1;
        

        if(idx == 0) {
            if(visit[idx]) return;
        } else {
            if(idx >= len || visit[idx] || visit[prevIdx]) {                
                return;
            }
        }

        visit[idx] = true;
        curSum += arr[idx];
        mx = Math.max(mx, curSum);

        for(int i = idx; i < len; i++) {
            dfs(arr, i);
        }        

        visit[idx] = false;
        curSum -= arr[idx];
    }
}