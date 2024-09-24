/**
 *  시간 복잡도: O(n)
 *  공간 복잡도: O(n)
 */
class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> map = new HashMap<>(){{
            put(')', '(');
            put('}', '{');
            put(']', '[');
        }};

        Deque<Character> stack = new ArrayDeque<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (!map.containsKey(c)) {
                stack.push(c);
                continue;
            }

            if (stack.isEmpty() || stack.removeFirst() != map.get(c)) {
                return false;
            }
        }

        return stack.size() == 0;
    }
}
