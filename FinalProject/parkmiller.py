def PM_hash(pwd, length=32):
    if not len(pwd):
        print("String may not be empty")
        return 0

    def Park_Miller(seed):
        last = seed
        while 1:
            last = (16807 * last % 2147483647)
            yield last % 65535

    print("\nString is: {0}").format(pwd)
    pwd += '0'
    seed = 0

    print('Generating seed...')
    for i in range(len(pwd)):
        seed += ord(pwd[i]) * (257 ** i)

    print('Generated seed: {0}').format(seed)

    hat = Park_Miller(seed)
    result = ''
    # print('Generated seed: {0}').format(hat.next())
    print('Generating hash...')
    for i in range(length):
        result += hex((ord(pwd[i % len(pwd)]) + hat.next()) % 15)[2:-1]
        print(': {0}').format(hat.next())
        print('=: {0}').format((ord(pwd[i % len(pwd)]) + hat.next()) % 15)

    return result


while 1:
    print(u"Input password or ENTER for exit")
    string = input()
    if not string:
        break
    print("Hash generated: {0}").format(PM_hash(string))