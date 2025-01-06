import java.util.ArrayList;
import java.util.List;
// n: 문자열 리스트 길이, m: 각 문자열의 길이. 

// 시간 복잡도
// Encoding: O(n * m) 
// Decoding: O(n * m)
// 공간 복잡도
// Encoding: O(n * m),
// Decoding: O(n * m) 
class Solution {

    // 받아온 string 들을 한 문자열로 합침
    // (문자열길이)#(문자열) 형식
    public String encode(List<String> strs) {
        StringBuilder encodedStr = new StringBuilder();
        for (String str : strs) {
            encodedStr.append(str.length()).append('#').append(str);
        }
        return encodedStr.toString();
    }

    // Decodes a single string to a list of strings
    public List<String> decode(String s) {
        List<String> result = new ArrayList<>();
        int i = 0;
        
        while (i < s.length()) {
            
            int j = i;
            while (s.charAt(j) != '#') { // # 문자 찾기
                j++;
            }
            
            // 문자열 길이 추출
            int length = Integer.parseInt(s.substring(i, j));
            
            // 위에서 구한 문자열 길이만큼 문자열 추출
            result.add(s.substring(j + 1, j + 1 + length));
            
            // i 위치 변경
            i = j + 1 + length;
        }
        
        return result;
    }

}
