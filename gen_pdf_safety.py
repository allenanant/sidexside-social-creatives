#!/usr/bin/env python3
"""PDF 1: Safety-adjacent Meta ad copy for sidexside."""

from fpdf import FPDF
import os

def clean(text):
    return (text
        .replace('\u2014', ' - ')
        .replace('\u2013', ' - ')
        .replace('\u2192', '->')
        .replace('\u2019', "'")
        .replace('\u2018', "'")
        .replace('\u201c', '"')
        .replace('\u201d', '"')
        .replace('\u2026', '...')
        .replace('\u2022', '*')
    )

class CopyPDF(FPDF):
    def normalize_text(self, text):
        return super().normalize_text(clean(text))

    def header(self):
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(7, 108, 199)
        self.cell(0, 8, 'sidexside  |  Meta Ad Copy - Safety Angle', align='R')
        self.ln(12)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', '', 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f'sidexside.ai  |  Page {self.page_no()}/{{nb}}', align='C')

    def section_title(self, title):
        self.ln(4)
        self.set_font('Helvetica', 'B', 16)
        self.set_text_color(7, 108, 199)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(230, 255, 0)
        self.set_line_width(1.5)
        self.line(self.l_margin, self.get_y(), self.l_margin + 40, self.get_y())
        self.ln(6)

    def sub_section(self, title):
        self.ln(2)
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(50, 50, 50)
        self.cell(0, 7, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def ad_block(self, angle, headline, body, primary="", fmt=""):
        self.set_font('Helvetica', 'B', 9)
        self.set_text_color(7, 108, 199)
        self.cell(0, 5, angle, new_x="LMARGIN", new_y="NEXT")
        self.set_font('Helvetica', 'B', 13)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 6, headline, new_x="LMARGIN", new_y="NEXT")
        self.set_font('Helvetica', '', 10)
        self.set_text_color(80, 80, 80)
        self.multi_cell(0, 5, body, new_x="LMARGIN", new_y="NEXT")
        if primary:
            self.ln(2)
            self.set_font('Helvetica', 'I', 9)
            self.set_text_color(100, 100, 100)
            self.multi_cell(0, 5, f'Primary text: {primary}', new_x="LMARGIN", new_y="NEXT")
        self.ln(2)
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(230, 80, 0)
        self.cell(0, 6, 'CTA: Book a Demo -> sidexside.ai/demo', new_x="LMARGIN", new_y="NEXT")
        if fmt:
            self.set_font('Helvetica', 'I', 8)
            self.set_text_color(150, 150, 150)
            self.cell(0, 5, f'[{fmt}]', new_x="LMARGIN", new_y="NEXT")
        self.ln(4)

    def divider(self):
        self.set_draw_color(230, 230, 230)
        self.set_line_width(0.3)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(4)

pdf = CopyPDF()
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=20)
pdf.add_page()

