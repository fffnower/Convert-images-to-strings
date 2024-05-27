# 导入模块
import os
from PIL import Image

# 定义字符列表
chars = "#@&$%*o!;."

# 假设要遍历的源文件夹是source_dir
source_dir = "./images"
# 假设要存放新文件的目标文件夹是target_dir
target_dir = "./image_to_txt"
# 用os.listdir()函数获取源文件夹中的所有文件名
filenames = os.listdir(source_dir)

if not os.path.exists(source_dir): # 检查路径是否存在
    os.makedirs(source_dir) # 创建新的文件夹

if not os.path.exists(target_dir): # 检查路径是否存在
    os.makedirs(target_dir) # 创建新的文件夹

# 用for循环遍历每个文件名
for filename in filenames:

    # 用os.path.splitext()函数分割出不带后缀的原文件名
    basename = os.path.splitext(filename)[0]

    # 检测文件是否已经存在
    if os.path.exists("./image_to_txt/") and os.path.isfile(f"./image_to_txt/{basename}.txt"):
        continue

    # 打开图片并转化为灰度图像
    img = Image.open(f"./images/{filename}").convert("L")

    # 获取图片的宽度和高度
    width, height = img.size

    # 方法一：缩小图片尺寸
    new_width = 800 # 你想要的新宽度
    new_height = int(height * new_width / width * 0.50) # 根据比例计算新高度(最后的系数是用来平衡字符的高宽比)
    img = img.resize((new_width, new_height)) # 缩小图片
    # 获取图片的宽度和高度
    width, height = img.size

    # 创建一个空字符串用于存储字符
    text = ""

    # 遍历每个像素点
    for y in range(height):
        for x in range(width):
            # 获取像素点的灰度值（0-255）
            gray = img.getpixel((x, y))
            # 根据灰度值选择一个字符
            char = chars[int(gray / 256 * len(chars))]
            # 把字符添加到字符串中
            text += char
        # 每行结束后换行
        text += "\n"

    # 拼接出新的以.txt为后缀的新文件名
    new_filename = basename + ".txt"

    # 用os.path.join()函数拼接出目标文件的完整路径
    target_file = os.path.join(target_dir, new_filename)

    # 打开一个txt文件并写入字符串
    with open(target_file, "w") as f:
        f.write(text)
    print(f'已输出{target_file}')


