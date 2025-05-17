class Solution {
    //계단 갯수 n 입력받음
    func climbStairs(_ n: Int) -> Int {
        var result = 0
        
        ///1계단씩 올라가는 경우 = 1스탭
        ///2계단씩 올라가는 경우 = 2스탭
        ///2스탭인 경우를 1씩 증가시켜줌
        for i in 0...(n/2) {
            ///2스탭이 없는 경우 -> 전부 1스탭임
            if i == 0 {
                result += 1
                continue
            }
            
            ///n에서 2스탭 횟수를 빼서 1스탭 횟수 구하기
            let x = n - (2 * i)
            
            ///조합계산식 (2스탭,1스탭 전체 횟수 C 2스탭 횟수)
            result += ncm(x+i, i)
        }

        return result
    }
    
    ///ncm함수로 조합 계산식을 구현
    func ncm(_ n: Int, _ m: Int) -> Int {
        if m == 1 { return n } ///nC1 이라면 전체횟수 n 반환
        if m == n { return 1 } ///nCn 이라면 1반환
    
        ///조합 계산식을 코드로 계산할 수 있도록 최적화하면 다음과 같아짐
        return (1...m).reduce(1) { $0 * ($1 + n-m)/$1 }
    }
}
