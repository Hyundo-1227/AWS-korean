# AGENTS.md

## Cursor Cloud specific instructions

### What this repository is
This is a **content-only** repository: 12 Korean-language AWS Certified Cloud
Practitioner practice exams (`practice-exam-1-ko.md` … `practice-exam-12-ko.md`).
Each file is Markdown with Jekyll `layout: exam` front matter and multiple-choice
questions whose answers are hidden inside collapsible
`<details markdown=1><summary>Answer</summary> Correct answer: X </details>` blocks.

There is **no application code, no build system, and no test/lint suite** in this
repo. The files are designed to be dropped into an external Jekyll site (the
upstream `AWS-Certified-Cloud-Practitioner-Notes` project) that provides the
`exam` layout. That Jekyll scaffolding is not part of this repo.

### Previewing the content (the closest thing to "running the app")
A self-contained preview server is committed at `preview.py`. It renders every
`practice-exam-*-ko.md` file into interactive HTML (collapsible answer toggles +
per-exam nav) using the Python `markdown` library, without needing Jekyll/Ruby.

```bash
python3 preview.py            # serves all 12 exams on http://localhost:8080/0
PORT=9000 python3 preview.py  # custom port
```

Exam index is 0-based (`/0` = 연습 시험 1). The only dependency is the Python
`markdown` package (installed by the startup update script). `preview.py` is a
dev/preview convenience tool only — it is **not** the source of truth; the
Markdown files are.

### Editing content
- Keep the `---\nlayout: exam\n---` front matter at the top of each file intact.
- Preserve the `<details markdown=1>` answer blocks and their indentation so the
  `md_in_html` extension (and the upstream Jekyll/Kramdown renderer) keeps
  treating them as collapsible answers.
