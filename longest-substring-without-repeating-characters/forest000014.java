/*
Time Complexity: O(n)
Space Complexity: O(c)
(c는 사용되는 모든 character의 가짓수)

solution (two pointers)

begin, end 포인터를 각각 1에 두고 시작한다.
end 포인터를 1씩 증가하면서 탐색하다가, 현재 window 내에 이미 존재하는 문자가 또 추가된다면, 그 문자가 window에서 사라질 때까지 begin을 증가시킨다.

(1) end++을 하는 도중의 모든 end에 대해서는, 또 다른 begin을 찾을 필요성은 없는가?
    - 현재 begin보다 더 왼쪽의 begin : 현재의 begin은, window 내에 중복 문자가 없게끔 하는 leftmost 인덱스이다. 따라서, 더 작은 begin은 중복이 있을 것이므로, 탐색할 필요가 없다.
    - 현재 begin보다 더 오른쪽의 begin : 더 짧은 길이는 탐색할 필요가 없다.

(2) begin++을 하는 도중의 모든 begin에 대해서는, 또 다른 end를 찾을 필요성은 없는가?
    - 현재 end보다 더 왼쪽의 end : 더 짧은 길이는 탐색할 필요가 없다.
    - 현재 end보다 더 오른쪽의 end : 중복된 문자가 있는 구간은 LSWRC가 될 수 없으므로, 탐색할 필요가 없다.
*/
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<>();
        int begin = 0, end = 0;

        int ans = 0;
        while (end < s.length()) {
            if (set.contains(s.charAt(end))) {
                while (begin < end && s.charAt(begin) != s.charAt(end)) {
                    set.remove(s.charAt(begin++));
                }
                set.remove(s.charAt(begin++));
            } else {
                set.add(s.charAt(end++));
                ans = Math.max(ans, end - begin);
            }
        }

        return ans;
    }
}
