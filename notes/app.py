import re

from flask import Flask, render_template,send_from_directory
import markdown
import os

app = Flask(__name__)




@app.route('/')
def index():

    return render_template('notes.html')


# 假设你的 'db' 文件夹与 app.py 同级
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # 获取当前目录的绝对路径
MARKDOWN_FOLDER = os.path.join(BASE_DIR, "db", "notes")  # 构造 'notes' 文件夹的路径
IMAGE_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'db', 'notes', 'python', 'images')
@app.route('/db/notes/python/images/<filename>')
def serve_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)
@app.route('/db/notes/<folder_name>/<file_name>')
def serve_markdown(folder_name,  file_name):
    # 构造文件路径
    file_path = os.path.join(MARKDOWN_FOLDER, folder_name, file_name)

    try:
        # 确保文件存在
        if not os.path.exists(file_path):
            return render_template('under_construction.html'), 500  # 使用 500 错误码

        # 读取 .md 文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()



        # 使用 markdown 库将 Markdown 内容转换为 HTML，并使用扩展
        html_content = markdown.markdown(content, extensions=['markdown.extensions.toc',
                                                              'markdown.extensions.fenced_code',
                                                              'markdown.extensions.tables'])

        # 渲染模板并传递文件内容
        return render_template('markdown_display.html', title=file_name, content=html_content)
    except Exception as e:
        return f"错误: {e}"


if __name__ == '__main__':
    app.run(debug=True)
