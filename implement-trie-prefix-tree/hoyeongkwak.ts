/*
    time complexity : O(n)
    space complexity : O(n)
*/
class TriedNode {
    children: Map<string, TriedNode>
    isEnd: boolean
    constructor(){
        this.children = new Map()
        this.isEnd = false
    }
}

class Trie {
    root: TriedNode

    constructor() {
        this.root = new TriedNode()
    }

    insert(word: string): void {
        let node = this.root
        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TriedNode())
            }
            node = node.children.get(char)
        }
        node.isEnd = true
    }

    search(word: string): boolean {
        let node = this.root
        for (const char of word) {
            if (!node.children.has(char)) {
                return false
            }
            node = node.children.get(char)
        }
        return node.isEnd
    }

    startsWith(prefix: string): boolean {
        let node = this.root
        for (const char of prefix) {
            if (!node.children.has(char)) {

                return false
            }
            node = node.children.get(char)
        }
        return true
    }
}