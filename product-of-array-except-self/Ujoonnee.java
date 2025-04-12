/*
# 목표 : i 전까지의 곱 * i 이후로의 곱
## i 전까지의 곱
- 0 : 1 (nums[0]은 이전 곱이 없으므로, 1 * (이후 곱)로 처리한다)
- 1   : nums[0]
- 2   : nums[0] * nums[1]
- 3   : nums[0] * nums[1] * nums[2]
- n-1 : nums[0] * nums[1] * ... * nums[n-1]

### 매 단계 겹치는 부분을 저장한다. (before)
- 0 : 1
- 1 : before[0] * nums[0];
- 2 : before[1] * nums[1];
- 3 : before[2] * nums[2];
=> O(n)

## i 이후로의 곱
- 0 : nums[1] * nums[2] * nums[3] ... nums[n-1]
- 1 :           nums[2] * nums[3] ... nums[n-1]
- 2 :                     nums[3] ... nums[n-1]
...
- n-1 : 1 (nums[n-1]은 이후 곱이 없으므로, (이전 곱) * 1로 처리한다)

### 매 단계 겹치는 부분을 저장하되, 역순으로 반복해 저장한 값을 사용한다. (after)
- n-1 : 1
- n-2 : after[n-1] * nums[n-1]
- n-3 : after[n-2] * nums[n-2]
...
- 0 : after[1] * nums[1]
=> O(n)

## before 와 after 의 값을 곱한다.
=> O(n)
*/

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] before = new int[n];
        int[] after = new int[n];

        before[0] = 1;
        for(int i=1; i<n; i++) {
            before[i] = before[i-1] * nums[i-1];
        }

        after[n-1] = 1;
        for(int i=n-2; i>=0; i--) {
            after[i] = after[i+1] * nums[i+1];
        }

        for(int i=0; i<n; i++) {
            after[i] *= before[i];
        }

        return after;
    }
}
