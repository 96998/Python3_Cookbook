from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    # UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 2:
    # illegal multibyte sequence
    with open(r'./data/天龙八部.txt', encoding='UTF-8') as f:
        for line, prevlines in search(f, '王语嫣', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
