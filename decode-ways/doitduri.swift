class Solution {
    func numDecodings(_ s: String) -> Int {
         if s.first == "0" {
            return 0
        }

        if s.count == 1 {
            return 1
        }

        var tables = Array(repeating: 0, count: s.count+1)
        let chars = Array(s)
        tables[0] = 1
        tables[1] = 1
        
        for i in 2...s.count {
            if chars[i-1] != "0" {
                tables[i] += tables[i-1]
            }

            if let twoDigit = Int(String(chars[i-2...i-1])) {
                if 10 <= twoDigit && twoDigit <= 26 {
                    tables[i] += tables[i-2]
                }
            }
            
        }
        
        return tables[s.count]
    }
}
