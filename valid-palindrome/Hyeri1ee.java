import java.util.*;

//palindrome
class Solution {
    public boolean isPalindrome(String s) {

        ArrayList<Character> list = new ArrayList<>();
        //list에 넣기
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (!Character.isLetterOrDigit(c))
                continue;

            list.add(c);
        }

        System.out.println(list.size());

        boolean ok = true;
        int start = 0;
        int end = list.size() - 1;

        if (list.size() == 0 || list.size() == 1)
            return true;

        //디버깅
        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i));
        }

        while (start < end) {
            if (Character.toLowerCase(list.get(start)) != 
    Character.toLowerCase(list.get(end))) {
    return false;
}

            start++;end--;
        } //end of while

        return ok;
    }

    private static boolean isInRange(char c) {
        return (c >= 'A') && (c <= 'Z') || (c >= 'a') && (c <= 'z');
    }

}
