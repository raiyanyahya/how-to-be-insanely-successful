import sys

from fpdf import FPDF
from fpdf.enums import TextMode

PAGES = 300

YELLOW = (255, 230, 0)
BLACK = (10, 10, 10)
BLUE = (41, 116, 204)
WHITE = (255, 255, 255)
RED = (227, 49, 60)
ORANGE = (255, 120, 0)
GRAY = (60, 60, 60)

pdf = FPDF(orientation="P", unit="mm", format="letter")
pdf.set_title("How To Be Insanely Successful")
pdf.set_author("Dr. Knarp Atsuj")
pdf.set_auto_page_break(False)
W, H = pdf.w, pdf.h


def ctext(y, txt, size, color=BLACK, style="B", spacing=0.0):
    pdf.set_font("helvetica", style, size)
    pdf.set_text_color(*color)
    pdf.set_char_spacing(spacing)
    pdf.set_xy(0, y)
    pdf.cell(W, size * 0.42, txt, align="C")
    pdf.set_char_spacing(0)


# ---------------------------------------------------------------- cover
pdf.add_page()
pdf.set_fill_color(*YELLOW)
pdf.rect(0, 0, W, H, "F")

# top banner, solid black with yellow text
pdf.set_fill_color(*BLACK)
pdf.rect(0, 0, W, 14, "F")
ctext(4.5, "OVER 9,000,000 COPIES SOLD WORLDWIDE", 10.5, color=YELLOW, spacing=1.2)

# review quote
ctext(27, "'A must-read for everyone who cares", 15)
ctext(35, "about being insanely successful'", 15)
pdf.set_font("helvetica", "B", 9.5)
w1 = pdf.get_string_width("CIRE SEIR, ")
pdf.set_font("helvetica", "I", 9.5)
w2 = pdf.get_string_width("author of The Lean Excuse")
x0 = (W - w1 - w2) / 2
pdf.set_text_color(*BLACK)
pdf.set_xy(x0, 45)
pdf.set_font("helvetica", "B", 9.5)
pdf.cell(w1, 5, "CIRE SEIR, ")
pdf.set_font("helvetica", "I", 9.5)
pdf.cell(w2, 5, "author of The Lean Excuse")

# hero title: red drop shadow, then white letters with black outline
pdf.text_mode = TextMode.FILL
ctext(65.4, "SUCCESS", 90, color=RED, spacing=1.0)
pdf.text_mode = TextMode.FILL_STROKE
pdf.set_line_width(1.0)
pdf.set_draw_color(*BLACK)
ctext(64, "SUCCESS", 90, color=WHITE, spacing=1.0)
pdf.text_mode = TextMode.FILL

# ---------------------------------------------------------- rocket launch
cx, y0 = W / 2, 104
pdf.set_draw_color(*BLACK)

# fins first so the body overlaps their roots
pdf.set_line_width(1.2)
pdf.set_fill_color(*RED)
pdf.polygon([(cx - 12, y0 + 40), (cx - 26, y0 + 62), (cx - 12, y0 + 58)], style="DF")
pdf.polygon([(cx + 12, y0 + 40), (cx + 26, y0 + 62), (cx + 12, y0 + 58)], style="DF")

# nozzle and flame under the body
pdf.set_fill_color(*GRAY)
pdf.polygon([(cx - 7, y0 + 60), (cx + 7, y0 + 60), (cx + 5, y0 + 65), (cx - 5, y0 + 65)], style="F")
with pdf.new_path() as p:
    p.style.paint_rule = "stroke_fill_nonzero"
    p.style.fill_color = "#FF7800"
    p.style.stroke_color = "#0A0A0A"
    p.style.stroke_width = 1.0
    p.style.stroke_join_style = "round"
    p.move_to(cx - 6, y0 + 65)
    p.curve_to(cx - 10, y0 + 72, cx - 5, y0 + 80, cx, y0 + 87)
    p.curve_to(cx + 5, y0 + 80, cx + 10, y0 + 72, cx + 6, y0 + 65)
    p.close()
with pdf.new_path() as p:
    p.style.paint_rule = "fill_nonzero"
    p.style.fill_color = "#FFFFFF"
    p.move_to(cx - 3, y0 + 65)
    p.curve_to(cx - 5, y0 + 70, cx - 2, y0 + 75, cx, y0 + 79)
    p.curve_to(cx + 2, y0 + 75, cx + 5, y0 + 70, cx + 3, y0 + 65)
    p.close()

# body, nose cone, window
pdf.set_line_width(1.2)
pdf.set_fill_color(*WHITE)
pdf.rect(cx - 13, y0 + 22, 26, 38, style="DF", round_corners=True, corner_radius=3)
with pdf.new_path() as p:
    p.style.paint_rule = "stroke_fill_nonzero"
    p.style.fill_color = "#E3313C"
    p.style.stroke_color = "#0A0A0A"
    p.style.stroke_width = 1.2
    p.style.stroke_join_style = "round"
    p.move_to(cx - 13, y0 + 24)
    p.curve_to(cx - 11, y0 + 8, cx - 6, y0 + 2, cx, y0)
    p.curve_to(cx + 6, y0 + 2, cx + 11, y0 + 8, cx + 13, y0 + 24)
    p.close()
pdf.set_fill_color(*BLUE)
pdf.ellipse(cx - 7.5, y0 + 30, 15, 15, "DF")
pdf.set_fill_color(*WHITE)
pdf.ellipse(cx - 4, y0 + 33.5, 8, 8, "F")

# speed lines and sparkles
pdf.set_line_width(1.4)
pdf.line(cx - 32, y0 + 28, cx - 32, y0 + 42)
pdf.line(cx + 32, y0 + 34, cx + 32, y0 + 48)
pdf.line(cx - 24, y0 + 68, cx - 24, y0 + 78)
pdf.line(cx + 24, y0 + 68, cx + 24, y0 + 78)
pdf.set_line_width(1.2)
for sx_, sy_ in [(cx - 44, y0 + 10), (cx + 46, y0 + 16), (cx + 38, y0 + 66)]:
    pdf.line(sx_ - 3, sy_, sx_ + 3, sy_)
    pdf.line(sx_, sy_ - 3, sx_, sy_ + 3)

# blue badge
pdf.set_fill_color(*BLUE)
bcx, bcy, br = W - 38, 156, 22
pdf.ellipse(bcx - br, bcy - br, 2 * br, 2 * br, "F")
pdf.set_text_color(*WHITE)
pdf.set_font("helvetica", "B", 10.5)
pdf.set_xy(bcx - br, bcy - 8)
pdf.multi_cell(2 * br, 5.2, "COMPLETELY\nREVISED AND\nSHORTENED", align="C")

# subtitle, then author in a black footer band
ctext(204, "How to Be", 27)
ctext(216.5, "Insanely Successful", 27, color=RED)
pdf.set_fill_color(*BLACK)
pdf.rect(0, 250, W, H - 250, "F")
ctext(257, "DR. KNARP ATSUJ", 28, color=WHITE, spacing=0.8)

# ---------------------------------------------------------------- pages
for n in range(1, PAGES + 1):
    pdf.add_page()
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("helvetica", "", 12)
    pdf.set_xy(25, 25)
    pdf.cell(0, 6, "work harder")
    pdf.set_font("helvetica", "", 9)
    pdf.set_text_color(120, 120, 120)
    pdf.set_xy(0, H - 18)
    pdf.cell(W, 5, str(n), align="C")

pdf.output(sys.argv[1])
print(f"pages: {PAGES + 1}", file=sys.stderr)
