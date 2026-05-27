def decode_korean(s):
    raw = s.encode("latin-1")

    # 1차: euc-kr 시도
    try:
        return raw.decode("euc-kr"), "euc-kr"
    except UnicodeDecodeError:
        pass

    # 2차: cp949 시도 (0x5F → 0xAD 치환)
    raw_patched = bytes([0xAD if b == 0x5F else b for b in raw])
    try:
        return raw_patched.decode("cp949"), "cp949 (0x5F -> 0xAD)"
    except UnicodeDecodeError:
        pass

    # 3차: 치환 없이 cp949 시도
    return raw.decode("cp949", errors="replace"), "cp949 (w/ replace)"



s = input()
result, enc = decode_korean(s)
print(f"[{enc}] {result}")