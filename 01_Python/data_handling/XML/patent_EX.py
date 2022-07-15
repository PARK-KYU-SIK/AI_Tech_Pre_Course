import urllib.request
from bs4 import BeautifulSoup

with open('./US08621662-20140107.xml', 'r', encoding = 'utf8') as patent_file :
    xml = patent_file.read()

soup = BeautifulSoup(xml, 'lxml')

# invention-title 찾기
invention_title_tag = soup.find('invention-title')
    # BeautifulSoup 을 이용하여 지정한 Tag 명에 저장된 정보 검색
# print(invention_title_tag)
#     # Tag 열림 닫힘 전체
print(invention_title_tag.get_text())
    # Tag 안의 내용만