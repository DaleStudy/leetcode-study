class Solution {
    func climbStairs(_ n: Int) -> Int {
        var arr = [1, 2, 3, 5, 8]
        if arr.count > n { return arr[n-1] }

        for i in 4..<n {
            arr.append(arr[i] + arr[i-1])
        }
        return arr[n-1]
    }
}

/*
규칙 찾기
1
1

2
1 1
2

3
1 1 1
1 2
2 1

4
1 1 1 1
1 1 2
1 2 1
2 1 1
2 2

5
1 1 1 1 1
1 1 1 2
1 1 2 1
1 2 1 1
2 1 1 1
1 2 2
2 1 2
2 2 1

1 2 3 5 8

이전 두 결과값을 더한게 다음 결과값임
*/
