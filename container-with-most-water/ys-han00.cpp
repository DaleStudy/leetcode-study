// class Solution {
// public:
//     int maxArea(vector<int>& height) {
//         int n = height.size();
//         pair<int, int> left_wall = {0, height[0]};
//         int maxi = -1;
//         vector<int> dp(n, 0);

//         for(int i = 1; i < n; i++) {
//             for(int j = 0; j < i; j++) {
//                 dp[i] = max(dp[i], min(height[i], height[j]) * (i - j));
//                 if(height[j] > height[i]) 
//                     break;
//             }
//             maxi = max(maxi, dp[i]);
//         }

//         return maxi;
//     }
// };

class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1; 
        int ans = -1;

        while(left != right) {
            ans = max(ans, (right - left) * min(height[left], height[right]));
            if(height[left] < height[right])
                left++;
            else
                right--;
        }

        return ans;
    }
};

