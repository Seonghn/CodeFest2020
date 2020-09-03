# CodeFest2020 

안드로이드 악성 앱 탐지 프로젝트

해당 프로젝트는 KC-ML2의 지원을 받아 진행하였습니다.

## Introduction
![image](https://user-images.githubusercontent.com/48518526/92078760-c373b080-edf9-11ea-9c1d-f142368c3f21.png)

스마트폰, 태블릿과 같은 모바일 기기가 대중화됨에 따라 모바일 기기 사용자들을 대상으로 개인정보 탈취, 저작권 침해 등 여러 보안 위협이 증가
최근 2019년 미국표준기술연구소(NIST)가 공개한 ‘국가취약점 데이터베이스(NVD)’를 보면 2019년 한해 가장 많은 보안 취약점이 발견된 운영체제는 구글 안드로이드로 총 414건이었다. 이처럼 많은 취약점 존재하기 때문에 다수 공격자들의 타겟이 될 가능성이 높다. 많은 안드로이드 사용자들이 공식적으로 검증되지 않은 악성 앱들을 블랙마켓 등 여러 불법 앱 마켓에서 다운받아 사용한다. 이에 따라, 본 프로젝트에서는 기하급수적으로 불어나는 안드로이드 악성 앱들에 대처하기 위해 머신러닝 기법을 이용한 악성 앱 탐지 시스템을 제안한다.

## Android Malware Detection System
* 악성 행위에 사용되는 API 목록 생성
* 악성 앱 데이터셋 생성
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
* dexdump2 
  API 추출 도구
  (Google Git, "DexDump.cc.“ https://android.googlesource.com/platform/art/+/master
/dexdump/dexdump.cc)
