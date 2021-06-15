#讀取對話
def read_file(filename):
    chat = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            chat.append(line.strip())
    return chat

#改變格式
def convert(chat):
    new = []
    person = None #預設值
    for line in chat:
        if line == 'Allen':
            person = 'Allen'
            continue 
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:  #如果person有值 
            new.append(person + ":" + line)
    return new


#存出檔案
def write_file(filename, chat):
    with open (filename, 'w') as f:
        for line in chat:
            f.write(line + '\n')

def main():
	chat = read_file('input.txt')
	chat = convert(chat)
	write_file('output.txt', chat)

main()


