/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    var stack = [];

    var openDic = {
        '{': '}',
        '[': ']',
        '(': ')'
    };
    var closeDic = {
        '}': '{',
        ']': '[',
        ')': '('
    };

    for(let e of [...s]) {
        if(!stack.length) { 
            stack.push(e);
            continue;
        };

        const lastEle = stack.pop();

        if(closeDic[e]) {
            if(!openDic[lastEle]) return false;
            if(openDic[lastEle] !== e) return false;
            continue;
        } else {
            stack.push(lastEle);
            stack.push(e);
        }
    }

    return stack.length === 0;
};
