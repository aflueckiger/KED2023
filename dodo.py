from pathlib import Path
from datetime import datetime



TITLE = "BA Seminar: The ABC of Computational Text Analysis"
AUTHOR = "Alex Flückiger"

## Location of CSS file
CSSFILE = Path("/home/alex/KED2023/lectures/resources/custom_style_reveal.css")

## Location of your working bibliography file
BIBFILE = Path("/home/alex/zotero.bib")

TITLE = "BA Seminar: The ABC of Computational Text Analysis"
AUTHOR = "Alex Flückiger"

MAIN_DIR = Path.cwd()
LECTURES_DIR = MAIN_DIR / "lectures"
LECTURES_MD_DIR = LECTURES_DIR / "md"
LECTURES_HTML_DIR = LECTURES_DIR / "html"
LECTURES_PDF_DIR = LECTURES_DIR / "pdf"
LECTURES_NOTES_DIR = LECTURES_DIR / "notes"

ASSIGNMENTS_DIR = MAIN_DIR / "assignments"
MATERIALS_DIR = MAIN_DIR / "materials"


def task_prepare_dir():
    """Create all directories"""

    for outdir in (
        LECTURES_PDF_DIR,
        LECTURES_HTML_DIR,
        LECTURES_MD_DIR,
        LECTURES_NOTES_DIR,
        ASSIGNMENTS_DIR,
        MATERIALS_DIR,
    ):

        yield {
            "name": outdir,
            "actions": [f"mkdir -p {outdir}"],
            "targets": [outdir],
        }


# def task_run_jekyll():
#     pass
#     """Running jekyll locally"""
#     return {
#         "actions": ["bundle exec jekyll serve"],
#     }


def task_create_html_slide():

    infiles = sorted(LECTURES_MD_DIR.glob("*.md"))

    for infile in infiles:
        outfile = Path(LECTURES_HTML_DIR) / Path(infile).with_suffix(".html").name
        # TODO: involves a dirty hack of changing working directory as Quarto can not handle relative paths
        yield {
            "name": infile,
            "file_dep": [infile, CSSFILE],
            "actions": [
                f"cd {LECTURES_MD_DIR} && quarto render {infile} -o {outfile.name} \
                -f markdown+emoji+strikeout --standalone --embed-resources \
                --bibliography {BIBFILE} \
                -V width=1920 -V height=1080 \
                --include-in-header {CSSFILE} --quiet",
                f"cd {LECTURES_MD_DIR} && mv {outfile.name} {outfile}",
            ],
            "targets": [outfile],
        }


def task_create_pdf_slide():

    infiles = sorted(LECTURES_HTML_DIR.glob("*.html"))

    for infile in infiles:
        outfile = Path(LECTURES_PDF_DIR) / Path(infile).with_suffix(".pdf").name
        yield {
            "name": infile,
            "file_dep": [infile],
            "actions": [
                f"decktape --load-pause 500 --pdf-author '{AUTHOR}' --pdf-title '{TITLE}' {infile} {outfile}",
                f"gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/prepress -dNOPAUSE -dQUIET -dBATCH -sOutputFile={outfile}.temp {outfile}",
                f"mv {outfile}.temp {outfile}",
            ],
            "targets": [outfile],
        }


# def task_create_lecture_notes():
#     infiles = sorted(LECTURES_MD_DIR.glob("*.md"))

#     for infile in infiles:
#         outfile = Path(LECTURES_NOTES_DIR) / infile.with_suffix(".notes.pdf").name
#         yield {
#             "name": infile,
#             "file_dep": [infile],
#             "actions": [
#                 f"python lib/extract_notes.py < {infile} | pandoc -o {outfile} -f markdown --pdf-engine=xelatex -V geometry:margin=2cm",
#             ],
#             "targets": [outfile],
#         }




def task_create_syllabus():

    outfile = Path("KED2022_syllabus.pdf")
    today = datetime.today().strftime('%d %B %Y')
    return {
        "file_dep": ["index.md", "schedule.md", "lectures.md", "assignments.md"],
        "actions": [
            "cat index.md <(echo '[Go to Course Website](https://aflueckiger.github.io/KED2022/)' ) | grep -v 'Go to UniLu website' | sed '/<div/,/div>/d'	> index.md.tmp",
            "sed '5 a # Schedule' schedule.md | sed 's/.lectures//' > schedule.md.tmp",
            "sed '5 a # Lectures' lectures.md | sed 's/!.*\.svg)//' | grep -v '{.*comment .}' | grep -v 'recorded video'  > lectures.md.tmp",
            "sed '5 a # Assignments' assignments.md > assignments.md.tmp",
            f"pandoc -o {outfile} index.md.tmp schedule.md.tmp lectures.md.tmp assignments.md.tmp \
            --from markdown \
            --toc \
            --toc-depth=1 \
            --number-sections \
            -V geometry:margin=2.5cm \
            -V urlcolor='[HTML]{{111bab}}' \
            -V linkcolor='[HTML]{{111bab}}' \
            -V filecolor='[HTML]{{111bab}}' \
            --metadata title='{TITLE}' \
            --metadata date='{today}'",
           
        ],
        "targets": [outfile],
        # 'title': show_cmd
    }
	            

# %.pdf: %.md
# 	pandoc -f  markdown+rebase_relative_paths -o $@ $< \
# 	-V urlcolor='[HTML]{111bab}' \
# 	-V linkcolor='[HTML]{111bab}' \
# 	-V filecolor='[HTML]{111bab}' \
# 	-V geometry:margin=2.5cm \
# 	--number-sections \
# 	--metadata date="`date -u '+%d %B %Y'`"

def show_cmd(task):
    return "executing... %s" % task.actions[0]