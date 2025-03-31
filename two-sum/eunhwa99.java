// two pointer

import java.util.Arrays;
import java.util.Comparator;

class Point {
    int index;
    int value;
    Point(int index, int value){
        this.index = index;
        this.value = value;}

}

// 시간 복잡도: O(nlogn) - 정렬
// 공간 복잡도: O(n) - Point 객체 배열
class Solution{
    public int[] twoSum(int[] nums, int target) {
        Point[] points = new Point[nums.length];
        for(int i = 0; i < nums.length; i++){
            points[i] = new Point(i, nums[i]);
        }
        Arrays.sort(points, Comparator.comparingInt(p -> p.value));
        int[] result = new int[2];
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            int sum = points[left].value + points[right].value;
            if (sum == target) {
                result[0] = points[left].index;
                result[1] = points[right].index;
                break;
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        return result;
    }
}