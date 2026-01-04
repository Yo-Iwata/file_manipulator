import sys
import os

# file = open('test.txt')
# print(file.read())
# file.close()

# file_path = 'test.txt'
# file = open(file_path)
# file_contents = file.read()
# file.close()

# file = open(file_path, 'w')
# file.write(file_contents + "\nAppending more text to this file")
# file.close()

# pathname = 'test.txt'
# contents = ''

# with open(pathname) as f:
#     contents = f.read()

# with open(pathname, 'w') as f:
#     f.write(contents + "\nAppending more text to this file")

argv = sys.argv
argv_num = len(sys.argv)-1

if argv_num < 1:
    print("引数にコマンドを指定してください！")
    print("入力例：reverse inputpath outputpath")
    exit()

command_str = argv[1]
# command: neededArgNum
command_lists = {
    'reverse': 3, 'copy': 3, 'duplicate-contens': 3, 'replace-string': 4
}
def checkCommnadValidation(commandStr):
    for key, val in command_lists.items():
        if commandStr == key:
            if argv_num == val:
                return
            else:
                print(f"指定されたコマンド {commandStr} は {val} 個の引数を指定する必要があります。")
                exit()
    
    print(f"指定されたコマンド {commandStr} は見つかりませんでした。")
    print("以下の中からコマンドを指定してください")
    print(list(command_lists.keys()))
    exit()

checkCommnadValidation(command_str)

def checkFileValidation(filepath):
    if not os.path.isfile(filepath):
        print(f"指定したファイル {filepath} は存在しません！")
        exit()

def reverse():
    filepath_in = argv[2]
    checkFileValidation(filepath_in)

    filepath_out = argv[3]
    checkFileValidation(filepath_out)

    lines = ''

    with open(filepath_in) as input_file:
        lines = input_file.readlines()

    reversed_lines = lines[::-1]

    with open(filepath_out, 'w') as output_file:
        for line in reversed_lines:
            output_file.write(line[::-1])

    print(f"{filepath_out} に書き込み完了！")

reverse()

    