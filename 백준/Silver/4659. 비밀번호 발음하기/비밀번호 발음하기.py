def test():
    lst = ['a', 'e', 'i', 'o', 'u']
    accept = ['ee', 'oo']
    while True:
        x = y = 0
        password = input()
        if password == 'end':
            break
        cnt = 0
        # 모음 개수 새기
        for i in lst:
            if i in password:
                cnt += 1
        # 모음이 없다면 부적합
        if cnt < 1:
            print(f'<{password}> is not acceptable.')
            continue
        # 모음 연속 3개 or 자음 연속 3개 => check
        for i in range(len(password) - 2):
            if password[i] in lst and password[i + 1] in lst and password[i + 2] in lst:
                x = 1
            elif not (password[i] in lst) and not (password[i + 1] in lst) and not (password[i + 2] in lst):
                x = 1
        if x == 1:
            print(f'<{password}> is not acceptable.')
            continue
        # 같은 글이 연속 두개인지 체크 하지만 'e'나 'o'면 컨티뉴
        for i in range(len(password) - 1):
            if password[i] == password[i + 1]:
                if password[i] == 'e' or password[i] == 'o':
                    continue
                else:
                    y = 1
        if y == 1:
            print(f'<{password}> is not acceptable.')
            continue
        print(f'<{password}> is acceptable.')


test()
