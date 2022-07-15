import re    # Regular Expression modul import
import urllib.request
url = 'https://bit.ly/3rxQFS4'        # url 지정
html = urllib.request.urlopen(url)  # html 소스요청 (request.urlopen)
html_contents = str(html.read())    # html 소스코드 추출 (read)
id_result = re.findall(r'([A-Za-z0-9]+\*\*\*)', html_contents)  # 정규표현식 적용 추출
print(id_result)

# for result in id_result :
#     print(result)