#!/usr/bin/env python3
"""Render one or more Markdown course scripts as polished PDFs.

This intentionally supports the Markdown subset used by criar-ementa-curso:
headings, paragraphs, blockquotes, lists, checkboxes, fenced code and pipe tables.
"""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

try:
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import (
        CondPageBreak,
        HRFlowable,
        Paragraph,
        Preformatted,
        SimpleDocTemplate,
        Spacer,
        Table,
        TableStyle,
    )
except ModuleNotFoundError as exc:
    raise SystemExit(
        "Dependencia ausente: reportlab. Use o Python retornado por "
        "load_workspace_dependencies para gerar os PDFs."
    ) from exc


EMOJI_LABELS = {
    "🔑": "[Regra]",
    "💡": "[Dica]",
    "⚠️": "[Atenção]",
    "⚠": "[Atenção]",
    "📌": "[Nota]",
    "🤓": "[Detalhe]",
    "🎯": "[Objetivo]",
    "🧰": "[Recursos]",
    "👐": "[Prática]",
    "✅": "[Verificação]",
    "🚑": "[Se travar]",
    "🚀": "[Desafio]",
    "🏁": "[Ponto de controle]",
}


def normalize_text(value: str) -> str:
    for emoji, label in EMOJI_LABELS.items():
        value = value.replace(emoji, label)
    return (
        value.replace("\u2010", "-")
        .replace("\u2011", "-")
        .replace("\u2012", "-")
        .replace("\u2013", "-")
        .replace("\u2014", "-")
    )


def find_font_set() -> tuple[str, str, str, str]:
    candidates = [
        (
            Path("C:/Windows/Fonts/arial.ttf"),
            Path("C:/Windows/Fonts/arialbd.ttf"),
            Path("C:/Windows/Fonts/ariali.ttf"),
            Path("C:/Windows/Fonts/arialbi.ttf"),
        ),
        (
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf"),
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf"),
        ),
    ]
    for regular, bold, italic, bold_italic in candidates:
        if all(path.exists() for path in (regular, bold, italic, bold_italic)):
            names = ("CourseSans", "CourseSans-Bold", "CourseSans-Italic", "CourseSans-BoldItalic")
            for name, path in zip(names, (regular, bold, italic, bold_italic)):
                if name not in pdfmetrics.getRegisteredFontNames():
                    pdfmetrics.registerFont(TTFont(name, str(path)))
            pdfmetrics.registerFontFamily(
                "CourseSans",
                normal=names[0],
                bold=names[1],
                italic=names[2],
                boldItalic=names[3],
            )
            return names
    return ("Helvetica", "Helvetica-Bold", "Helvetica-Oblique", "Helvetica-BoldOblique")


def inline_markup(text: str) -> str:
    text = normalize_text(text.strip())
    code_values: list[str] = []

    def keep_code(match: re.Match[str]) -> str:
        code_values.append(match.group(1))
        return f"@@CODE{len(code_values) - 1}@@"

    text = re.sub(r"`([^`]+)`", keep_code, text)
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)
    for index, value in enumerate(code_values):
        replacement = f'<font name="Courier">{html.escape(normalize_text(value))}</font>'
        text = text.replace(f"@@CODE{index}@@", replacement)
    return text


