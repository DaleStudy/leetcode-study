class Solution {
    public int findMin(int[] nums) {
        /**
        1.problem: 오름차순 정렬된 original으로부터 최소횟수만큼 n번 rotate한다. 이 배열에서 최솟값 구하기
        2.조건
        - 주어진 배열은 1 ~ n 번 rotated 되었다.
        - 배열의 원소는 모두 unique 한 값
        - n = numslength
        - O(log n)으로 풀이할것
        - n = 1 ~ 5000
        3.풀이
        - bruteforce: nums 돌다가 작아지는 부분이 생기면 거기가 rotate 한 횟수, time : O(n), space: O(1)
        - binary search: left, right 탐색

        [1, 2, 3, 4, 5]
        [5, 1, 2, 3, 4] -> 1
        [4, 5, 1, 2, 3] -> 2
        [3, 4, 5, 1, 2] -> 3 : index 3 구간에서 숫자 작아짐
         */
        int answer = nums[0];
         int n = nums.length;
         if(n == 1) return answer;

        //sol 1)
        // for(int i = 0; i < n-1; i++) {
        //     if(nums[i] > nums[i+1]) {
        //         return nums[i+1];
        //     }
        // }
        //return answer;

        //sol 2)
        int left = 0;
        int right = n - 1;
        while(left < right) {
            int mid = (left + right) / 2;
            if(nums[mid] > nums[right]) {
               left = mid + 1;
            } else {
                right = mid;
            }
        }

        return nums[left];

    }
}
