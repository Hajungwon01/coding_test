# 펭귄 조사하기

## 📝 문제 설명
Palmer Penguins 데이터베이스를 활용하여 각 서식지(`island`)에 살고 있는 펭귄의 종(`species`)을 조사합니다. 데이터 중복을 제거하고, 요청한 정렬 기준에 맞춰 결과를 출력하는 문제입니다.

## 🎯 요구 사항
- **중복 제거**: 각 서식지에 대해 동일한 종이 여러 번 나오지 않도록 합니다.
- **출력 컬럼**:
    - `species`: 펭귄의 종
    - `island`: 펭귄 서식지
- **정렬 조건**:
    1. 서식지(`island`) 기준 오름차순 정렬
    2. 서식지가 같을 경우, 펭귄 종(`species`) 기준 오름차순 정렬

## 💡 해결 방법 (SQL)
```sql
select DISTINCT(species), island
from penguins
ORDER BY island, species;