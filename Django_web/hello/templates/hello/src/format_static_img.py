from bs4 import BeautifulSoup
import re


def convert_img_src_to_django_static(html_file, output_file):
    # 读取 HTML 文件
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 检查是否已经存在 {% load static %} 指令
    if not soup.find(string=re.compile(r'{%\s*load\s+static\s*%}')):
        # 检查并插入 {% load static %} 在 <head> 或 HTML 开头
        load_static_tag = BeautifulSoup("{% load static %}", 'html.parser')
        if soup.head:
            soup.head.insert(0, load_static_tag)
        else:
            soup.insert(0, load_static_tag)

    # 查找所有的 <img> 标签
    img_tags = soup.find_all('img')

    for img in img_tags:
        src = img.get('src')
        # 检查 src 是否符合特定模式
        if re.match(r'attachment/.*\.png', src):
            # 替换 src 属性为 Django 的静态文件路径格式
            new_src = "{% static '" + src + "' %}"
            img['src'] = new_src

    # Find all <a> tags that might contain document links
    a_tags = soup.find_all('a')

    for a in a_tags:
        href = a.get('href')
        # Check if href matches the specific pattern for .docx, .xlsx, or .png files within the "attachment" directory
        if re.match(r'attachment\\.*\.(docx|xlsx)$', href):
            # Replace href attribute with Django's static file path format
            new_href = "{% static '" + href + "' %}"
            a['href'] = new_href

    # 将修改后的 HTML 内容写入到新文件或覆盖原文件
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))


html_file_path = '../国有控股企业名单.html'  # 指定的 HTML 文件路径
output_file_path = '../国有控股企业名单.html'  # 指定的 HTML 文件路径
convert_img_src_to_django_static(html_file_path, output_file_path)
