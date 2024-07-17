- 문제: https://leetcode.com/problems/jump-game/
- 풀이: https://algorithm.jonghoonpark.com/2024/07/17/leetcode-55

## dfs로 풀기

```java
class Solution {
    boolean canJump = false; // 마지막 위치에 도착 할 수 있으면 true 로 변경

    public boolean canJump(int[] nums) {
        dfs(nums, 0);

        return canJump;
    }

    private void dfs(int[] nums, int pointer) {
        // 위치가 범위를 벗어났을 경우
        // 이미 방문한 위치일 경우
        // 이미 마지막에 도달 가능하다는 것을 확인했을 경우
        if (pointer >= nums.length || nums[pointer] == -1 || canJump) {
            return;
        }

        int maxHeight = nums[pointer];
        nums[pointer] = -1;

        // 마지막이 아닌데 0 이 나왔을 경우 이동 불가능
        if (maxHeight == 0 && pointer != nums.length - 1) {
            return;
        }

        if (pointer == nums.length - 1) {
            canJump = true;
        } else {
            while (maxHeight > 0) {
                dfs(nums, pointer + maxHeight);
                maxHeight--;
            }
        }
    }
}
```

### TC, SC

시간복잡도는 `O(n^2)`, 공간복잡도는 `O(n)` 이다.

## dp로 풀기

중간에 도달하지 못하는 위치가 있을 경우 false를 반환한다. dp 라고 해도 되려나 애매한 것 같다.

```java
class Solution {
    public boolean canJump(int[] nums) {
        int[] dp = new int[nums.length];
        int lastIndex = nums.length - 1;
        dp[0] = 1;

        for (int i = 0; i < nums.length; i++) {
            if (dp[i] == 0) {
                return false;
            }

            int current = nums[i];
            int toIndex = i + current + 1;
            if(toIndex > lastIndex) {
                toIndex = nums.length;
            }
            Arrays.fill(dp, i, toIndex, 1);
            if (dp[lastIndex] > 0) {
                return true;
            }
        }

        return dp[lastIndex] != 0;
    }
}
```

### TC, SC

시간복잡도는 `O(n^2)`, 공간복잡도는 `O(n)` 이다.

## greedy 방식으로 풀기

greedy 문제는 항상 어떻게 증명할 수 있는지를 고민을 많이 해봐야 하는 것 같다.

```java
class Solution {
    public boolean canJump(int[] nums) {
        int maxReach = 0;  // 현재까지 도달할 수 있는 가장 먼 인덱스

        for (int i = 0; i < nums.length; i++) {
            if (i > maxReach) {
                return false;  // 현재 인덱스에 도달할 수 없는 경우
            }
            maxReach = Math.max(maxReach, i + nums[i]);
            if (maxReach >= nums.length - 1) {
                return true;  // 마지막 인덱스에 도달하거나 그 이상일 경우
            }
        }

        return false;
    }
}
```

### TC, SC

시간복잡도는 `O(n)`, 공간복잡도는 `O(1)` 이다.
