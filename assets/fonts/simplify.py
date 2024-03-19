import argparse
import logging
from fontTools import subset
from fontTools.ttLib import TTFont

# 设置日志
logging.basicConfig(level=logging.INFO)

# 解析命令行参数
parser = argparse.ArgumentParser(description='Simplify a font file based on a list of characters.')
parser.add_argument('font_file', type=str, help='The font file to simplify.')

args = parser.parse_args()

# 读取3500个常用汉字
logging.info('Reading characters from 3500.txt...')
with open('3500.txt', 'r', encoding='utf-8') as f:
    chars = f.read().splitlines()

# 添加ascii字符
logging.info('Adding ASCII characters...')
chars.extend([chr(i) for i in range(32, 127)])

# 打开字体文件
logging.info('Opening font file...')
font = TTFont(args.font_file)

# 创建一个子集
logging.info('Creating a subset...')
options = subset.Options()
options.layout_features = '*'
options.notdef_outline = True

# 提取字符
logging.info('Subsetting the font...')
subsetter = subset.Subsetter(options=options)
subsetter.populate(unicodes=[ord(c) for c in chars])
subsetter.subset(font)

# 保存新的字体文件
logging.info('Saving the new font file...')
new_font_file = args.font_file.replace('.woff2', '_sim.woff2')
font.save(new_font_file)

logging.info('Done.')
