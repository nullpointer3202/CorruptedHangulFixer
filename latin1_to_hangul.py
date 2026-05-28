def latin_to_cp949(txt) :
    raw = txt.encode("latin-1")
    raw_patched = bytearray();
    is_fair = 0

    for idx, b in enumerate (raw):
        if (chr(b).isascii()) :         #   바이트가 아스키문자라면
            if (is_fair == 1 and b == 0x5F) :   # 한글 바이트 끝부분이면서 _ 문자일경우
                raw_patched.append(0xAD)
                is_fair = 0
                continue

            raw_patched.append(b)
            is_fair = 0
            continue
        else :
            if (is_fair == 0) : #한글 바이트 시작점
                raw_patched.append(b)
                is_fair = 1
                continue
            else :  #한글 바이트 끝
                raw_patched.append(b)
                is_fair = 0
            

    return raw_patched.decode("cp949", errors="replace"), "cp949"



s = input()
result, enc = latin_to_cp949(s)
print(f"[{enc}] {result}")