def build_styles(fonts: tuple[str, str, str, str]) -> dict[str, ParagraphStyle]:
    regular, bold, italic, _ = fonts
    sample = getSampleStyleSheet()
    body = ParagraphStyle(
        "CourseBody",
        parent=sample["BodyText"],
        fontName=regular,
        fontSize=9.3,
        leading=13.2,
        textColor=colors.HexColor("#243142"),
        spaceAfter=3.5 * mm,
        alignment=TA_LEFT,
    )
    return {
        "body": body,
        "title": ParagraphStyle(
            "CourseTitle",
            parent=body,
            fontName=bold,
            fontSize=23,
            leading=28,
            textColor=colors.HexColor("#153A5B"),
            alignment=TA_LEFT,
            spaceAfter=8 * mm,
            keepWithNext=True,
        ),
        "h2": ParagraphStyle(
            "CourseH2",
            parent=body,
            fontName=bold,
            fontSize=15,
            leading=19,
            textColor=colors.HexColor("#0E7490"),
            spaceBefore=5 * mm,
            spaceAfter=3 * mm,
            keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "CourseH3",
            parent=body,
            fontName=bold,
            fontSize=11.5,
            leading=15,
            textColor=colors.HexColor("#245C73"),
            spaceBefore=3 * mm,
            spaceAfter=2 * mm,
            keepWithNext=True,
        ),
        "h4": ParagraphStyle(
            "CourseH4",
            parent=body,
            fontName=bold,
            fontSize=9.8,
            leading=13,
            textColor=colors.HexColor("#384B5C"),
            spaceBefore=2 * mm,
            spaceAfter=1.5 * mm,
            keepWithNext=True,
        ),
        "quote": ParagraphStyle(
            "CourseQuote",
            parent=body,
            fontName=italic,
            fontSize=8.7,
            leading=12.3,
            textColor=colors.HexColor("#334155"),
            leftIndent=6 * mm,
            rightIndent=3 * mm,
            borderColor=colors.HexColor("#38BDF8"),
            borderWidth=1.2,
            borderPadding=(2 * mm, 3 * mm, 2 * mm, 3 * mm),
            backColor=colors.HexColor("#F0F9FF"),
            spaceBefore=1.5 * mm,
            spaceAfter=3.5 * mm,
        ),
        "list": ParagraphStyle(
            "CourseList",
            parent=body,
            leftIndent=8 * mm,
            firstLineIndent=-4 * mm,
            spaceAfter=1.5 * mm,
        ),
        "code": ParagraphStyle(
            "CourseCode",
            parent=body,
            fontName="Courier",
            fontSize=7.6,
            leading=10.2,
            leftIndent=4 * mm,
            rightIndent=2 * mm,
            borderColor=colors.HexColor("#CBD5E1"),
            borderWidth=0.5,
            borderPadding=3 * mm,
            backColor=colors.HexColor("#F8FAFC"),
            spaceAfter=3.5 * mm,
        ),
        "table": ParagraphStyle(
            "CourseTable",
            parent=body,
            fontSize=7.4,
            leading=9.5,
            spaceAfter=0,
        ),
        "table_header": ParagraphStyle(
            "CourseTableHeader",
            parent=body,
            fontName=bold,
            textColor=colors.white,
            fontSize=7.4,
            leading=9.5,
            spaceAfter=0,
        ),
        "footer": ParagraphStyle(
            "CourseFooter",
            parent=body,
            fontSize=7.5,
            leading=9,
            textColor=colors.HexColor("#64748B"),
            alignment=TA_CENTER,
        ),
    }


