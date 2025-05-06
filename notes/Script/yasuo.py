from PIL import Image
import os


def compress_image(input_path, output_path, quality=85):
    # 打开图片
    with Image.open(input_path) as img:
        # 保存压缩后的图片，quality 控制画质（从 0 到 100，100 是无损压缩）
        img.save(output_path, quality=quality)
        print(f"图片已压缩：{output_path}")


def compress_images_in_folder(folder_path, output_folder, quality=85):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历文件夹中的所有图片
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_folder, file)

                # 压缩图片
                compress_image(input_path, output_path, quality)

    print("所有图片压缩完成！")


# 示例调用
folder_path = r'D:\study\project\notes\static\notes_picture\background'  # 设置图片所在的文件夹
output_folder = r'D:\study\project\notes\static\notes_picture\background'  # 设置压缩后图片保存的文件夹
quality = 85  # 设置压缩质量，范围从 0 到 100，值越低压缩越强，质量越差

compress_images_in_folder(folder_path, output_folder, quality)
