class Solution {
  private DELIMITER = "*";

  /**
   * @param strs: a list of strings
   * @returns: encodes a list of strings to a single string.
   */
  public encode(strs: string[]): string {
    let encoded = "";

    for (const str of strs) {
      encoded += `${str.length}${this.DELIMITER}${str}`;
    }

    return encoded;
  }

  /**
   * @param str: A string
   * @returns: decodes a single string to a list of strings
   */
  public decode(str: string): string[] {
    const decoded: string[] = [];

    let stack: string[] = [];
    let pointer = 0;

    while (pointer < str.length) {
      const char = str[pointer];

      if (char === this.DELIMITER) {
        let strLength: number = Number(stack.join(""));
        stack = [];

        const word = str.substring(pointer + 1, pointer + 1 + strLength);
        pointer = pointer + 1 + strLength;

        decoded.push(word);
      } else {
        stack.push(char);
        pointer++;
      }
    }

    return decoded;
  }
}
