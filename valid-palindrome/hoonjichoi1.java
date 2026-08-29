class Solution {
    public boolean isPalindrome(String s) {

        // removing all non-alphanumeric characters and convert them to lower case
        String conveted = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();

        // early return of the empty string case
        if (conveted.length() == 0) {
            return true;
        }

        // check the symmetry
        int left = 0, right = conveted.length() - 1;
        while (left <= right) {
            if (conveted.charAt(left) != conveted.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
