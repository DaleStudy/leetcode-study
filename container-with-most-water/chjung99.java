// two pointer
// time: O(N)
// space: O(1)
class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length-1;
        int answer = 0;

        int waterWidth = 0;
        int waterHeight = 0;

        while (left < right){
            waterWidth = (right - left);
            waterHeight = Math.min(height[left], height[right]);
            answer = Math.max(answer, waterWidth * waterHeight);
            if (height[left] <= height[right]) {
                left ++;
            }else{
                right --;
            }
        }

        return answer;
    }
}

