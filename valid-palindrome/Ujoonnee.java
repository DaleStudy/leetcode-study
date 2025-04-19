// time complexity : O(n)
// space complexity : O(1)

class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        int i = 0;
        int j = s.length() - 1;
        while(i < j) {
            char c1 = s.charAt(i);
            if (!isAlphanumeric(c1)) {
                i++;
                continue;
            }

            char c2 = s.charAt(j);
            if (!isAlphanumeric(c2)) {
                j--;
                continue;
            }

            if (c1 != c2) {
                return false;
            }
            i++;
            j--;
        }

        return true;
    }

    private boolean isAlphanumeric(char c) {
        return (c >= '0' && c<='9') || (c >= 'A' && c <= 'Z') || (c >= 'a' && c<= 'z');
    }
}

/*
class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        String[] split = s.replaceAll("[^A-Za-z0-9]", "").split("");
        for (int i=0; i<split.length/2; i++) {
            if (!split[i].equals(split[split.length-1-i])) {
                return false;
            }
        }

        return true;
    }
}
*/
