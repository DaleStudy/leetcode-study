const isValid = (s) => {
    const stack = [];
    const map = {
        "(": ")",
        "[": "]",
        "{": "}"
    };
    
    for (const char of s) {
        if (map[char]) {
            console.log(char);
            stack.push(char);
        } else {
            if (stack.length === 0 || map[stack.pop()] !== char) {
                return false;
            }
        }
    }
    return stack.length === 0;
}
