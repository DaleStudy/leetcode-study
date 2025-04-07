class Solution {
    func climbStairs(_ n: Int) -> Int {
        var result = 0
        
        for i in 0...(n/2) {
            if i == 0 {
                result += 1
                continue
            }

            let x = n - (2 * i)

            result += ncm(x+i, i)
        }

        return result
    }
    
    func ncm(_ n: Int, _ m: Int) -> Int {
        if m == 1 { return n }
        if m == n { return 1 }
        return (1...m).reduce(1) { $0 * ($1 + n-m)/$1 }
    }
}
