class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        var count = [Character:Int]()
        for char in s {
            count[char, default: 0] += 1
        }
        
        for char in t {
            count[char, default: 0] -= 1

            if count[char]! < 0 {
                return false
            }
        }
        
        return count.values.allSatisfy {$0 == 0}

        //시간 복잡도 O(n)
        //공간 복잡도 O(n)
    }
}

