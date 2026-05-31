
var WordDictionary = function() {
    const dictionary = new Set('');

    this.dictionary = dictionary
};

/** 
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function(word) {
    this.dictionary.add(word);
};

/** 
 * @param {string} word
 * @return {boolean}
 */
WordDictionary.prototype.search = function(word) {
    if(word.includes('.')){
        const dictionaryList = [...this.dictionary];

        return dictionaryList.some((dic) =>  {
            if(dic.length !== word.length) return false;
            
            return [...dic].every((char, index) => word[index] === '.' ? true : word[index] === char)
        })
    };

    return this.dictionary.has(word)
};

/** 
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
