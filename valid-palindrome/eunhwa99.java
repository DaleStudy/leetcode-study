class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder str = new StringBuilder();
    
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isLetterOrDigit(c)) {
                str.append(Character.toLowerCase(c));  
            }
        }
        
        int left = 0, right = str.length() - 1;
        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;  
            }
            left++;
            right--;
        }
        
        return true;  
    }
}
