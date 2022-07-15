# 추출 정보
'''
        <dl class="blind">
	        <dt>종목 시세 정보</dt>
	        <dd>2022년 07월 08일 16시 11분 기준 장마감</dd>
	        <dd>종목명 삼성전자</dd>
	        <dd>종목코드 005930 코스피</dd>
	        <dd>현재가 58,700 전일대비 상승 500 플러스 0.86 퍼센트</dd>
	        <dd>전일가 58,200</dd>
	        <dd>시가 58,600</dd>
	        <dd>고가 59,300</dd>
	        <dd>상한가 75,600</dd>
	        <dd>저가 58,200</dd>
	        <dd>하한가 40,800</dd>
	        <dd>거래량 15,179,249</dd>
	        <dd>거래대금 892,735백만</dd>
        </dl>
'''
# 정보 구성
    # 1. <dl class = "blind"> ... <\dl> 에 있는 data 1차 추출
    # 2. <dd> ... </dd> data 2차 추출

import re
import urllib.request

url = 'https://finance.naver.com/item/main.naver?code=005930'   # 주소설정
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode('ms949'))

stock_result = re.findall("(\<dl class=\"blind\"\>)([\s\S]*?)(\<\/dl\>)", html_contents)
    # <dl class="blind" 와 </dl> 사이에
    # \s(공백), \S(공백X)
    # *(0번 이상 반복) ?(또는 아니다)
sansung_stock = stock_result[0]    # 검색된 여러개(2)의 tuple() 값 중 원하는 tuple 값인 첫번째 값 추출
samsung_index = sansung_stock[1]     # tuple 값의 세개의 리스트값중 필요한 두번째 값만 추출
                                        # 하나의 괄호가 tuple index 가 됨
index_list = re.findall("(\<dd\>)([\s\S]+?)(\<\/dd\>)", samsung_index)
    # <dd> 와 </dd> 사이에
    # \s(공백), \S(공백X)
    # *(0번 이상 반복) ?(또는 아니다)

for index in index_list :
    print(index[1])
    # 한출씩 반복 출력