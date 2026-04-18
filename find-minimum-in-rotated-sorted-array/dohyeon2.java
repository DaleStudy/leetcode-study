public class Solution {
    // TC : O(log n)
    // SC : O(1)
    public int findMin(int[] nums) {
        // You must write an algorithm that runs in O(log n) time. => this means the solution is binary search
        int left = 0;
        int right = nums.length - 1;

        while(left < right){
            int mid = left + ((right - left) / 2);

            if(nums[right] > nums[mid]){
                right = mid;
            }else{
                left = mid + 1;
            }
        }

        return nums[left];
    }
}

// First attempt : the algorithm is correct but the condition is wrong.
// class Solution {
//     public int findMin(int[] nums) {
//         // You must write an algorithm that runs in O(log n) time. => this means the solution is binary search
//         int cursor = (nums.length - 1)  / 2;
//         int left = 0;
//         int right = nums.length - 1;

//         // 이전 값이 현재 값보다 커지는 경우가 종료
//         while(cursor - 1 >= 0 && nums[cursor - 1] < nums[cursor]){
//             int n = nums[cursor];
//             int rn = nums[right];

//             if(rn > n){
//                 right = cursor;
//             }else{
//                 left = cursor;
//             }

//             cursor = left + ((right - left) / 2);
//         }

//         return nums[cursor];
//     }
// }
