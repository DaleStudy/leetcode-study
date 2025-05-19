function isValid(s: string): boolean {
    const stack: string[] = []
    const strMap = new Map<string, string>([
        ['(', ')'],
        ['[', ']'] ,
        ['{', '}']
    ])
    for (let str of s) {
        if (strMap.has(str)) {
            stack.push(strMap.get(str))
        } else if (stack.length > 0 && stack[stack.length - 1] === str) {
            stack.pop()
        } else {
            return false
        }
    }
    return stack.length === 0
};
