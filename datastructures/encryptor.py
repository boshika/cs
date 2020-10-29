"""
Input: "xyz", 2
Output: "zab"
Time Complexity: O(n), Space: O(n)
"""
alphabet_dict = {chr(i+96): i for i in range(1,27)}

def encryptor(string, key):
    current_value = 0
    str = ''
    for i in string:
        current_value = alphabet_dict[i] + key
        circular_key = current_value % 26
        k = get_key(circular_key)
        str += k
        return str

def get_key(val):
    for key, value in alphabet_dict.items():
        if val == value:
            return key
        elif val == 0:
            return 'z'
    return "key doesn't exist"
