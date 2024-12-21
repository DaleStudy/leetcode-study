import java.util.Arrays;
/*
풀이:
- 문자열 s와 t를 배열로 저장하고, 오름차순으로 문자를 정렬한다.
- 정렬된 두 배열이 동일하면 애너그램으로 판단한다.
시간 복잡도:
- O(n log n) 
- 배열 정렬은 O(n log n)의 시간 복잡도를 갖는다.
공간 복잡도:
- O(n)
- 문자열을 배열로 변환하고 정렬할 때 O(n)의 공간 복잡도를 갖는다.
 */
class Solution {
    public boolean isAnagram(String s, String t) {
        // 두 문자열의 길이가 다르면 false
        if (s.length() != t.length()) {
            return false;
        }
        //문자열의 문자를 배열로 저장한다
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();

        // 각 배열의 문자를 오름차순으로 정렬한다
        Arrays.sort(sArray);
        Arrays.sort(tArray);

        // 정렬한 두 배열을 비교한다. 
        return Arrays.equals(sArray, tArray);      
    }
}
 
