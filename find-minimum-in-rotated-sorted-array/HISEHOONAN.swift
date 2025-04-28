//그냥 정렬 하고 0번째 인덱스 원소 추출
//O(nlogn)
// class Solution {
//     func findMin(_ nums: [Int]) -> Int {
//         var sortednums = nums.sorted()
//         return sortednums[0]
//     }
// }


//이진 탐색
//배열이 다 정렬이 되어야 가능하지 않나? 했는데
//이 문제는 '회전된 정렬 배열'이라서 이진 탐색이 가능하다캄.
//O(logn)
class Solution {
    func findMin(_ nums: [Int]) -> Int {
        var left = 0
        var right = nums.count - 1
        
        while left < right{
            var mid = (left+right)/2
            if nums[mid] > nums[right]{
                left = mid + 1
            }else{
                right = mid
            }
        }

        return nums[left]
    }
}
