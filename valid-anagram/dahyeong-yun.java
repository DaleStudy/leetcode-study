/**
 * 0. 풀이 개요
 *   - 시간복잡도 : O(n log n)
 *   - 공간복잡도 : O(n)
 */
class Solution {
    /**
     * 1. 풀이 과정
     * 1.1 문제 이해
     *   - 애니어램이 가능한 문자열인지 판단하는 문제임. 두 문자열 s와 t가 주어지고, t가 s의 애니어그램이라면 true를 반환
     * 1.2 제약 사항
     *   - s, 와 t의 문자열의 길이가 5 * 10^4 이므로 문자열 길이 만큼 순회해야 한다면 O(n^2)은 불가능해 보임. O(n log n) 이하가 필요.
     *   - 문자는 반드시 영소문자로만 구성되어 있으나, 만약 Follow up 질문 처럼 유니코드를 포함해야 된다면 이를 포괄하는 자료형이 필요. 
     * 1.3 풀이 아이디어
     *   - 문자열을 정렬했을 때, 같은 문자열이라면 애니그램이 될 것.
     *   - 문자열의 character를 배열로 만들고 정렬하면, bulit-in 메서드에 의해 O(n log n)의 시간복잡도가 가짐,
     *   - 문자열의 길이만큼 character 배열이 필요하므로 2n 만큼의 공간이 더 필요하므로 O(n)의 공간복잡도를 가짐.
     */
    public boolean isAnagram(String s, String t) {
        char[] arrayS = s.toCharArray();
        char[] arrayT = t.toCharArray();

        Arrays.sort(arrayS);
        Arrays.sort(arrayT);

        return Arrays.equals(arrayS, arrayT);
    }
}
