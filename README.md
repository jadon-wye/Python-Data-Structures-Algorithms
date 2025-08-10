# Python Data Structures & Algorithms

이 저장소는 **파이썬 자료구조 직접 구현**과 **알고리즘 문제 풀이**를 통해  
CS 기초와 코딩 실력을 동시에 향상시키기 위한 개인 학습 프로젝트입니다.

---

## 폴더 구조
```plaintext
project_root/
├── src/
│   ├── algorithms/  # 내장 자료구조 활용 문제 풀이
│   │   ├── __init__.py
│   │   ├── bin_array_sort.py
│   │   ├── find_max_two.py
│   │   ├── find_sub_array.py
│   │   └── is_palindrome.py
│   └── data_structures/  # 자료구조 직접 구현
│       └── __init__.py
├── tests/  # pytest 테스트 파일
│   ├── test_bin_array_sort.py
│   ├── test_find_max_two.py
│   ├── test_find_sub_array.py
│   └── test_is_palindrome.py
└── pyproject.toml # pytest 설정
```
---

## 개발 환경
- Python 3.11+
- 가상환경: `venv`
- 테스트: `pytest`

---

## 설치 및 실행
```bash
# 가상환경 생성 및 활성화
python -m venv .venv
# Windows
.venv\Scripts\activate

# 의존성 설치
python -m pip install -U pip pytest

# 테스트 실행
pytest -q
```
## 학습 진행 방식
- Notion 로드맵 DB로 주차별 목표 관리
- 주차별 브랜치(feature/weekX-topic)에서 작업 → PR → main 병합
- 주차 완료 시 태그(v0.X-weekX) 생성

## 라이선스
- 이 프로젝트는 학습용이며, 별도의 라이선스 제약 없이 사용 가능합니다
