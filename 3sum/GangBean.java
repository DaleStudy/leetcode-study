class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        /**
            1. understanding
            - integer array nums, find the whole combination of 3 nums, and the sum of the 3 nums equal to 0. And don't allow reusing same indiced number(but can duplicate in value)
            2. solve strategy
            - brute force 
                - in every combination, validate sum of the nums equal to 0
                - but it can take O(N^3) times where N is the length of input array, and given that the N can be 3000 at most(3 * 10^3), time can be 27 * 10^9, which takes too long...
            - sort and two pointers
                - sort nums in ascending order, so move the left pointer to right means the sum of window is getting bigger.
                - and mid pointer set to left + 1 index
                - if sum of pointers is less than 0, then move mid pointer to right, until the sum is bigger than 0, and while processing them, if the sum of pointers is 0, then add the combination to the return list.
                - [-4, -1, -1, 0, 1, 2]: 
            
            3. complexity
                - time: O(N^2) -> each left pointer, you can search at most N-1, and left pointer's range is [0, N-1), so the max length is N-1 for left index pointer.
                - space: O(1) -> no extra space is needed
        */
        // 0. assign return variable Set
        Set<List<Integer>> answer = new HashSet<>();

        // 1. sort the num array in ascending order
        Arrays.sort(nums); // O(NlogN)
        // Arrays.stream(nums).forEach(System.out::println);

        // 3. move the mid pointer from left to right to find the combination of which's sum is 0, and if the sum is over 0, and then move right pointer to the left. else if the sum is under 0, then move left pointer to right direction.
        for (int left = 0; left < nums.length - 1; left++) {
            int mid = left + 1;
            int right = nums.length - 1;
            while (mid < right) {
                // System.out.println(String.format("%d,%d,%d", nums[left], nums[mid], nums[right]));
                int sum = nums[left] + nums[mid] + nums[right];
                if (sum > 0) {
                    right--;
                } else if (sum == 0) {
                    answer.add(List.of(nums[left], nums[mid], nums[right]));
                    right--;
                } else {
                    mid++;
                }
            }
        }

        return new ArrayList<>(answer);
    }
}

