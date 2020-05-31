class Solution:
    def lengthOfLongestSubstringKDistinct(self, given_string: str, num_unique_char: int) -> int:
        """
        The general idea is to iterate over string s.
        Always put the character c and its location i in the dictionary d.
        1) If the sliding window contains less than or equal to k distinct characters, simply record the return value, and move on.
        2) Otherwise, we need to remove a character from the sliding window.
        Here's how to find the character to be removed:
        Because the values in d represents the rightmost location of each character in the sliding window, in order to find the longest substring T, we need to locate the smallest location, and remove it from the dictionary, and then record the return value.
        
        :type given_string: str
        :type num_unique_char: int
        :return_type: int
        """
        
        # Use dictionary d to keep track of (character, location) pair,
        # where location is the rightmost location that the character appears at
        unique_char_map = {}
        low, result = 0, 0
        for i, c in enumerate(given_string):
            unique_char_map[c] = i
            if len(unique_char_map) > num_unique_char:
                low = min(unique_char_map.values())
                del unique_char_map[given_string[low]]
                low += 1
            result = max(i - low + 1, result)
        return result