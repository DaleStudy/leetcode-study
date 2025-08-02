// TC : O(n) : it iterates for the length of nums
// SC : O(n) : hashmap is created with the size of nums

func containsDuplicate(nums []int) bool {
    hashmap := make(map[int]bool)

    for i:=0;i<len(nums);i++ {
        if hashmap[nums[i]] {
            return true
        }

        hashmap[nums[i]] = true
    }

    return false
}

