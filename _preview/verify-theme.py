"""Verify remote-theme output against site-owned source and allowed static files."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Document(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.elements = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('output', type=Path)
parser.add_argument('--baseurl', default='')
args = parser.parse_args()
root = Path(__file__).resolve().parent.parent
output = args.output.resolve()
base = args.baseurl.rstrip('/')
failures = []


def check(condition, message):
    if not condition:
        failures.append(message)


pages = [root / 'index.md', *sorted((root / 'albiononline').rglob('index.md'))]
expected = set()
for source in pages:
    rel = source.relative_to(root).with_suffix('.html')
    expected.add(rel.as_posix())
    target = output / rel
    check(target.is_file(), f'Missing page: {rel}')
    if not target.is_file():
        continue
    html = target.read_text()
    doc = Document(html)
    check('layout: default' in source.read_text().split('---')[1], f'Unexpected source layout: {source}')
    check(' • Epoiisa</title>' in html, f'Missing branding: {rel}')
    check('Gaming tools, mechanics, builds and guides by Epoiisa.' in html, f'Missing description: {rel}')
    check(any(tag == 'a' and attrs.get('class') == 'site-title' and attrs.get('href') == base + '/' for tag, attrs in doc.elements), f'Incorrect home URL: {rel}')
    check(any(tag == 'nav' and attrs.get('aria-label') == 'Breadcrumb' for tag, attrs in doc.elements), f'Missing breadcrumbs: {rel}')
    check('aria-current="page"' in html, f'Missing current breadcrumb: {rel}')
    check('Join me in <a href="https://discord.gg/j7EJgJ3D5M">Frostborn Exiles</a> on the Asia server.' in html, f'Missing invitation: {rel}')
    for tag, key, resource in [('link', 'href', '/assets/css/style.css'), ('link', 'href', '/assets/css/guild-invite.css'), ('script', 'src', '/assets/js/guild-invite.js')]:
        check(any(t == tag and urlsplit(a.get(key, '')).path == base + resource for t, a in doc.elements), f'Missing resource {resource}: {rel}')
    for tag, attrs in doc.elements:
        for key in ('href', 'src'):
            raw = attrs.get(key)
            if not raw:
                continue
            url = urlsplit(raw)
            if url.scheme or url.netloc or not url.path:
                continue
            path = unquote(url.path)
            if path.startswith('/'):
                check(not base or path.startswith(base + '/'), f'URL ignores baseurl: {rel}: {raw}')
                resolved = output / path.removeprefix(base).lstrip('/')
            else:
                resolved = target.parent / path
            if path.endswith('/') or resolved.is_dir():
                resolved = resolved / 'index.html'
            check(resolved.is_file(), f'Broken local link/resource: {rel}: {raw}')

# Only content assets and the central stylesheet should be published.
for directory in ('albiononline', 'assets'):
    for source in (root / directory).rglob('*'):
        if source.is_file() and source.suffix != '.md' and not source.name.startswith('.'):
            expected.add(source.relative_to(root).as_posix())
expected.add('assets/css/style.css')
actual = {p.relative_to(output).as_posix() for p in output.rglob('*') if p.is_file()}
check(actual == expected, f'Published inventory differs: extra={sorted(actual - expected)}, missing={sorted(expected - actual)}')
check(not (root / '_layouts/default.html').exists(), 'Local layout overrides theme')
check(not (root / '_includes/breadcrumbs.html').exists(), 'Local breadcrumbs override theme')
check(not (root / 'assets/css/style.css').exists(), 'Local stylesheet overrides theme')
if failures:
    raise SystemExit('\n'.join(failures))
print(f'Verified {len(pages)} pages and {len(actual)} published files (baseurl={base!r}).')
