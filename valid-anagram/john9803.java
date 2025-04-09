import java.util.Arrays;

public class john9803{
        public boolean isAnagram(String s, String t) {
            // Max 시간복잡도 -> 5^2 * 10^8 = 1억 미만, 브루트포스 풀이
            char[] charS = s.toCharArray();
            char[] charT = t.toCharArray();

            Arrays.sort(charS);
            Arrays.sort(charT);

            if(String.valueOf(charS).equals(String.valueOf(charT))){return true;}
            else{return false;}
}
