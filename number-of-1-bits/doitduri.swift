class Solution {
    func hammingWeight(_ n: Int) -> Int {
        let bitString = String(n, radix: 2)
        return bitString.filter { $0 == "1" }.count
    }
}
