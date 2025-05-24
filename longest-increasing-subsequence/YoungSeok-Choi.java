import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

// tc: O(n)
// idea: max largest subseq length for "N" th array index
class Solution {

    public int lengthOfLIS(int[] nums) {

        int[] arr = new int[nums.length];
        Arrays.fill(arr, 1);

        for(int i = 1; i < nums.length; i++) {
            for(int j = 0; j < i; j++) {
                if(nums[j] < nums[i]) {
                    arr[i] = Math.max(arr[i], arr[j] + 1);
                }
            }
        }

        int mx = -987654321;
        for(int anInt : arr) {
            System.out.print(anInt + " ");
            mx = Math.max(mx, anInt);
        }
        
        return mx;
    }
}

// time limit exceed

class WrongSolution {

    public boolean[] visit;
    public int mxVal = -987654321;
    public int mx = 1;
    public Map<Integer, Boolean> m = new HashMap<>();

    public int lengthOfLIS(int[] nums) {
        for(int i = 0; i < nums.length; i++) {
            m = new HashMap<>();
            mxVal = Math.max(mxVal, nums[i]);
            m.put(nums[i], true);
            dfs(i, nums);
            mxVal = -987654321;
        }

        return mx;   
    }

    public void dfs(int idx, int[] nums) {
        mx = Math.max(mx, m.size());

        for(int i = idx + 1; i < nums.length; i++) {
            if(mxVal < nums[i]) {
                int prev = mxVal;
                mxVal = nums[i];
                m.put(nums[i], true);

                dfs(i, nums);

                mxVal = prev;
                m.remove(nums[i]);
            }            
        }
    }
}
