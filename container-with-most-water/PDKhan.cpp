class Solution {
    public:
        int maxArea(vector<int>& height) {
            int result = 0;
            int left = 0;
            int right = height.size() - 1;
    
            while(left < right){
                int len = right - left;
    
                if(height[left] < height[right]){
                    result = max(result, height[left] * len);
                    left++;
                }else{
                    result = max(result, height[right] * len);
                    right--;
                }
            }
    
            return result;
        }
    };
