class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = height.size() - 1;

        int area = 0;

        // 투 포인터로 접근
        while (l < r)
        {
            // 너비(물 저장량)를 구하고 최댓값 업데이트
            area = max(area, (r - l) * min(height[r], height[l]));

            // 높이가 낮은 쪽의 커서를 이동
            // -> 높은 쪽의 커서를 움직이면 무조건 손해
            // -> 너비는 줄어들고 높이까지 줄어드니까
            if (height[l] < height[r])
            {
                l++;
            }
            else
            {
                r--;
            }
        }

        return area;
    }
};
