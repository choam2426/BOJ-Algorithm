word = input().lower() #소문자로 입력
a = list(set(word)) # 중복제거(종류파악)
b =[] #각 개체들 개수 리스트
for i in a:
    b.append(word.count(i)) #개체 개수 산출 후 b에 추가

c=b.count(max(b)) #가장 큰 개체의 개수

if c == 1:
    print(a[b.index(max(b))].upper()) #[b에서 가장 큰 수의 인수]
else:
    print("?")