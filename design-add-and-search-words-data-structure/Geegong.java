import java.util.*;

public class Geegong {

    /**
     * 이전 기수와는 다르게 배열을 활용해서 문제 풀이
     * time complexity : O(N^2)
     * space complexity : O(26 * N) => O(N)
     */
    public static class Node {
        private Node[] next = new Node[26];
        private boolean end;

        public void setNext(char ch) {
            int idx = ch - 'a';
            if (next[idx] == null) {
                next[idx] = new Node();
            }
        }

        public Node getSpecificNext(char ch) {
            int idx = ch - 'a';
            return this.next[idx];
        }

        public void setEnd(boolean isEnd) {
            this.end = isEnd;
        }
    }





    /**
     * case 1. Letter 라는 클래스 안에 각 char 를 가지고 있고 하나씩 순회하면서 search 를 하니 응답속도가 너무 느림..
     */
    public class WordDictionary {
        private Node entry;

        public WordDictionary(Node entry) {
            this.entry = entry;
        }

        public WordDictionary() { }

        public void addWord(String word) {
            char[] chArray = word.toCharArray();

            if (entry == null) {
                entry = new Node();
            }
            Node curr = entry;
            for (char ch : chArray) {
                curr.setNext(ch);
                curr = curr.getSpecificNext(ch);
            }
            curr.setEnd(true);
        }

        public boolean search(String word) {

            char[] chArray = word.toCharArray();

            Node curr = entry;
            for (int idx = 0; idx<chArray.length; idx++) {
                char ch = chArray[idx];

                if (ch == '.') {
                    // dfs, back tracking,
                    // . 이 있는 경우에는 그 다음 문자열부터 찾음
                    String temp = word.substring(idx + 1, chArray.length);

                    for (Node next : curr.next) {
                        WordDictionary newWordDict = new WordDictionary(next);
                        if (newWordDict.search(temp)) {
                            return true;
                        }
                    }
                    return false;
                }

                if (curr == null || curr.getSpecificNext(ch) == null) {
                    return false;
                }

                curr = curr.getSpecificNext(ch);
            }

            return curr.end;
        }









// 이전 기수에서 풀었던 방법, 전에는 List, Map을 이용하여 코드 풀이 하였음
//        public Map<Integer, List<Letter>> wordsLengthMap;
//
//        public WordDictionary() {
//            this.wordsLengthMap = new HashMap<>();
//        }
//
//        public void addWord(String word) {
//            char[] wordChars = word.toCharArray();
//
//            Letter prev = new Letter(null);
//            Letter root = new Letter(prev);
//            for (char wordChar : wordChars) {
//                Letter curr = new Letter(wordChar, false);
//
//                prev.nextLetter = curr;
//
//                prev = curr;
//            }
//
//            prev.isEnd = true;
//
//            wordsLengthMap.computeIfAbsent(wordChars.length, ArrayList::new).add(root.nextLetter);
//        }
//
//        public boolean search(String word) {
//            char[] wordChars = word.toCharArray();
//            int length = wordChars.length;
//
//            if (!wordsLengthMap.containsKey(length)) {
//                return false;
//            }
//
//            List<Letter> letters = wordsLengthMap.get(length);
//            for (Letter letter : letters) {
//                if (letter.isMatched(wordChars)) {
//                    return true;
//                }
//            }
//
//            return false;
//        }
//    }
//
//    public static class Letter {
//        public char currentLetterOfAsciiCode; // '?'-'a'
//        public Letter nextLetter;
//        public boolean isEnd; // 마지막 글자 인지 여부
//
//        public Letter(Letter next) {
//            this.nextLetter = next;
//        }
//
//        public Letter(char wordChar, boolean isEnd) {
//            this.currentLetterOfAsciiCode = wordChar;
//            this.isEnd = isEnd;
//        }
//
//        public boolean isMatched(char[] wordChars) {
//
//            Letter current = this.nextLetter;
//            // 본인 시점으로 부터 wordChars 마지막까지 체크
//            for (char wordChar : wordChars) {
//
//                // . 이면 그냥 패스
//                boolean isMatched = wordChar == '.' || wordChar == current.currentLetterOfAsciiCode;
//                if (isMatched) {
//                    if (current.isEnd) {
//                        return true;
//                    } else {
//                        current = current.nextLetter;
//                    }
//
//                } else {
//                    return false;
//                }
//            }
//
//            return false;
//
//        }
//    }
}

