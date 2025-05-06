import os
import re


def merge_md_files(directory, output_filename):
    # 检查目标文件夹是否存在
    if not os.path.exists(directory):
        print(f"错误: 目录 '{directory}' 不存在!")
        return
    # 获取目录下所有的 .md 文件
    md_files = [f for f in os.listdir(directory) if f.endswith('.md')]
    if not md_files:
        print(f"错误: 目录 '{directory}' 中没有 .md 文件!")
        return
    md_files.sort()  # 确保文件按名字排序
    # 创建输出文件并写入 TOC 标记
    output_file_path = os.path.join(directory, output_filename)
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write('[TOC]\n\n')  # 添加 TOC 标记

        # 依次读取每个 .md 文件并合并内容
        for md_file in md_files:
            file_path = os.path.join(directory, md_file)
            with open(file_path, 'r', encoding='utf-8') as file:
                output_file.write(f'# {md_file}\n\n')  # 在每个文件前加上文件名
                output_file.write(file.read())  # 将文件内容写入到输出文件中
                output_file.write('\n\n')  # 文件之间加两个换行符

    print(f"所有 .md 文件已合并并保存为 {output_filename}")





# 调用合并函数
folder_path = r'D:\study\project\notes\db\notes\python\01.Python基础语法'  # 替换成你的目标文件夹路径
output_md_file = '../linux基础.md'  # 生成的合并后的文件名

merge_md_files(folder_path, output_md_file)
