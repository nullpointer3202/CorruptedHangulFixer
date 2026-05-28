
#UTF-8 -> CP949 강제 변환 중 바이트 소실 과정을 비슷하게 구현한 코드.
#UTF-8 바이트를 강제로 2바이트씩 나눠서 CP949 형식으로 변환 및 유효하지 않은 바이트 치환.
#망가진 한글 바이트 뒤 ASCII가 올 경우 ASCII 바이트까지 한글 바이트로 인식하는 문제 해결.


import unicodedata

#text_raw = "텍스트 샘플"
text_raw = input()
text_raw = unicodedata.normalize("NFD", text_raw)
test_bytes = text_raw.encode("utf-8")

print(f"올바른 값 : {test_bytes.decode('utf-8', errors='ignore')}")
print("오류 구현 값 : ", end="")

i = 0
n = len(test_bytes)


while i < n:
    b = test_bytes[i]

    # ASCII와 공백류는 그대로 출력
    if b <= 0x7F:
        # 그대로 단일 바이트를 문자로 변환하여 출력
        print(chr(b), end="")
        i += 1
        continue

    # ASCII 아닌 바이트 2바이트씩 끊는 구간
    tmp_s = 0   # 소실된 바이트 뒤 ASCII가 붙을 경우 그 바이트도 한글 바이트로 인식하는 문제 해결용 문자 백업
    if i + 1 < n:
        try:
            chunk = bytes((test_bytes[i], test_bytes[i + 1]))
            tmp_s = test_bytes[i + 1]
            decoded = chunk.decode("cp949")
            print(decoded, end="")

        except UnicodeDecodeError:
            # 인코딩 실패 시 치환문자 추가
            print("�", end="")
        i += 2
        if tmp_s <= 0x7F:
            # 그대로 단일 바이트를 문자로 변환하여 출력
            print(chr(tmp_s), end="")
    else:
        # 마지막 남은 1바이트가 ascii가 아닌 경우도 치환문자 적용
        print("�", end="")
        i += 1