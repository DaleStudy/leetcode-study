class Solution {
    public boolean isValid(String s) {
        // 스택... 머리속에 떠오르는 생각은 있는데 정리가 안됌..
        // 해설 읽음

        Map<Character, Character> parens = new HashMap<>();
        parens.put('(', ')');
        parens.put('{', '}');
        parens.put('[', ']');

        Stack<Character> stack = new Stack<>();

        for(char c : s.toCharArray()) {
            if (parens.containsKey(c)) {
                stack.push(c);
            } else {
                if (stack.isEmpty() || c != parens.get(stack.pop())) {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
}