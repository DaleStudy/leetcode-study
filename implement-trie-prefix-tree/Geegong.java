public class Geegong {

    /**
     * 각 글자마다 Node 클래스 인스턴스를 가지고 그 안에 Node[] 배열을 갖고 있는 형태
     * 찾는것은 매우 빠르나 (인덱스를 글자 - 'a' )
     * 불필요한 공간을 26 byte의 배열을 가지고 있음
     *
     *  N은 word 의 길이라고 치면
     * Time complexity
     * search, startsWith : O(N)
     *
     * Space complexity :
     * O(26 * N)
     * = O(N)
     */
    class Trie {
        private Node node;

        public static class Node {
            private Node[] next = new Node[26]; // 글자 a ~ z, A ~ Z
            private boolean end; // 마지막 노드인지의 여부
        }

        public Trie() {
            this.node = new Node();
        }

        public void insert(String word) {

            Node current = this.node;
            for (char wordChar : word.toCharArray()) {
                int index = wordChar - 'a'; // word 가 'a' ~ 'Z' 까지가 보장된다면
                if (current.next[index] == null) {
                    current.next[index] = new Node();
                }
                current = current.next[index];
            }
            current.end = true;
        }

        public boolean search(String word) {
            Node current = this.node;
            for (char wordChar : word.toCharArray()) {
                int index = wordChar - 'a';
                if (current.next[index] == null) {
                    return false;
                }
                current = current.next[index];
            }

            return current != null && current.end;
        }

        public boolean startsWith(String prefix) {
            Node current = this.node;
            for (char wordChar : prefix.toCharArray()) {
                int index = wordChar - 'a';
                if (current.next[index] == null) {
                    return false;
                }
                current = current.next[index];
            }

            return current != null;
        }
    }

}
