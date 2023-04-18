import csv
from datetime import datetime
import os

# 找到符合要求的csv文件
filename = ''
for file in os.listdir('.'):
    if file.startswith('月账单') and file.endswith('.csv'):
        filename = file
        break

if not filename:
    print('未找到符合要求的csv文件')
else:
    # 获取月份信息并构建输出文件名
    with open(filename, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        first_row = next(reader) # 跳过第一行
        second_row = next(reader) # 获取第二行
        date_str = second_row[4]
        date_obj = datetime.strptime(date_str, '%Y/%m/%d')
        output_filename = f"{date_obj.month}.bean"

    # 解析csv文件并生成bean文件
    with open(filename, 'r', encoding='utf-8-sig') as f, open(output_filename, 'w', encoding='utf-8') as output:
        reader = csv.reader(f)
        next(reader) # 跳过第一行
        for row in reader:
            if row[0] and row[1] and row[2] and row[3] and row[4]:
                date_obj = datetime.strptime(row[4], '%Y/%m/%d')
                output.write(f"{date_obj.date()} * \"{row[0]}\" \"{row[5]}\"\n")
                output.write(f"\t{row[3]}  {row[1]} CNY\n")
                output.write(f"\t{row[2]}  -{row[1]} CNY\n\n")
