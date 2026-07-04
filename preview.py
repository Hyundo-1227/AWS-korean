#!/usr/bin/env python3
"""Local preview server for the AWS-korean practice-exam markdown content.

This repository is content-only: 12 Korean-language AWS Certified Cloud
Practitioner practice exams written in Markdown with Jekyll `layout: exam`
front matter and collapsible <details> answer blocks.

This helper renders each `practice-exam-*-ko.md` file into an interactive HTML
page (mirroring the intended `exam` layout) so the content can be previewed
locally without the external Jekyll site.

Usage:
    pip install --break-system-packages markdown   # one-time dependency
    python3 preview.py                              # serves on :8080
    PORT=9000 python3 preview.py                    # custom port

Then open http://localhost:8080/0 (exam index is 0-based).
"""
import glob
import html
import os
import re
from http.server import BaseHTTPRequestHandler, HTTPServer

import markdown

REPO = os.environ.get("REPO_DIR", os.path.dirname(os.path.abspath(__file__)))

FRONT_MATTER = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)

PAGE = """<!doctype html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
 body{{font-family:-apple-system,Segoe UI,Roboto,'Noto Sans KR',sans-serif;max-width:900px;margin:0 auto;padding:24px;line-height:1.6;color:#1a1a1a}}
 nav{{margin-bottom:24px}} nav a{{margin-right:8px}}
 ol>li{{margin:14px 0}} ul{{margin:6px 0}}
 details{{background:#f2f7ff;border:1px solid #b9d3ff;border-radius:6px;padding:8px 12px;margin:8px 0}}
 summary{{cursor:pointer;font-weight:600;color:#0a58ca}}
 h1{{border-bottom:2px solid #eee;padding-bottom:8px}}
</style></head><body>
<nav>{nav}</nav>
{body}
</body></html>"""


def list_exams():
    return sorted(
        glob.glob(os.path.join(REPO, "practice-exam-*-ko.md")),
        key=lambda p: int(re.search(r"exam-(\d+)-", p).group(1)),
    )


def render(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    text = FRONT_MATTER.sub("", text)
    md = markdown.Markdown(
        extensions=["md_in_html", "attr_list", "tables", "fenced_code"]
    )
    return md.convert(text)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_GET(self):
        files = list_exams()
        if not files:
            self.send_error(404, "No practice-exam-*-ko.md files found")
            return
        nav = " ".join(
            f'<a href="/{i}">시험 {re.search(r"exam-(\d+)-", os.path.basename(f)).group(1)}</a>'
            for i, f in enumerate(files)
        )
        m = re.match(r"/(\d+)", self.path)
        idx = int(m.group(1)) if m else 0
        idx = max(0, min(idx, len(files) - 1))
        page = PAGE.format(
            title=html.escape(os.path.basename(files[idx])),
            nav=nav,
            body=render(files[idx]),
        )
        data = page.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    print(f"Serving {len(list_exams())} exams from {REPO} on http://0.0.0.0:{port}")
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()
