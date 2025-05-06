import os
import re

def update_image_paths_in_md(md_file_path):
    # 目标图片目录路径
    base_path = r'/static/notes_picture/linux/linux基础/'

    # 读取 Markdown 文件内容
    with open(md_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 使用正则表达式匹配并替换图片路径
    # 匹配 ![alt_text](image_path) 中的 image_path 部分
    updated_content = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)',
                             lambda match: f'![{match.group(1)}]({base_path}{os.path.basename(match.group(2))})',
                             content)

    # 将修改后的内容写回文件
    with open(md_file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print(f"图片路径已更新并保存至 {md_file_path}")

# 调用函数
md_file_path = r'D:\study\project\notes\db\notes\linux\01.Linux基础.md'  # 替换为你的 .md 文件路径
update_image_paths_in_md(md_file_path)
