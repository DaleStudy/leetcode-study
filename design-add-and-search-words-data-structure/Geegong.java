import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Geegong {

    /**
     * case 1. Letter 라는 클래스 안에 각 char 를 가지고 있고 하나씩 순회하면서 search 를 하니 응답속도가 너무 느림..
     */
    class WordDictionary {
        public Map<Integer, List<Letter>> wordsLengthMap;

        public WordDictionary() {
            this.wordsLengthMap = new HashMap<>();
        }

        public void addWord(String word) {
            char[] wordChars = word.toCharArray();

            Letter prev = new Letter(null);
            Letter root = new Letter(prev);
            for (char wordChar : wordChars) {
                Letter curr = new Letter(wordChar, false);

                prev.nextLetter = curr;

                prev = curr;
            }

            prev.isEnd = true;

            wordsLengthMap.computeIfAbsent(wordChars.length, ArrayList::new).add(root.nextLetter);
        }

        public boolean search(String word) {
            char[] wordChars = word.toCharArray();
            int length = wordChars.length;

            if (!wordsLengthMap.containsKey(length)) {
                return false;
            }

            List<Letter> letters = wordsLengthMap.get(length);
            for (Letter letter : letters) {
                if (letter.isMatched(wordChars)) {
                    return true;
                }
            }

            return false;
        }
    }

    public static class Letter {
        public char currentLetterOfAsciiCode; // '?'-'a'
        public Letter nextLetter;
        public boolean isEnd; // 마지막 글자 인지 여부

        public Letter(Letter next) {
            this.nextLetter = next;
        }

        public Letter(char wordChar, boolean isEnd) {
            this.currentLetterOfAsciiCode = wordChar;
            this.isEnd = isEnd;
        }

        public boolean isMatched(char[] wordChars) {

            Letter current = this.nextLetter;
            // 본인 시점으로 부터 wordChars 마지막까지 체크
            for (char wordChar : wordChars) {

                // . 이면 그냥 패스
                boolean isMatched = wordChar == '.' || wordChar == current.currentLetterOfAsciiCode;
                if (isMatched) {
                    if (current.isEnd) {
                        return true;
                    } else {
                        current = current.nextLetter;
                    }

                } else {
                    return false;
                }
            }

            return false;

        }
    }
}

