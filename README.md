# 중고차 가격예측 선형회귀모델

## 개요
코로나로 인한 공급망 사태로 인해 새로운 자동차 공급이 차질이 빚어지고 있다. 이에 따라 중고차 가격이 급증하는 현상이 발생하였다.  
그렇다면 중고차 가격을 예측하는 시스템을 만들 수 있지 않을까?

## 개발환경
  1. 개발언어
  - Python3
  2. 개발 어플리케이션
  - GoogleColab, jupyter
  - VSCode
  3. 기술 스택
  - ML : sklearn, pandas, pycaret
  - Web : flask
  - Crawling : Selenium
 
 ## 개발 순서 개요
 1. Selenium을 이용해서 엔카(http://www.encar.com/) 에서 데이터 수집
 2. pycaret 회귀모델 이용해서 가격 예측 알고리즘 생성
 3. flask를 이용하여 웹 어플리케이션 구현
