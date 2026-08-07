# [level 2] 스킬트리 - 49993 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/49993) 

### 성능 요약

메모리: 11.4 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > Summer／Winter Coding（～2018）

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2026년 05월 29일 13:21:32

### 문제 설명

<p>선행 스킬이란 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 뜻합니다.</p>

<p>예를 들어 선행 스킬 순서가 <code>스파크 → 라이트닝 볼트 → 썬더</code>일때, 썬더를 배우려면 먼저 라이트닝 볼트를 배워야 하고, 라이트닝 볼트를 배우려면 먼저 스파크를 배워야 합니다.</p>

<p>위 순서에 없는 다른 스킬(힐링 등)은 순서에 상관없이 배울 수 있습니다. 따라서 <code>스파크 → 힐링 → 라이트닝 볼트 → 썬더</code>와 같은 스킬트리는 가능하지만, <code>썬더 → 스파크</code>나 <code>라이트닝 볼트 → 스파크 → 힐링 → 썬더</code>와 같은 스킬트리는 불가능합니다.</p>

<p>선행 스킬 순서 skill과 유저들이 만든 스킬트리<sup id="fnref1"><a href="#fn1">1</a></sup>를 담은 배열 skill_trees가 매개변수로 주어질 때, 가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.</p>

<h5>제한 조건</h5>

<ul>
<li>스킬은 알파벳 대문자로 표기하며, 모든 문자열은 알파벳 대문자로만 이루어져 있습니다.</li>
<li>스킬 순서와 스킬트리는 문자열로 표기합니다.

<ul>
<li>예를 들어, <code>C → B → D</code> 라면 "CBD"로 표기합니다</li>
</ul></li>
<li>선행 스킬 순서 skill의 길이는 1 이상 26 이하이며, 스킬은 중복해 주어지지 않습니다.</li>
<li>skill_trees는 길이 1 이상 20 이하인 배열입니다.</li>
<li>skill_trees의 원소는 스킬을 나타내는 문자열입니다.

<ul>
<li>skill_trees의 원소는 길이가 2 이상 26 이하인 문자열이며, 스킬이 중복해 주어지지 않습니다.</li>
</ul></li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>skill</th>
<th>skill_trees</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td><code>"CBD"</code></td>
<td><code>["BACDE", "CBADF", "AECB", "BDA"]</code></td>
<td>2</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<ul>
<li>"BACDE": B 스킬을 배우기 전에 C 스킬을 먼저 배워야 합니다. 불가능한 스킬트립니다.</li>
<li>"CBADF": 가능한 스킬트리입니다.</li>
<li>"AECB": 가능한 스킬트리입니다.</li>
<li>"BDA": B 스킬을 배우기 전에 C 스킬을 먼저 배워야 합니다. 불가능한 스킬트리입니다.</li>
</ul>

<div class="footnotes">
<hr>
<ol>

<li id="fn1">
<p>스킬 트리: 유저가 스킬을 배울 순서&nbsp;<a href="#fnref1">↩</a></p>
</li>

</ol>
</div>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

---

## 🔍 시행착오 및 해결 과정

### 1. `set()`에 대한 오해 (해시 테이블의 특징)
* **초기 접근:** 유저의 스킬트리와 선행 스킬의 교집합을 빠르게 구하기 위해 `set(list())` 구조를 고민했습니다.
* **배운 점:** `set` 자료형은 내부적으로 **해시 테이블(Hash Table)** 구조를 사용하는 **순서가 없는(Unordered) 자료형**입니다. 원소가 적을 때 가끔 알파벳 순서대로 정렬된 것처럼 보이는 것은 단순한 우연일 뿐이며 정렬을 보장하지 않습니다. 순서 유지가 핵심인 이 문제에서는 `set`을 사용하면 데이터가 꼬이게 됩니다.

### 2. `in` 연산자의 한계와 잘못된 카운트 문제
* **추출 방식:** 유저의 스킬트리에서 선행 스킬에 포함된 글자들만 순서대로 뽑아 문자열 `f`를 만들었습니다.
* **문제 발생:** 추출된 스킬 순서가 올바른지 판별하기 위해 `if f in skill:` 조건을 썼더니, `"BD"`와 같은 잘못된 순서가 필터링되지 않고 통과했습니다. `"BD"`는 원래 스킬인 `"CBD"`의 **부분 문자열(Substring)** 이기 때문에 `in` 연산자가 `True`를 반환하는 논리적 오류가 있었습니다. (실제로는 `C`를 배우지 않고 `B`와 `D`를 배운 것이므로 탈락해야 합니다.)

---

## 💡 해결 방법: 접두사(Prefix) 매칭과 `startswith()`

스킬트리가 성립하려면 추출한 문자열이 원래 `skill` 문자열의 **앞부분부터 순서대로 빈틈없이 일치(접두사)**해야 합니다. 
예를 들어 `skill`이 `"CBD"`일 때, 가능한 조합은 `""`, `"C"`, `"CB"`, `"CBD"` 뿐입니다.

이를 해결하기 위해 원래 `skill` 문자열이 내가 추출한 문자열(`f`)로 시작하는지 검사하는 방식을 적용했습니다.

### 💻 최종 제출 코드
```python
def solution(skill, skill_trees):
    answer = 0
    tmp_list = list(skill)
    filter_list = []
    
    # 1. 유저 스킬트리에서 선행 스킬(skill)에 포함된 문자만 순서대로 추출
    for skill_tree in skill_trees:
        tmp_s = ''
        for s in skill_tree:
            if s in tmp_list:
                tmp_s += s
        filter_list.append(tmp_s)
        
    # 2. skill이 추출된 스킬 순서(f)로 시작하는지 접두사 검사
    for f in filter_list:
        if skill.startswith(f):
            answer += 1
            
    return answer
