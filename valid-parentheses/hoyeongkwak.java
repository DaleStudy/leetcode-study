class Solution {
    public boolean isValid(String s) {
        if (s == null || s.length() % 2 != 0) {
            return false;
        }
        Stack<Character> stack = new Stack<>();
        HashMap<Character, Character> strList = new HashMap<>();
        strList.put(')', '(');
        strList.put(']', '[');
        strList.put('}', '{');

        for (char c : s.toCharArray()) {
            if (strList.containsKey(c)) { 
                if (stack.isEmpty() || stack.pop() != strList.get(c)) {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }
        
        return stack.isEmpty();
    }
}
