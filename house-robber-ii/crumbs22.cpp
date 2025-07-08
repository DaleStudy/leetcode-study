class Solution {
public:
    int rob(vector<int>& nums) {
        
        if (nums.size() == 1)
            return (nums[0]);

        // 첫번째 집 ~ 마지막 - 1번째 집까지
        int prev = 0;
        int curr = nums[0];

        for (int i = 1; i + 1 < nums.size(); i++) {
            int tmp = curr;
            // 바로 전 집을 터는 게 나은지, 전전번째 집과 현재(nums[i])집을 터는 게 나은지 판별
            curr = max(curr, prev + nums[i]); 
            prev = tmp; // 전전번째 집의 값을 갱신
        }
        int fstrob = curr;

        // 두번째 집 ~ 마지막 집까지
        prev = 0;
        curr = nums[1];
        for (int i = 2; i < nums.size(); i++) {
            int tmp = curr;
            curr = max(curr, prev + nums[i]); 
            prev = tmp;
        }
        int scdrob = curr;

        return max(fstrob, scdrob);
    }
};
