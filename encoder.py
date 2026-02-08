def shift_cipher(text, shifts, direction=1):
    result = []
    period = 5

    for i, ch in enumerate(text):
        pos = i + 1
        shift = 0

        for offset, value in enumerate(shifts):
            if (pos - (offset + 1)) % period == 0:
                shift = value
                break

        shift *= direction

        if ch.isalpha() and shift:
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        elif ch.isdigit() and shift:
            result.append(str((int(ch) + shift) % 10))
        else:
            result.append(ch)

    return ''.join(result)
