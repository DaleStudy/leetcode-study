// 해설 참조..
class Solution {
    func combinationSum(_ candidates: [Int], _ target: Int) -> [[Int]] {
        // 우선 답변용, 조합 찾기용 변수 생성
        var answer = [[Int]]()
        var nums = [Int]()
        // 백트래킹 기법으로 로직 작성,
        // 현재 원소 위치와 합했을때의 값을 인자로 받음
        func backtracking(start: Int, total: Int) {
            // 전처리
            if total > target { return } // total이 target 보다 크면 조합X
            else if total == target { return answer.append(nums) } // 같으면 답변용 변수에 추가
            
            // 시작 부분부터 값을 하나씩 더해서 재귀로 돌려봄
            for index in start..<candidates.count {
                let temp = candidates[index]
                nums.append(temp) //먼저 선택된 원소를 조합 배열에 추가
                backtracking(start: index, total: total + temp) // 현재 선택된 원소의 인덱스와 총 합을 인자로 함수 호출
                nums.removeLast() // 조합찾기가 끝나면 종료
            }
        }
        // 초기부터 시작함
        backtracking(start: 0, total: 0)
        return answer
    }
}
