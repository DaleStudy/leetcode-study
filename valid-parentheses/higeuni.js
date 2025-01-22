class Stack {
  constructor() {
      this.container = [];
  }

  push(item) {
      this.container.push(item);
  }

  pop() {
      return this.container.pop();
  }

  top() {
      if (this.container.length === 0) return null;
      return this.container[this.container.length - 1];
  }

  isEmpty() {
      return this.container.length === 0;
  }
} 

/**
 * @param {string} s
 * @return {boolean}
 * 
 * complexity
 * time: O(n)
 * space: O(n)
 */
var isValid = function(s) {
    const stack = new Stack();
    for (let x of s) {
        if (x === '(' || x === '[' || x === '{') {
            stack.push(x);
        } else {
            if (stack.isEmpty()) return false;
            if (x === ')' && stack.top() !== '(') return false;
            if (x === ']' && stack.top() !== '[') return false;
            if (x === '}' && stack.top() !== '{') return false;
            stack.pop();
        }
    }
    return stack.isEmpty();
};

