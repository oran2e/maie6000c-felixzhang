# Week 03 Readiness Lab Submission

## 1. What I Changed
- Extended `LABEL_KEYWORDS` in `services/ai/app/main.py` under the `"incident"` label to include the `"timeout"` keyword.
- Added a corresponding unit test `test_triage_text_timeout_keyword` in `tests/unit/test_ai_timeout.py`.

## 2. How I Verified It
- Rebuilt API image with `docker compose build --no-cache api`.
- Executed containerized unit tests via `docker compose run --rm --no-deps api pytest -q tests/unit`.
- Confirmed all unit tests passed successfully without regressions.
