class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length; 
        int[] answer = new int[n]; 

        // prefix product 
        answer[0] = 1; 
        for (int i = 1; i < n; i++) {
            answer[i] = answer[i - 1] * nums[i - 1]; 
        }

        // suffix product 
        int suffix = 1; 
        for (int i = n - 1; i >= 0; i--) {
            answer[i] *= suffix; // answer의 prefix에 곱 ->  자기 자신 제외한 전체 곱 완성
            suffix *= nums[i]; // suffix 갱신 (*nums[i] 누적)
        }

        return answer; 
    }
}

/**
    return int[] answer 
    -> product of all nums except nums[i]

    prefix -> answer[i] = nums[0] * nums[1] * ... * nums[i-1]
    answer[i-1] * nums[i-1] 로 점화식 표현. 
    suffix -> suffix[i] = nums[i+1] * nums[i+2] * ... * nums[n-1]

    MUST: O(n) time w/o division like total product / nums[i] 

    answer[i] = prefix[i] * suffix[i]; 
    but in O(1) extra space complexity 
    -> no extra arr for suffix -> var suf *= nums[i] 로 누적 
 */
