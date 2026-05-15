class Solution {
public:
    int missingNumber(vector<int>& nums) {
        // 1부터 n까지 합을 구하고, 배열 요소들의 합을 빼서 빠진 수를 찾음
        int n = nums.size();
        int sum = (n * (n + 1)) / 2;
        int acc = 0;
        for (int num : nums)
        {
            acc += num;
        }

        return sum - acc;
    }
};
