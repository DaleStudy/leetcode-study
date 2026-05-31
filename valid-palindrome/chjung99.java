class Solution {
    public boolean isPalindrome(String s) {
        String filterd = s.toLowerCase();
        StringBuilder filterdBuilder = new StringBuilder();

        for (int i = 0; i < filterd.length(); i++){
            Character c = filterd.charAt(i);
            if (Character.isLetterOrDigit(c)){
                filterdBuilder.append(c.toString());
            }
        }

        String ori = filterdBuilder.toString();
        String rev = new StringBuilder(ori).reverse().toString();

        return rev.equals(ori);
    }
}

