# CodeFest2020 

안드로이드 악성 앱 탐지 프로젝트

해당 프로젝트는 KC-ML2의 지원을 받아 진행하였습니다.

## Introduction
![image](https://user-images.githubusercontent.com/48518526/92078760-c373b080-edf9-11ea-9c1d-f142368c3f21.png)

스마트폰, 태블릿과 같은 모바일 기기가 대중화됨에 따라 모바일 기기 사용자들을 대상으로 개인정보 탈취, 저작권 침해 등 여러 보안 위협이 증가
최근 2019년 미국표준기술연구소(NIST)가 공개한 ‘국가취약점 데이터베이스(NVD)’를 보면 2019년 한해 가장 많은 보안 취약점이 발견된 운영체제는 구글 안드로이드로 총 414건이었다. 이처럼 많은 취약점 존재하기 때문에 다수 공격자들의 타겟이 될 가능성이 높다. 많은 안드로이드 사용자들이 공식적으로 검증되지 않은 악성 앱들을 블랙마켓 등 여러 불법 앱 마켓에서 다운받아 사용한다. 이에 따라, 본 프로젝트에서는 기하급수적으로 불어나는 안드로이드 악성 앱들에 대처하기 위해 머신러닝 기법을 이용한 악성 앱 탐지 시스템을 제안한다.

## Android Malware Detection System
* 악성 앱 데이터셋 
* 악성 행위에 사용되는 API 목록 생성
* 데이터셋 전처리
* CSV 파일 생성
* 머신러닝 모델 구축
* 모델 검증 및 테스트
* 결론

## Dataset
* Androzoo (https://androzoo.uni.lu/)

  개수 : 19,453 개
  연도 : 2017년 ~ 2018년
  (https://androzoo.uni.lu/static/papers/androzoo-msr.pdf)

* AMD (http://amd.arguslab.org/)

  개수 : 19,453 개
  연도 : 2010년 ~ 2016년
  
## Tools
* dexdump2 - API 추출 도구
  
  ![image](https://user-images.githubusercontent.com/48518526/92080854-261a7b80-edfd-11ea-9405-6af64c92149c.png)

  Google Git, "DexDump.cc.“ https://android.googlesource.com/platform/art/+/master
/dexdump/dexdump.cc


## 악성 행위에 사용되는 API 목록 생성
* 참고 논문 출처
  Yousra Aafer, Wenliang Du, and Heng Yin(2014) "DroidAPIMiner: Mining API-Level Features for Robust Malware Detection in Android." International conference on security and privacy in communication systems, Springer.
  
 * 위험 API 목록 (1,848 개)
  ![image](https://user-images.githubusercontent.com/48518526/92081320-d5efe900-edfd-11ea-89ff-45e2dfacb6cf.png)
  
  * 위험 API 목록 정제 (1,848 → 137 개)
  ![image](https://user-images.githubusercontent.com/48518526/92082614-bf4a9180-edff-11ea-8707-0981d359f80f.png)
  사용 빈도에 따라 위험 API 목록의 개수를 줄임 (용량, 차원 감소)
  
## 데이터셋 전처리
 * 정제된 위험 API 목록으로 데이터셋 전처리
  ![image](https://user-images.githubusercontent.com/48518526/92083245-b0b0aa00-ee00-11ea-9cfa-bcc90cb69629.png)
