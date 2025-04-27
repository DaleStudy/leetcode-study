///정수 문자열 암호문을 습득했고, 1 -> A, 2 -> B ... 25 -> Y, 26 -> Z 이런식으로 해독됨
///정수 문자열을 어떻게 끊느냐에 따라 해독이 다르게 된다는 점을 고려해서
///해독 될수 있는 모든 경우의 수를 반환하라, 해독이 안된다면 0을 반환하라
///
///EX) s = "12"
///output : 2  -> (1 2) "AB" or (12) "L"


class Solution {
    func numDecodings(_ s: String) -> Int {
        let arr = Array(s)
        var memo: [Int:Int] = [arr.count:1]
        
        func dfs(_ start: Int) -> Int {
            if let result = memo[start] {
                return result
            }
            
            
            if arr[start] == "0" {
                memo[start] = 0
            } else if start + 1 < arr.count, Int(String(arr[start...start+1]))! <= 26 {
                memo[start] = dfs(start+1) + dfs(start+2)
            } else {
                memo[start] = dfs(start + 1)
            }
            
            return memo[start]!
        }
        
        return dfs(0)
    }
}
