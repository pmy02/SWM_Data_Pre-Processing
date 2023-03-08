from cgi import print_arguments
import os
import sys
import json
from konlpy.tag import Mecab


#불용어 리스트
stop_words = "+ - * / . , ? ! n u o b b\ \ ( ) ㅇ ㅇㅇ ㅇㅇㅇ ㅇㅇㅇㅇ 은 는 을 를 이 있 하 것 들 그 되 수 이 보 않 없 나 사람 주 아니 등 같 우리 때 년 가 한 지 대하 오 말 일 그렇 위하 때문 그것 두 말하 알 그러나 받 못하 일 그런 또 문제 더 사회 많 그리고 좋 크 따르 중 나오 가지 씨 시키 만들 지금 생각하 그러 속 하나 집 살 모르 적 월 데 자신 안 어떤 내 내 경우 명 생각 시간 그녀 다시 이런 앞 보이 번 나 다른 어떻 여자 개 전 들 사실 이렇 점 싶 말 정도 좀 원 잘 통하 소리 놓"
stop_words = stop_words.split(' ')
tokenizer = Mecab()


print("지정된 경로로부터 불러오는 중...\n")
def get_document(fileDir): # 파일 읽기
    num = 1
    for i in os.listdir(fileDir):
        if i not in '.DS_Store':
            address = fileDir+i
            
            with open(address, encoding='utf-8') as file:
                contents = json.load(file)
                contents = list(contents.values())
                for j in contents:
                    doc = " ".join(j)
                    if(len(doc)>1000):
                        print(doc, len(doc))
                        token = tokenizer.morphs(doc) # 형태소 분석기
                        
                        print(token)
                        results = []
                        for w in token:
                            if w not in stop_words: #불용어 제거
                                results.append(w)
                        results = " ".join(results)
                        
                        with open("/Users/minyoung/Desktop/Curiosity_Data/Normal_Data/second_data/Normal_Raw_Data/" + str(num) + ".txt", 'w', encoding = 'utf-8') as file:
                            file.write(doc)
                            num += 1


data = get_document("/Users/minyoung/Desktop/Git_Projects/transcript_data/Validation/")