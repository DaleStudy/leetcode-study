/*
O(n)
O(n)
*/

class TriedNode {
    children: Map<string, TriedNode>
    isEndOfWord: boolean

    constructor(){
        this.children = new Map()
        this.isEndOfWord = false
    }
}

class WordDictionary {
    root: TriedNode
    constructor() {
        this.root = new TriedNode()
    }

    addWord(word: string): void {
        let node = this.root
        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TriedNode())
            }
            node = node.children.get(char)
        }
        node.isEndOfWord = true
    }

    search(word: string): boolean {
        const searchInNode = (word: string, index: number, node: TriedNode): boolean => {
            if (index === word.length) return node.isEndOfWord

            const char = word[index]

            if (char === '.') {
                for (const [, childNode] of node.children) {
                    if (searchInNode(word, index + 1, childNode)) {
                        return true
                    }
                }
                return false
            } else {
                if (!node.children.has(char)) {
                    return false
                }
                return searchInNode(word, index + 1, node.children.get(char))
            }
        }
        return searchInNode(word, 0, this.root)
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
 