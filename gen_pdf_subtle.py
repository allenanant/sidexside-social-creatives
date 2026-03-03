#!/usr/bin/env python3
"""PDF 2: Subtle safety-implied Meta ad copy for sidexside.
Safety is FELT, not said. The copy is about companionship, walking together,
peer matching - but the reader naturally concludes 'this is for campus safety'
without the copy ever going there explicitly."""

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
        self.cell(0, 8, 'sidexside  |  Meta Ad Copy - Subtle Angle', align='R')
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
pdf.cell(0, 10, 'Meta Ad Copy - Subtle Angle', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.ln(8)
pdf.set_draw_color(230, 255, 0)
pdf.set_line_width(2)
pdf.line(75, pdf.get_y(), 135, pdf.get_y())
pdf.ln(12)
pdf.set_font('Helvetica', '', 11)
pdf.set_text_color(120, 120, 120)
pdf.multi_cell(0, 6, (
    'Copy where safety is FELT, not said.\n\n'
    'The words are about companionship, walking together,\n'
    'peer connection, campus experience.\n\n'
    'But the reader - especially a university decision-maker -\n'
    'naturally concludes: "This solves a safety problem."\n\n'
    'The safety implication lives in the subtext:\n'
    '  "women matching with women" = safety\n'
    '  "no one walks alone" = safety\n'
    '  "someone heading your way" = safety\n'
    '  "the walk home, together" = safety\n\n'
    'Every ad ends with: Book a Demo'
), align='C')

# ================================================================
# SECTION 1: "WALKING TOGETHER" FRAMING
# ================================================================
pdf.add_page()
pdf.section_title('1. THE WALK HOME, TOGETHER')
pdf.set_font('Helvetica', '', 9)
pdf.set_text_color(120, 120, 120)
pdf.multi_cell(0, 5, 'The phrase "walk together" does all the heavy lifting. A decision-maker reads this and immediately thinks safety without the word appearing once.')
pdf.ln(4)

pdf.ad_block(
    'COMPANIONSHIP = SAFETY',
    'What If Every Woman on Your Campus Had Someone Walking Her Way?',
    'sidexside matches women heading the same direction.\nPeer-to-peer. Real-time. On every pathway.\nNo one has to walk alone unless they choose to.\nOne app. Deploys in weeks.',
    'What if no woman on your campus walked alone? sidexside matches women going the same direction - peer-to-peer, on-demand. See how.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'COMPANIONSHIP = SAFETY',
    'The Walk Home, Together.',
    'From the library. From the dining hall. From the late lecture.\nsidexside connects women heading the same way.\nJust company. Just a peer. Just the walk home made better.\nBuilt for universities. Deploys in weeks.',
    'The walk home shouldn\'t be a solo experience. sidexside connects women heading the same direction - real-time, on-demand.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'COMPANIONSHIP = SAFETY',
    'Someone Is Already Heading Your Way.',
    'On every campus, at every hour, women are walking the same direction.\nsidexside connects them.\nReal-time matching. Peer-to-peer. Women-only.\nThe simplest way to make sure no one walks alone.',
    'On any campus, women are already heading the same way. sidexside connects them. See how it works.',
    'Square 1080x1080'
)
pdf.divider()

pdf.ad_block(
    'COMPANIONSHIP = SAFETY',
    'No Student Should Have to Walk Alone.',
    'They shouldn\'t have to plan around it either.\nsidexside matches women heading the same direction - on demand.\nNo scheduling. No waiting. Just open and go.\nPeer companionship, built for campus.',
    'No planning. No scheduling. Just a peer going your way. sidexside makes sure no woman walks alone on campus.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'COMPANIONSHIP = SAFETY',
    'She\'s Heading to West Campus. So Is Another Student. We Connect Them.',
    'That\'s sidexside.\nWomen matched with women, heading the same direction.\nReal-time. On-demand. On every pathway.\nThe peer companion layer your campus needs.',
    'Two students heading the same way. sidexside connects them. Peer-to-peer, real-time. See how it works on your campus.',
    'Portrait 1080x1350'
)

# ================================================================
# SECTION 2: "WOMEN MATCHING WOMEN" FRAMING
# ================================================================
pdf.add_page()
pdf.section_title('2. WOMEN WITH WOMEN')
pdf.set_font('Helvetica', '', 9)
pdf.set_text_color(120, 120, 120)
pdf.multi_cell(0, 5, '"Women-only" signals safety without saying it. The exclusivity implies the purpose. Decision-makers understand immediately.')
pdf.ln(4)

pdf.ad_block(
    'WOMEN-ONLY = SAFETY',
    'Women Walking with Women. That\'s the Whole Idea.',
    'sidexside is a women-only peer matching platform for campus.\nStudents heading the same direction connect in real time.\nPeer-to-peer companionship that your students actually want to use.\nBuilt for universities.',
    'A women-only walking companion platform. Students match with students heading the same way. See how it works on campus.',
    'Portrait 1080x1350 / Square 1080x1080'
)
pdf.divider()

pdf.ad_block(
    'WOMEN-ONLY = SAFETY',
    'Built by Women. For Women. On Every Campus.',
    'sidexside was founded by women who\'ve walked those campus paths.\nWe built what we wished existed - a way to find another woman heading your way.\nNow we\'re bringing it to universities nationwide.',
    'Founded by women who get it. Built for women on campus. See what sidexside looks like on your campus.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'WOMEN-ONLY = SAFETY',
    'A Walking Companion. Whenever She Wants One.',
    'Not a service she has to book. Not a number she has to call.\nJust another woman heading the same direction.\nsidexside makes it happen - real-time, on-demand, peer-to-peer.',
    'Companionship on her terms. sidexside connects women heading the same way - no booking, no calling, just a peer going her direction.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'WOMEN-ONLY = SAFETY',
    'Your Female Students Deserve a Companion on Every Route.',
    'sidexside matches women heading the same direction across your entire campus.\nNot just the shuttle route. Not just the escort path.\nEvery sidewalk. Every pathway. Every hour.\nPeer-to-peer. Deploys in weeks.',
    'Every route. Every hour. sidexside gives your female students a walking companion across the entire campus. No infrastructure needed.',
    'Portrait 1080x1350'
)

# ================================================================
# SECTION 3: "PEER-TO-PEER" FRAMING
# ================================================================
pdf.add_page()
pdf.section_title('3. PEER-TO-PEER POWER')
pdf.set_font('Helvetica', '', 9)
pdf.set_text_color(120, 120, 120)
pdf.multi_cell(0, 5, '"Students helping students" implies safety at scale. The peer-to-peer model signals both community AND protection without saying either.')
pdf.ln(4)

pdf.ad_block(
    'PEER POWER = SAFETY',
    'The Most Powerful Campus Resource? Each Other.',
    'sidexside unlocks what\'s already there - students heading the same direction.\nWe just connect them.\nWomen matched with women. Real-time. On-demand.\nThe campus companion platform.',
    'Your best campus resource is your students. sidexside connects women heading the same way - peer-to-peer, real-time.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'PEER POWER = SAFETY',
    'Students Helping Students. On Every Pathway.',
    'sidexside connects women heading the same direction across campus.\nNo dispatchers. No schedules. No overhead.\nJust peers matching with peers, in real time.\nThe companion layer that scales with your student body.',
    'Peer-to-peer. On-demand. Scales with enrollment. sidexside turns your student body into a companion network.',
    'Square 1080x1080'
)
pdf.divider()

pdf.ad_block(
    'PEER POWER = SAFETY',
    'Drop a Pin. Find a Match. Walk Together.',
    'Three steps. That\'s all it takes for a student to find a walking companion.\nsidexside matches women heading the same direction - in real time.\nPeer-to-peer. Privacy-first. Built for campus.',
    'Three steps to a walking companion. Drop a pin, find a match, walk together. See how sidexside works on your campus.',
    'Portrait 1080x1350 / Square 1080x1080'
)
pdf.divider()

pdf.ad_block(
    'PEER POWER = SAFETY',
    'One App Turns Your Entire Campus Into a Companion Network.',
    'Every student heading somewhere is a potential walking companion for another.\nsidexside connects them.\nWomen matched with women. On-demand. Real-time.\nThe larger your campus, the more powerful it gets.',
    'The more students on sidexside, the more companions available on every pathway. It gets stronger as it grows.',
    'Portrait 1080x1350'
)

# ================================================================
# SECTION 4: OUTCOME FRAMING (SAFETY FELT)
# ================================================================
pdf.add_page()
pdf.section_title('4. THE CAMPUS THEY PICTURE')
pdf.set_font('Helvetica', '', 9)
pdf.set_text_color(120, 120, 120)
pdf.multi_cell(0, 5, 'Paint the picture of the outcome. When a decision-maker reads "no woman walks alone" they think safety. You never had to say it.')
pdf.ln(4)

pdf.ad_block(
    'OUTCOME = SAFETY',
    'Picture Your Campus Where No Woman Walks Alone.',
    'That\'s what sidexside builds.\nWomen matched with women heading the same way. Across every pathway.\nPeer-to-peer. On-demand. Privacy-first.\nSee what it looks like on your campus.',
    'Imagine a campus where no woman walks alone unless she chooses to. sidexside makes it real. See how.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'OUTCOME = SAFETY',
    'What If the Walk Home Was the Best Part of Her Night?',
    'Right now it\'s a solo trip.\nWith sidexside, it\'s a connection.\nA new friend. A familiar face. Someone going her way.\nPeer companionship that makes campus feel different.',
    'The walk home can be the loneliest or the most connected part of campus. sidexside makes it the latter.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'OUTCOME = SAFETY',
    'A Campus That Feels Like Community. Even at Midnight.',
    'sidexside connects women heading the same direction - at every hour.\nThe campus that goes quiet doesn\'t have to feel empty.\nPeer-to-peer companions on every pathway.',
    'Campus community doesn\'t stop at sunset. sidexside keeps it going on every pathway, at every hour.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'OUTCOME = SAFETY',
    'Every Pathway Covered. Every Hour. No Infrastructure.',
    'sidexside doesn\'t need blue lights or shuttle routes.\nIt runs on students\' phones.\nWomen matched with women heading the same way.\nThe companion layer that goes everywhere your students go.',
    'Full campus coverage. No hardware. No construction. Just women connecting with women on every pathway.',
    'Square 1080x1080'
)
pdf.divider()

pdf.ad_block(
    'OUTCOME = SAFETY',
    'She Opened the App. Found a Match. Walked Home With Company.',
    'That\'s a sidexside moment.\nTwo women. Same direction. Matched in seconds.\nIt happens hundreds of times a night on connected campuses.\nBring it to yours.',
    'Matched in seconds. Walking together in minutes. That\'s sidexside. See how it works on your campus.',
    'Portrait 1080x1350'
)

# ================================================================
# SECTION 5: READY-TO-PASTE META ADS
# ================================================================
pdf.add_page()
pdf.section_title('5. READY-TO-PASTE META ADS')

ads = [
    ('Ad 1: The Match',
     'Headline: A Walking Companion for Every Student\n'
     'Primary text: sidexside matches women heading the same direction - '
     'in real time, on every pathway. Peer-to-peer companionship that your students '
     'actually want to use. No infrastructure. No headcount. Deploys in weeks.\n'
     'Description: See how it works in 15 minutes.\n'
     'CTA Button: Book Now'),

    ('Ad 2: Walk Together',
     'Headline: No Woman Walks Alone on Campus\n'
     'Primary text: sidexside connects women heading the same way. '
     'Drop a pin, find a match, walk together. That simple. '
     'Peer-to-peer. Women-only. Built for universities.\n'
     'Description: 15-min demo. Deploys in weeks.\n'
     'CTA Button: Book Now'),

    ('Ad 3: The Network',
     'Headline: Turn Your Campus Into a Companion Network\n'
     'Primary text: Every student heading somewhere is a potential walking companion. '
     'sidexside connects women going the same direction - real-time, on-demand. '
     'The larger your campus, the stronger it gets.\n'
     'Description: See how it scales. Book a demo.\n'
     'CTA Button: Book Now'),

    ('Ad 4: Women for Women',
     'Headline: Women Walking with Women. Built for Campus.\n'
     'Primary text: A women-only walking companion platform designed for higher ed. '
     'Students match with peers heading their direction. '
     'Privacy-first. On-demand. Founded by women who get it.\n'
     'Description: Book a campus demo.\n'
     'CTA Button: Book Now'),

    ('Ad 5: The Origin',
     'Headline: Built by Women Who Walked Those Paths\n'
     'Primary text: We wished for a companion on those late campus walks. '
     'So we built one. sidexside matches women heading the same way - '
     'peer-to-peer, real-time. Now bringing it to campuses nationwide.\n'
     'Description: See the platform. Book a demo.\n'
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
# SECTION 6: ON-IMAGE TEXT
# ================================================================
pdf.add_page()
pdf.section_title('6. ON-IMAGE TEXT FOR CREATIVES')

pdf.sub_section('Walking Together Creatives')
texts = [
    ('What if every woman\non your campus\nhad someone\nwalking her way?\n\nBook a Demo', 'Golden hour campus photo'),
    ('The walk home,\ntogether.\n\nsidexside.\n\nBook a Demo', 'Two women walking, shot from behind'),
    ('Someone is already\nheading your way.\n\nBook a Demo', 'Campus pathway, warm light'),
    ('No one walks alone.\nNot anymore.\n\nBook a Demo', 'Night campus, warm pathway lights'),
    ('She\'s heading\nto West Campus.\nSo is she.\n\nWe connect them.\n\nBook a Demo', 'Split frame or two women'),
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

pdf.sub_section('Women-Only Creatives')
texts = [
    ('Women walking\nwith women.\n\nThat\'s the whole idea.\n\nBook a Demo', 'Group walking, editorial'),
    ('Built by women.\nFor women.\nOn every campus.\n\nBook a Demo', 'Branded, minimal'),
    ('A walking companion.\nWhenever she\nwants one.\n\nBook a Demo', 'Woman on phone, campus bg'),
    ('Your female students\ndeserve a companion\non every route.\n\nBook a Demo', 'Aerial campus pathways'),
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

pdf.sub_section('Peer-to-Peer Creatives')
texts = [
    ('Drop a pin.\nFind a match.\nWalk together.\n\nBook a Demo', '3-step branded layout'),
    ('The most powerful\ncampus resource?\n\nEach other.\n\nBook a Demo', 'Group of women, campus'),
    ('Students helping students.\nOn every pathway.\n\nBook a Demo', 'Library exit photo'),
    ('One app.\nEvery pathway.\nEvery hour.\n\nBook a Demo', 'Aerial quad, warm light'),
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

pdf.sub_section('Outcome Creatives')
texts = [
    ('Picture your campus\nwhere no woman\nwalks alone.\n\nBook a Demo', 'Aspirational, warm tone'),
    ('What if the walk home\nwas the best part\nof her night?\n\nBook a Demo', 'Two women laughing, walking'),
    ('A campus that feels\nlike community.\nEven at midnight.\n\nBook a Demo', 'Night campus, warm lights'),
    ('Matched in seconds.\nWalking together\nin minutes.\n\nBook a Demo', 'Dynamic, phone UI style'),
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
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sidexside-meta-ads-SUBTLE-ANGLE.pdf")
pdf.output(out_path)
print(f"PDF generated: {out_path}")
