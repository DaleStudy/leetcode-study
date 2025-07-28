/*
Clarifications
1) Is this sorted Array?
2) What is the maximum / minimum value in nums?

Solutions
1) Brute force - two nested for loop 
T(C): O(n^2)
S(C): O(1)
2) Sort - Mergesort or library sort(Merge+quick)
T(C) : O(NlogN)
S(C) : O(N)
3) Hash
T(C) : O(1)
S(C) : O(N)
*/

class Solution {
public:
    // Solution 2-1) Library Sort
    // bool containsDuplicate(vector<int>& nums) {
    //     sort(nums.begin(), nums.end());
    //     for (size_t i = 0; i < nums.size() - 1; i++)
    //     {
    //         if (nums[i] == nums[i + 1])
    //             return true;
    //     }
    //     return false;
    // }

    // Solution 2-2) Implement Sort
    void mergeSort(vector<int>& nums, int start, int end, vector<int>& temp)
    {
        if (start >= end)
            return;
        int mid = (start + end) / 2;
        mergeSort(nums, start, mid, temp);
        mergeSort(nums, mid + 1, end, temp);
        int i = start, j = mid + 1, k = start;
        while (i <= mid && j <= end)
        {
            if (nums[i] < nums[j])
                temp[k++] = nums[i++];
            else
                temp[k++] = nums[j++];
        }
        while (i <= mid)
            temp[k++] = nums[i++];
        while (j <= end)
            temp[k++] = nums[j++];
        for (int p = start; p <= end; p++)
            nums[p] = temp[p];
    }
    // Solution 1-2) Library Sort
    // bool containsDuplicate(vector<int>& nums) {
    //     vector<int> temp(nums.size(), 0);
    //     mergeSort(nums, 0, nums.size() - 1, temp);
    //     for (size_t i = 0; i < nums.size() - 1; i++)
    //     {
    //         if (nums[i] == nums[i + 1])
    //             return true;
    //     }
    //     return false;
    // }

    // solution 2 - hash
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> hash;
        for (size_t i = 0; i < nums.size(); i++)
        {
            if (hash.find(nums[i]) != hash.end())
                return true;
            hash[nums[i]] = i;
        }
        return false;
    }
};