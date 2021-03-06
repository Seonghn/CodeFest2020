# 안드로이드 악성 앱 탐지 프로젝트

### 해당 프로젝트는 [KC-ML2](https://www.kc-ml2.com/)에서 개최한 [CodeFest2020](https://blog.kc-ml2.com/codefest2020/)에 참가하여 진행한 내용입니다. 


## 서론

 ![image](https://user-images.githubusercontent.com/48518526/92185521-25322a00-ee8f-11ea-8f52-361ac14f6e20.png)

 스마트폰, 태블릿과 같은 모바일 기기가 대중화됨에 따라 모바일 기기 사용자들을 대상으로 개인정보 탈취, 저작권 침해 등 여러 보안 위협이 증가
최근 2019년 미국표준기술연구소(NIST)가 공개한 ‘국가취약점 데이터베이스(NVD)’를 보면 2019년 한해 가장 많은 보안 취약점이 발견된 운영체제는 구글 안드로이드로 총 414건이었다. 이처럼 많은 취약점 존재하기 때문에 다수 공격자들의 타겟이 될 가능성이 높다. 많은 안드로이드 사용자들이 공식적으로 검증되지 않은 악성 앱들을 블랙마켓 등 여러 불법 앱 마켓에서 다운받아 사용한다. 이에 따라, 본 프로젝트에서는 기하급수적으로 불어나는 안드로이드 악성 앱들에 대처하기 위해 머신러닝 기법을 이용한 악성 앱 탐지 시스템을 제안한다.

## 악성 앱 탐지 시스템 진행사항

* 악성 앱 데이터셋 

* 악성 행위에 사용되는 API 목록 생성

* 데이터셋 전처리 (CSV 파일 생성)

* 모델 생성

* 모델 검증 및 테스트

* 결론 및 한계점

## 데이터셋

* Androzoo (https://androzoo.uni.lu/)
 
  개수 : 19,453 개
  연도 : 2017년 ~ 2018년
  
  개수 : 5,501 개
  연도 : 2016년
  
  (https://androzoo.uni.lu/static/papers/androzoo-msr.pdf)

* AMD (http://amd.arguslab.org/)

  개수 : 19,453 개
  연도 : 2010년 ~ 2016년
  
* Drebin 
  
  개수 : 5,501 개
  연도 : 2010년 ~ 2012년
  
  (D. Arp, Michael Spreitzenbarth, Malte Hubner, Hugo Gascon, and Konrad Rieck (2014) "DREBIN: Effective and Explainable Detection of Android Malware in Your Pocket." NDSS Symposium 2014.)
  
## 추출 도구

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
  
    - 하지만 사용 빈도에 따른 feature selection은 과적합의 요인이 될 수 있다고 판단
    
      따라서, 2가지 데이터셋 생성
      
       1. '정제 전 API 목록'으로 생성한 데이터셋
       
       2. '정제 후 API 목록'으로 생성한 데이터셋
  
## 데이터셋 전처리
 * class
  
  1) training & validation set
   
    정상 앱 : Androzoo 19,453 apks
  
    악성 앱 : AMD 19,453 apks
  
  2) testing set
  
    정상 앱 : Androzoo 5,501 apks (중복 아님)
  
    악성 앱 : Drebin 5,501 apks

 1. '정제 전 API 목록'으로 생성한 데이터셋
 
   ![image](https://user-images.githubusercontent.com/48518526/92087244-3edb5f00-ee06-11ea-9ca4-dc4e8e1dc0e0.png)

 2. '정제 후 API 목록'으로 생성한 데이터셋
 
  ![image](https://user-images.githubusercontent.com/48518526/92083245-b0b0aa00-ee00-11ea-9cfa-bcc90cb69629.png)
  
## 모델 생성

  ![image](https://user-images.githubusercontent.com/48518526/92087648-b90be380-ee06-11ea-8e2a-18867786c076.png)
  
 * LightGBM
  
    RandomForest와 k-NN을 사용한 모델보다 LGBM이 더 뛰어난 성능을 보여줌
    
    ## Azure Machine Learning Studio 사용
   
   ![image](https://user-images.githubusercontent.com/48518526/92093475-5b7b9500-ee0e-11ea-8971-4aff36721d00.png)

    
 * 실제 모델 구현
 
  ![image](https://user-images.githubusercontent.com/48518526/92093297-253e1580-ee0e-11ea-9356-698e1fa74e96.png)

    
## 모델 검증 및 테스트

 * 모델 검증
  
  1.1) '정제 전 API 목록'으로 생성한 데이터셋
  
   ![image](https://user-images.githubusercontent.com/48518526/92185157-1434e900-ee8e-11ea-845e-8cba9d9a4842.png)
   ![image](https://user-images.githubusercontent.com/48518526/92185176-21ea6e80-ee8e-11ea-8b0e-47ebba4a1e8d.png)
  
  1.2) 정확도
  
   ![image](https://user-images.githubusercontent.com/48518526/92185193-2dd63080-ee8e-11ea-93a7-23499cdacd12.png)
 
  2. '정제 후 API 목록'으로 생성한 데이터셋
  
   ![image](https://user-images.githubusercontent.com/48518526/92185043-bef8d780-ee8d-11ea-81d2-dcec72889303.png)
   ![image](https://user-images.githubusercontent.com/48518526/92185068-cfa94d80-ee8d-11ea-8fb1-d3b35719f499.png)
  
  2.2) 정확도
    
   ![image](https://user-images.githubusercontent.com/48518526/92185086-dd5ed300-ee8d-11ea-96ba-48ee857743ec.png)

## 결론
  
  1. 정적으로 추출한 API들로도 높은 성능으로 악성 앱들을 구분 가능
  
  2. 특징정보를 축소시킨 경우에도 충분히 높은 성능을 보여줌
      - 데이터셋 크기 감소
      - 차원 축소로 인한 모델의 분류 속도 향상
  
## 한계점

  1. 동적 탐지보다 속도는 빠르지만 탐지에 한계
  
  2. 현재 가지고있는 데이터셋의 연도차에 대한 한계
  
  3. AMD와 Drebin 데이터셋이 판단하는 악성 앱의 기준이 다를 수 있음
