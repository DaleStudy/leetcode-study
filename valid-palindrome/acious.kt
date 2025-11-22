class Solution {
    fun isPalindrome(s: String): Boolean {
         // 문장의 길이는 최대 20만
        // 문자열이 공백이면 return true
        // for-loop 한턴에 양쪽 끝에서부터 시작. 양쪽 index가 서로 교차되면 return true
        // 각각 char이 alphanumeric이 아니면 한칸 더이동.
        // 영문 대문자면 영문 소문자로 치환.
        // - 양쪽 끝의 char를 비교해서 같으면 양쪽 index를 이동시킴.
        // - 양쪽 끝의 char를 비교해서 같지않으면 return false
        // 시간복잡도 : O(n/2)
        // 공간복잡도 : O(n)
        if (s.isEmpty()) {
            return true
        }

        var left = 0
        var right = s.length - 1

        while (left <= right) { // 서로 교차하기 전까지만 비교하면 됨 (<= 대신 < 사용 가능)
            
            // 1. Char가 영문자나 숫자가 아닌지 확인
            if (!s[left].isLetterOrDigit()) { 
                left += 1
                continue
            }
            
            if (!s[right].isLetterOrDigit()) {
                right -= 1
                continue
            }

            // 2. 대소문자 통일 후 비교
            if (s[left].lowercaseChar() != s[right].lowercaseChar()) {
                return false
            } else {
                left += 1
                right -= 1
            }
        }

        return true
    }
}