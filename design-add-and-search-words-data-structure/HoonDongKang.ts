/**
 * [Problem]: [211] Design Add and Search Words Data Structure
 * (https://leetcode.com/problems/design-add-and-search-words-data-structure/description/)
 */
class WordNode {
    children = new Map<string, WordNode>();
    isEnd: boolean = false;
    constructor() {}
}

class WordDictionary {
    root = new WordNode();
    constructor() {}

    //시간복잡도: O(n)
    //공간복잡도: O(n)
    addWord(word: string): void {
        let currentNode = this.root;

        for (const char of word) {
            if (!currentNode.children.has(char)) {
                currentNode.children.set(char, new WordNode());
            }
            currentNode = currentNode.children.get(char)!;
        }

        currentNode.isEnd = true;
    }

    //시간복잡도: O(n)
    //공간복잡도: O(n)
    search(word: string): boolean {
        return this.dfsSearch(word, 0, this.root);
    }

    private dfsSearch(word: string, index: number, node: WordNode): boolean {
        if (index === word.length) {
            return node.isEnd;
        }

        const char = word[index];
        const isDot = char === ".";

        if (isDot) {
            for (const child of node.children.values()) {
                if (this.dfsSearch(word, index + 1, child)) {
                    return true;
                }
            }

            return false;
        } else {
            const nextNode = node.children.get(char);
            if (!nextNode) return false;
            return this.dfsSearch(word, index + 1, nextNode);
        }
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
