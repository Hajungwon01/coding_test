# SQL 코딩 테스트: 크리스마스 게임 찾기

## 📝 문제 설명
Video Game Sales with Ratings 데이터베이스에서 조카와 함께 즐길 수 있는 크리스마스 테마의 게임을 찾는 문제입니다. `games` 테이블에서 게임 이름에 **"Christmas"** 또는 **"Santa"**가 포함된 데이터를 추출합니다.

## 🎯 요구 사항
- **대상 테이블**: `games`
- **필터 조건**: `name` 컬럼에 "Christmas" 혹은 "Santa"가 포함된 경우
- **출력 컬럼**:
    - `game_id`: 게임 ID
    - `name`: 게임 이름
    - `year`: 발매 연도

## 💡 해결 방법 (SQL)
```sql
SELECT 
    game_id, 
    name, 
    year
FROM 
    games
WHERE 
    name LIKE '%Christmas%' 
    OR name LIKE '%Santa%';
