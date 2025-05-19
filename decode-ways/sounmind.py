def numDecodings(s: str) -> int:
    """
    Count the number of ways to decode a string where:
    'A' -> '1', 'B' -> '2', ..., 'Z' -> '26'

    Args:
        s: A string of digits

    Returns:
        The number of ways to decode the input string
    """
    # Handle edge cases
    if not s or s[0] == "0":
        return 0

    # Optimization: we only need to track the previous two results
    prev = 1  # Ways to decode up to index i-2
    curr = 1  # Ways to decode up to index i-1

    for i in range(1, len(s)):
        # Start with 0 for the new current calculation
        next_val = 0  # Ways to decode up to index i

        # Single digit decode - if current digit is not '0'
        if s[i] != "0":
            # We can decode it independently,
            # adding all ways to decode up to the previous position.
            next_val += curr

        # Two digit decode - if the last two digits form a valid letter (10-26)
        two_digit = int(s[i - 1 : i + 1])
        if 10 <= two_digit <= 26:
            next_val += prev

        # Shift two trackers for the next iteration
        prev, curr = curr, next_val

        # If there's no way to decode at this point, the whole string is invalid
        if curr == 0:
            return 0

    return curr
