import argparse
from fontTools.ttLib import TTFont

# 解析命令行参数
parser = argparse.ArgumentParser(description='Check a font file for a list of characters.')
parser.add_argument('font_file', type=str, help='The font file to check.')

args = parser.parse_args()

# 读取3500个常用汉字
with open('3500.txt', 'r', encoding='utf-8') as f:
    chars = f.read().splitlines()

# 添加ascii字符
chars.extend([chr(i) for i in range(32, 127)])

# 打开字体文件
font = TTFont(args.font_file)

# 获取字体中的所有字符
font_chars = {chr(y[0]) for x in font['cmap'].tables for y in x.cmap.items()}

# 检查每个字符
missing_chars = [c for c in chars if c not in font_chars]

if missing_chars:
    print(f'The font file is missing the following characters: {missing_chars}')
else:
    print('All characters are present in the font file.')
