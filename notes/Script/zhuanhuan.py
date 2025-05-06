import os
from PIL import Image

def convert_png_to_jpg(folder_path):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件是否是 .png 格式
        if filename.endswith('.png'):
            png_path = os.path.join(folder_path, filename)
            jpg_path = os.path.join(folder_path, filename.replace('.png', '.jpg'))

            # 打开 png 文件并转换为 jpg
            with Image.open(png_path) as img:
                # 转换为 RGB 模式以保存为 jpg 格式
                rgb_img = img.convert('RGB')
                # 保存为 jpg 文件
                rgb_img.save(jpg_path, 'JPEG')
                print(f"Converted {filename} to {jpg_path}")

            # 删除原始 png 文件
            os.remove(png_path)
            print(f"Deleted original file: {png_path}")

# 指定要转换的文件夹路径
folder_path = r'D:\study\project\notes\static\notes_picture\background'  # 替换为你的文件夹路径

convert_png_to_jpg(folder_path)
