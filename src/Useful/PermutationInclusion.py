from string import ascii_lowercase


def check_inclusion(s1: str, s2: str) -> bool:
    inclusion: bool = False
    if len(s1) <= len(s2):
        s1map: dict[str, int] = {symbol: 0 for symbol in list(ascii_lowercase)}
        s2map: dict[str, int] = {symbol: 0 for symbol in list(ascii_lowercase)}
        for count, symbol in enumerate(s1):
            add_item(symbol, s1map)
            add_item(s2[count], s2map)

        count: int = 0
        while count < len(s2) - len(s1) and not inclusion:
            if s1map == s2map:
                inclusion = True
            symbol: str = s2[count + len(s1)]
            add_item(symbol, s2map)
            s2map[s2[count]] -= 1
            count += 1
        if not inclusion:
            inclusion = s1map == s2map
    return inclusion


def add_item(symbol: str, s: dict[str, int]):
    if symbol in s:
        s[symbol] += 1
    else:
        s[symbol] = 1
