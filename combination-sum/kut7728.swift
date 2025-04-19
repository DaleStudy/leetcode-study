///고유한 정수배열의 candidate와 목표 정수 target가 주어졌을 때,
///요소들을 더해서 target을 만들수 있는 candidate의 유니크한 조합 목록을 반환합니다.
///- 어떤 순서로든 조합을 반환할 수 있습니다.
///- 후보에서 같은 숫자를 무제한으로 선택할 수 있습니다.
///- 선택한 숫자 중 하나 이상의 빈도가 다른 경우 두 조합은 고유한 조합입니다.
///- 테스트 케이스는 주어진 입력에 대해 합산되는 고유 조합의 수가 150개 미만이 되도록 생성됩니다.
///Ex) candidate [2, 3, 6, 7] target = 7 -> [[2, 2, 3], [7]]


class Solution {
    func combinationSum(_ candidates: [Int], _ target: Int) -> [[Int]] {
        result: [[Int]] = []
        nums: [Int] = []
        
        func dfs(_ start: Int, _ total: Int) {
            //타겟에 적중하면 result로 복사
            if total == target {
                result.append(nums)
                return
            }
            
            //합이 타겟보다 크다면 그냥 종료
            if total > target {
                return
            }
            
            //start부터 시작하는것은 이전 요소들에 대한 조합은 이미 테스트했기 때문
            for i in start..<candidates.count {
                nums.append(candidates[i])
                dfs(i, total + candidates[i])
                nums.removeLast()
            }
        }
        
        dfs(0, 0)
        return result
    }
}
