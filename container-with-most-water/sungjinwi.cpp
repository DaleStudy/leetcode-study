class Solution {
    public:
        int maxArea(vector<int>& height) {
            int left = 0;
            int right = height.size() - 1;
            int ans = 0;
    
            while (left < right)
            {
                int cur = (right - left) * min(height[left], height[right]);
                if (cur > ans)
                    ans = cur;
                if (height[left] <= height[right])
                    left++;
                else
                    right--;
            }
            return ans;
        }
    };
