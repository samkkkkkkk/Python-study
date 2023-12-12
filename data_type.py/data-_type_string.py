'''
* 문자열 (string)

- 단일 문자들을 따옴표('', "")로 감싸서
나열한 문자 데이터의 집합 형태입니다.
- 따옴표 안에 어떤 형태의 데이터가 들어가도 문자로 인식
- 전 세계의 모든 문자를 저장할 수 있고, 길이에도 제한이 없습니다.
'''

# 나는 그에게 "도와줘!" 라고 말했다.
# 탈출 문자를 적용해서(\) 따옴표를 문자로 표현할 수 있습니다.

# s1 = "나는 그에게 "도와줘!" 라고 말했다."
s1 = "나는 그에게 \"도와줘!\" 라고 말했다."
print(s1)

# Let's go together!
s2 = 'Let\'s go together!'
print(s2)

# file1 = 'C:\temp\new.jpg' (x)
file1 = 'C:\\temp\\new.jpg'
print(file1)

# 문자열 앞에 r이라는 접두어를 붙이면
# 해당 문자열은 탈출 문자열을 적용하지 않습니다.
file2 = r'C:\temp\new.jpg'
print(file2)

# 쌍따옴표(홑따옴표)를 세개 지정해서 문장을 작성하면
# 내부에서 줄 개행, 공백을 표현할 수 있습니다.
# ''' ''' 은 주석이 아니지만 문장 주석처럼 사용된다.
anthem = '''동해물과 백두산이 마르고 닳도록 
하느님이 보우하사 우리나라만세 
무궁화 삼천리 화려강산 대한사람 
대한으로 길이보전하세'''
print(anthem)

# \를 문장 끝에 붙이면 line continue 효과를 줍니다.
anthem2 = '''동해물과 백두산이 마르고 닳도록  \
하느님이 보우하사 우리나라만세 \
무궁화 삼천리 화려강산 대한사람 \
대한으로 길이보전하세'''
print(anthem2)

'''
* 문자열 연산

- 파이썬은 문자열의 덧셈 연산과 곱셈 연산을 지원합니다.
- 덧셈 연산은 문자열을 서로 연결하여 결합합니다.
'''

s3 = '오늘 저녁은 '
s4 = '치킨 입니다.'
print(s3 + s4 + ' 와 맛있겟다!!!')

'''
- 파이썬은 문자열의 곱셈 연산 또한 지원합니다.
- 곱셈 연산자(*)로 문자열을 정해진 수 만큼 반복해서 연결합니다.

'''
print('배고파' * 4)
print('-' * 10)

# print(s3 * 1.7) (x) -> 횟수는 정수.
# print(s3 * s4) (x) -> 문자열 끼리는 곱할 수 없습니다.

