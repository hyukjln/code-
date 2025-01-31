# -*- coding: utf-8 -*-
"""202210688_안혁진_계산물리학 중요도 추출법.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ee57RcbtyIRIzFYjqNYcHqnTI9ou6ZQe

예제 5.3.1
"""

import math
import random as rd
import numpy as np

"""1번"""

import numpy as np
import numpy.random as rd

# g(x) 함수 정의
def g(x):
    return np.exp(-0.5 * x**2)

# 샘플 크기 설정
N = 10000

# [0, 10] 구간에서 균등 분포를 따르는 난수 생성
random_values = rd.uniform(0, 10, N)

# g(x) 함수에 난수 값을 입력하여 결과 계산
results = g(random_values)

# 결과의 평균 계산
average_result = np.mean(results)

# 평균 결과 출력
print(average_result)

"""2번

"""

import numpy as np
import numpy.random as rd

# g(x) 함수 정의
def g(x):
    return np.exp(-0.5 * x**2)

# 균등 분포의 확률 밀도 함수 정의
def p(x, a=0, b=10):
    return 1 / (b - a)

# q(x) 함수 정의
def q(x):
    return np.exp(-x) / (1 - np.exp(-10))

# 중요도 샘플링 가중치 함수 정의
def w(x, a=0, b=10):
    return p(x, a, b) / q(x)

# 샘플 크기 설정
N = 10000

# [0, 1] 구간에서 균등 분포를 따르는 난수 생성
u_values = rd.uniform(0, 1, N)

# 역변환 샘플링을 사용하여 x 값 생성
x_values = -np.log(1 - (1 - np.exp(-10)) * u_values)

# g(x) 함수에 난수 값을 입력하여 결과 계산
g_values = g(x_values)

# 중요도 샘플링 가중치 계산
w_values = w(x_values)

# 가중치를 적용한 g(x) 값의 평균 계산
result = np.sum(g_values * w_values) / N

# 결과 출력
print(result)

"""예제 5.3.2"""

import numpy as np
import numpy.random as rd

def g(x):
    if x > 3:
        return 1
    else:
        return 0

def p(x):
    return np.exp(-x**2 / 2) * (1 / np.sqrt(2 * np.pi))

def q(x, z=3):
    return np.exp(-(x - z)**2 / 2) * (1 / np.sqrt(2 * np.pi))

# 샘플 크기 설정
N = 10000

# q(x)에서 샘플링하여 x 값 생성
x_values = rd.normal(3, 1, N)

# 가중치 계산 및 결과 계산
w_values = np.array([g(x) * p(x) / q(x) for x in x_values])
average_result = np.mean(w_values)

print(average_result)

"""1번"""

import numpy as np

N = 10000
x = np.random.normal(0, 1, N)  # 평균 0, 표준편차 1인 정규 분포에서 N개의 샘플 생성
y = np.where(x > 3, 1, 0)  # x > 3인 경우 1, 그렇지 않으면 0으로 변환
result = np.sum(y) / N  # y의 평균 계산하여 기대값 추정

print(result)

"""2번"""

import numpy as np

N = 10000
x = np.random.normal(3, 1, N)  # 평균 3, 표준편차 1인 정규 분포에서 N개의 샘플 생성
g = np.where(x > 3, 1, 0)  # x > 3인 경우 1, 그렇지 않으면 0으로 변환
w = np.array(p(x) / q(x))  # p(x) / q(x)를 계산하여 가중치 배열 생성
result = np.sum(g * w) / N  # g * w의 합을 계산하여 평균을 구함

print(result)