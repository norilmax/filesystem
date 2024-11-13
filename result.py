import os

file_names = ['1.txt', '2.txt', '3.txt']

file_info = []

for file_name in file_names:
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        line_count = len(lines)
        file_info.append((file_name, line_count, lines))

file_info.sort(key=lambda x: x[1])

with open('result.txt', 'w', encoding='utf-8') as result_file:
    for file_name, line_count, lines in file_info:
        result_file.write(f"{file_name}\n")
        result_file.write(f"{line_count}\n")
        result_file.writelines(lines)

print("Файлы успешно объединены в result.txt")