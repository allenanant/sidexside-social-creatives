#!/usr/bin/env python3
"""Generate B2B Meta Ad copy PDF for sidexside."""

from fpdf import FPDF
import os

def clean(text):
    """Replace all Unicode chars that Helvetica can't handle."""
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
        self.cell(0, 8, 'sidexside  |  B2B Meta Ad Copy', align='R')
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

    def ad_block(self, hook_angle, headline, body, primary_text="", format_note=""):
        # Hook angle
        self.set_font('Helvetica', 'B', 9)
        self.set_text_color(7, 108, 199)
        self.cell(0, 5, hook_angle, new_x="LMARGIN", new_y="NEXT")
        # Headline
        self.set_font('Helvetica', 'B', 13)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 6, headline, new_x="LMARGIN", new_y="NEXT")
        # Body
        self.set_font('Helvetica', '', 10)
        self.set_text_color(80, 80, 80)
        self.multi_cell(0, 5, body, new_x="LMARGIN", new_y="NEXT")
        # Primary text
        if primary_text:
            self.ln(2)
            self.set_font('Helvetica', 'I', 9)
            self.set_text_color(100, 100, 100)
            self.multi_cell(0, 5, f'Primary text: {primary_text}', new_x="LMARGIN", new_y="NEXT")
        # CTA
        self.ln(2)
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(230, 80, 0)
        self.cell(0, 6, 'CTA: Book a Demo -> sidexside.ai/demo', new_x="LMARGIN", new_y="NEXT")
        # Format
        if format_note:
            self.set_font('Helvetica', 'I', 8)
            self.set_text_color(150, 150, 150)
            self.cell(0, 5, f'[{format_note}]', new_x="LMARGIN", new_y="NEXT")
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

