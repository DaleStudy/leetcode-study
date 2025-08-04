from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        zero_sum_triplets = []
        nums.sort()  # Sort to handle duplicates and enable two-pointer approach

        for first_index in range(len(nums) - 2):
            # Skip duplicate values for the first position
            if first_index > 0 and nums[first_index] == nums[first_index - 1]:
                continue

            # Use two-pointer technique to find complementary pairs
            second_index = first_index + 1
            third_index = len(nums) - 1

            while second_index < third_index:
                current_sum = nums[first_index] + nums[second_index] + nums[third_index]

                if current_sum == 0:
                    # Found a valid triplet
                    zero_sum_triplets.append(
                        [nums[first_index], nums[second_index], nums[third_index]]
                    )

                    # Skip duplicates for second and third positions
                    while (
                        second_index < third_index
                        and nums[second_index] == nums[second_index + 1]
                    ):
                        second_index += 1
                    while (
                        second_index < third_index
                        and nums[third_index] == nums[third_index - 1]
                    ):
                        third_index -= 1

                    # Move both pointers inward
                    # (In a balanced state where sum=0, moving only one pointer would unbalance it)
                    second_index += 1
                    third_index -= 1

                elif current_sum < 0:
                    # Current sum is too small, need a larger value
                    second_index += 1
                else:
                    # Current sum is too large, need a smaller value
                    third_index -= 1

        return zero_sum_triplets
