'''
문제 설명

Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

carpet.png

Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.
Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.
제한사항
갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

입출력 예
brown	yellow	return
10	    2	    [4, 3]
8	    1	    [3, 3]
24	    24	    [8, 6]

출처
※ 공지 - 2020년 2월 3일 테스트케이스가 추가되었습니다.
※ 공지 - 2020년 5월 11일 웹접근성을 고려하여 빨간색을 노란색으로 수정하였습니다.
'''

import math
import numpy as np

def solution(brown, yellow) :
    answer = []
    max_y_h = math.floor(np.sqrt(yellow)) # 세로 <= 가로
    max_b_h = math.floor(brown/2) # 세로 <= 가로
    for y_h in range(1, max_y_h+1) :
        y_w = yellow/y_h
        if math.floor(y_w) - y_w == 0 :
            for n in (1, max_b_h+1) :
                if 2*(n*(y_w + y_h)+2*(n*n)) == brown : # 브라운이 노랑이를 둘러쌀 수 있는지
                    w = int(y_w + 2)
                    h = int(y_h + 2)
                    answer = [w,h]
                else :
                    pass
        else :
            pass
    return answer

b1 = 10
y1 = 2

b2 = 8
y2 = 1

b3 = 24
y3 = 24

print(solution(b1,y1))
print(solution(b2,y2))
print(solution(b3,y3))