# COVER
pdf.ln(30)
pdf.set_font('Helvetica', 'B', 36)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 14, 'sidexside', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.set_font('Helvetica', '', 16)
pdf.set_text_color(7, 108, 199)
pdf.cell(0, 10, 'Meta Ad Copy - Safety Angle', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.ln(8)
pdf.set_draw_color(230, 255, 0)
pdf.set_line_width(2)
pdf.line(75, pdf.get_y(), 135, pdf.get_y())
pdf.ln(12)
pdf.set_font('Helvetica', '', 11)
pdf.set_text_color(120, 120, 120)
pdf.multi_cell(0, 6, (
    'Copy that implies safety through framing:\n'
    '"walking alone", "after dark", "escort gaps", "at night"\n\n'
    'Never says "safe/safer/safety" explicitly.\n'
    'The feeling comes through the problem and the solution.\n\n'
    'Every ad ends with: Book a Demo\n'
    'Objective: University decision-makers book a call'
), align='C')

# ================================================================
# SECTION 1: ESCORT / SHUTTLE GAP
# ================================================================
pdf.add_page()
pdf.section_title('1. THE SERVICE GAP')

pdf.ad_block(
    'ESCORT GAP',
    'Your Escort Runs Until Midnight. Your Students Don\'t Stop.',
    'Campus escorts cover fixed routes on fixed schedules.\nBut students move everywhere, at every hour.\nsidexside fills what\'s left - matching women with women heading the same direction.\nPeer-to-peer. On-demand. No new infrastructure.',
    'Your escort covers 3 routes. sidexside covers all of them - no headcount, no hardware. See how it fills the gap.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'SHUTTLE GAP',
    'The Shuttle Covers 4 Stops. Your Students Walk Everywhere.',
    'Fixed routes can\'t solve a moving problem.\nsidexside goes where your students go - matching peers heading the same direction, in real time.\nOne app. Every pathway. Zero infrastructure.',
    'Shuttles and escorts cover fixed points. sidexside covers the spaces in between.',
    'Square 1080x1080'
)
pdf.divider()

pdf.ad_block(
    'BLUE LIGHT GAP',
    'Blue Light Phones Don\'t Walk Students Home.',
    'They\'re stationary. They\'re underused.\nsidexside goes where students go - matching women with women, in real time, on every pathway.\nThe mobile peer layer your campus is missing.',
    'Static infrastructure can\'t solve a moving problem. See how sidexside adds the peer layer that goes everywhere.',
    'Portrait 1080x1350 / Square 1080x1080'
)
pdf.divider()

pdf.ad_block(
    'INFRASTRUCTURE GAP',
    'You Have Escorts, Shuttles, and Blue Lights. What\'s Missing?',
    'The peer layer.\nAll that infrastructure is great - but students still walk alone between the gaps.\nsidexside connects them with other women heading the same direction.\nComplements everything you already have.',
    'Great campus services still leave gaps. sidexside fills them with peer companionship. No infrastructure needed.',
    'Portrait 1080x1350'
)

# ================================================================
# SECTION 2: AFTER DARK
# ================================================================
pdf.add_page()
pdf.section_title('2. THE AFTER-DARK PROBLEM')

pdf.ad_block(
    'DAY VS NIGHT',
    'Your Campus Feels Connected at Noon. What About 10pm?',
    'The quad that buzzes during the day goes quiet after dark.\nBut students still need to get home.\nsidexside turns those solo walks into shared ones - matching peers heading the same way.',
    'Day campus and night campus are two different experiences. sidexside bridges the gap.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'DISCONNECTION',
    '52% of Your Students Feel Disconnected After Dark.',
    'That\'s a retention problem.\nStudents who feel disconnected don\'t stay.\nsidexside builds peer connection on campus - one walk at a time.\nOn-demand. Women-only. Privacy-first.',
    '52% of women report disconnection at night. That impacts retention, wellbeing, and campus experience.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'SOLO WALKS',
    'The Walk Between the Library and the Dorm Shouldn\'t Feel Lonely.',
    'For 73% of women on your campus, it does.\nsidexside changes that - connecting students heading the same direction, on demand.\nPeer-to-peer companionship that fits naturally into campus life.',
    'Library to dorm. Dining hall to parking lot. Every walk is better with company.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'REROUTING',
    '67% of Women Have Changed Their Route to Avoid Walking Alone.',
    'What if they didn\'t have to?\nsidexside connects women heading the same direction.\nNo rerouting. No avoiding. Just a peer going your way.',
    '67% of women reroute to avoid solo walks. sidexside gives them a peer heading their way instead.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'ISOLATION',
    '1 in 3 Students Say Campus Feels Isolating at Night.',
    'What if the walk home felt like a social moment instead?\nsidexside matches women heading the same direction.\nNo planning. No scheduling. Just companionship on demand.',
    '1 in 3 students feel isolated on campus after dark. sidexside turns solo walks into shared ones.',
    'Square 1080x1080'
)

# ================================================================
# SECTION 3: PROACTIVE FRAMING
# ================================================================
pdf.add_page()
pdf.section_title('3. PROACTIVE > REACTIVE')

pdf.ad_block(
    'PROACTIVE',
    'Don\'t Wait for an Incident. Build Connection Now.',
    'The best time to add peer companionship to your campus was last semester.\nThe second best time is now.\nsidexside deploys in weeks - not months.',
    'Proactive beats reactive. sidexside builds organic peer connection across your campus.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'PROACTIVE',
    'What If You Could Prevent the Problem Instead of Responding to It?',
    'Peer connection is the most natural form of campus wellbeing.\nsidexside creates it automatically - matching women walking the same direction.\nEvery night. Every pathway. On demand.',
    'Connection prevents disconnection. sidexside builds it naturally across your campus. See how.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'DEMAND SIGNAL',
    '73% of Women on Your Campus Want One Thing on the Walk Home.',
    'Not a tracking app. Not a panic button.\nJust someone heading the same direction.\nsidexside delivers exactly that.',
    '73% of college women want a walking companion. Not an app. Not a device. Just someone going their way.',
    'Portrait 1080x1350 / Square 1080x1080'
)

# ================================================================
# SECTION 4: READY-TO-PASTE META ADS
# ================================================================
pdf.add_page()
pdf.section_title('4. READY-TO-PASTE META ADS')

ads = [
    ('Ad 1: The Gap',
     'Headline: Peer Walking Companions for Campus\n'
     'Primary text: Your escort runs until midnight. Your students don\'t stop. '
     'sidexside fills the gap - matching women with women heading the same direction. '
     'Peer-to-peer. On-demand. No infrastructure. No headcount.\n'
     'Description: 15-min demo. Deploys in weeks.\n'
     'CTA Button: Book Now'),

    ('Ad 2: The Stat',
     'Headline: 73% of Women Want a Walking Companion\n'
     'Primary text: Not a tracking app. Not a panic button. Just someone heading the same way. '
     'sidexside matches women on campus in real time - peer-to-peer, on-demand.\n'
     'Description: See how it works in 15 minutes.\n'
     'CTA Button: Book Now'),

    ('Ad 3: After Dark',
     'Headline: Your Campus After Dark Needs This\n'
     'Primary text: The campus that feels connected at noon goes quiet at 10pm. '
     'But students still need to get home. sidexside matches women heading the same way - '
     'turning solo walks into shared ones.\n'
     'Description: See how it works. Book a demo.\n'
     'CTA Button: Book Now'),

    ('Ad 4: Blue Lights',
     'Headline: Blue Lights Are Stationary. Your Students Aren\'t.\n'
     'Primary text: Static infrastructure can\'t solve a moving problem. '
     'sidexside adds the mobile peer layer - matching women heading the same direction. '
     'Every pathway. Every hour. No hardware.\n'
     'Description: 15-min demo. No commitment.\n'
     'CTA Button: Book Now'),

    ('Ad 5: The Reroute',
     'Headline: 67% of Women Reroute to Avoid Walking Alone\n'
     'Primary text: What if they didn\'t have to? sidexside connects women heading the same direction '
     'so no one reroutes, no one avoids, no one walks alone unless they choose to.\n'
     'Description: See how it works on your campus.\n'
     'CTA Button: Book Now'),
]

for title, content in ads:
    pdf.sub_section(title)
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(80, 80, 80)
    pdf.multi_cell(0, 5, content, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)
    pdf.divider()

# ================================================================
# SECTION 5: ON-IMAGE TEXT
# ================================================================
pdf.add_page()
pdf.section_title('5. ON-IMAGE TEXT FOR CREATIVES')

pdf.sub_section('Gap Creatives')
texts = [
    ('Your escort stops\nat midnight.\n\nYour students don\'t.\n\nBook a Demo', 'Night campus photo, dark overlay'),
    ('The shuttle covers\n4 stops.\n\nYour students walk\neverywhere.\n\nBook a Demo', 'Aerial campus photo'),
    ('Blue light phones\ndon\'t walk\nstudents home.\n\nsidexside does.\n\nBook a Demo', 'Night pathway photo'),
    ('Great infrastructure.\nStudents still walk alone.\n\nThe peer layer\nis missing.\n\nBook a Demo', 'Campus buildings, overlay'),
]
for text, note in texts:
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(0, 5, text, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('Helvetica', 'I', 8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 5, f'[{note}]', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)
    pdf.divider()

pdf.sub_section('Stat Creatives')
texts = [
    ('73% of women\nwant a walking companion.\n\nYour campus can deliver.\n\nBook a Demo', 'Blue bg, yellow stat'),
    ('52% feel disconnected\nafter dark.\n\nThat\'s a retention problem.\n\nBook a Demo', 'Black bg, blue accent'),
    ('67% of women\nreroute to avoid\nwalking alone.\n\nWhat if they didn\'t\nhave to?\n\nBook a Demo', 'Dark bg, yellow highlight'),
    ('1 in 3 students\nsay campus feels\nisolating at night.\n\nBook a Demo', 'Blue gradient'),
]
for text, note in texts:
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(0, 5, text, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('Helvetica', 'I', 8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 5, f'[{note}]', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)
    pdf.divider()

pdf.sub_section('Proactive Creatives')
texts = [
    ('Don\'t wait for\nan incident.\n\nBuild connection now.\n\nBook a Demo', 'Professional, brand blue'),
    ('73% of women want\none thing on the\nwalk home.\n\nCompany.\n\nBook a Demo', 'Campus golden hour photo'),
]
for text, note in texts:
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(0, 5, text, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('Helvetica', 'I', 8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 5, f'[{note}]', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)
    pdf.divider()

# OUTPUT
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sidexside-meta-ads-SAFETY-ANGLE.pdf")
pdf.output(out_path)
print(f"PDF generated: {out_path}")
