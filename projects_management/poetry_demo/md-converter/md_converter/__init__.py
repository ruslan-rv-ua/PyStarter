import click
from pathlib import Path
from markdown_it_pyrs.markdown_it_pyrs import MarkdownIt

TEMPLATE_PATH = Path(__file__).parent / "template.html"
TEMPLATE = TEMPLATE_PATH.read_text(encoding="utf-8")

def convert_md_to_html_document(text: str, title: str, lang: str | None = None) -> str:
    md = MarkdownIt("gfm")
    pure_html = md.render(text)
    html = TEMPLATE.format(title=title, content=content, lang=lang)
    return html


@click.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--title", type=str, help="Title of the document", default=None)
@click.option("--lang", type=str, help="Language of the document", default=None)
def convert(file: str | Path, title: str | None = None, lang: str | None = None) -> int:
    """Convert markdown file to html file"""
    file = Path(file)
    title = title or file.stem
    lang = lang or "en"
    html = convert_md_file(file)
    output_file = file.with_suffix(".html")
    output_file.write_text(html, encoding="utf-8")
    click.echo(f"Converted {file} to {output_file}")
    return 0
