// two pointer
// time: O(N)
// space: O(N)
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int answer = 0;
        Set<Character> charSet = new HashSet<>();
        int head = 0;
        int tail = 0;

        for (int i = 0; i < s.length(); i++){
            Character ch = Character.valueOf(s.charAt(i));
            while (charSet.contains(ch)) {
                charSet.remove(Character.valueOf(s.charAt(head++)));
            }
            charSet.add(ch);
            tail += 1;
            answer = Math.max(answer, charSet.size());
        }
        return answer;
    }
}

