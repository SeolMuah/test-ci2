# Day 4 Mission

## 환경 설정

```bash
# 의존성 설치 (개발 도구 포함)
uv sync --extra dev

# Pre-commit 훅 설치
uv run pre-commit install

# 환경변수 설정
cp .env.example .env
```

## 실행

```bash
# 테스트 실행
uv run pytest tests/ -v

# 린트 검사
uv run ruff check app/ tests/

# Pre-commit 전체 실행
uv run pre-commit run --all-files
```

## 미션

### 1. `.github/workflows/ci.yml` - CI 파이프라인 구축

| TODO | 내용 |
|------|------|
| TODO 1 | 트리거 이벤트 설정 (main 브랜치 push/PR) |
| TODO 2 | lint job 작성 |
| TODO 3 | test job 작성 |
