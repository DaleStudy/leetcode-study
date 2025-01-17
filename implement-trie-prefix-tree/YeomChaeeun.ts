/**
 * 트라이 알고리즘
 * 달레 해설을 보고 참고하여 TypeScript로 작성
 */
class Node {
    children: { [key: string]: Node };
    ending: boolean;

    constructor(ending: boolean = false) {
        this.children = {};
        this.ending = ending;
    }
}

class Trie {
    private root: Node;

    constructor() {
        this.root = new Node(true);
    }

    insert(word: string): void {
        let node = this.root;
        for (const ch of word) {
            if (!(ch in node.children)) {
                node.children[ch] = new Node();
            }
            node = node.children[ch];
        }
        node.ending = true;
    }

    search(word: string): boolean {
        let node = this.root;
        for (const ch of word) {
            if (!(ch in node.children)) {
                return false;
            }
            node = node.children[ch];
        }
        return node.ending;
    }

    startsWith(prefix: string): boolean {
        let node = this.root;
        for (const ch of prefix) {
            if (!(ch in node.children)) {
                return false;
            }
            node = node.children[ch];
        }
        return true;
    }
}
