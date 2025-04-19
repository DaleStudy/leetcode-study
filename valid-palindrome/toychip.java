class Solution {
    public boolean isPalindrome(String s) {
        char[] charArray = s.toCharArray();
        StringBuilder stringBuilder = new StringBuilder();

        for (char c : charArray) {
            if (Character.isLetterOrDigit(c)) {
                stringBuilder.append(c);
            }
        }

        String validChars = stringBuilder.toString();

        char[] validArray = validChars.toCharArray();
        char[] reversArray = new char[validArray.length];

        for (int i = 0; i < validArray.length; i++) {
            validArray[i] = Character.toLowerCase(validArray[i]);
            reversArray[i] = Character.toLowerCase(reversArray[i]);
        }

        for (int i = 0; i < validArray.length; i++) {
            reversArray[validArray.length - 1 - i] = validArray[i];
        }

        for (int i = 0; i < validArray.length; i++) {
            if (reversArray[i] != validArray[i]) {
                return false;
            }
        }
        return true;
    }
}
