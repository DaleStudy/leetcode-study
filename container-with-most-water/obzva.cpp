/**
 * 풀이
 * - container의 밑변이 넓고 높이가 높을 수록 저장하는 물의 양이 많습니다
 * - 따라서 밑변이 가장 넓은 container부터 탐색하면 탐색 효율을 높일 수 있다는 생각을 했습니다
 * - 양 끝에서부 two pointer를 이용하여 탐색을 시작합니다
 * - lo, hi 중에서 높이가 더 낮은 pointer를 안쪽으로 이동시킵니다
 * - 왜냐하면 높이가 더 낮은 pointer를 이동시켰을 때 기존 container보다 더 높이가 높은 container를 만들 수 있는 가능성이 생기기 때문입니다
 * 
 * Big O
 * - N: 주어진 배열 height의 크기
 * 
 * - Time complexity: O(N)
 *   - 배열 height를 조회하므로 전체 실행시간 또한 N에 비례하여 선형적으로 증가합니다
 * 
 * - Space complexity: O(1)
 */

class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        int lo = 0;
        int hi = n - 1;

        int res = 0;
        while (lo < hi) {
            int w = hi - lo;
            int h = min(height[lo], height[hi]);
            
            res = max(res, w * h);

            if (height[lo] > height[hi]) {
                --hi;
            } else {
                ++lo;
            }
        }

        return res;
    }
};
