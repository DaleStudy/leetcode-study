/**
 * ==================== Complexity Summary ====================
 * | Operation  | Time Complexity        | Space Complexity   |
 * |------------|------------------------|--------------------|
 * | addWord    | O(n)                   | O(n)              |
 * | search     | O(n) (no '.')          | O(n)              |
 * |            | O(k^n) (with '.')      | O(n)              |
 * ============================================================
 *
 * Notes:
 * - n: Length of the word being added/searched.
 * - k: Average branching factor (number of children per node).
 * - Worst-case time complexity for `search` with '.' can grow exponentially
 *   when many wildcards are present in the word.
 */

var WordDictionary = function () {
  this.root = { $: false };
};

/**
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function (word) {
  let node = this.root;

  for (char of word) {
    if (!node[char]) {
      node[char] = { $: false };
    }
    node = node[char];
  }

  node["$"] = true;
};

/**
 * @param {string} word
 * @return {boolean}
 */
WordDictionary.prototype.search = function (word) {
  const dfs = (node, index) => {
    // Base case: If we've reached the end of the word
    if (index === word.length) {
      return node["$"] === true;
    }

    const char = word[index];

    // If the character is not a wildcard
    if (char !== ".") {
      if (node[char]) {
        return dfs(node[char], index + 1); // Continue DFS
      } else {
        return false; // Character not found
      }
    }

    // If the character is a wildcard
    for (const key of Object.keys(node).filter((key) => key !== "$")) {
      if (dfs(node[key], index + 1)) {
        return true; // Return true if any child path matches
      }
      // Why we need to check if the recursive call to dfs returns true or false:
      // 1) Early termination of recursion when a match is found:
      //    - Once we find a valid match, there's no need to explore other branches.
      // 2) Proper propagation of the result back up the recursion stack:
      //    - A valid match found in a deeper level of recursion needs to return true
      //      all the way back to the initial search call to indicate success.
    }

    return false; // No paths matched for the wildcard
  };

  return dfs(this.root, 0); // Start DFS from the root node
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */

// ***** second trial *****
// var WordDictionary = function () {
//   this.root = { $: true };
// };

// /**
//  * @param {string} word
//  * @return {void}
//  */
// WordDictionary.prototype.addWord = function (word) {
//   const dfs = (node, index) => {
//     // exit
//     if (index === word.length) {
//       node["$"] = true;
//       return;
//     }

//     // add .
//     if (!node["."]) {
//       node["."] = { $: false };
//     }
//     dfs(node["."], index + 1);

//     // add each character
//     const temp = word[index];

//     if (!node[temp]) {
//       node[temp] = { $: false };
//     }
//     dfs(node[temp], index + 1);
//   };

//   dfs(this.root, 0);
// };

// /**
//  * @param {string} word
//  * @return {boolean}
//  */
// WordDictionary.prototype.search = function (word) {
//   let node = this.root;

//   for (char of word) {
//     if (!node[char]) {
//       return false;
//     }
//     node = node[char];
//   }

//   return node["$"];
// };

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */

// ***** first trial *****
// var WordDictionary = function () {
//   this.root = new Set();
// };

// /**
//  * @param {string} word
//  * @return {void}
//  */
// WordDictionary.prototype.addWord = function (word) {
//   this.root.add(word);
// };

// /**
//  * @param {string} word
//  * @return {boolean}
//  */
// WordDictionary.prototype.search = function (word) {
//   if (this.root.size === 0) {
//     return false;
//   } else {
//     for (dict of this.root) {
//       if (dict.length === word.length) {
//         const found = word
//           .split("")
//           .every((str, index) => str === "." || dict[index] === str);
//         if (found) {
//           return true;
//         }
//       } else {
//         continue;
//       }
//     }
//     return false;
//   }
// };

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
