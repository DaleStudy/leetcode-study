/**
 * 특이사항
 * 시간복잡도가 (1)번 풀이는 O(N log N) / (2), (3)번 풀이는 O(N)인데
 * 리트코드에서 Runtime - (1)번 : 3ms, (3)번 : 6ms, (2)번 : 13ms
 *
 * 시간복잡도로만 따지면 당연히 (2), (3)번 풀이가 빨라야하는데도 불구하고 오히려 (1)번 풀이가 더 빠른 결과가 나온다.
 * chatgpt 확인했을 때 가장 큰 차이점은 문자열을 배열로 변경해서 정렬을 하는데 이 때 정렬 알고리즘의 성능에 따라 차이가 난다는 내용이 있었다.
 * N이 높아질수록 (2), (3)의 성능이 좋아질 것으로 예상되나 해당 문제의 결과에서는 (1)의 성능이 좋게 나올 수 있다는 것을 알게 되었다.
 */

class Solution {
    public boolean isAnagram(String s, String t) {
        // (1) 문자 배열 - 정렬 & 비교
        // 시간복잡도 : O(N log N), 공간복잡도 : O(N)

        // char[] sArr = s.toCharArray();
        // char[] tArr = t.toCharArray();
        // Arrays.sort(sArr);
        // Arrays.sort(tArr);

        // return new String(sArr).equals(new String(tArr)); // 문자열을 비교한다 생각했을 때 방법
        // return Arrays.equals(sArr, tArr); // char 배열 자체를 비교

        // (2) HashMap 이용해 알파벳 개수 체크
        // 시간복잡도 : O(N), 공간복잡도 : O(N)

        // Map<Character, Integer> count = new HashMap<>();

        // for (char x : s.toCharArray()) {
        //     count.put(x, count.getOrDefault(x, 0) + 1);
        // }

        // for (char x : t.toCharArray()) {
        //     count.put(x, count.getOrDefault(x, 0) - 1);
        // }

        // for (int val : count.values()) {
        //     if (val != 0) {
        //         return false;
        //     }
        // }

        // return true;

        // (3) 배열로 알파벳 개수 체크
        // 시간복잡도 : O(N), 공간복잡도 : O(N)

        // if (s.length() != t.length()) {
        //     return false;
        // }

        // int[] freq = new int[26];
        // for (int i = 0; i < s.length(); i++) {
        //     freq[s.charAt(i) - 'a']++;
        //     freq[t.charAt(i) - 'a']--;
        // }

        // for (int i = 0; i < freq.length; i++) {
        //     if (freq[i] != 0) {
        //         return false;
        //     }
        // }

        // return true;
    }
}
