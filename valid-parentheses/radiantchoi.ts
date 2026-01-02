function isValid(s: string): boolean {
    let stack: string[] = [];

    // 스택에 대응하는 문자가 있다면 제거, 없다면 현재 문자를 추가
    for (const letter of s) {
        if (stack.length > 0) {
            const top = stack[stack.length - 1];

            if (top === "(" && letter === ")") {
                stack.pop();
            } else if (top === "{" && letter === "}") {
                stack.pop();
            } else if (top === "[" && letter === "]") {
                stack.pop();
            } else {
                stack.push(letter);
            }
        } else {
            stack.push(letter);
        }
    }

    // 스택에 내용물이 있는지 없는지만으로도 "Valid"한지 판별 가능
    return stack.length === 0;
};
