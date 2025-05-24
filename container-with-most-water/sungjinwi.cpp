/*
    풀이 :
        최대 넓이는 양 끝 기둥 길이 중 짧은 쪽을 기준으로 정해진다
        양 끝에서 기둥을 시작하고 둘 중 짧은 쪽을 안쪽으로 이동하면서 최대 넓이를 찾는다

    height의 개수 : N

    TC : O(N)

    SC : O(1)
*/

class Solution {
    public:
        int maxArea(vector<int>& height) {
            int left = 0;
            int right = height.size() - 1;
            int max_area = 0;
    
            while (left < right)
            {
                int cur_area = (right - left) * min(height[left], height[right]);
                if (cur_area > max_area)
                    max_area = cur_area;
                if (height[left] <= height[right])
                    left++;
                else
                    right--;
            }
            return max_area;
        }
    };
