class Solution {
    public int lengthOfLongestSubstring(String s) {
        // HashSet 풀이
        // 시간복잡도 : O(n), 공간복잡도 O(1)
        // 풀이
        // HashSet에 동일한 문자가 있는지 체크하고 동일한 문자가 있으면 왼쪽 기준점을 하나씩 이동 (동일 문자가 없을 때까지 반복)
        // 동일한 문자가 없을 때 현재 기준(right) - 왼쪽 기준(left) + 1 의 최대 길이를 maxLength 저장 후 반환

        int left = 0;
        int maxLength = 0;
        HashSet<Character> charSet = new HashSet<>();

        for (int right = 0; right < s.length(); right++) {
            while (charSet.contains(s.charAt(right))) {
                charSet.remove(s.charAt(left));
                left++;
            }

            charSet.add(s.charAt(right));
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}
