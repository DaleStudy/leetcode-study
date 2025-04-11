///정수배열 nums가 주어질때 정수배열 answer를 반환하시오
///answer의 각 요소는 nums의 같은 인덱스의 요소를 제외한 나머지 요소의 곱

//복잡도 O(n)
class Solution {
    func productExceptSelf(_ nums: [Int]) -> [Int] {  //nums = 1,2,3,4
        let n = nums.count
        var answer = [Int](repeating: 1, count: n)  //answer = 1,1,1,1
        var left = [Int](repeating: 1, count: n)  //left = 1,1,1,1

        let revNums = Array(nums.reversed())  //revNums = 4,3,2,1
        var right = [Int](repeating: 1, count: n)  //right = 1,1,1,1

        for i in 1..<n {  //i = 1,2,3
            left[i] = left[i-1] * nums[i-1] //left = 1,1,2,6
            right[i] = right[i-1] * revNums[i-1] //right = 1,4,12,24
        }

        for i in answer.indices {
            answer[i] = left[i] * right[n-i-1]
        }

        return answer

    }
}
