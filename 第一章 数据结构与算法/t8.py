with open('./data/write.bin', 'wb') as f:
    text = 'Hello World\n我现在就要付诸行动!'
    f.write(text.encode('utf-8'))
