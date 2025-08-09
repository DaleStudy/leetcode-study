class Solution {
    func isPalindrome(_ s: String) -> Bool {
        let string = s.replacingOccurrences(of: " ", with: "").lowercased().map { $0 }
        var leftIndex = string.startIndex
        var rightIndex = string.endIndex - 1
        let letterRange: ClosedRange<UInt8> = 97...122
        let numberRange: ClosedRange<UInt8> = 48...57
        while leftIndex <= rightIndex {
            guard let leftCharAscii = string[leftIndex].asciiValue else { break }
            guard let rightCharAscii = string[rightIndex].asciiValue else { break }
            if !letterRange.contains(leftCharAscii) && !numberRange.contains(leftCharAscii) {
                leftIndex += 1
                continue
            }
            if !letterRange.contains(rightCharAscii) && !numberRange.contains(rightCharAscii) {
                rightIndex -= 1
                continue
            }
            if leftCharAscii == rightCharAscii {
                leftIndex += 1
                rightIndex -= 1
            } else {
                return false
            }
        }
        return true
    }
}
 
