def get_shifted_index(char, shift, map):
    if not isinstance(map.get(char), int):
        raise TypeError("Invalid character")
    return (map.get(char) + shift) % 26
