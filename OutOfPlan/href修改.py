from bs4 import BeautifulSoup

# 从文件中读取HTML内容
with open('index.html', 'r', encoding='utf-8') as file:
    html_doc = file.read()

# 解析HTML
soup = BeautifulSoup(html_doc, 'html.parser')

# 找出所有的<a>标签并修改href属性
for a_tag in soup.find_all('a', href=True):
    # 修改href属性，在其后面加上/index.html
    a_tag['href'] = a_tag['href'].strip('/') + '/index.html'

# 将修改后的HTML写回到新的文件或者覆盖原文件
# 注意：如果直接覆盖原文件，请先备份以防数据丢失
output_filename = 'index.html'  # 或者使用 'index.html' 覆盖原文件
with open(output_filename, 'w', encoding='utf-8') as file:
    file.write(str(soup.prettify()))  # 使用 prettify() 方法使输出的HTML格式化