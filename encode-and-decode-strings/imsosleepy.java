// 아이디어로 푸는 문제라 선호하지 않는 문제...
// 그냥 사용하지 않는 것을 구분자로 두고 스플릿하는게 가장 편하다. 아예 나오지 않을 문자를 기준으로 두면 길이를 알 필요가 없기 때문
public class Solution {
    // 인코딩 메서드
    public String encode(List<String> strs) {
        StringBuilder encodedString = new StringBuilder();
        
        for (String str : strs) {
            encodedString.append(str.length()).append("#").append(str);
        }
        
        return encodedString.toString();
    }
    
    // 디코딩 메서드
    public List<String> decode(String s) {
        List<String> decodedList = new ArrayList<>();
        int i = 0;
        
        while (i < s.length()) {

            int j = i;
            while (s.charAt(j) != '#') {
                j++;
            }
            
            int length = Integer.parseInt(s.substring(i, j));
            decodedList.add(s.substring(j + 1, j + 1 + length));

            i = j + 1 + length;
        }
        
        return decodedList;
    }
}
// 🚀를 기준으로 문자열을 분리
// @!#$@#$ 이런걸 스플릿 문자로 두는 방법도 있다.아이온
public class Solution {

    public String encode(List<String> strs) {
        StringBuilder encodedString = new StringBuilder();
        
        for (String str : strs) {
            encodedString.append(str).append("🚀");
        }
        
        return encodedString.toString();
    }

    public List<String> decode(String s) {
        String[] parts = s.split("🚀");     
        List<String> decodedList = new ArrayList<>();
        for (String part : parts) {
            if (!part.isEmpty()) {
                decodedList.add(part);
            }
        }
        
        return decodedList;
    }
}
