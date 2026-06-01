# 🚲 지자체별 따릉이 정류소 개수 세기

[solvesql](https://solvesql.com/problems/count-stations/)의 '지자체별 따릉이 정류소 개수 세기' 문제 해결을 위한 SQL 쿼리입니다.

## 📝 문제 설명
`station` 테이블을 활용하여 소속 지자체(`local`)별 따릉이 정류소의 개수를 집계하는 문제입니다.

## 🎯 요구 사항
* **출력 컬럼:**
    * `local`: 소속 지자체
    * `num_stations`: 해당 지자체에 소속된 정류소 개수
* **정렬 조건:** `num_stations` 기준 오름차순 정렬

## 💡 해결 방법 (SQL)
```sql
select local, count(station_id) as num_stations
from station
group by local
ORDER by num_stations;