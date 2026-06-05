# 🎮 게임을 10개 이상 발매한 게임 배급사 찾기

## 📌 문제 정보
- **플랫폼**: [solvesql](https://solvesql.com/problems/publisher-with-many-games/)
- **난이도**: 2
- **카테고리**: SQL 기초, 집계 함수, 서브쿼리

## 💡 문제 설명
'Video Game Sales with Ratings' 데이터베이스에서 게임 배급사로 참여한 게임이 10개 이상인 회사의 이름을 찾아야 합니다.

## 🔑 정답 쿼리
```sql
SELECT 
    name
FROM 
    companies
WHERE 
    company_id IN (
        SELECT 
            publisher_id
        FROM 
            games
        GROUP BY 
            publisher_id
        HAVING 
            COUNT(game_id) >= 10
    );
```

## 📝 배운 점 & 팁
GROUP BY와 HAVING을 사용하여 특정 조건(10개 이상)을 만족하는 그룹을 필터링하는 방법을 복습했습니다.

서브쿼리를 사용하여 games 테이블에서 조건에 맞는 publisher_id를 먼저 추출한 뒤, 이를 companies 테이블과 연결하는 방식을 사용했습니다.