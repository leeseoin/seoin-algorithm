---
name: review-pr
description: GitHub PR을 리뷰하고 gh CLI로 코멘트를 남깁니다. 사용법 /review-pr [PR-NUMBER]
---

# GitHub PR 코드 리뷰

PR #$ARGUMENTS 를 리뷰하고 GitHub에 코멘트를 남긴다.

## 절차

1. **PR 정보 수집**
   ```bash
   gh pr view $ARGUMENTS
   gh pr diff $ARGUMENTS
   gh pr diff $ARGUMENTS --name-only
   ```

2. **코드 분석** — 변경된 파일의 diff를 읽고 다음을 확인:
   - 논리 오류, 버그
   - 보안 취약점 (인젝션, XSS, 인증 우회 등)
   - 에러 핸들링 누락
   - 성능 문제
   - 코드 스타일 / 일관성
   - 필요시 변경된 파일의 전체 코드도 Read로 확인

3. **리뷰 코멘트 작성** — 발견 사항을 정리하여 `gh pr comment`로 게시:
   ```bash
   gh pr comment $ARGUMENTS --body "리뷰 내용"
   ```

## 리뷰 포맷

```markdown
## Code Review

### 발견 사항

| # | 심각도 | 파일 | 내용 |
|---|--------|------|------|
| 1 | ... | ... | ... |

심각도 기준:
- 🔴 Bug: 반드시 수정 필요
- 🟡 Nit: 사소하지만 개선 권장
- 🟢 Good: 잘 된 부분

### 총평

(전체적인 코드 품질 평가 및 권장 사항)

---
🤖 Reviewed by Claude Code
```

## 주의사항

- PR을 승인(approve)하거나 차단(request changes)하지 않는다. 코멘트만 남긴다.
- CLAUDE.md의 프로젝트 컨벤션을 참고한다.
- 사용자가 단 주석은 삭제 제안하지 않는다.
