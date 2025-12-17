class Solution {
    public boolean isPalindrome(String s) {
        String cleaned = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        if (cleaned.length() == 1 || cleaned.length() == 0) {
            return true;
        } else if(cleaned.length() ==2) {
            return cleaned.charAt(0) == cleaned.charAt(1);
        }
        int length = cleaned.length();
        int mid = length / 2;

        String leftPart;
        String rightPart;

        if (length % 2 == 1) {
            leftPart = cleaned.substring(0, mid);
            rightPart = cleaned.substring(mid + 1, length);
        } else {
            leftPart = cleaned.substring(0, mid);
            rightPart = cleaned.substring(mid, length);
        }

        String reversedRightPart = new StringBuilder(rightPart).reverse().toString();

        return leftPart.equals(reversedRightPart);

    }
}
