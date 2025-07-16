# chr(num) : 숫자 -> 아스키코드 
# ord(str) : 문자 -> 아스키코드
ch = input() 
# if '0' <= ch <= '9' : 
#     print(chr(int(ch))) # python에서는 String -> int 시 int(str) 사용
# --> 숫자문자를 굳이 숫자로 변경해줄 필요 없음 (문자이므로 문자의 아스키코드 변환 함수) 
print(ord(ch))