"""
defaultdict으로 dictionary의 사전 기본값을 setting
또 다른 방법으로는 딕셔너리이름.setdefault(key,디폴트값) 이 있다

sorted(리스트1) 정렬된 새로운 리스트인 리스트2를 반환한다
리스트1.sort() 기존의 리스트1을 정렬해준다

'구분자'.join(리스트이름)
리스트이름 의 원소들을 구분자로 연결하여 하나의 문자열로 반환한다
"""

from collections import defaultdict

n=int(input())
fdic=defaultdict(int)
for i in range(n):
    fname,fexte=input().rstrip().split(".")
    fdic[fexte]+=1

for i in sorted(fdic.items()):
    print(" ".join(map(str,i)))