lowercase_letters = [chr(i) for i in range(ord("a"), ord("z") + 1)]
uppercase_letters = [chr(i) for i in range(ord("A"), ord("Z") + 1)]

lowercase_map = dict(zip(lowercase_letters, range(26)))
uppercase_map = dict(zip(uppercase_letters, range(26)))
