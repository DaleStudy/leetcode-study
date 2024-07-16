- 문제: https://leetcode.com/problems/maximum-product-subarray/
- 풀이: https://algorithm.jonghoonpark.com/2024/07/09/leetcode-152

```java
class Solution {
    public int maxProduct(int[] nums) {
        int max = Integer.MIN_VALUE;
        int temp = 0;
        int lastZeroIndex = 0;
        for (int i = 0; i < nums.length; i++) {
            int current = nums[i];
            if (temp == 0) {
                temp = current;
                lastZeroIndex = i;
            } else {
                if (current == 0) {
                    temp = 0;
                } else if (temp > 0 && current < 0) {
                    if (hasNextMinus(nums, i + 1)) {
                        temp = temp * current;
                    } else {
                        temp = temp * current;
                        for (int j = lastZeroIndex; j < i + 1; j++) {
                            temp = temp / nums[j];
                            if (temp > 0) {
                                break;
                            }
                        }
                    }
                } else {
                    temp = temp * current;
                }
            }
            max = Math.max(max, temp);
            if (temp < 0 && !hasNextMinus(nums, i + 1)) {
                temp = 0;
            }
        }
        return max;
    }

    private boolean hasNextMinus(int[] nums, int i) {
        for (; i < nums.length; i++) {
            if (nums[i] < 0) {
                return true;
            } else if (nums[i] == 0) {
                return false;
            }
        }
        return false;
    }
}
```

### TC, SC

시간 복잡도는 O(n^2)이다. 공간 복잡도는 O(1)이다. hasNextMinus 이 적게 호출된다면 시간 복잡도는 O(n)에 가깝게 동작한다.
