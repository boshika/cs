"""
Description:Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Example
Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
"""


class EncodeDecode:
    def __init__(self, s):
        self.s = s

    def encode(self):
        res = " "
        for i in self.s:
            res += str(len(i)) + '#' + i

        return res

    def decode(self, encoded_str):
        decoded_list, i = [], 0

        while i < len(encoded_str):
            j = i

            while encoded_str[j] != '#':
                j += 1

            length = int(encoded_str[i:j])
            decoded_list.append(encoded_str[j + 1:j + 1 + length])
            i = j + 1 + length

        return decoded_list