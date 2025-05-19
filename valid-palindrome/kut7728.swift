///주어진 문자열에서 문자, 숫자가 아닌 경우를 지우고, 모두 소문자로 바꿨을때
///앞, 뒤에서 읽었을 때 동일한 경우를 palindrome이라고 부름
///문자열 s가 주어질때 palindrome이면 true, 아니면 False 리턴하시오

class Solution {
    func isPalindrome(_ s: String) -> Bool {
        let alpList = Set("abcdefghijklmnopqrstuvwxyz0123456789")
        
        if s == " " { return true }  // 공백인 경우 바로 true
        
        var pureString = s.lowercased().filter { alpList.contains($0) }
        
        
        let reverseString = String(pureString.reversed())
        
        if pureString == reverseString { return true } else { return false }
        
    }
    
    //.isLetter, .isNumber이라는 끝내주는 메서드가 있었다...
    func isPalindrome2(_ s: String) -> Bool {
        let s = s.lowercased().filter { $0.isLetter || $0.isNumber }
        return s == String(s.reversed())
    }
    
}