def is_table_separator(line: str) -> bool:
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def parse_table(lines: list[str], styles: dict[str, ParagraphStyle], width: float) -> Table:
    rows = [[cell.strip() for cell in line.strip().strip("|").split("|")] for line in lines]
    if len(rows) > 1 and is_table_separator(lines[1]):
        rows.pop(1)
    max_cols = max(len(row) for row in rows)
    for row in rows:
        row.extend([""] * (max_cols - len(row)))
    rendered = []
    for row_index, row in enumerate(rows):
        style = styles["table_header"] if row_index == 0 else styles["table"]
        rendered.append([Paragraph(inline_markup(cell), style) for cell in row])
    table = Table(rendered, colWidths=[width / max_cols] * max_cols, repeatRows=1, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#245C73")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("BACKGROUND", (0, 1), (-1, -1), colors.white),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F1F5F9")]),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#CBD5E1")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return table


def markdown_story(markdown: str, styles: dict[str, ParagraphStyle], width: float) -> list[object]:
    lines = markdown.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    story: list[object] = []
    index = 0
    first_h1 = True
    while index < len(lines):
        raw = lines[index].rstrip()
        stripped = raw.strip()
        if not stripped:
            index += 1
            continue

        if stripped.startswith("```"):
            index += 1
            code: list[str] = []
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code.append(normalize_text(lines[index].rstrip()))
                index += 1
            index += 1
            story.append(Preformatted("\n".join(code), styles["code"], maxLineLength=105))
            continue

        heading = re.match(r"^(#{1,4})\s+(.+)$", stripped)
        if heading:
            level = len(heading.group(1))
            text = inline_markup(heading.group(2))
            if level == 1:
                if not first_h1:
                    story.append(CondPageBreak(70 * mm))
                first_h1 = False
                story.append(Paragraph(text, styles["title"]))
            else:
                story.append(Paragraph(text, styles[f"h{level}"]))
            index += 1
            continue

        if re.fullmatch(r"-{3,}", stripped):
            story.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#CBD5E1")))
            story.append(Spacer(1, 2.5 * mm))
            index += 1
            continue

        if "|" in stripped and index + 1 < len(lines) and is_table_separator(lines[index + 1]):
            table_lines = [stripped, lines[index + 1].strip()]
            index += 2
            while index < len(lines) and "|" in lines[index] and lines[index].strip():
                table_lines.append(lines[index].strip())
                index += 1
            story.append(parse_table(table_lines, styles, width))
            story.append(Spacer(1, 4 * mm))
            continue

        if stripped.startswith(">"):
            quote_lines: list[str] = []
            while index < len(lines) and lines[index].strip().startswith(">"):
                quote_lines.append(lines[index].strip()[1:].strip())
                index += 1
            story.append(Paragraph(inline_markup(" ".join(quote_lines)), styles["quote"]))
            continue

        list_match = re.match(r"^\s*([-*+] |\d+[.)] )(.*)$", raw)
        if list_match:
            ordered = bool(re.match(r"\d", list_match.group(1)))
            items: list[str] = []
            while index < len(lines):
                match = re.match(r"^\s*([-*+] |\d+[.)] )(.*)$", lines[index])
                if not match or bool(re.match(r"\d", match.group(1))) != ordered:
                    break
                item_text = re.sub(r"^\[([ xX])\]\s*", lambda m: "☒ " if m.group(1).lower() == "x" else "☐ ", match.group(2))
                item_text = item_text.replace("☒", "[x]").replace("☐", "[ ]")
                items.append(item_text)
                index += 1
            for item_index, item_text in enumerate(items, start=1):
                prefix = f"{item_index}." if ordered else "-"
                story.append(Paragraph(f"<b>{prefix}</b>&nbsp;&nbsp;{inline_markup(item_text)}", styles["list"]))
            story.append(Spacer(1, 1.5 * mm))
            continue

        paragraph_lines = [stripped]
        index += 1
        while index < len(lines):
            candidate = lines[index].strip()
            if not candidate:
                break
            if (
                candidate.startswith(("#", ">", "```"))
                or re.fullmatch(r"-{3,}", candidate)
                or re.match(r"^([-*+] |\d+[.)] )", candidate)
                or ("|" in candidate and index + 1 < len(lines) and is_table_separator(lines[index + 1]))
            ):
                break
            paragraph_lines.append(candidate)
            index += 1
        story.append(Paragraph(inline_markup(" ".join(paragraph_lines)), styles["body"]))

    return story


def footer(canvas, document) -> None:
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#CBD5E1"))
    canvas.setLineWidth(0.4)
    canvas.line(20 * mm, 15 * mm, A4[0] - 20 * mm, 15 * mm)
    canvas.setFillColor(colors.HexColor("#64748B"))
    canvas.setFont("Helvetica", 7.5)
    canvas.drawCentredString(A4[0] / 2, 10 * mm, f"Roteiro de curso | página {document.page}")
    canvas.restoreState()


def render(source: Path, destination: Path) -> None:
    markdown = source.read_text(encoding="utf-8-sig")
    fonts = find_font_set()
    styles = build_styles(fonts)
    destination.parent.mkdir(parents=True, exist_ok=True)
    document = SimpleDocTemplate(
        str(destination),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=22 * mm,
        title=source.stem,
        author="criar-ementa-curso",
    )
    story = markdown_story(markdown, styles, document.width)
    if not story:
        raise ValueError(f"Markdown sem conteúdo: {source}")
    document.build(story, onFirstPage=footer, onLaterPages=footer)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Converte roteiros Markdown em PDFs A4.")
    parser.add_argument("inputs", nargs="+", type=Path, help="Arquivos .md de entrada")
    parser.add_argument("--output-dir", required=True, type=Path, help="Pasta dos PDFs")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    missing = [path for path in args.inputs if not path.is_file()]
    if missing:
        raise FileNotFoundError("Entradas ausentes: " + ", ".join(str(path) for path in missing))
    for source in args.inputs:
        destination = args.output_dir / f"{source.stem}.pdf"
        render(source, destination)
        print(destination.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
