import java.util.*;
class Solution {
    public boolean isPalindrome(String s) {
        String words = s.toLowerCase().replaceAll("[^0-9A-Za-z]","");
        //System.out.println(words);
        Deque<Character> stack = new ArrayDeque<>();
        for(int i=0;i<words.length();i++){
            stack.push(words.charAt(i));
        }
        while(!stack.isEmpty()){
            for(int i=0;i<words.length();i++){
                if(words.charAt(i)==stack.pop()) continue;
                else return false;
            }
        }
        return true;
    }
}