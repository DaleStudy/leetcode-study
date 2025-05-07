from typing import List


class Solution:
    # Special character used as delimiter between length and actual string
    delimiter = "$"

    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings into a single string.
        Format: [length]$[string][length]$[string]...
        """
        encoded = []
        # Encode each word using the format: length + delimiter + word
        for word in strs:
            # Convert word length to string, add delimiter, then add the word itself
            encoded.append(f"{len(word)}{self.delimiter}{word}")

        # Join all encoded elements into a single string and return
        return "".join(encoded)

    def decode(self, encoded: str) -> List[str]:
        """
        Decodes a single string back to the original list of strings.
        """
        decoded = []  # List to store the decoded strings
        current_index = 0  # Pointer to track current position in the encoded string

        # Process the encoded string until we reach the end
        while current_index < len(encoded):
            # Starting from current_index, find the position of delimiter
            delimiter_index = current_index

            # Move forward until we find the delimiter character
            while encoded[delimiter_index] != self.delimiter:
                delimiter_index += 1

            # Extract and convert the length prefix to integer
            word_length = int(encoded[current_index:delimiter_index])

            # Calculate the start position of the word (after the delimiter)
            word_start = delimiter_index + 1

            # Calculate the end position of the word
            word_end = word_start + word_length

            # Extract the word using the calculated positions
            word = encoded[word_start:word_end]

            # Add the decoded word to our result list
            decoded.append(word)

            # Move the current index to the end of this word for the next iteration
            current_index = word_end

        return decoded
