/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const smallBracket = ['(',')'];
    const middleBracket = ['{','}'];
    const largeBracket = ['[',']'];


    const leftStack = [];

    for(const char of s) {
        if(char === smallBracket[0]){
            leftStack.push(smallBracket[1])
        }else if (char === middleBracket[0]){
            leftStack.push(middleBracket[1])
        }else if(char === largeBracket[0]){
            leftStack.push(largeBracket[1])
        }else{
            const last = leftStack.pop();
            if(char === smallBracket[1] && last !== char) return false;
            if(char === middleBracket[1] && last !== char) return false;
            if(char === largeBracket[1] && last !== char) return false;
        }
    }

        
    return leftStack.length === 0
};
