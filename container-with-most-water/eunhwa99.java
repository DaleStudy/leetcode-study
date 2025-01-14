// two pointer

// 시간 복잡도: O(n) - 투 포인터
// 공간 복잡도: O(n) - height 배열 크기

class Solution {
    public int maxArea(int[] height) {
        int left=0;
        int right = height.length-1;

        int maxContainer = 0;
        while(left<right){
            int container = (Math.min(height[left], height[right])) * (right-left);
    
            maxContainer = Math.max(maxContainer, container);
            if(height[left]< height[right]) left++;
            else right--;
        }

        return maxContainer;
    }
}
