---
name: update-docs
description: CLAUDE.md, TODO.md, DALY_REPORTS.md 문서를 업데이트합니다. 사용법 /update-docs [claude|daily|todo]
---

# 문서 업데이트

$ARGUMENTS 섹션을 업데이트한다.

## 명령어

### claude
1. 현재 대화에서 수행한 작업 내용을 파악
2. `CLAUDE.md`의 "현재 진행 상황" 섹션에 항목 추가
3. 형식: `- **작업명** (YYYY-MM-DD): 설명`
4. 프로젝트 구조가 변경되었으면 해당 섹션도 업데이트
5. docs/ 디렉토리에 새 문서가 추가되었으면 인덱스 업데이트

### daily
1. 현재 대화에서 수행한 작업을 요약
2. `docs/DALY_REPORTS.md`에 추가
3. 형식:
```
## YYYY-MM-DD

### 작업 내용
- 항목 1
- 항목 2

### 결과
- 결과 요약

### 다음 계획
- 다음에 할 것
```

### todo
1. `docs/TODO.md` 읽기
2. 완료된 항목은 체크 처리 (`- [x]`)
3. 새로운 할 일이 있으면 추가
4. 변경 내용 요약 출력

## 주의사항
- 날짜는 항상 YYYY-MM-DD 형식
- CLAUDE.md는 프로젝트 루트에 위치
- 기존 내용을 삭제하지 말고 추가만 할 것
- docs/ 경로: /Users/iseoin/SpringBoot_project/webrtc/docs/
