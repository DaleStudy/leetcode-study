class Solution {
    func hammingWeightDivide(_ n: Int) -> Int {
        var count = 0
        var dividedNumber = n
        while dividedNumber > 0 {
            let remainder = dividedNumber % 2
            if remainder == 1 {
                count += 1
            }
            dividedNumber /= 2
        }
        
        return count
        
        //시간 복잡도(O(log n))
        //공간 복잡도(O(1))
    }
    
    func hammingWeightShift(_ n: Int) -> Int {
        var count = 0
        
        var shiftedNumber = n
        while shiftedNumber > 0 {
            if (shiftedNumber & 1) == 1 {
                count += 1
            }
            shiftedNumber >>= 1
        }
        
        return count
        
        //시간 복잡도(O(log n))
        //공간 복잡도(O(1))
    }
    
    func hammingWeightMask(_ n: Int) -> Int {
        var count = 0
        
        var mask = 1 << 31
        
        while mask > 0 {
            if mask & n == mask {
                count += 1
            }
            mask >>= 1
        }
        
        return count
        
        //시간 복잡도(O(1))
        //공간 복잡도(O(1))
    }
}

