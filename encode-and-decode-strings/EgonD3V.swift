import Foundation

class Solution {
    static let DELIMITER = ","
    
    /* ASCII 풀이 */
    static let ASCII_STR_LENGTH = 3
    
    func encodeWithASCII(strs: [String]) -> String {
        return strs.map { (str) in
            str.compactMap { (char) in
                guard let asciiValue = char.asciiValue else {
                    return nil
                }
        
                let asciiStr = String(asciiValue)
                
                return String(
                    repeating: "0",
                    count: Solution.ASCII_STR_LENGTH - asciiStr.count
                ) + asciiStr
            }.reduce("") { (acc, cur) in acc + cur }
        }
        .joined(separator: Solution.DELIMITER)
    }
    
    func decodeWithASCII(str: String) -> [String] {
        return str.components(separatedBy: Solution.DELIMITER)
            .map { (encodedStr) in
                return stride(from: 0, to: encodedStr.count, by: Solution.ASCII_STR_LENGTH)
                    .compactMap { i in
                        let startIndex = String.Index(utf16Offset: i, in: encodedStr)
                        let endIndex = String.Index(utf16Offset: i + Solution.ASCII_STR_LENGTH, in: encodedStr)
                        let asciiValue = UInt8(encodedStr[startIndex..<endIndex])
                        return asciiValue
                    }
            }.compactMap { String(bytes: $0, encoding: .ascii) }
    }
    
    /* BASE64 풀이 */
    func encodeWithBASE64(strs: [String]) -> String {
        return strs.compactMap { (str) in
            if let data = str.data(using: .utf8) {
                return data.base64EncodedString()
            } else {
                return nil
            }
        }.joined(separator: Solution.DELIMITER)
    }
    
    func decodeWithBASE64(str: String) -> [String] {
        return str.components(separatedBy: Solution.DELIMITER)
            .compactMap { (encodedStr) in
                if let data = Data(base64Encoded: encodedStr) {
                    return String(data: data, encoding: .utf8)
                } else {
                    return nil
                }
            }
    }
}

let solution = Solution()
let strs = ["lint", "code", "love", "you"]
let encoded = solution.encodeWithBASE64(strs: strs)
print(encoded)
let decoded = solution.decodeWithBASE64(str: encoded)
print(decoded)
