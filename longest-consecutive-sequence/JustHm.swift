class Solution {
    func longestConsecutive(_ nums: [Int]) -> Int {
        guard !nums.isEmpty else { return 0 }
        /*
         중복 제거 후 소팅 후 배열로 만드는것은 N + NlogN + N 으로 예상된다..
         그래서 정렬만 하고 로직에서 중복 숫자는 그냥 무시하게 만드는 방식으로 속도를 개선
         문제에서 O(N)으로 작성하자 라는 제약아닌 제약이 있었는데, O(N)은 도저히 떠오르지 않는다.
        */
        let nums = nums.sorted()//Array(Set(nums).sorted())
        var answer = 1
        var count = 1
        for index in 0..<nums.count-1 {
            if nums[index] - nums[index + 1] == -1 {
                count += 1
            }
            else if nums[index] == nums[index + 1] { continue }
            else {
                answer = max(answer, count)
                count = 1
            }
        }
        return max(answer, count)
    }
}
// MARK: time: O(n) 풀이
/*
 몰랐던점 Set의 contains는 O(n) 아님, O(1)임 (내부적으로 Hash table로 구현되어있음)
 하지만 풀이 제출해보니까 속도가 sort 한거보다 덜나옴.. 왜?
 Set은 contains를 확인할때, 들어온 값을 hash로 변경후 검색, 버킷찾기, 충돌 검사 등을 거치기 때문에... O(1)은 맞는데 시간이 조금 걸린다.
 그렇기에 set방식으로 O(n)에 짠거보다 sorted 내장함수를 이용한 O(nlogn)의 실제 실행시간이 더 빠른것.
*/
class AnotherSolution {
    func longestConsecutive(_ nums: [Int]) -> Int {
        var numSet = Set(nums)
        var answer = 0
        
        for num in numSet {
            // num-1이 없으면 시작지점이니까 여기부터 +1 하면서 길이 확인
            // num-1이 있으면 그냥 무시
            if !numSet.contains(num-1) { //Set의 contains는 O(1)임!! (내부적으로 Hash table로 구현되어있기 때문)
                var count = 1
                var temp = num + 1
                while numSet.contains(temp) {
                    count += 1
                    temp += 1
                }
                answer = max(answer, count)
            }
        }
        return answer
    }
}
