# [level 1] 신고 결과 받기 - 92334

> 🤖 **이 문제는 AI를 참고하여 풀었습니다.**

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/92334)

### 성능 요약

메모리: 38.7 MB, 시간: 110.70 ms

### 구분

코딩테스트 연습 > 2022 KAKAO BLIND RECRUITMENT

### 채점결과

정확성: 100.0  
합계: 100.0 / 100.0

### 제출 일자

2026년 05월 25일 12:33:25

---

## 문제 설명

신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다.

- 각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
- 한 유저를 여러 번 신고해도 **신고 횟수는 1회**로 처리됩니다.
- k번 이상 신고된 유저는 이용이 정지되며, 신고한 모든 유저에게 메일이 발송됩니다.

### 입출력 예

| id_list | report | k | result |
|---------|--------|---|--------|
| `["muzi", "frodo", "apeach", "neo"]` | `["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]` | 2 | [2,1,1,0] |
| `["con", "ryan"]` | `["ryan con", "ryan con", "ryan con", "ryan con"]` | 3 | [0,0] |

---

## ✅ 제출 코드

```python
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    id_dict = {id: i for i, id in enumerate(id_list)}
    
    # 중복 제거가 핵심!
    report = list(set(report))
    
    # 피신고자: {신고당한 횟수, 신고한 사람 목록}
    reported_count = {}   # 피신고자별 신고 횟수
    report_by = {}        # 신고자별 신고한 피신고자 목록
    for r in report:
        user1, user2 = r.split(' ')  # user1이 user2를 신고
        reported_count[user2] = reported_count.get(user2, 0) + 1
        if user1 not in report_by:
            report_by[user1] = []
        report_by[user1].append(user2)
    for reporter, reported_list in report_by.items():
        for reported in reported_list:
            if reported_count.get(reported, 0) >= k:
                answer[id_dict[reporter]] += 1
    return answer
```

---

## 💡 핵심 풀이 포인트

### 1. 유저 인덱스 매핑 — 딕셔너리 컴프리헨션

`answer` 배열은 `id_list` 순서 그대로 결과를 담아야 합니다.  
유저 이름 → 인덱스 번호로 바로 접근할 수 있도록 딕셔너리를 미리 만듭니다.

```python
id_dict = {id: i for i, id in enumerate(id_list)}
# {"muzi": 0, "frodo": 1, "apeach": 2, "neo": 3}
```

### 2. 중복 신고 제거 — `set` 활용

같은 유저가 같은 사람을 여러 번 신고해도 1회로 처리해야 합니다.  
`set`으로 변환하면 `"ryan con"`이 4번 들어와도 1번만 남습니다.

```python
report = list(set(report))
```

### 3. 두 개의 딕셔너리로 정보 분리

| 딕셔너리 | 키 | 값 | 역할 |
|----------|----|----|------|
| `reported_count` | 피신고자 ID | 신고당한 횟수 | k 이상인지 판단 |
| `report_by` | 신고자 ID | 신고한 사람 목록 | 메일 수 계산 |

```python
reported_count[user2] = reported_count.get(user2, 0) + 1
```

`dict.get(key, 0)`은 키가 없을 때 0을 반환해 `KeyError` 없이 카운팅할 수 있습니다.

### 4. 메일 수 계산

신고자별로 신고한 사람 목록을 순회하면서,  
그 사람의 신고 횟수가 k 이상이면 해당 신고자의 메일 수를 +1 합니다.

```python
for reporter, reported_list in report_by.items():
    for reported in reported_list:
        if reported_count.get(reported, 0) >= k:
            answer[id_dict[reporter]] += 1
```

---

## 🔍 동작 과정 예시

입력: `id_list = ["muzi", "frodo", "apeach", "neo"]`, `k = 2`  
`report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]`

**① 중복 제거 후 신고 횟수 집계**

| 신고당한 유저 | 신고 횟수 | 정지 여부 (k=2) |
|--------------|-----------|-----------------|
| frodo | 2 | ✅ 정지 |
| neo | 2 | ✅ 정지 |
| muzi | 1 | ❌ |

**② 각 유저가 받는 메일 수**

| 유저 | 신고한 사람 | 정지된 사람 | 메일 수 |
|------|------------|------------|---------|
| muzi | frodo, neo | frodo, neo | **2** |
| frodo | neo | neo | **1** |
| apeach | frodo, muzi | frodo | **1** |
| neo | 없음 | 없음 | **0** |

→ 최종 결과: `[2, 1, 1, 0]` ✅

---

## 📌 사용한 파이썬 문법 정리

### 딕셔너리 컴프리헨션

```python
id_dict = {id: i for i, id in enumerate(id_list)}
# enumerate: (인덱스, 값) 쌍으로 순회
```

### `dict.get(key, default)`

키가 없을 때 `KeyError` 대신 기본값을 반환합니다.

```python
d = {}
d['a'] = d.get('a', 0) + 1  # {'a': 1}  — KeyError 없이 카운팅 가능
```

### `set`을 이용한 중복 제거

```python
lst = ["a b", "a b", "c d"]
lst = list(set(lst))   # ["a b", "c d"] — 순서는 보장 안 됨
```

### `str.split()`

```python
user1, user2 = "muzi frodo".split(' ')  # user1="muzi", user2="frodo"
```
