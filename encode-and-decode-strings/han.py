#!/usr/bin/env python3
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        return '-'.join([
            '.'.join([
                str(ord(c))
                for c in s
            ])
            for s in strs
        ])

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        return [
            ''.join([
                chr(int(c))
                for c in s.split('.')
            ])
            for s in str.split('-')
        ]


# 아래는 간단한 테스트 코드
import random

def generate_random_string(min_length=5, max_length=20):
    # Choose a random string length between min_length and max_length
    string_length = random.randint(min_length, max_length)

    # Define the character categories
    alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    hanguls = '가나다라마바사아자차카타파하'
    emojis = ['😀', '😂', '😉', '😍', '😎', '😭', '😊', '😜', '😢', '😱']

    # Probability of selecting from each category
    weights = [0.25, 0.25, 0.25, 0.25]

    # Combine all categories into a single list
    all_chars = list(alphabets + numbers + hanguls) + emojis

    # Select characters based on the weights and create the final string
    random_chars = random.choices(all_chars, k=string_length)
    random_string = ''.join(random_chars)

    return random_string

def generate_multiple_random_strings():
    strings_list = []
    # Generate a random number of strings, between 1 and 10
    number_of_strings = random.randint(1, 10)

    for _ in range(number_of_strings):
        random_string = generate_random_string()
        strings_list.append(random_string)

    return strings_list

strs = generate_multiple_random_strings()
print(strs)
print(strs==Solution().decode(Solution().encode(strs)))
