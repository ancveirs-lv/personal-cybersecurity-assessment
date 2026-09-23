# Personal Cybersecurity Self-Assessment

[Latviski](README.lv.md) · **English**

**24-item bilingual self-assessment · global English baseline · Latvian edition**

This is practical self-assessment guidance, not a guarantee of safety, legal advice or a substitute for incident-response support.

This repository is a **gap-to-action instrument**, not a quiz that declares a person or organisation “safe” from one overall score.

## Model

`framework → domain → question → response state → gap → recommended action → reassessment`

## Response model

`UNKNOWN → NOT_IN_PLACE → PARTIAL → CONSISTENT → VERIFIED`

Unknown areas remain visible. The project intentionally does **not** produce a single overall safety, compliance or maturity score.

## Quick start

```bash
python3 scripts/validate.py
python3 scripts/render.py --check
python3 -m unittest discover -s tests -v
python3 scripts/assess.py examples/answers.example.json
```

No assessment answers are transmitted by the repository tooling.

## Structure

- `data/assessment.en.json` — canonical global English assessment;
- `data/assessment.lv.json` — Latvian edition;
- `data/sources.json` — official source registry;
- `docs/` — deterministically generated questionnaires;
- `scripts/assess.py` — local gap/action report generator;
- `scripts/validate.py` and `scripts/render.py` — validation contracts;
- `tests/` — regression tests.

## Sources and adaptation

Assessment items are original project wording informed by registered sources. References indicate alignment or rationale, not official source wording or endorsement.

## Version status

`v0.1.0` is a **pilot baseline** for review and calibration before a stable 1.0 release.

## Author

**Zigmārs Ancveirs** — technology leader, software engineer and independent cybersecurity researcher.

## Licence

Documentation and assessment data: **CC BY 4.0**. Code and automation: **MIT**.
