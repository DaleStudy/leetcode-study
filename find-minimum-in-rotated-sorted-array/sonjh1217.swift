class Solution {
    func findMin(_ nums: [Int]) -> Int {
        var low = 1
        var high = nums.count - 1
        
        while low <= high {
            let mid = (low + high) / 2
            
            if nums[mid] < nums[mid - 1] {
                return nums[mid]
            }
            
            if nums[mid] > nums[0] {
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        
        return nums[0]
        
        //시간복잡도 O(logn)
        //공간복잡도 O(1)
    }
}

