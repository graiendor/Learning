def length_of_longest_substring(s: str) -> int:
    """Given a string s, find the length of the longest substring without repeating characters"""
    total_length = 0
    check_index = 0
    non_duplicate_symbols: dict[str, int] = {}
    for count, symbol in enumerate(s):
        if symbol not in non_duplicate_symbols:
            non_duplicate_symbols.update({symbol: 1})
        else:
            non_duplicate_symbols.update({symbol: non_duplicate_symbols.get(symbol) + 1})
            while non_duplicate_symbols.get(symbol) > 1:
                non_duplicate_symbols.update({s[check_index]: non_duplicate_symbols.get(s[check_index]) - 1})
                check_index += 1
        total_length = max(total_length, count + 1 - check_index)
    return total_length
