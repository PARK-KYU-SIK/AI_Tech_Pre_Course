# 데이터 url : https://s3.ap-northeast-2.amazonaws.com/teamlab-gachon/books.xml
from bs4 import BeautifulSoup   # module import

with open('./data_handling/XML/books.xml', 'r', encoding = 'utf8') as books_file :  # 파일 주소설정 및 열기
    books_xml = books_file.read()   # str 형식으로 열기


# xml module 을 이용한 분석
soup = BeautifulSoup(books_xml, 'lxml')     # 객체생성 (파일명, parser)

book_info = soup.find_all('author') # Tag 찾는 함수 find_all 생성
    # find_all( )
        # 정규식과 마찬가지로 해당 패턴을 모두 반환
    # find('invention-title')
        # Tag 네임 = title
        # 하나를 찾아 반환
    # get_text()
        # 반환된 패턴의 값 반환 (태그와 태그 사이)
for i in book_info :
    print(i)
    print(i.get_text())