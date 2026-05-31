/**
	브루트포스를 통해 모든 경우의 수를 연산하여 찾는 방식
	배열 height의 길이 -> N 
	시간 복잡도 : O(N^2) -> 시간 초과
	공간 복잡도 : O(1)
*/
class FailSolution {
    public int maxArea(int[] height) {
        int max=0;
        int area=0;
        for(int i=0;i<height.length;i++){
            for(int j=i+1;j<height.length;j++){
                area= Math.max(area,Math.min(height[j],height[i])*(j-i));
                if(area>max){
                    max=area;
                }
            }
        }
        return max;
    }
}

/**
	투포인터를 활용하여, 낮은 높이의 포인터를 갱신하면서 최대 넓이를 구하는 방식
	배열 height의 길이 -> N 
	시간 복잡도 : O(N)
	공간 복잡도 : O(1)
*/
class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int max = 0;
        while(left < right) {
            int h = Math.min(height[right], height[left]);
            int w = right - left;
            max = Math.max(max, w * h);

            if(h == height[right]) {
                right--;
            } else {
                left++;
            }
        }
        return max;
    }
}
