"""
문자열.isalnum()
알파벳이나 숫자로 이루어 진 경우 return True

for문의 경우 반복 횟수가 정해져 있을 때 사용
while문의 경우 반복 조건을 수정하기 간편
"""

word=list(input().rstrip())

i=0
while i<len(word):
    if word[i]=="<":
        while word[i]!=">":
            i+=1
        i+=1
    elif word[i].isalnum():
        start=i
        while i<len(word) and word[i].isalnum():
            i+=1
        tmp=word[start:i]
        tmp.reverse()
        word[start:i]=tmp
    else:
        i+=1

print("".join(word))
