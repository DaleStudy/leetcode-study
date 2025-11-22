import java.util.HashMap;
import java.util.Map;

public class Geegong {

    public boolean isAnagram(String s, String t) {
        char[] sArray = s.toCharArray()
        char[] tArray = t.toCharArray();

        // early return
        if (sArray.length != tArray.length) {
            return false;
        }

        Map<Character, Integer> numOfLetters = new HashMap<>();
        for (Character sLetter : sArray) {
            numOfLetters.merge(sLetter, 1, Integer::sum);
        }

        for (Character tLetter : tArray) {
            Integer num = numOfLetters.get(tLetter);
            if (num <= 0) return false;
            numOfLetters.computeIfPresent(tLetter, (key, oldValue) -> oldValue - 1);
        }

        return true;
    }

}
