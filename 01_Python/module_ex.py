# fah_converter.py
    # def convert_c_to_f(celcius_value) :
    #     return celcius_value * 9.0 / 5 + 32

import fah_converter    # 동일 디렉토리에 저장된 fah_converter.py 파일을 import

if __name__ == '__main__' :
    print('Enter a celcius value : ')
    celsius = float(input())
    
    fah = fah_converter.convert_c_to_f(celsius)  # 모듈명.함수명(객체명)
    print("That's {} degrees Fahrenheit".format(fah))