# -- COVER PAGE --
pdf.ln(30)
pdf.set_font('Helvetica', 'B', 36)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 14, 'sidexside', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.set_font('Helvetica', '', 16)
pdf.set_text_color(7, 108, 199)
pdf.cell(0, 10, 'B2B Meta Ad Copy Bank', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.ln(8)
pdf.set_draw_color(230, 255, 0)
pdf.set_line_width(2)
pdf.line(75, pdf.get_y(), 135, pdf.get_y())
pdf.ln(12)
pdf.set_font('Helvetica', 'B', 12)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 8, 'Objective: Book a Demo Call', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.ln(6)
pdf.set_font('Helvetica', '', 11)
pdf.set_text_color(120, 120, 120)
pdf.multi_cell(0, 6, (
    'Direct-response Meta ad creatives targeting\n'
    'US university decision-makers.\n\n'
    'Strategy: Let the problem do the targeting.\n'
    'The right person self-selects because the problem is theirs.\n'
    'No role callouts. The language, framing, and pain points\n'
    'naturally filter for decision-makers.\n\n'
    'CTA on every creative: Book a Demo\n\n'
    'Messaging rules:\n'
    '  * Positive-only framing\n'
    '  * No "safe/safer/safety" language\n'
    '  * No pricing displayed\n'
    '  * No false claims\n'
    '  * No role callouts in headlines'
), align='C')

# ================================================================
# SECTION 1: OPERATIONAL GAP ADS
# ================================================================
pdf.add_page()
pdf.section_title('1. THE GAP YOUR CAMPUS HAS')
pdf.set_font('Helvetica', '', 9)
pdf.set_text_color(120, 120, 120)
pdf.multi_cell(0, 5, 'These expose a gap that only a campus decision-maker would recognize. Students scroll past. Deans, VPs, and directors stop.')
pdf.ln(4)

pdf.ad_block(
    'OPERATIONAL GAP',
    'Your Escort Runs Until Midnight. Your Students Don\'t Stop.',
    'Campus escorts cover fixed routes on fixed schedules.\nBut students move everywhere, at every hour.\nsidexside fills what\'s left - matching women with women heading the same direction.\nPeer-to-peer. On-demand. No new infrastructure.',
    '73% of women on campus want a walking companion. Your escort covers 3 routes. sidexside covers all of them - no headcount, no hardware. See how.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'OPERATIONAL GAP',
    'The Shuttle Covers 4 Stops. Your Students Walk Everywhere.',
    'Fixed routes can\'t solve a moving problem.\nsidexside goes where your students go - matching peers heading the same direction, in real time.\nOne app. Every pathway. Zero infrastructure.',
    'Shuttles and escorts cover fixed points. sidexside covers the spaces in between. See how universities are adding peer-to-peer companionship.',
    'Square 1080x1080'
)
pdf.divider()

pdf.ad_block(
    'OPERATIONAL GAP',
    'Blue Light Phones Don\'t Walk Students Home.',
    'They\'re stationary. They\'re underused. And your students know it.\nsidexside goes where students go - matching women with women, in real time, on every pathway.\nThe mobile peer layer your campus is missing.',
    'Static infrastructure can\'t solve a moving problem. sidexside adds the peer-to-peer layer that goes everywhere your students do.',
    'Portrait 1080x1350 / Square 1080x1080'
)
pdf.divider()

pdf.ad_block(
    'OPERATIONAL GAP',
    'Your Campus Feels Connected at Noon. What About 10pm?',
    'The quad that buzzes during the day goes quiet after dark.\nBut students still need to get home.\nsidexside turns those solo walks into shared ones - matching peers heading the same way.\nNo scheduling. No planning. Just open and go.',
    'Day campus and night campus are two different experiences. sidexside bridges the gap - peer-to-peer, on-demand.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'OPERATIONAL GAP',
    'You Have Escorts, Shuttles, and Blue Lights. What\'s Missing?',
    'The peer layer.\nAll that infrastructure is great - but students still walk alone between the gaps.\nsidexside connects them with other women heading the same direction.\nIt complements what you already have.',
    'Great campus services still leave gaps. sidexside fills them with peer-to-peer companionship. No infrastructure. No headcount.',
    'Portrait 1080x1350'
)

# ================================================================
# SECTION 2: STAT-LED ADS
# ================================================================
pdf.add_page()
pdf.section_title('2. THE NUMBERS THEY CAN\'T IGNORE')
pdf.set_font('Helvetica', '', 9)
pdf.set_text_color(120, 120, 120)
pdf.multi_cell(0, 5, 'Data-driven hooks. The stat stops the scroll. The framing makes it their problem. "Your campus" = decision-maker language.')
pdf.ln(4)

pdf.ad_block(
    'STAT HOOK',
    '73% of Women on Your Campus Want One Thing on the Walk Home.',
    'Not a tracking app. Not a panic button.\nJust someone heading the same direction.\nsidexside delivers exactly that - peer-to-peer walking companionship, built for universities.',
    '73% of college women want a walking companion. Not an app. Not a device. Just someone going their way. See how sidexside delivers it.',
    'Portrait 1080x1350 / Square 1080x1080'
)
pdf.divider()

pdf.ad_block(
    'STAT HOOK',
    '52% of Your Students Feel Disconnected After Dark.',
    'That\'s a retention problem.\nStudents who feel disconnected don\'t stay.\nsidexside builds peer connection on campus - one walk at a time.\nOn-demand. Women-only. Privacy-first.',
    '52% of women report disconnection on campus at night. That\'s not just a wellbeing issue - it\'s a retention issue. See how sidexside changes the number.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'STAT HOOK',
    '1 in 3 Students Say Campus Feels Isolating at Night.',
    'What if the walk home felt like a social moment instead?\nsidexside matches women heading the same direction.\nNo planning. No scheduling. Just companionship on demand.',
    '1 in 3 students feel isolated on campus after dark. sidexside turns solo walks into shared ones. See how.',
    'Square 1080x1080'
)
pdf.divider()

pdf.ad_block(
    'STAT HOOK',
    '89% of Students on Large Campuses Wish It Felt Smaller.',
    'sidexside makes a 40,000-student campus feel like a neighborhood.\nPeer-to-peer matches. Real-time connections. One walk at a time.\nThe belonging layer your campus is missing.',
    '89% of students on large campuses want it to feel smaller. sidexside builds that connection - one walk at a time.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'STAT HOOK',
    '67% of Women Have Changed Their Route to Avoid Walking Alone.',
    'What if they didn\'t have to?\nsidexside connects women heading the same direction - so no one reroutes, no one avoids, no one walks alone unless they choose to.',
    '67% of women reroute to avoid solo walks. sidexside gives them a peer heading their way instead. See how it works on campus.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'STAT HOOK + RETENTION',
    'Retention Starts with Belonging. And Belonging Starts on the Walk Home.',
    'Students who feel connected stay.\nStudents who feel isolated transfer.\nsidexside builds organic peer connections across your campus - naturally, nightly, on demand.',
    'Retention and belonging are connected. sidexside creates the peer connections that keep students engaged - one walk at a time.',
    'Portrait 1080x1350'
)

# ================================================================
# SECTION 3: OUTCOME / ASPIRATION ADS
# ================================================================
pdf.add_page()
pdf.section_title('3. THE OUTCOME THEY WANT')
pdf.set_font('Helvetica', '', 9)
pdf.set_text_color(120, 120, 120)
pdf.multi_cell(0, 5, 'Paint the picture of what their campus looks like WITH sidexside. Decision-makers buy outcomes, not features.')
pdf.ln(4)

pdf.ad_block(
    'OUTCOME',
    'What If Every Woman on Campus Had a Walking Buddy?',
    'sidexside makes it possible.\nStudents drop a pin. Find a match. Walk together.\nPeer-to-peer companionship that covers every pathway, every hour.\nNo new staff. No new infrastructure. Deploys in weeks.',
    'What if no woman on your campus had to walk alone? sidexside makes it possible - peer-to-peer, on-demand, deployable in weeks.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'OUTCOME',
    'What Would It Mean If Your Students Actually Looked Forward to the Walk Home?',
    'Right now it\'s a solo commute.\nWith sidexside, it\'s a social moment.\nNew connections. New friendships. A campus that feels connected even after dark.',
    'The walk home can be the loneliest part of campus or the most connected. sidexside turns it into the latter.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'OUTCOME',
    'Add Walking Companions to Your Campus. Without Adding Headcount.',
    'sidexside is peer-to-peer - students helping students.\nNo new hires. No overtime. No scheduling.\nJust an app that matches women heading the same direction.\nDeploys in weeks. Runs on students\' phones.',
    'Peer-to-peer walking companionship that costs less than a single new hire. No infrastructure. No headcount. See how.',
    'Portrait 1080x1350 / Square 1080x1080'
)
pdf.divider()

pdf.ad_block(
    'OUTCOME',
    'A More Connected Campus. No Construction Required.',
    'You don\'t need new infrastructure to make campus feel connected after dark.\nYou need sidexside.\nWomen matched with women. Real-time. On-demand. Privacy-first.\nThe peer layer that runs on students\' phones.',
    'Zero hardware. Zero construction. Full campus coverage. sidexside runs on students\' phones and covers every pathway.',
    'Square 1080x1080'
)
pdf.divider()

pdf.ad_block(
    'OUTCOME',
    'The Walk Between the Library and the Dorm Shouldn\'t Feel Lonely.',
    'For 73% of women on your campus, it does.\nsidexside changes that - connecting students heading the same direction, on demand.\nPeer-to-peer companionship that fits naturally into campus life.',
    'Library to dorm. Dining hall to parking lot. Every walk is better with company. sidexside makes it happen.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'OUTCOME + ZERO FRICTION',
    'One App. Every Pathway. Zero Friction.',
    'sidexside runs on students\' phones.\nNo campus servers. No hardware. No IT tickets.\nJust a peer-to-peer platform that matches women walking the same direction.\nDeploys in weeks. See how it works.',
    'No IT burden. No infrastructure. sidexside runs on students\' phones and covers every pathway on campus. See the 15-min walkthrough.',
    'Square 1080x1080'
)

# ================================================================
# SECTION 4: URGENCY / COMPETITIVE ADS
# ================================================================
pdf.add_page()
pdf.section_title('4. URGENCY & MOMENTUM')
pdf.set_font('Helvetica', '', 9)
pdf.set_text_color(120, 120, 120)
pdf.multi_cell(0, 5, 'Create urgency through semester timelines and competitive positioning. Decision-makers don\'t want to be the last to move.')
pdf.ln(4)

pdf.ad_block(
    'SEMESTER URGENCY',
    'Fall Semester Is 12 Weeks Away. Your Students Will Be Back.',
    '73% of them want a walking companion.\nsidexside deploys in weeks - not months.\nBook a demo now and have it ready for move-in day.',
    'Move-in day is coming. Get sidexside deployed before fall semester starts. 15-min demo - see the timeline.',
    'Portrait 1080x1350 / Square 1080x1080'
)
pdf.divider()

pdf.ad_block(
    'COMPETITIVE MOMENTUM',
    'Universities Are Adding Peer Companionship Technology. Is Yours?',
    'Forward-thinking campuses are already exploring how peer-to-peer solutions can support their students.\nsidexside is the platform built specifically for higher ed.\nSee what they\'re seeing.',
    'Peer-to-peer campus technology is moving fast. See why universities are booking demos with sidexside this semester.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'SEMESTER URGENCY',
    'Don\'t Wait for an Incident. Build Connection Now.',
    'The best time to add peer companionship to your campus was last semester.\nThe second best time is now.\nsidexside deploys in weeks. See how it works.',
    'Proactive beats reactive. sidexside builds organic peer connection across your campus. See how in 15 minutes.',
    'Portrait 1080x1350'
)
pdf.divider()

pdf.ad_block(
    'DEMAND SIGNAL',
    'Your Students Are Already Asking for This.',
    '73% of women want a walking companion on campus.\nThat\'s not a guess - that\'s a demand signal.\nsidexside is the platform that delivers it.\nPeer-to-peer. On-demand. Built for higher ed.',
    'The demand is already there. 73% of women want company on their walk. sidexside meets them where they are.',
    'Square 1080x1080'
)
pdf.divider()

pdf.ad_block(
    'RETENTION URGENCY',
    'Every Semester You Lose Students Who Felt Disconnected.',
    'They don\'t always tell you why.\nBut 52% of women report feeling disconnected on campus after dark.\nsidexside builds the peer connections that make students want to stay.',
    'Disconnection drives attrition. sidexside builds peer connection that supports retention. See the data in a 15-min demo.',
    'Portrait 1080x1350'
)

# ================================================================
# SECTION 5: READY-TO-PASTE META AD SETS
# ================================================================
pdf.add_page()
pdf.section_title('5. READY-TO-PASTE META AD COPY')
pdf.set_font('Helvetica', '', 9)
pdf.set_text_color(120, 120, 120)
pdf.multi_cell(0, 5, 'Copy-paste into Meta Ads Manager. Each includes Headline, Primary Text, Description, and CTA Button.')
pdf.ln(4)

ads = [
    ('Ad 1: The Gap',
     'Headline: Peer Walking Companions for Campus\n'
     'Primary text: Your escort runs until midnight. Your students don\'t stop. '
     'sidexside fills the gap - matching women with women heading the same direction. '
     'Peer-to-peer. On-demand. No infrastructure. No headcount. '
     'See how it works on your campus.\n'
     'Description: 15-min demo. Deploys in weeks.\n'
     'CTA Button: Book Now'),

    ('Ad 2: The Stat',
     'Headline: 73% of Women Want a Walking Companion\n'
     'Primary text: Not a tracking app. Not a panic button. Just someone heading the same way. '
     'sidexside matches women on campus in real time - peer-to-peer, on-demand. '
     'Designed for universities. Deploys in weeks.\n'
     'Description: See how it works in 15 minutes.\n'
     'CTA Button: Book Now'),

    ('Ad 3: The Budget Play',
     'Headline: Full Campus Coverage. Zero Headcount.\n'
     'Primary text: sidexside is peer-to-peer - students connecting with students. '
     'No new hires. No overtime. No scheduling. Just an app that matches women '
     'heading the same direction. Runs on their phones. Covers every pathway.\n'
     'Description: Book a 15-min campus demo.\n'
     'CTA Button: Book Now'),

    ('Ad 4: The Tech Play',
     'Headline: No Servers. No Hardware. Just an App.\n'
     'Primary text: Looking for campus solutions that don\'t add IT burden? '
     'sidexside is mobile-first. Runs on students\' phones. '
     'No campus servers. No hardware installs. Privacy-first. Deployable in weeks.\n'
     'Description: See the architecture in 15 minutes.\n'
     'CTA Button: Learn More'),

    ('Ad 5: The Retention Play',
     'Headline: Retention Starts with Belonging\n'
     'Primary text: Students who feel connected stay. Students who feel isolated transfer. '
     '52% of women feel disconnected on campus after dark. '
     'sidexside builds peer connection - one walk at a time. On-demand. Women-only.\n'
     'Description: See the retention impact. Book a demo.\n'
     'CTA Button: Book Now'),

    ('Ad 6: The Complement',
     'Headline: The Peer Layer Your Campus Is Missing\n'
     'Primary text: Escorts cover routes. Shuttles cover stops. '
     'sidexside covers everything in between - matching women heading the same direction. '
     'It complements what you already offer. No replacing. Just enhancing.\n'
     'Description: 15-min demo. See how it integrates.\n'
     'CTA Button: Book Now'),

    ('Ad 7: The Night Problem',
     'Headline: Your Campus After Dark Needs This\n'
     'Primary text: The campus that feels connected at noon goes quiet at 10pm. '
     'But students still need to get home. sidexside matches women heading the same way - '
     'turning solo walks into shared ones. Peer-to-peer. Real-time.\n'
     'Description: See how it works. Book a demo.\n'
     'CTA Button: Book Now'),

    ('Ad 8: The Fall Deadline',
     'Headline: Ready for Fall Semester?\n'
     'Primary text: Your students will be back in weeks. 73% of women want a walking companion. '
     'sidexside deploys fast - have peer-to-peer companionship ready for move-in day. '
     'No infrastructure. No headcount.\n'
     'Description: Book a demo now. Deploy by fall.\n'
     'CTA Button: Book Now'),

    ('Ad 9: The Aspiration',
     'Headline: What If No Woman Walked Alone on Campus?\n'
     'Primary text: sidexside makes it possible. Women matched with women heading the same direction. '
     'On-demand. Real-time. Privacy-first. The peer companionship layer designed for higher ed.\n'
     'Description: See how it works in 15 minutes.\n'
     'CTA Button: Book Now'),

    ('Ad 10: The Origin',
     'Headline: Built by Women Who Walked Those Paths\n'
     'Primary text: sidexside wasn\'t designed in a boardroom. It was built by women who\'ve walked '
     'those late-night campus paths and wished someone was heading their way. '
     'Now bringing peer-to-peer companionship to universities nationwide.\n'
     'Description: Book a demo. See the platform.\n'
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
# SECTION 6: ON-IMAGE TEXT FOR AD CREATIVES
# ================================================================
pdf.add_page()
pdf.section_title('6. ON-IMAGE TEXT FOR AD CREATIVES')
pdf.set_font('Helvetica', '', 9)
pdf.set_text_color(120, 120, 120)
pdf.multi_cell(0, 5, 'Text that goes ON the creative image. Short, bold, scannable. Max 20% text for Meta. Every one ends with Book a Demo.')
pdf.ln(4)

pdf.sub_section('Stat-Led Creatives')
texts = [
    ('73% of women on campus\nwant a walking companion.\n\nYour campus can deliver.\n\nBook a Demo',
     'Blue gradient bg, yellow "73%"'),
    ('52% feel disconnected\nafter dark.\n\nThat\'s a retention problem.\n\nBook a Demo',
     'Black bg, blue accent'),
    ('1 in 3 students\nsay campus feels isolating\nat night.\n\nBook a Demo',
     'Dark bg, yellow stat number'),
    ('89% on large campuses\nwish it felt smaller.\n\nsidexside makes it.\n\nBook a Demo',
     'Blue gradient, white text'),
]
for text, note in texts:
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(0, 5, text, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('Helvetica', 'I', 8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 5, f'[{note}]', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)
    pdf.divider()

pdf.sub_section('Gap-Exposing Creatives')
texts = [
    ('Your escort stops at midnight.\nYour students don\'t.\n\nBook a Demo',
     'Campus night photo bg, dark overlay'),
    ('The shuttle covers 4 stops.\nYour students walk everywhere.\n\nBook a Demo',
     'Aerial campus photo bg'),
    ('Blue light phones\ndon\'t walk students home.\n\nsidexside does.\n\nBook a Demo',
     'Night campus pathway photo'),
    ('Your campus at noon:\nconnected.\n\nYour campus at 10pm:\nempty.\n\nBook a Demo',
     'Split visual - day/night'),
    ('Great infrastructure.\nBut students still walk alone.\n\nThe peer layer is missing.\n\nBook a Demo',
     'Campus buildings photo, overlay'),
]
for text, note in texts:
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(0, 5, text, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('Helvetica', 'I', 8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 5, f'[{note}]', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)
    pdf.divider()

pdf.sub_section('Outcome Creatives')
texts = [
    ('What if every woman\non campus had a\nwalking buddy?\n\nBook a Demo',
     'Golden hour campus photo, warm overlay'),
    ('Add walking companions.\nNo headcount.\nNo infrastructure.\n\nBook a Demo',
     'Clean blue gradient'),
    ('One app.\nEvery pathway.\nZero friction.\n\nBook a Demo',
     'Aerial quad photo'),
    ('Drop a pin.\nFind a match.\nWalk together.\n\nBook a Demo',
     '3-step layout, branded'),
    ('The walk home,\ntogether.\n\nPeer companionship\nfor campus.\n\nBook a Demo',
     'Two women walking, campus pathway photo'),
    ('Peer-to-peer.\nOn-demand.\nPrivacy-first.\n\nBuilt for your campus.\n\nBook a Demo',
     'Minimal, brand blue bg'),
]
for text, note in texts:
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(0, 5, text, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('Helvetica', 'I', 8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 5, f'[{note}]', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)
    pdf.divider()

pdf.sub_section('Urgency Creatives')
texts = [
    ('Fall semester is coming.\n73% of women want this.\n\nDeploys in weeks.\n\nBook a Demo',
     'Bold, time-sensitive'),
    ('Your students are back\nin 12 weeks.\n\nAre you ready?\n\nBook a Demo',
     'Campus move-in style photo'),
    ('Don\'t wait for an incident.\nBuild connection now.\n\nBook a Demo',
     'Professional, proactive tone'),
]
for text, note in texts:
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(0, 5, text, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('Helvetica', 'I', 8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 5, f'[{note}]', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)
    pdf.divider()

# -- OUTPUT --
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sidexside-b2b-meta-ad-copy.pdf")
pdf.output(out_path)
print(f"PDF generated: {out_path}")
