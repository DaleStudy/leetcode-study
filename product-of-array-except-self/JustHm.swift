class Solution {
    // time: O(n), space: O(n)
    func productExceptSelf(_ nums: [Int]) -> [Int] {
        var resultFromFirst = [1]
        var resultFromLast = [1]
        // 기준 원소의 왼쪽 곱은 resultFromFirst에 저장
        // 기준 원소의 오른쪽 곱은 resultFromLast에 저장
        for i in 1..<nums.count {
            resultFromFirst.append(resultFromFirst[i-1] * nums[i-1])
            resultFromLast.append(resultFromLast[i-1] * nums[nums.count - i])
        }
        // 결과 반환시 순서를 생각해서
        //resultFromFirst는 첫번째 원소부터 마지막 원소까지, resultFromLast는 마지막 원소 부터 첫번째 원소까지, 서로를 곱해준다.
        return (0..<nums.count).map { resultFromFirst[$0] * resultFromLast[nums.count - $0 - 1] }
    }
}
//Input: nums = [1,2,3,4]
//Output: [24,12,8,6]
/*
 2*3*4, 3*4, 4, 1 오른쪽 부분 곱
 1, 1, 1*2, 1*2*3 왼쪽 부분 곱
*/

// 공간 복잡도를 O(1)로도 해결이 가능하다! (결과배열 제외)
// 아이디어를 생각해보자.
/*
 1. 결과 배열을 하나 만든다.
 2. nums의 원소들을 사용해 왼쪽부분 곱을 먼저 결과배열에 저장한다.
 3. 오른쪽 부분 곱을 차례대로 계산에 결과배열 원소에 곱연산해 저장한다.
 4. 반환!
*/
class Solution {
    func productExceptSelf(_ nums: [Int]) -> [Int] {
        var result = Array(repeating: 1, count: nums.count)
        for i in 1..<nums.count {
            // 원래 하던대로 왼쪽 부분 곱으로 초기화
            result[i] = result[i-1] * nums[i-1]
        }
        
        var temp = 1 // 오른쪽 곱 값을 저장해 둘 변수
        for i in 1...nums.count {
            // 결과 배열의 마지막 부터 self 의 오른쪽 부분 곱 시작
            result[nums.count - i] *= temp
            // 연산 후 temp에 nums의 오른쪽 원소 하나씩 곱하기
            temp *= nums[nums.count - i]
        }
        
        return result
    }
}
