import java.util.ArrayList;
import java.util.List;

// 답지보고 풀이..
class Solution {
    public int maxProduct(int[] nums) {
        int max = nums[0];
        int currMax = nums[0];
        int currMin = nums[0];

        for (int i = 1; i < nums.length; i++) {
            int temp = currMax;
            currMax = Math.max(nums[i], Math.max(currMax * nums[i], currMin * nums[i]));
            currMin = Math.min(nums[i], Math.min(temp * nums[i], currMin * nums[i]));
            max = Math.max(max, currMax);
        }

        return max;
    }
}

// NOTE:핵심 컨셉은 0을 만나기 전까지 한칸씩 늘려가며 모든 원소의 곱을 만든다. 0을 만나면 첫 번째 원소를 뺀 나머지 원소들의 곱의
// 값으로 최대값을 계속 갱신해나간다.
class WrongSolution {

    public int mx = -98764321;
    public List<Boolean> bList = new ArrayList<>();
    public boolean isStartInit = true;
    public boolean isOverZero = false;

    public int maxProduct(int[] nums) {
        int start = 1;
        int zeroIdx = 0;
        if (nums.length == 1) {
            return nums[0];
        }

        for (int i = 0; i < nums.length; i++) {

            if (nums[i] == 0) {
                if (mx <= 0) {
                    bList.add(false);
                } else {
                    bList.add(true);
                }

                while (zeroIdx < i) {
                    start /= nums[zeroIdx];
                    mx = Math.max(mx, start);

                    if (mx >= 1) {
                        bList.add(true);
                    }

                    zeroIdx++;
                }

                start = 1;
                isStartInit = true;
                zeroIdx++; // 0값인 인덱스를 건너뛰고 다음 번 인덱스를 대입
            } else {
                start *= nums[i];
                mx = Math.max(mx, start);

                if (start >= 1) {
                    isStartInit = false;
                    isOverZero = true;
                }
            }
        }

        while (zeroIdx < nums.length) {
            start /= nums[zeroIdx];
            mx = Math.max(mx, start);
            zeroIdx++;
        }

        mx = Math.max(mx, nums[nums.length - 1]);

        if (nums[nums.length - 1] >= 1) {
            isOverZero = true;
        }

        if (mx > 0 && isOverZero) {
            bList.add(true);
        }

        for (boolean b : bList) {
            if (b) {
                return mx;
            }
        }

        if (bList.size() > 0) {
            return isStartInit ? 0 : mx;
        }

        return mx;
    }
}
