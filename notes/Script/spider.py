import requests
from bs4 import BeautifulSoup
import os


def spider(base_url, folder_path, num_pages=5, num_images=100):
    # 确保目标文件夹存在
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    counter = 1
    # 循环爬取多个页面
    for page in range(1, num_pages + 1):
        # 构建 URL，页数会变化
        url = f"{base_url}?page={page}"

        # 发送 GET 请求，获取网页内容
        response = requests.get(url)

        if response.status_code == 200:
            html_content = response.text
            # 使用 BeautifulSoup 解析 HTML
            soup = BeautifulSoup(html_content, 'html.parser')

            # 查找所有 <a class="preview"> 标签
            links = soup.find_all('a', class_='preview')

            for link in links:
                if counter > num_images:
                    break

                # 提取 href 属性，即图片页面链接
                image_page_url = link.get('href')

                if image_page_url:
                    # 进入图片页面，获取图片实际链接
                    image_page_response = requests.get(image_page_url)

                    if image_page_response.status_code == 200:
                        image_page_soup = BeautifulSoup(image_page_response.text, 'html.parser')

                        # 查找 <img> 标签，获取 src 属性中的图片链接
                        img_tag = image_page_soup.find('img', id='wallpaper')
                        if img_tag:
                            img_url = img_tag.get('src')

                            if img_url:
                                print(f"正在下载图片：{img_url}")

                                # 发送 GET 请求下载图片
                                img_response = requests.get(img_url)

                                # 构建文件名，按顺序命名，例如 1.png, 2.png, 3.png
                                file_extension = img_url.split('.')[-1]  # 获取文件扩展名（例如 jpg, png）
                                filename = os.path.join(folder_path, f"{counter}.{file_extension}")

                                # 保存图片到指定文件夹
                                with open(filename, 'wb') as f:
                                    f.write(img_response.content)

                                print(f"{filename} 下载完成")
                                counter += 1
                    else:
                        print(f"无法访问图片页面：{image_page_url}")
        else:
            print(f"网页请求失败，状态码: {response.status_code}")


# 使用你想爬取的 URL 和保存图片的目标文件夹路径
base_url = 'https://wallhaven.cc/toplist'  # 替换为实际的目标网页 URL（如首页）
folder_path = r'D:\study\project\notes\static\notes_picture\background'  # 设置图片保存文件夹
spider(base_url, folder_path)
