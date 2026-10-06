# -*- coding: utf-8 -*-
"""Happexhibition site generator v2 — EN (root) + TH (/th/) + SEO."""
import os, html, json

OUT = "/Users/pokkritjeerapat/Desktop/happexhibition company profile/happexhibition-website"
BASE = "https://happexhibition.com"
import datetime as _dt, time as _time
LASTMOD = _dt.date.today().isoformat()
ASSETV = str(int(_time.time()))   # change if hosted elsewhere (e.g. https://user.github.io/repo)

LINE = "https://line.me/R/ti/p/@happexhibition"
FB = "https://www.facebook.com/profile.php?id=61593124306637&mibextid=wwXIfr"
IG = "https://www.instagram.com/happexhibition/"
MAPS = "https://maps.app.goo.gl/vSq9KAFU9sLEjzBo8"
YT = "https://youtu.be/eJvwgSBmA-Q"
TEL = "+66 81-488-0475"
TELHREF = "tel:+66814880475"
MAIL = "nathawat.j@happexhibition.com"
APPLY_MAILTO = "mailto:pakavadee.c@happexhibition.co.th,nathawat.j@happexhibition.com?subject=Job%20Application%20%E2%80%94%20Happ%20Exhibition"
CONTACT_MAILTO = f"mailto:{MAIL}?subject=Website%20Enquiry%20%E2%80%94%20Happ%20Exhibition"
ARROW = '<span class="arrow">→</span>'

CLIENT_LOGOS = ["chanel","clinique","dolce","gucci","hourglass","issey","lamerr","narciso","olay",
                "origins","pandora","shieshedo","sk2","tomforrd","bobbibrown","cleaclea","eliesaab","harnn",
                "paulsmith","panpuri","sunnies","samsung","burberry","polo","vancleef","charlottetilbury",
                "bluebottle","anotherstory","philips","popmart"]
# per-logo display height (px) so every mark carries equal visual weight,
# and real brand names for alt text
LOGO_H = {"chanel":26,"clinique":29,"dolce":20,"gucci":25,"hourglass":23,"issey":18,
          "lamerr":28,"narciso":18,"olay":35,"origins":22,"pandora":29,"shieshedo":26,
          "sk2":42,"tomforrd":25,"bobbibrown":22,"cleaclea":31,"eliesaab":21,"harnn":18,
          "paulsmith":27,"panpuri":28,"sunnies":20,"samsung":32,"burberry":26,"polo":17,
          "vancleef":22,"charlottetilbury":25,"bluebottle":54,"anotherstory":19,"philips":26,"popmart":24}
LOGO_NAME = {"chanel":"Chanel","clinique":"Clinique","dolce":"Dolce & Gabbana","gucci":"Gucci",
             "hourglass":"Hourglass","issey":"Issey Miyake","lamerr":"La Mer","narciso":"Narciso Rodriguez",
             "olay":"Olay","origins":"Origins","pandora":"Pandora","shieshedo":"Shiseido","sk2":"SK-II",
             "tomforrd":"Tom Ford","bobbibrown":"Bobbi Brown","cleaclea":"Clé de Peau Beauté",
             "eliesaab":"Elie Saab","harnn":"HARNN",
             "paulsmith":"Paul Smith","panpuri":"Pañpuri","sunnies":"Sunnies Studios","samsung":"Samsung",
             "burberry":"Burberry","polo":"Ralph Lauren","vancleef":"Van Cleef & Arpels",
             "charlottetilbury":"Charlotte Tilbury","bluebottle":"Blue Bottle Coffee",
             "anotherstory":"Another Story","philips":"Philips","popmart":"Pop Mart"}
CLIENT_TEXT = []  # every referenced client now has its original logo file

# ==================== UI STRINGS ====================
UI = {
"en": dict(
  nav_about="About", nav_services="Services", nav_works="Works", nav_news="News",
  nav_careers="Careers", nav_contact="Contact", nav_home="Home",
  quote="Get a Quote", quote_line="Get a Quote — add us on LINE",
  tagline="Making Retail Architecture a Reality.",
  all_works="All Works", view_index="View the index",
  cat_retail="Luxury Retail & Beauty", cat_hosp="Hospitality", cat_corp="Corporate & Commercial",
  cat_fnb="F&B & Lifestyle", cat_gal="Galleries, Museums & Exhibitions",
  sub_retail="Our heritage", sub_hosp="New market", sub_corp="Samsung + more",
  sub_fnb="Next frontier", sub_gal="In our name",
  positioning="For twenty years, the world's most demanding luxury houses have trusted us to build the spaces where their brands live. Today we bring that same standard to every environment where detail decides everything.",
  more_about="MORE ABOUT US", our_services="OUR SERVICES",
  services_h="From drawing to standing finished.", all_services="ALL SERVICES",
  works_eyebrow="WORKS", works_h="Proven where standards are highest.", view_more="VIEW MORE",
  stat1="YEARS OF CONTINUOUS OPERATION", stat1s="Founded Bangkok, March 2004",
  stat2="PEOPLE", stat2s="120 production craftsmen · 60 design & office",
  stat3="SQM ACROSS THREE FACTORIES", stat3s="Pathumthani, 40 minutes from Bangkok",
  stat4="PROJECTS DELIVERED PER YEAR", stat4s="To luxury-house standards",
  featured="FEATURED PROJECT", years_partner="YEARS PARTNERSHIP", delivered="DELIVERED", sqm="SQM",
  featured_body="More than half our revenue has come from a single relationship sustained for over a decade. That kind of partnership is only retained through thousands of flawless deliveries — fragrance walls, fibre-optic ceilings and millimetre counters, installed overnight inside Bangkok's newest landmark.",
  view_case="View Case Study", how_we_work="HOW WE WORK", process_h="One accountable team, five steps.",
  our_process="OUR PROCESS", news_eyebrow="NEWS & ACTIVITY", news_h="What we've been building.", all_news="ALL NEWS",
  careers_eyebrow="CAREERS", careers_band="Join the quiet company behind the loudest brands.",
  view_openings="View Openings", follow="FOLLOW THE BUILD", fb_h="Happexhibition on Facebook",
  cta_eyebrow="LET'S BUILD SOMETHING THAT LASTS", cta_h="Planning your next space?",
  cta_sub="Talk to the team that builds for the world's hardest judges.", cta_call="Call",
  f_explore="Explore", f_company="Company", f_works="Works", f_office="Head Office & Factories",
  f_line="Add us on LINE", f_privacy="Privacy Policy (PDPA)", f_cookies="Cookie Preferences",
  addr_html="Happ Exhibition Co., Ltd.<br>52/8 Moo 11, Ladsawai, Lamlookka,<br>Pathumthani 12150, Thailand",
  about_eyebrow="ABOUT HAPPEXHIBITION", about_h="The quiet company behind<br>the loudest brands.",
  overview_eyebrow="COMPANY OVERVIEW", overview_h="Precisely, layer by layer.",
  overview_p1="Happexhibition was founded in Bangkok in March 2004 with a simple conviction: that Thailand could build retail environments to the same standard the great European maisons expect at home. We started with 3D modelling and technical detailing when few others offered it, earned our first luxury commissions, and grew the way we build — precisely, layer by layer.",
  overview_p2="Twenty years later, we are a 180-person design-build fabricator with three factories in Pathumthani totalling 11,300 square metres, purpose-built workshops for wood, metal, glass and paint, and an in-house installation force trusted to work overnight inside Asia's busiest malls.",
  pullquote="“That heritage is our proof,<br>not our boundary.”",
  timeline_eyebrow="TIMELINE", timeline_h="Twenty years, same hands.",
  whyus_eyebrow="WHY US", whyus_h="The luxury standard is not a style. It is a system.",
  leadership_eyebrow="LEADERSHIP", leadership_h="The people who hold the standard.",
  factory_eyebrow="THE FACTORY", factory_h="11,300 square metres of controlled quality.",
  watch_tour="WATCH THE FACTORY TOUR", clients_eyebrow="CLIENTS", clients_h="Judge us by the company we keep.",
  svc_eyebrow="SERVICES", svc_h="From drawing to standing finished.",
  svc_sub="One factory. One standard. One accountable team.",
  cap_h="Capabilities at a glance", faq_h="Questions we hear often",
  works_idx_h="Judge us by the company we keep —<br>and what they trusted us to build.",
  all="All", projects_word="projects", project_word="project",
  empty_h="No projects in this category — yet.",
  empty_p="We are bringing our overnight-install discipline here now. Talk to us about being the first.",
  talk_line="Talk to us on LINE",
  client="Client", venue="Venue", city="City", year="Year", area="Area", scope="Scope",
  scope_v="Fabrication · fit-out · overnight installation", bangkok="Bangkok, Thailand",
  prev="PREVIOUS", next="NEXT", more_retail="More in Luxury Retail & Beauty",
  disruption="DISRUPTION TO MALL", qc_shipped="QC TRAIL SHIPPED", sqm_delivered="SQM DELIVERED",
  min_read="MIN READ", share="Share:", copy_link="Copy link",
  careers_h="Craft knowledge compounds.<br>Come compound with us.",
  why_stay="Why people stay for decades", open_roles="Open roles",
  role_ft="Full-time", apply_h="Apply for this role", apply="Apply",
  attach_note="↑ Attach your portfolio to the email draft that opens · PDF · max 25 MB",
  name="Name", company="Company", email="Email", phone="Phone", message="Message",
  ph_name="Your full name", ph_company="Company name", ph_email="name@company.com",
  ph_phone="+66 8x xxx xxxx", ph_msg="How can we help?", ph_exp="Tell us about your experience",
  reply_1d="We reply within 1 business day.", send="Send Message",
  contact_eyebrow="CONTACT", contact_h="Let's build something that lasts.",
  ceo_line="Nathawat Jeerapat (William J.) — Chief Executive Officer",
  hours="Hours: Mon–Sat 8:30–17:30", scan="Scan to chat on LINE",
  nf_h="This page moved — or never shipped QC.", back_home="Back to Home", view_works="View Works",
  map_alt="Map — Happ Exhibition, Ladsawai, Lam Luk Ka",
  role_meta="Design · Pathumthani · Full-time",
),
"th": dict(
  nav_about="เกี่ยวกับเรา", nav_services="บริการ", nav_works="ผลงาน", nav_news="ข่าวสาร",
  nav_careers="ร่วมงานกับเรา", nav_contact="ติดต่อเรา", nav_home="หน้าแรก",
  quote="ขอใบเสนอราคา", quote_line="ขอใบเสนอราคา — เพิ่มเพื่อนใน LINE",
  tagline="ออกแบบ ผลิต ติดตั้ง ดูแล — ครบจบในที่เดียว",
  all_works="ผลงานทั้งหมด", view_index="ดูผลงานทั้งหมด",
  cat_retail="รีเทลหรูและบิวตี้", cat_hosp="โรงแรมและฮอสพิทัลลิตี้", cat_corp="สำนักงานและองค์กร",
  cat_fnb="ร้านอาหารและไลฟ์สไตล์", cat_gal="แกลเลอรี พิพิธภัณฑ์ และนิทรรศการ",
  sub_retail="รากฐานของเรา", sub_hosp="ตลาดใหม่", sub_corp="Samsung และอีกมากมาย",
  sub_fnb="ก้าวต่อไปของเรา", sub_gal="อยู่ในชื่อของเรา",
  positioning="ตลอด 20 ปี ลักชัวรีเฮาส์ชั้นนำของโลกไว้วางใจให้เราสร้างพื้นที่ที่แบรนด์ของพวกเขามีชีวิต วันนี้เรานำมาตรฐานเดียวกัน — โรงงานเดียวกัน ช่างฝีมือคนเดิม วินัยเดียวกัน — มาสู่ทุกพื้นที่ที่รายละเอียดคือทุกสิ่ง",
  more_about="เกี่ยวกับเราเพิ่มเติม", our_services="บริการของเรา",
  services_h="จากแบบร่างสู่งานเสร็จสมบูรณ์", all_services="บริการทั้งหมด",
  works_eyebrow="ผลงาน", works_h="พิสูจน์แล้วในมาตรฐานที่สูงที่สุด", view_more="ดูเพิ่มเติม",
  stat1="ปีที่ดำเนินงานต่อเนื่อง", stat1s="ก่อตั้งที่กรุงเทพฯ มีนาคม 2547",
  stat2="บุคลากร", stat2s="ช่างฝีมือฝ่ายผลิต 120 คน · ฝ่ายออกแบบและสำนักงาน 60 คน",
  stat3="ตร.ม. รวม 3 โรงงาน", stat3s="ปทุมธานี ห่างจากใจกลางกรุงเทพฯ 40 นาที",
  stat4="โปรเจกต์ที่ส่งมอบต่อปี", stat4s="ด้วยมาตรฐานระดับลักชัวรีเฮาส์",
  featured="โปรเจกต์เด่น", years_partner="ปีแห่งความไว้วางใจ", delivered="ส่งมอบ", sqm="ตร.ม.",
  featured_body="รายได้กว่าครึ่งของเรามาจากความสัมพันธ์เดียวที่ยาวนานกว่าทศวรรษ ความไว้วางใจเช่นนี้รักษาไว้ได้ด้วยการส่งมอบที่ไร้ที่ติหลายพันครั้ง — ผนังน้ำหอม เพดานไฟเบอร์ออปติก และเคาน์เตอร์ความละเอียดระดับมิลลิเมตร ติดตั้งข้ามคืนในแลนด์มาร์กใหม่ล่าสุดของกรุงเทพฯ",
  view_case="ดูกรณีศึกษา", how_we_work="วิธีการทำงานของเรา", process_h="ทีมเดียวที่รับผิดชอบทั้งหมด ใน 5 ขั้นตอน",
  our_process="ขั้นตอนการทำงาน", news_eyebrow="ข่าวสารและกิจกรรม", news_h="สิ่งที่เรากำลังสร้าง", all_news="ข่าวทั้งหมด",
  careers_eyebrow="ร่วมงานกับเรา", careers_band="ร่วมงานกับบริษัทเงียบ ๆ เบื้องหลังแบรนด์ที่ดังที่สุด",
  view_openings="ดูตำแหน่งงาน", follow="ติดตามงานสร้างของเรา", fb_h="Happexhibition บน Facebook",
  cta_eyebrow="มาสร้างสิ่งที่ยั่งยืนไปด้วยกัน", cta_h="กำลังวางแผนพื้นที่ถัดไปของคุณ?",
  cta_sub="คุยกับทีมที่สร้างงานให้ผู้ตรวจสอบที่เข้มงวดที่สุดในโลก", cta_call="โทร",
  f_explore="เมนู", f_company="บริษัท", f_works="ผลงาน", f_office="สำนักงานใหญ่และโรงงาน",
  f_line="เพิ่มเพื่อนใน LINE", f_privacy="นโยบายความเป็นส่วนตัว (PDPA)", f_cookies="การตั้งค่าคุกกี้",
  addr_html="Happ Exhibition Co., Ltd.<br>52/8 หมู่ 11 ต.ลาดสวาย อ.ลำลูกกา<br>จ.ปทุมธานี 12150 ประเทศไทย",
  about_eyebrow="เกี่ยวกับ HAPPEXHIBITION", about_h="บริษัทเงียบ ๆ<br>เบื้องหลังแบรนด์ที่ดังที่สุด",
  overview_eyebrow="ภาพรวมบริษัท", overview_h="อย่างประณีต ทีละชั้น",
  overview_p1="Happexhibition ก่อตั้งขึ้นที่กรุงเทพฯ ในเดือนมีนาคม 2547 ด้วยความเชื่อที่เรียบง่าย: ประเทศไทยสามารถสร้างพื้นที่รีเทลได้ในมาตรฐานเดียวกับที่เมซงชั้นนำของยุโรปคาดหวังในบ้านของตนเอง เราเริ่มจากงานโมเดล 3 มิติและแบบเทคนิคในยุคที่แทบไม่มีใครทำ ได้รับความไว้วางใจจากลักชัวรีแบรนด์แรก ๆ และเติบโตแบบเดียวกับที่เราสร้างงาน — อย่างประณีต ทีละชั้น",
  overview_p2="ยี่สิบปีต่อมา เราคือผู้ผลิตแบบดีไซน์-บิลด์ที่มีบุคลากร 180 คน โรงงาน 3 แห่งในปทุมธานีรวม 11,300 ตารางเมตร เวิร์กช็อปเฉพาะทางสำหรับงานไม้ โลหะ กระจก และงานสี พร้อมทีมติดตั้งของเราเองที่ได้รับความไว้วางใจให้ทำงานข้ามคืนในห้างที่พลุกพล่านที่สุดของเอเชีย",
  pullquote="“มรดกนั้นคือข้อพิสูจน์ของเรา<br>ไม่ใช่ขอบเขตของเรา”",
  timeline_eyebrow="เส้นทางของเรา", timeline_h="ยี่สิบปี ช่างฝีมือคนเดิม",
  whyus_eyebrow="ทำไมต้องเรา", whyus_h="มาตรฐานลักชัวรีไม่ใช่สไตล์ แต่คือระบบ",
  leadership_eyebrow="ทีมผู้บริหาร", leadership_h="ผู้ที่รักษามาตรฐานของเรา",
  factory_eyebrow="โรงงานของเรา", factory_h="คุณภาพที่ควบคุมได้บน 11,300 ตารางเมตร",
  watch_tour="ชมวิดีโอทัวร์โรงงาน", clients_eyebrow="ลูกค้าของเรา", clients_h="ตัดสินเราจากแบรนด์ที่เลือกเรา",
  svc_eyebrow="บริการ", svc_h="จากแบบร่างสู่งานเสร็จสมบูรณ์",
  svc_sub="หนึ่งโรงงาน หนึ่งมาตรฐาน หนึ่งทีมที่รับผิดชอบ",
  cap_h="ขีดความสามารถของเรา", faq_h="คำถามที่พบบ่อย",
  works_idx_h="ตัดสินเราจากแบรนด์ที่เลือกเรา —<br>และสิ่งที่พวกเขาไว้วางใจให้เราสร้าง",
  all="ทั้งหมด", projects_word="โปรเจกต์", project_word="โปรเจกต์",
  empty_h="ยังไม่มีโปรเจกต์ในหมวดนี้",
  empty_p="เรากำลังนำวินัยการติดตั้งข้ามคืนของเรามาสู่หมวดนี้ คุยกับเราเพื่อเป็นโปรเจกต์แรก",
  talk_line="คุยกับเราทาง LINE",
  client="ลูกค้า", venue="สถานที่", city="เมือง", year="ปี", area="พื้นที่", scope="ขอบเขตงาน",
  scope_v="งานผลิต · ตกแต่งภายใน · ติดตั้งข้ามคืน", bangkok="กรุงเทพฯ ประเทศไทย",
  prev="ก่อนหน้า", next="ถัดไป", more_retail="ผลงานอื่นในหมวดรีเทลหรูและบิวตี้",
  disruption="การรบกวนห้าง", qc_shipped="ขั้นตอน QC พร้อมเอกสาร", sqm_delivered="ตร.ม. ที่ส่งมอบ",
  min_read="นาที", share="แชร์:", copy_link="คัดลอกลิงก์",
  careers_h="ความรู้เชิงช่างยิ่งสั่งสมยิ่งลึก<br>มาสั่งสมไปด้วยกัน",
  why_stay="เหตุผลที่ทีมของเราอยู่กันเป็นสิบปี", open_roles="ตำแหน่งที่เปิดรับ",
  role_ft="งานประจำ", apply_h="สมัครตำแหน่งนี้", apply="สมัครงาน",
  attach_note="↑ แนบพอร์ตโฟลิโอในอีเมลที่เปิดขึ้น · PDF · ไม่เกิน 25 MB",
  name="ชื่อ-นามสกุล", company="บริษัท", email="อีเมล", phone="โทรศัพท์", message="ข้อความ",
  ph_name="ชื่อ-นามสกุลของคุณ", ph_company="ชื่อบริษัท", ph_email="name@company.com",
  ph_phone="+66 8x xxx xxxx", ph_msg="ให้เราช่วยอะไรได้บ้าง?", ph_exp="เล่าประสบการณ์ของคุณให้เราฟัง",
  reply_1d="เราตอบกลับภายใน 1 วันทำการ", send="ส่งข้อความ",
  contact_eyebrow="ติดต่อเรา", contact_h="มาสร้างสิ่งที่ยั่งยืนไปด้วยกัน",
  ceo_line="Nathawat Jeerapat (William J.) — ประธานเจ้าหน้าที่บริหาร (CEO)",
  hours="เวลาทำการ: จันทร์–เสาร์ 8:30–17:30", scan="สแกนเพื่อแชทกับเราใน LINE",
  nf_h="หน้านี้ถูกย้าย — หรือยังไม่ผ่าน QC", back_home="กลับหน้าแรก", view_works="ดูผลงาน",
  map_alt="แผนที่ — แฮพ เอ็กซิบิชั่น ลาดสวาย ลำลูกกา",
  role_meta="ฝ่ายออกแบบ · ปทุมธานี · งานประจำ",
),
}

# ==================== CONTENT DATA (EN + TH) ====================
PROJECTS = [
 dict(slug="chanel-emsphere", title="Chanel @ Emsphere", client="Chanel", venue="Emsphere", year="2025", sqm="99",
      hero="chanel-hero", d1="chanel-counter", d2="chanel-stools", plan=None,
      narr_en="A decade-long partnership, delivered again. This fragrance-and-beauty environment pairs black millwork with a fibre-optic ceiling detail — engineered in 3D, pre-assembled at the factory, and installed overnight inside Bangkok's newest retail landmark. The boutique opened for business on schedule, with zero disruption to the operating mall.",
      narr_th="ความไว้วางใจที่ยาวนานกว่าทศวรรษ ส่งมอบอีกครั้ง พื้นที่น้ำหอมและบิวตี้แห่งนี้ผสานงานไม้สีดำเข้ากับรายละเอียดเพดานไฟเบอร์ออปติก — ออกแบบด้วยระบบ 3 มิติ ประกอบทดลองที่โรงงาน และติดตั้งข้ามคืนในแลนด์มาร์กรีเทลใหม่ล่าสุดของกรุงเทพฯ บูติกเปิดให้บริการตรงตามกำหนด โดยไม่รบกวนการดำเนินงานของห้างแม้แต่น้อย"),
 dict(slug="gucci-mega-bangna", title="Gucci @ Mega Bangna", client="Gucci", venue="Mega Bangna", year="2025", sqm="50",
      hero="gucci-megabangna-front", d1="gucci-megabangna-int", d2=None, plan=None,
      narr_en="Gucci Beauty in blush pink: an illuminated portal facade, a curved central counter and backlit display walls across 50 square metres at Mega Bangna. Millimetre-tolerance casework and chemical-resistant finishes, fabricated in Pathumthani and installed overnight inside the live mall.",
      narr_th="Gucci Beauty ในโทนชมพูบลัช: ซุ้มทางเข้าเรืองแสง เคาน์เตอร์กลางทรงโค้ง และผนังดิสเพลย์ไฟแบ็คไลท์ บนพื้นที่ 50 ตารางเมตรที่เมกาบางนา งานตู้ความละเอียดระดับมิลลิเมตรและผิวเคลือบทนสารเคมี ผลิตที่ปทุมธานีและติดตั้งข้ามคืนภายในห้างที่เปิดให้บริการตามปกติ"),
 dict(slug="burberry-gucci-dusit-central-park", title="Burberry & Gucci @ Dusit Central Park", client="Burberry & Gucci", venue="Dusit Central Park", year="2026", sqm="115",
      hero="burberry-gucci-front", d1="burberry-gucci-counter", d2="burberry-gucci-corner", plan=None,
      narr_en="Two houses, one garden. Inside Dusit Central Park's Olfactory Garden we delivered a dual-brand fragrance environment — Burberry's warm sand-toned arcade flowing into Gucci's celadon corner. 115 square metres of curved millwork, backlit vitrines and integrated testers, built and QC'd as one seamless environment.",
      narr_th="สองเมซง หนึ่งสวนหอม ภายใน Olfactory Garden ของดุสิต เซ็นทรัล พาร์ค เราส่งมอบพื้นที่น้ำหอมสองแบรนด์ — อาร์เคดโทนทรายอบอุ่นของ Burberry ไหลต่อเนื่องสู่มุมสีเซลาดอนของ Gucci งานไม้ทรงโค้ง ตู้โชว์ไฟแบ็คไลท์ และจุดเทสเตอร์ในตัว รวม 115 ตารางเมตร สร้างและตรวจสอบคุณภาพเป็นงานเดียวที่ไร้รอยต่อ"),
 dict(slug="paul-smith-central-village", title="Paul Smith @ Central Village", client="Paul Smith", venue="Central Village", year="2026", sqm="110",
      hero="paulsmith-ext", d1="paulsmith-int", d2="works/paul-smith-central-village/thai-gable-exterior", plan=None,
      narr_en="Colour-critical joinery for a British house — signature-stripe fitting rooms, gallery walls and display tables, fabricated in Pathumthani and installed to the outlet village's opening programme.",
      narr_th="งานไม้ที่ความแม่นยำของสีคือหัวใจ สำหรับแบรนด์อังกฤษ — ห้องลองเสื้อลายแถบซิกเนเจอร์ ผนังแกลเลอรี และโต๊ะดิสเพลย์ ผลิตที่ปทุมธานีและติดตั้งให้ทันกำหนดเปิดของเอาต์เล็ตวิลเลจ"),
 dict(slug="shiseido-centralworld", title="Shiseido @ CentralWorld", client="Shiseido", venue="CentralWorld", year="2026", sqm="34",
      hero="shiseido-wide", d1="shiseido-counter", d2="works/shiseido-centralworld/counter-hall", plan=None,
      narr_en="Beauty-counter craft on Thailand's busiest retail floor: illuminated red canopies, curved casework and integrated testers — installed overnight while CentralWorld kept trading.",
      narr_th="งานเคาน์เตอร์บิวตี้บนพื้นที่รีเทลที่พลุกพล่านที่สุดของประเทศไทย: หลังคาสีแดงเรืองแสง งานตู้โค้ง และจุดเทสเตอร์ในตัว — ติดตั้งข้ามคืนขณะที่เซ็นทรัลเวิลด์ยังเปิดให้บริการตามปกติ"),
 dict(slug="panpuri-one-bangkok", title="Panpuri @ One Bangkok", client="Panpuri", venue="One Bangkok", year="2026", sqm="115",
      hero="works/panpuri-one-bangkok/storefront", d1="works/panpuri-one-bangkok/oculus-interior", d2=None, plan=None,
      narr_en="Thai luxury wellness built to global-house tolerances: warm neutral millwork, museum-grade display niches and a treatment-room package inside Bangkok's newest landmark district.",
      narr_th="เวลเนสลักชัวรีสัญชาติไทย สร้างด้วยความละเอียดระดับแบรนด์โลก: งานไม้โทนอบอุ่น ช่องดิสเพลย์เกรดพิพิธภัณฑ์ และห้องทรีตเมนต์ครบชุด ภายในย่านแลนด์มาร์กใหม่ล่าสุดของกรุงเทพฯ"),
 dict(slug="cpb-dusit-central-park", title="Clé de Peau Beauté @ Dusit Central Park", client="Clé de Peau Beauté", venue="Dusit Central Park", year="2026", sqm="115",
      hero="cpb-dusit-front", d1="cpb-dusit-side", d2="works/cpb-dusit-central-park/facade", plan=None,
      narr_en="A maison of skin arrives at Bangkok's newest landmark. Bronze fluted columns, a jewel-faceted centre wall and a sculpted island counter — 115 square metres of museum-grade finish, engineered to survive alcohol-based product, ten thousand hands and daily cleaning, delivered to Clé de Peau Beauté's exacting global standard.",
      narr_th="เมซงแห่งผิวพรรณมาถึงแลนด์มาร์กใหม่ล่าสุดของกรุงเทพฯ เสาบรอนซ์เซาะร่อง ผนังกลางลายเหลี่ยมอัญมณี และเคาน์เตอร์กลางทรงประติมากรรม — งานเก็บผิวเกรดพิพิธภัณฑ์ 115 ตารางเมตร ออกแบบให้ทนผลิตภัณฑ์แอลกอฮอล์ มือนับหมื่น และการทำความสะอาดทุกวัน ส่งมอบตามมาตรฐานระดับโลกอันเข้มงวดของ Clé de Peau Beauté"),
 dict(slug="popmart-maya-chiangmai", title="Pop Mart @ Maya Chiangmai", client="Pop Mart", venue="Maya Chiangmai", year="2026", sqm="366",
      city_en="Chiang Mai, Thailand", city_th="เชียงใหม่ ประเทศไทย",
      hero="popmart-front", d1="works/popmart-maya-chiangmai/crybaby-interior", d2="works/popmart-maya-chiangmai/badge-wall", plan=None,
      narr_en="Our largest playful-retail build yet: 366 square metres at Maya Chiangmai. A curved stainless facade, an art-toy display theatre and warm timber gondolas — serious fabrication behind joyful retail, delivered outside Bangkok with the same 5-step QC and overnight-installation discipline as our luxury-house work.",
      narr_th="งานรีเทลสายสนุกที่ใหญ่ที่สุดของเรา: 366 ตารางเมตรที่เมญ่า เชียงใหม่ เปลือกอาคารสเตนเลสทรงโค้ง พื้นที่ดิสเพลย์อาร์ตทอย และกอนโดลาไม้โทนอบอุ่น — งานผลิตจริงจังเบื้องหลังรีเทลแสนสนุก ส่งมอบนอกกรุงเทพฯ ด้วยวินัย QC 5 ขั้นตอนและการติดตั้งข้ามคืนเดียวกับงานลักชัวรีเฮาส์ของเรา"),
]

# ==================== NEW WORKS (archive import, Oct 2026) ====================
# Facts policy: no sqm anywhere (owner will never supply it); scope is end-to-end
# per owner; year only where the archive folder name states one or owner supplied.
SCOPE_FULL = ("End-to-end: design · fabrication · installation",
              "ครบวงจร: ออกแบบ · ผลิต · ติดตั้ง")
SCOPE_VM = ("Visual merchandising: fabrication & installation",
            "Visual Merchandising: ผลิตและติดตั้ง")
CATKEY = {"luxury-retail":"cat_retail","hospitality":"cat_hosp","corporate":"cat_corp",
          "fnb":"cat_fnb","galleries":"cat_gal"}

from works_data import NEWP, GROUPS  # archive-import data (same folder as this script)

def all_meta(lang):
    """one ordered list of every project (old 8 + new), drives works grid, prev/next, related"""
    L = UI[lang]
    out = []
    for p in PROJECTS:
        out.append(dict(slug=p["slug"], title=p["title"], cat="luxury-retail", hero=p["hero"],
                        meta=f'{p["client"]} · {p["venue"]} · {p["year"]} · {p["sqm"]} {L["sqm"].lower() if lang=="en" else L["sqm"]}'))
    for p in NEWP:
        yr = f' · {p["year"]}' if p.get("year") else ""
        ven = p.get("venue_th") if (lang == "th" and p.get("venue_th")) else p["venue"]
        out.append(dict(slug=p["slug"], title=p["title"], cat=p["cat"], hero=f'works/{p["slug"]}/{p["imgs"][0][0]}',
                        meta=f'{p["client"]} · {ven}{yr}'))
    for g in GROUPS:
        out.append(dict(slug=g["slug"], title=g["title"], cat=g["cat"], hero=f'works/{g["slug"]}/{g["hero"]}',
                        meta=g["meta_th"] if lang == "th" else g["meta_en"]))
    return out

ARTICLES = [
 dict(slug="h3-factory", cat="FACTORY", cat_th="โรงงาน", date="12 JAN 2026", date_th="12 ม.ค. 2569", iso="2026-01-12", mins=4, img="factory-exterior",
      t_en="H3 turns three: inside our 6,000 sqm third factory",
      t_th="ครบ 3 ปี H3: เจาะลึกโรงงานแห่งที่สามขนาด 6,000 ตร.ม. ของเรา",
      q_en="Materials arrive raw; environments leave finished, packed and sequenced for installation.",
      q_th="วัตถุดิบเข้ามาแบบดิบ ๆ แต่ออกไปเป็นพื้นที่สำเร็จ แพ็กเรียงลำดับพร้อมติดตั้ง",
      b1_en="Opened in 2023, H3 completed the Pathumthani campus — 11,300 square metres across three facilities, bringing every trade under one standard and one QC regime.",
      b1_th="เปิดใช้งานในปี 2566 โรงงาน H3 ทำให้แคมปัสปทุมธานีของเราสมบูรณ์ — พื้นที่รวม 11,300 ตารางเมตรใน 3 อาคาร รวมทุกงานช่างไว้ภายใต้มาตรฐานเดียวและระบบ QC เดียว",
      b2_en="From the corten-clad exterior to the pre-assembly floor inside, H3 was purpose-built for the way we work: materials arrive raw and leave as finished environments, packed in install sequence.",
      b2_th="ตั้งแต่เปลือกอาคารเหล็กคอร์เทนไปจนถึงพื้นที่ประกอบทดลองด้านใน H3 ถูกสร้างขึ้นเพื่อวิธีการทำงานของเราโดยเฉพาะ: วัตถุดิบเข้ามาแบบดิบ ๆ และออกไปเป็นพื้นที่สำเร็จรูป แพ็กตามลำดับการติดตั้ง",
      grid=["laser-cut","spray"]),
 dict(slug="overnight-emsphere", cat="PROJECTS", cat_th="โปรเจกต์", date="9 FEB 2026", date_th="9 ก.พ. 2569", iso="2026-02-09", mins=5, img="chanel-hero",
      t_en="Overnight at Emsphere: how a boutique opens by morning",
      t_th="ข้ามคืนที่เอ็มสเฟียร์: บูติกเปิดทันเช้าได้อย่างไร",
      q_en="Factory pre-assembly means site time is compressed to hours, not days.",
      q_th="การประกอบทดลองที่โรงงานทำให้เวลาหน้างานเหลือเพียงหลักชั่วโมง ไม่ใช่หลายวัน",
      b1_en="The hardest constraint in retail is the overnight window. When a boutique must be standing by the time the mall doors open, everything upstream changes: the environment is trial-built at the factory, packed in install sequence, and moved through protected logistics after the last shopper leaves.",
      b1_th="ข้อจำกัดที่ยากที่สุดของงานรีเทลคือหน้าต่างเวลาข้ามคืน เมื่อบูติกต้องตั้งเสร็จก่อนห้างเปิดประตู ทุกอย่างต้นน้ำต้องเปลี่ยน: พื้นที่ทั้งหมดถูกประกอบทดลองที่โรงงาน แพ็กตามลำดับติดตั้ง และขนย้ายด้วยระบบโลจิสติกส์ที่ป้องกันอย่างดีหลังลูกค้าคนสุดท้ายออกจากห้าง",
      b2_en="Engineered lifting rigs and crews tooled for live environments mean zero disruption to the neighbours — and a boutique open for business by morning.",
      b2_th="อุปกรณ์ยกที่ออกแบบเฉพาะและทีมงานที่มีเครื่องมือสำหรับพื้นที่เปิดให้บริการ หมายถึงไม่มีการรบกวนร้านข้างเคียงเลย — และบูติกพร้อมเปิดขายในเช้าวันรุ่งขึ้น",
      grid=["workshop-wide","chanel-boh"]),
 dict(slug="ecovadis", cat="SUSTAINABILITY", cat_th="ความยั่งยืน", date="16 MAR 2026", date_th="16 มี.ค. 2569", iso="2026-03-16", mins=3, img="sustain-box",
      t_en="EcoVadis rated: procurement discipline, not decoration",
      t_th="ได้รับเรตติ้ง EcoVadis: วินัยในการจัดหา ไม่ใช่การตกแต่ง",
      q_en="The most sustainable fixture is the one that does not need replacing.",
      q_th="เฟอร์นิเจอร์ที่ยั่งยืนที่สุด คือชิ้นที่ไม่ต้องเปลี่ยนใหม่",
      b1_en="Sustainability at Happexhibition is procurement discipline. We hold an EcoVadis commitment rating, source materials with sustainable certifications through audited suppliers, and operate water-curtain paint systems to control emissions.",
      b1_th="ความยั่งยืนของ Happexhibition คือวินัยในการจัดหา เราได้รับเรตติ้งความมุ่งมั่นจาก EcoVadis จัดหาวัสดุที่มีการรับรองด้านความยั่งยืนผ่านซัพพลายเออร์ที่ผ่านการตรวจสอบ และใช้ระบบพ่นสีม่านน้ำเพื่อควบคุมการปล่อยมลพิษ",
      b2_en="Our maintenance and refurbishment programmes support clients' circularity goals — reuse, refurbishment and local repair — with documentation to match their group reporting standards.",
      b2_th="โปรแกรมบำรุงรักษาและปรับปรุงของเราสนับสนุนเป้าหมายเศรษฐกิจหมุนเวียนของลูกค้า — การใช้ซ้ำ การปรับปรุง และการซ่อมในประเทศ — พร้อมเอกสารที่สอดคล้องกับมาตรฐานการรายงานของกลุ่มบริษัท",
      grid=["spray","hands-detail"]),
 dict(slug="twenty-years-same-hands", cat="PEOPLE", cat_th="ทีมงาน", date="20 APR 2026", date_th="20 เม.ย. 2569", iso="2026-04-20", mins=4, img="team-dark",
      t_en="Twenty years, same hands: our senior artisans",
      t_th="ยี่สิบปี ช่างฝีมือคนเดิม: ช่างอาวุโสของเรา",
      q_en="It shows in the corners, the shut-lines and the silence of a drawer closing.",
      q_th="มันสะท้อนอยู่ในทุกมุมงาน ทุกรอยต่อ และความเงียบของลิ้นชักที่ปิดสนิท",
      b1_en="Every department at Happexhibition is led by a senior artisan with fifteen or more years of tenure — many have been here since the first 1,000-square-metre factory in 2005. That continuity is not sentiment; it is our quality system.",
      b1_th="ทุกแผนกของ Happexhibition นำโดยช่างอาวุโสที่ทำงานกับเรามา 15 ปีขึ้นไป — หลายคนอยู่มาตั้งแต่โรงงานแรกขนาด 1,000 ตารางเมตรในปี 2548 ความต่อเนื่องนี้ไม่ใช่เพียงความผูกพัน แต่คือระบบคุณภาพของเรา",
      b2_en="New craftsmen apprentice under these department heads for years before they touch a luxury-house commission. It is the slowest way to build a team — and the only way to build one that the world's most audited maisons will trust.",
      b2_th="ช่างใหม่ต้องฝึกงานกับหัวหน้าแผนกเหล่านี้หลายปีก่อนได้แตะงานลักชัวรีเฮาส์ นี่คือวิธีสร้างทีมที่ช้าที่สุด — แต่เป็นวิธีเดียวที่จะสร้างทีมที่เมซงที่ถูกตรวจสอบเข้มงวดที่สุดในโลกจะไว้วางใจ",
      grid=["worker-portrait","machine-worker","craft-bench","craft-table"]),
 dict(slug="save-thai-ocean", cat="SUSTAINABILITY", cat_th="ความยั่งยืน", date="18 MAY 2026", date_th="18 พ.ค. 2569", iso="2026-05-18", mins=3, img=None, sto=True,
      t_en="Save Thai Ocean: ฿73,300 of turtle cookies for cleaner shores",
      t_th="Save Thai Ocean: คุกกี้เต่า 73,300 บาท เพื่อชายหาดที่สะอาดขึ้น",
      q_en="1,205 sets of turtle cookies became trash pick-up gear and cleanup days on the shore.",
      q_th="คุกกี้เต่า 1,205 ชุด กลายเป็นอุปกรณ์เก็บขยะและวันเก็บขยะริมชายหาด",
      b1_en="Save Thai Ocean is our team's ocean-conservation project, run in cooperation with Koh Tao Clean Up. To fund it, the team ran a bake sale with a mascot-worthy product: turtle cookies. 1,205 sets — 2,410 cookies — sold out, raising a total of ฿73,300.",
      b1_th="Save Thai Ocean คือโครงการอนุรักษ์ทะเลของทีมเรา ดำเนินการร่วมกับ Koh Tao Clean Up ทีมระดมทุนด้วยการขายเบเกอรี่ที่สมกับเป็นมาสคอตของโครงการ: คุกกี้เต่า จำนวน 1,205 ชุด — 2,410 ชิ้น — ขายหมดเกลี้ยง ระดมทุนได้รวม 73,300 บาท",
      b2_en="Every baht went to work: the funds bought trash pick-up equipment, and the crew joined Koh Tao Clean Up to host collection activities along the shore. Follow @savethaiocean on Instagram and Facebook to support the next cleanup.",
      b2_th="ทุกบาทถูกนำไปใช้จริง: เงินทุนถูกใช้ซื้ออุปกรณ์เก็บขยะ และทีมงานร่วมกับ Koh Tao Clean Up จัดกิจกรรมเก็บขยะริมชายหาด ติดตาม @savethaiocean ทาง Instagram และ Facebook เพื่อสนับสนุนการเก็บขยะครั้งถัดไป",
      grid=[]),
 dict(slug="wiribed", cat="COMMUNITY", cat_th="ชุมชน", date="2022", date_th="2565", iso="2022-06-01", mins=5, img="wiribed-hero",
      t_en="Wiribed: 1,000+ origami hospital beds, delivered where they were needed most",
      t_th="Wiribed: เตียงสนามโอริกามิกว่า 1,000 เตียง ส่งถึงที่ที่ต้องการที่สุด",
      q_en="More than 1,000 beds reached field hospitals, isolation centres and patients' homes.",
      q_th="เตียงมากกว่า 1,000 เตียงไปถึงโรงพยาบาลสนาม ศูนย์พักคอย และบ้านผู้ป่วย",
      b1_en="When Thailand's field hospitals and community isolation centres ran short of beds, our factory answered with Wiribed — a low-cost hospital bed anyone can assemble without tools. The design borrows from Japanese origami: the top is a single bendable wood sheet, pressed and scored on the same CNC lines that cut our luxury casework.",
      b1_th="เมื่อโรงพยาบาลสนามและศูนย์พักคอยของไทยขาดแคลนเตียง โรงงานของเราตอบด้วย Wiribed — เตียงผู้ป่วยราคาประหยัดที่ใครก็ประกอบได้โดยไม่ต้องใช้เครื่องมือ ดีไซน์ได้แรงบันดาลใจจากโอริกามิญี่ปุ่น: พื้นเตียงคือแผ่นไม้ดัดชิ้นเดียว กดขึ้นรูปด้วยเครื่อง CNC สายเดียวกับที่ตัดงานตู้ลักชัวรีของเรา",
      b2_en="Wiribed was engineered for mass production from day one, and delivered together with partners Alliance, Modernform, Torheng and DesignTwo — proof that the discipline we learned from luxury retail can serve everyone. Read more at wiribed.org.",
      b2_th="Wiribed ถูกออกแบบเพื่อการผลิตจำนวนมากตั้งแต่วันแรก และส่งมอบร่วมกับพันธมิตร Alliance, Modernform, Torheng และ DesignTwo — ข้อพิสูจน์ว่าวินัยที่เราเรียนรู้จากงานรีเทลลักชัวรีสามารถรับใช้ทุกคนได้ อ่านเพิ่มเติมที่ wiribed.org",
      grid=["wiribed-process","wiribed-deploy"]),
 dict(slug="colour-lab", cat="FACTORY", cat_th="โรงงาน", date="15 JUN 2026", date_th="15 มิ.ย. 2569", iso="2026-06-15", mins=3, img="spray",
      t_en="Inside the colour lab: paint engineered for ten years of hands",
      t_th="เจาะลึกห้องแล็บสี: งานสีที่ออกแบบมาเพื่อรองรับมือนับหมื่นตลอดสิบปี",
      q_en="Our finishes are built for ten years of hands, cleaners and sunlight.",
      q_th="ผิวเคลือบของเราสร้างมาเพื่อทนมือ น้ำยาทำความสะอาด และแสงแดดตลอดสิบปี",
      b1_en="When alcohol-based fragrance began blistering standard lacquers on beauty counters, we did not switch suppliers — we built a lab. Today four dedicated paint booths run PU, PE and powder-coat systems behind a water-curtain clean system, and a colour-mixing room matches any maison's standard to the decimal.",
      b1_th="เมื่อน้ำหอมที่มีแอลกอฮอล์เริ่มทำให้แล็กเกอร์ทั่วไปบนเคาน์เตอร์บิวตี้พองตัว เราไม่ได้เปลี่ยนซัพพลายเออร์ — เราสร้างห้องแล็บ วันนี้ห้องพ่นสี 4 ห้องรันระบบ PU, PE และพาวเดอร์โค้ต หลังระบบม่านน้ำ พร้อมห้องผสมสีที่จับคู่มาตรฐานของทุกเมซงได้ละเอียดถึงทศนิยม",
      b2_en="Every mix is logged against the project's QC trail, so a counter refurbished in year five gets exactly the finish it shipped with in year one.",
      b2_th="ทุกสูตรสีถูกบันทึกไว้ในประวัติ QC ของโปรเจกต์ ดังนั้นเคาน์เตอร์ที่ปรับปรุงในปีที่ห้า จะได้ผิวเคลือบเดียวกับวันแรกที่ส่งมอบเป๊ะ ๆ",
      grid=["red-lacquer","box-paint"]),
]

LEADERS = [
 ("leader-nathawat","Nathawat Jeerapat (William J.)","Chief Executive Officer","ประธานเจ้าหน้าที่บริหาร"),
 ("leader-lisa","Lisa B.","General Manager","ผู้จัดการทั่วไป"),
 ("leader-pakavadee","Pakavadee C.","Human Resource Manager","ผู้จัดการฝ่ายทรัพยากรบุคคล"),
 ("leader-sitthiphong","Sitthiphong V.","Project Design Manager","ผู้จัดการฝ่ายออกแบบโปรเจกต์"),
 ("leader-warakorn","Warakorn L.","Technical Manager","ผู้จัดการฝ่ายเทคนิค"),
 ("leader-woranon","Woranon K.","Project Manager","ผู้จัดการโปรเจกต์"),
 ("leader-pongsatorn","Pongsatorn S.","Production Head Line 1","หัวหน้าฝ่ายผลิต สายที่ 1"),
 ("leader-sunet","Sunet S.","Production Head Line 2","หัวหน้าฝ่ายผลิต สายที่ 2"),
 ("leader-chantha","Chantha H.","Production Head Line 3","หัวหน้าฝ่ายผลิต สายที่ 3"),
]

SERVICES = [
 ("design-engineering","Design & Engineering","ออกแบบและวิศวกรรม","services-floorplan",
  "We turn brand guidelines and architects' intent into build-ready reality. Our design and technical team works in 3D from day one — resolving materials, tolerances and site constraints before they become site problems.",
  "เราเปลี่ยนไกด์ไลน์ของแบรนด์และแนวคิดของสถาปนิกให้เป็นแบบที่พร้อมสร้างจริง ทีมออกแบบและเทคนิคของเราทำงานในระบบ 3 มิติตั้งแต่วันแรก — แก้ปัญหาวัสดุ ค่าความคลาดเคลื่อน และข้อจำกัดหน้างาน ก่อนที่มันจะกลายเป็นปัญหาจริง",
  ["3D modelling & technical detailing","Shop drawings & material resolution","Site-constraint surveys","Tolerance engineering"],
  ["งานโมเดล 3 มิติและแบบเทคนิค","Shop drawing และการเลือกวัสดุ","สำรวจข้อจำกัดหน้างาน","วิศวกรรมความละเอียด"]),
 ("fabrication-millwork","Precision Fabrication & Millwork","งานผลิตความละเอียดสูงและเฟอร์นิเจอร์บิลท์อิน","machine-worker",
  "Wood, metal, glass and specialist finishes under one roof. Counters, wall systems, casegoods, display architecture and bespoke furniture — fabricated with CNC, laser and finishing lines, and checked against a five-step QC protocol.",
  "งานไม้ โลหะ กระจก และผิวเคลือบพิเศษ ภายใต้หลังคาเดียว เคาน์เตอร์ ระบบผนัง ตู้ งานดิสเพลย์ และเฟอร์นิเจอร์สั่งทำ — ผลิตด้วยเครื่อง CNC เลเซอร์ และสายงานเก็บผิว ตรวจสอบด้วยระบบ QC 5 ขั้นตอน",
  ["Counters & display architecture","Wall systems & casegoods","Bespoke furniture & vitrines","5-step documented QC"],
  ["เคาน์เตอร์และงานดิสเพลย์","ระบบผนังและตู้","เฟอร์นิเจอร์สั่งทำและตู้โชว์","QC 5 ขั้นตอนพร้อมเอกสาร"]),
 ("interior-fitout","Interior Fit-Out","ตกแต่งภายในครบวงจร","sector-white-retail",
  "Complete interior packages for retail flagships, back-of-house and customer-facing technical environments — now extending to hospitality and offices. We manage our own trades and hold the programme.",
  "งานตกแต่งภายในครบวงจรสำหรับแฟล็กชิปสโตร์ พื้นที่หลังบ้าน และพื้นที่เทคนิคที่ลูกค้ามองเห็น — ขยายสู่งานโรงแรมและสำนักงาน เราบริหารช่างของเราเองและคุมแผนงานทั้งหมด",
  ["Retail flagship fit-out","Hospitality & office interiors","Own trades, own programme","Back-of-house environments"],
  ["ตกแต่งแฟล็กชิปสโตร์","ภายในโรงแรมและสำนักงาน","ช่างของเราเอง แผนงานของเราเอง","พื้นที่หลังบ้าน"]),
 ("installation","Installation","งานติดตั้ง","workshop-wide",
  "Our own installation crews, tooled for the hardest constraint in retail: the overnight window. We routinely install in live, 24-hour environments — engineered lifting rigs, protected logistics, zero disruption, open by morning.",
  "ทีมติดตั้งของเราเอง พร้อมเครื่องมือสำหรับข้อจำกัดที่ยากที่สุดของงานรีเทล: หน้าต่างเวลาข้ามคืน เราติดตั้งในพื้นที่เปิดให้บริการ 24 ชั่วโมงเป็นประจำ — อุปกรณ์ยกที่ออกแบบเฉพาะ โลจิสติกส์ที่ป้องกันอย่างดี ไม่รบกวนใคร เปิดทันเช้า",
  ["Overnight install windows","Live-environment logistics","Engineered lifting rigs","Factory pre-assembly"],
  ["ติดตั้งข้ามคืน","โลจิสติกส์ในพื้นที่เปิดบริการ","อุปกรณ์ยกออกแบบเฉพาะ","ประกอบทดลองที่โรงงาน"]),
 ("care-maintenance","Care & Maintenance","ดูแลและบำรุงรักษา","hands-detail",
  "The build is the beginning. We run maintenance programmes, fixture stock management and refurbishment for clients who expect their spaces perfect on year five, not just day one.",
  "การสร้างเป็นเพียงจุดเริ่มต้น เราให้บริการโปรแกรมบำรุงรักษา บริหารสต๊อกเฟอร์นิเจอร์ และงานปรับปรุง สำหรับลูกค้าที่ต้องการให้พื้นที่สมบูรณ์แบบในปีที่ห้า ไม่ใช่แค่วันแรก",
  ["Maintenance programmes","Fixture stock management","Refurbishment & repair","Circularity documentation"],
  ["โปรแกรมบำรุงรักษา","บริหารสต๊อกเฟอร์นิเจอร์","ปรับปรุงและซ่อมแซม","เอกสารเศรษฐกิจหมุนเวียน"]),
]

FAQ = [
 ("Do you install in operating malls and hotels?",
  "Yes — it is our home ground. Our own crews are tooled for the overnight window: engineered lifting rigs, protected logistics, zero disruption to the neighbours, open for business by morning.",
  "รับติดตั้งในห้างและโรงแรมที่เปิดให้บริการอยู่หรือไม่?",
  "รับแน่นอน — นี่คือสนามของเรา ทีมของเรามีเครื่องมือสำหรับการติดตั้งข้ามคืนโดยเฉพาะ: อุปกรณ์ยกที่ออกแบบเฉพาะ โลจิสติกส์ที่ป้องกันอย่างดี ไม่รบกวนร้านข้างเคียง และเปิดให้บริการทันเช้า"),
 ("Do you work outside Thailand?",
  "Yes — and we welcome it. We deliver across Asia and beyond through strategic partnerships with vetted local contractors and logistics providers, always with our own supervisors on site. The standard that leaves Pathumthani is the standard that opens abroad.",
  "รับงานต่างประเทศหรือไม่?",
  "รับ — และยินดีอย่างยิ่ง เราส่งมอบงานทั่วเอเชียและไกลกว่านั้น ผ่านพันธมิตรเชิงกลยุทธ์กับผู้รับเหมาและผู้ให้บริการโลจิสติกส์ท้องถิ่นที่ผ่านการคัดกรอง โดยมีหัวหน้างานของเราประจำหน้างานเสมอ มาตรฐานที่ออกจากปทุมธานี คือมาตรฐานเดียวกับที่เปิดในต่างประเทศ"),
 ("Do you build exhibition booths, event spaces and pop-ups?",
  "Yes — exhibition craft is in our name. We design and fabricate event booths, trade-show stands, brand activations, pop-up stores and museum-grade exhibition environments, using the same factory, finishes and overnight-installation discipline as our luxury boutiques.",
  "รับทำบูธแสดงสินค้า งานอีเวนต์ และป๊อปอัพสโตร์หรือไม่?",
  "รับ — งานเอ็กซิบิชั่นคือที่มาของชื่อเรา เราออกแบบและผลิตบูธอีเวนต์ บูธแสดงสินค้า งานแบรนด์แอคทิเวชัน ป๊อปอัพสโตร์ และงานนิทรรศการเกรดพิพิธภัณฑ์ ด้วยโรงงาน วัสดุ และวินัยการติดตั้งข้ามคืนเดียวกับงานบูติกลักชัวรีของเรา"),
 ("Can you work from our architect's drawings?",
  "Absolutely. Most of our work starts from a maison's brand guidelines or an architect's intent. Our technical team translates them into build-ready 3D shop drawings — materials, tolerances and site constraints resolved — and returns them for approval before production begins.",
  "ทำงานจากแบบของสถาปนิกเราได้หรือไม่?",
  "ได้แน่นอน งานส่วนใหญ่ของเราเริ่มจากไกด์ไลน์ของแบรนด์หรือแนวคิดของสถาปนิก ทีมเทคนิคของเราแปลงมันเป็น shop drawing 3 มิติที่พร้อมผลิต — แก้ปัญหาวัสดุ ความคลาดเคลื่อน และข้อจำกัดหน้างานเรียบร้อย — แล้วส่งกลับให้อนุมัติก่อนเริ่มผลิต"),
 ("What is the typical lead time?",
  "Faster than you might expect. A boutique or counter programme typically runs 4–8 weeks from approved drawings to overnight installation; larger fit-outs run from 8 weeks onward, scoped to the project. Tell us your opening date and we plan backwards from it.",
  "ระยะเวลาผลิตโดยทั่วไปนานแค่ไหน?",
  "เร็วกว่าที่คุณคิด บูติกหรือโปรแกรมเคาน์เตอร์ทั่วไปใช้เวลา 4–8 สัปดาห์จากแบบที่อนุมัติจนถึงติดตั้งข้ามคืน งานตกแต่งขนาดใหญ่เริ่มที่ 8 สัปดาห์ขึ้นไปตามขอบเขตงาน บอกวันเปิดของคุณมา แล้วเราจะวางแผนย้อนกลับจากวันนั้น"),
 ("Do you offer maintenance after handover?",
  "Yes. Maintenance programmes, fixture stock management and refurbishment are a core service. Our longest client relationships are measured in decades because their spaces stay perfect on year five, not just day one.",
  "มีบริการบำรุงรักษาหลังส่งมอบหรือไม่?",
  "มี โปรแกรมบำรุงรักษา บริหารสต๊อกเฟอร์นิเจอร์ และงานปรับปรุงคือบริการหลักของเรา ความสัมพันธ์กับลูกค้าที่ยาวนานที่สุดของเราวัดกันเป็นสิบปี เพราะพื้นที่ของพวกเขายังสมบูรณ์แบบในปีที่ห้า ไม่ใช่แค่วันแรก"),
 ("What certifications do you hold?",
  "ISO 9001:2015 for the manufacture and installation of furniture, an EcoVadis sustainability rating, and embedded occupational safety and health compliance. Our factory also passes the global audit regimes of LVMH-tier maisons as a condition of doing business.",
  "มีการรับรองมาตรฐานอะไรบ้าง?",
  "ISO 9001:2015 สำหรับการผลิตและติดตั้งเฟอร์นิเจอร์ เรตติ้งความยั่งยืนจาก EcoVadis และระบบอาชีวอนามัยและความปลอดภัยที่ฝังอยู่ในทุกกระบวนการ โรงงานของเรายังผ่านการตรวจสอบระดับโลกของเมซงระดับ LVMH ซึ่งเป็นเงื่อนไขของการทำธุรกิจร่วมกัน"),
]

STEPS = [
 ("01","Brief & Audit","รับโจทย์และสำรวจ","Your goals, site constraints and brand standard — surveyed before we draw.","เป้าหมาย ข้อจำกัดหน้างาน และมาตรฐานแบรนด์ของคุณ — สำรวจครบก่อนเริ่มเขียนแบบ"),
 ("02","Design & Engineering","ออกแบบและวิศวกรรม","3D from day one. Materials and tolerances resolved before site.","3 มิติตั้งแต่วันแรก วัสดุและความคลาดเคลื่อนถูกแก้ก่อนถึงหน้างาน"),
 ("03","Fabricate & Pre-Assemble","ผลิตและประกอบทดลอง","Wood, metal, glass, paint under one roof. Trial-built, 5-step QC.","ไม้ โลหะ กระจก งานสี ใต้หลังคาเดียว ประกอบทดลองพร้อม QC 5 ขั้นตอน"),
 ("04","Overnight Install","ติดตั้งข้ามคืน","Live-environment logistics. Open for business by morning.","โลจิสติกส์ในพื้นที่เปิดบริการ เปิดขายทันเช้า"),
 ("05","Care & Maintain","ดูแลต่อเนื่อง","Programmes that keep spaces perfect on year five.","โปรแกรมที่ทำให้พื้นที่สมบูรณ์แบบแม้ในปีที่ห้า"),
]

DIFFS = [
 ("01","Audited by the hardest judges","ผ่านการตรวจจากผู้ตัดสินที่โหดที่สุด",
  "Our factory passes the global inspections of LVMH-tier maisons as a condition of doing business. Every client inherits the benefit.",
  "โรงงานของเราผ่านการตรวจสอบระดับโลกของเมซงระดับ LVMH ซึ่งเป็นเงื่อนไขของการทำธุรกิจ ลูกค้าทุกรายได้รับประโยชน์นี้ไปด้วย"),
 ("02","Finishes engineered, not applied","ผิวเคลือบที่ถูกออกแบบ ไม่ใช่แค่ทา",
  "When alcohol-based fragrance blistered standard lacquers, we developed our own chemical-resistant paint system. Built for ten years of hands.",
  "เมื่อน้ำหอมที่มีแอลกอฮอล์ทำให้แล็กเกอร์ทั่วไปพองตัว เราพัฒนาระบบสีทนสารเคมีของเราเอง สร้างมาเพื่อทนมือนับหมื่นตลอดสิบปี"),
 ("03","Everything in-house","ทุกอย่างทำเองในบ้าน",
  "Design, wood, metal, glass, paint, assembly, installation, aftercare. No broker layer, no subcontracted quality risk.",
  "ออกแบบ ไม้ โลหะ กระจก งานสี ประกอบ ติดตั้ง และดูแลหลังส่งมอบ ไม่มีนายหน้าคั่นกลาง ไม่มีความเสี่ยงจากการจ้างช่วง"),
 ("04","Speed without shortcuts","เร็วโดยไม่ลัดขั้นตอน",
  "Purpose-built install tooling and overnight crews compress site time to hours. Malls that never close are our home ground.",
  "เครื่องมือติดตั้งที่สร้างขึ้นเฉพาะและทีมงานข้ามคืน บีบเวลาหน้างานเหลือหลักชั่วโมง ห้างที่ไม่เคยปิดคือสนามของเรา"),
 ("05","Twenty years, same hands","ยี่สิบปี ช่างฝีมือคนเดิม",
  "Senior artisans with 15+ years' tenure lead every department. It shows in the corners and the shut-lines.",
  "ช่างอาวุโสที่ทำงานกับเรามากกว่า 15 ปีนำทุกแผนก มันสะท้อนอยู่ในทุกมุมงานและทุกรอยต่อ"),
]

TIMELINE = [
 ("2004","Founded in Bangkok — first commissions in 3D technical detailing","ก่อตั้งที่กรุงเทพฯ — งานแรกคือแบบเทคนิค 3 มิติ"),
 ("2005","First factories: 1,000 sqm, then 2,500 sqm in Pathumthani","โรงงานแรก 1,000 ตร.ม. ตามด้วย 2,500 ตร.ม. ที่ปทุมธานี"),
 ("2011","Overcame Thailand's great flood","ผ่านพ้นมหาอุทกภัยของไทย"),
 ("2015","Glass processing capability added","เพิ่มขีดความสามารถงานกระจก"),
 ("2019","Dedicated metal factory (H2), 2,800 sqm","โรงงานโลหะเฉพาะทาง (H2) 2,800 ตร.ม."),
 ("2020–23","Endured the pandemic without losing a key client; opened H3, 6,000 sqm","ผ่านโควิดโดยไม่เสียลูกค้าหลักแม้แต่ราย; เปิด H3 ขนาด 6,000 ตร.ม."),
 ("2026","3 factories · 11,300 sqm · 180 people · luxury-tier client base","โรงงาน 3 แห่ง · 11,300 ตร.ม. · บุคลากร 180 คน · ฐานลูกค้าระดับลักชัวรี"),
]

BENEFITS = [
 ("Senior craft mentorship","การถ่ายทอดฝีมือจากช่างอาวุโส","Department heads with 15+ years' tenure teach the trade.","หัวหน้าแผนกที่มีประสบการณ์ 15 ปีขึ้นไปสอนงานให้โดยตรง"),
 ("Real machinery","เครื่องจักรของจริง","CNC, laser, water jet — the best tools in the industry.","CNC เลเซอร์ วอเตอร์เจ็ต — เครื่องมือที่ดีที่สุดในอุตสาหกรรม"),
 ("Luxury-tier projects","โปรเจกต์ระดับลักชัวรี","Your work ships to the world's most demanding brands.","ผลงานของคุณส่งถึงแบรนด์ที่เข้มงวดที่สุดในโลก"),
 ("Growing team","ทีมที่กำลังเติบโต","Three factories, expanding markets, room to rise.","โรงงาน 3 แห่ง ตลาดที่ขยายตัว และพื้นที่ให้เติบโต"),
]

ROLES = [
 ("Senior Draftsman","ช่างเขียนแบบอาวุโส","Design · Pathumthani · Full-time","ฝ่ายออกแบบ · ปทุมธานี · งานประจำ"),
 ("Project Manager","ผู้จัดการโปรเจกต์","Projects · Bangkok / Pathumthani · Full-time","ฝ่ายโปรเจกต์ · กรุงเทพฯ / ปทุมธานี · งานประจำ"),
 ("Metal Fabricator","ช่างโลหะ","H2 Factory · Pathumthani · Full-time","โรงงาน H2 · ปทุมธานี · งานประจำ"),
]

CAP = [
 ("Materials","วัสดุ","Wood · metal · glass · acrylic · specialist paint","ไม้ · โลหะ · กระจก · อะคริลิก · งานสีพิเศษ"),
 ("Paint systems","ระบบสี","PU · PE · powder coat · proprietary chemical-resistant formulations","PU · PE · พาวเดอร์โค้ต · สูตรทนสารเคมีเฉพาะของเรา"),
 ("Machinery","เครื่องจักร","CNC router · fiber & CO2 laser · water jet · press brake · 6-side drill · UV / inkjet / 3D print","CNC เราเตอร์ · เลเซอร์ไฟเบอร์และ CO2 · วอเตอร์เจ็ต · เพรสเบรก · เจาะ 6 ด้าน · พิมพ์ UV / อิงค์เจ็ท / 3 มิติ"),
 ("Quality control","การควบคุมคุณภาพ","5-step protocol, documented trail on every project","ระบบ 5 ขั้นตอน พร้อมเอกสารทุกโปรเจกต์"),
 ("Install window","หน้าต่างการติดตั้ง","24 hr overnight — our standard in live retail","ข้ามคืน 24 ชม. — มาตรฐานของเราในพื้นที่รีเทลที่เปิดบริการ"),
 ("Storage & stock","คลังสินค้าและสต๊อก","Fixture stock management — 2,500 sqm dedicated storage","บริหารสต๊อกเฟอร์นิเจอร์ — คลังเฉพาะ 2,500 ตร.ม."),
]

CATS = [("luxury-retail","cat_retail"),("hospitality","cat_hosp"),("corporate","cat_corp"),
        ("fnb","cat_fnb"),("galleries","cat_gal")]

# ==================== TEMPLATES ====================
def esc(s): return html.escape(s, quote=True)

def head(L, lang, P, page, title, desc, ogimg="assets/img/chanel-hero.jpg", jsonld=""):
    en_url = f"{BASE}/{page}"
    th_url = f"{BASE}/th/{page}"
    canon = th_url if lang=="th" else en_url
    site = "Happexhibition"
    kw = ("รับตกแต่งภายใน, ผู้รับเหมาตกแต่งภายใน, ออกแบบตกแต่งภายใน, ตกแต่งร้านค้า, รับทำบูธ, บูธแสดงสินค้า, ออกแบบบูธอีเวนต์, รับจัดงานอีเวนต์, ป๊อปอัพสโตร์, ผลิตเฟอร์นิเจอร์บิลท์อิน, งานรีเทล, ตกแต่งบูติก"
          if lang=="th" else
          "retail fit-out Bangkok, interior contractor Thailand, interior design and build, shop fitting, retail solutions, luxury retail fabrication, exhibition booth builder, event booth making, trade show booth Thailand, brand activation, pop-up store builder, museum exhibition fit-out, furniture manufacturer")
    org = f"""<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"Happ Exhibition Co., Ltd.","alternateName":"Happexhibition","description":"Design-build fabricator in Bangkok: luxury retail fit-out, interior design and contracting, shop and retail solutions, exhibition and event booth making, pop-up stores and bespoke furniture manufacturing.","url":"{BASE}/","logo":"{BASE}/assets/img/logo.png","foundingDate":"2004-03","telephone":"{TEL}","email":"{MAIL}","address":{{"@type":"PostalAddress","streetAddress":"52/8 Moo 11, Ladsawai, Lamlookka","addressLocality":"Pathumthani","postalCode":"12150","addressCountry":"TH"}},"sameAs":["{FB}","{IG}","{LINE}"],"knowsAbout":["Retail fit-out","Interior design","Interior contracting","Shop fitting","Retail solutions","Exhibition booth fabrication","Event booth design","Trade show stands","Brand activations","Pop-up stores","Furniture manufacturing","Museum and exhibition environments"]}}</script>"""
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} — {site}</title>
<meta name="description" content="{esc(desc)}">
<meta name="keywords" content="{kw}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="th" href="{th_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{site}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{BASE}/{ogimg.replace(P,'') if ogimg.startswith(P) else ogimg}">
<meta property="og:locale" content="{'th_TH' if lang=='th' else 'en_US'}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,300;6..72,400;6..72,500&family=Noto+Serif+Thai:wght@300;400;500&family=Inter:wght@400;500;600&family=Anuphan:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{P}css/style.css?v={ASSETV}">
<link rel="icon" href="{P}assets/img/logo.png">
{org}{jsonld}
</head>
<body>"""

def header_html(L, lang, P, page, transparent=False):
    cls = "transparent" if transparent else "solid"
    other = f"../{page}" if lang=="th" else f"th/{page}"
    en_href = other if lang=="th" else page
    th_href = page if lang=="th" else other
    thumbs = {"luxury-retail":"chanel-counter","hospitality":"sector-hospitality","corporate":"sector-corporate",
              "fnb":"office-lounge","galleries":"sector-gallery"}
    subkey = {"luxury-retail":"sub_retail","hospitality":"sub_hosp","corporate":"sub_corp",
              "fnb":"sub_fnb","galleries":"sub_gal"}
    cells = "".join(
        f'<a href="works.html#{slug}"><img class="thumb" src="{P}assets/img/{thumbs[slug]}.jpg" alt="{L[key]}"><div class="t">{L[key]}</div><div class="s">{L[subkey[slug]]}</div></a>'
        for slug, key in CATS)
    cells += f'<a href="works.html"><img class="thumb" src="{P}assets/img/shiseido-wide.jpg" alt="{L["all_works"]}"><div class="t">{L["all_works"]}</div><div class="s">{L["view_index"]}</div></a>'
    return f"""
<header class="site-header {cls}">
  <div class="container">
    <a class="logo" href="index.html" aria-label="Happexhibition">
      <img class="logo-light" src="{P}assets/img/logo-white.png" alt="Happexhibition">
      <img class="logo-dark" src="{P}assets/img/logo.png" alt="Happexhibition">
    </a>
    <nav class="main-nav" aria-label="Main">
      <a href="about.html">{L['nav_about']}</a>
      <a href="services.html">{L['nav_services']}</a>
      <button class="nav-works" aria-haspopup="true">{L['nav_works']} <span aria-hidden="true">⌄</span></button>
      <a href="news.html">{L['nav_news']}</a>
      <a href="careers.html">{L['nav_careers']}</a>
      <a href="contact.html">{L['nav_contact']}</a>
    </nav>
    <div class="header-actions">
      <span class="lang"><a class="lang-btn{' active' if lang=='en' else ''}" href="{en_href}" hreflang="en">EN</a><span class="off">/</span><a class="lang-btn{' active' if lang=='th' else ''}" href="{th_href}" hreflang="th">TH</a></span>
      <a class="btn btn-primary" href="{LINE}" target="_blank" rel="noopener">{L['quote']}</a>
      <button class="burger icon-btn" aria-label="Menu">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      </button>
    </div>
  </div>
</header>
<div class="mega" id="mega">{cells}</div>
<div class="mobile-menu">
  <div class="top">
    <img src="{P}assets/img/logo-white.png" alt="Happexhibition">
    <button class="close-btn" aria-label="Close">
      <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M6 6l12 12M18 6L6 18"/></svg>
    </button>
  </div>
  <nav>
    <a href="index.html"><small>01</small>{L['nav_home']}</a>
    <a href="about.html"><small>02</small>{L['nav_about']}</a>
    <a href="services.html"><small>03</small>{L['nav_services']}</a>
    <a href="works.html"><small>04</small>{L['nav_works']}</a>
    <a href="news.html"><small>05</small>{L['nav_news']}</a>
    <a href="careers.html"><small>06</small>{L['nav_careers']}</a>
    <a href="contact.html"><small>07</small>{L['nav_contact']}</a>
  </nav>
  <a class="btn btn-primary btn-lg" href="{LINE}" target="_blank" rel="noopener">{L['quote_line']} {ARROW}</a>
</div>"""

def dock(P):
    return f"""
<div class="dock" aria-label="Contact">
  <a class="d-line" href="{LINE}" target="_blank" rel="noopener" aria-label="LINE"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/></svg></a>
  <a class="d-call" href="{TELHREF}" aria-label="Call"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 4h4l2 5-2.5 1.5a12 12 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg></a>
  <a class="d-quote" href="{CONTACT_MAILTO}" aria-label="Email"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3.5" y="5.5" width="17" height="13"/><path d="M4 6.5l8 6 8-6"/></svg></a>
</div>"""

def cta_band(L):
    return f"""
<section class="cta-band">
  <div class="container">
    <span class="eyebrow" style="color:var(--green-100)">{L['cta_eyebrow'].upper()}</span>
    <h2>{L['cta_h']}</h2>
    <p>{L['cta_sub']}</p>
    <div class="actions">
      <a class="btn btn-outline-white" href="{TELHREF}">{L['cta_call']} {TEL}</a>
      <a class="btn btn-outline-white" href="{LINE}" target="_blank" rel="noopener">LINE: @happexhibition</a>
      <a class="btn btn-on-green" href="{LINE}" target="_blank" rel="noopener">{L['quote']} {ARROW}</a>
    </div>
  </div>
</section>"""

def footer(L, lang, P):
    cat_links = "".join(f'<li><a href="works.html#{s}">{L[k]}</a></li>' for s, k in CATS)
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="cols">
      <div class="brand">
        <img class="flogo" src="{P}assets/img/logo-white.png" alt="Happexhibition">
        <p>{L['tagline']}</p>
        <p class="fseo">{'รับตกแต่งภายใน · ผู้รับเหมาตกแต่งภายใน · งานรีเทลและตกแต่งร้านค้า · รับทำบูธอีเวนต์และบูธแสดงสินค้า · ป๊อปอัพสโตร์' if lang=='th' else 'Retail fit-out · Interior design & contracting · Shop & retail solutions · Exhibition & event booths · Pop-up stores'}</p>
        <img class="qr" src="{P}assets/img/line-qr.png" alt="LINE QR — @happexhibition">
      </div>
      <div><h5>{L['f_explore']}</h5><ul>
        <li><a href="index.html">{L['nav_home']}</a></li><li><a href="about.html">{L['nav_about']}</a></li>
        <li><a href="services.html">{L['nav_services']}</a></li><li><a href="works.html">{L['nav_works']}</a></li>
        <li><a href="news.html">{L['nav_news']}</a></li></ul></div>
      <div><h5>{L['f_company']}</h5><ul>
        <li><a href="careers.html">{L['nav_careers']}</a></li><li><a href="contact.html">{L['nav_contact']}</a></li>
        <li><a href="{LINE}" target="_blank" rel="noopener">{L['quote']}</a></li></ul></div>
      <div><h5>{L['f_works']}</h5><ul>{cat_links}</ul></div>
      <div>
        <h5>{L['f_office']}</h5>
        <address><a href="{MAPS}" target="_blank" rel="noopener">{L['addr_html']}</a><br>
        <a href="{TELHREF}">{TEL}</a><br><a href="mailto:{MAIL}">{MAIL}</a></address>
        <h5 style="margin-top:20px">{L['f_line']}</h5>
        <a class="line-cta" href="{LINE}" target="_blank" rel="noopener">LINE · @happexhibition</a>
      </div>
    </div>
    <div class="legal">
      <span>© 2026 Happ Exhibition Co., Ltd.</span>
      <span>
        <a href="#">{L['f_privacy']}</a> · <a href="#">{L['f_cookies']}</a> ·
        <a href="{FB}" target="_blank" rel="noopener">Facebook</a> ·
        <a href="{IG}" target="_blank" rel="noopener">Instagram</a> ·
        <a href="{LINE}" target="_blank" rel="noopener">LINE</a>
      </span>
    </div>
  </div>
</footer>
<script src="{P}js/main.js?v={ASSETV}"></script>
</body></html>"""

def write(lang, name, htmlstr):
    d = OUT if lang=="en" else os.path.join(OUT,"th")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d,name),"w",encoding="utf-8") as f: f.write(htmlstr)

def T(p, lang):  # project narrative
    return p["narr_th"] if lang=="th" else p["narr_en"]

# ==================== PAGES ====================
def build_all(lang):
    L = UI[lang]; P = "../" if lang=="th" else ""
    META = all_meta(lang)
    def A(a,k): return a[k+"_th"] if lang=="th" and (k+"_th") in a else a[k+"_en"] if (k+"_en") in a else a[k]
    def acat(a): return a["cat_th"] if lang=="th" else a["cat"]
    def adate(a): return a["date_th"] if lang=="th" else a["date"]

    # ---- index ----
    hero_eyebrow = ("ผู้ออกแบบและผลิตงานรีเทลครบวงจร · กรุงเทพฯ" if lang == "th"
                    else "Design-build fabricator · Bangkok")
    hero = f"""
  <section class="hero" aria-label="Company film">
    <video class="hero-video" muted loop playsinline preload="metadata"
      poster="{P}assets/video/hero-poster.jpg"
      data-src-large="{P}assets/video/hero-bg-1920.mp4"
      data-src-small="{P}assets/video/hero-bg-720.mp4"
      aria-label="{'ภาพยนตร์แนะนำบริษัท Happ Exhibition' if lang=='th' else 'Happ Exhibition company film'}"></video>
    <div class="scrim"></div>
    <div class="slide-copy">
      <span class="eyebrow">{hero_eyebrow.upper() if lang=='en' else hero_eyebrow}</span>
      <h1 class="display-xl">{L['tagline']}</h1>
    </div>
  </section>"""
    SHORT = {
      "design-engineering": ("Brand guidelines and architects' intent, turned into build-ready reality in 3D from day one.",
                             "เปลี่ยนไกด์ไลน์แบรนด์และแนวคิดสถาปนิกให้เป็นแบบพร้อมสร้างจริง ด้วยระบบ 3 มิติตั้งแต่วันแรก"),
      "fabrication-millwork": ("Wood, metal, glass and specialist finishes under one roof, checked by 5-step QC.",
                               "งานไม้ โลหะ กระจก และผิวเคลือบพิเศษใต้หลังคาเดียว ตรวจสอบด้วย QC 5 ขั้นตอน"),
      "interior-fitout": ("Complete interior packages — our own trades, our own programme.",
                          "งานตกแต่งภายในครบวงจร — ช่างของเราเอง แผนงานของเราเอง"),
      "installation": ("Overnight windows in live malls. Zero disruption, open by morning.",
                       "ติดตั้งข้ามคืนในห้างที่เปิดบริการ ไม่รบกวนใคร เปิดทันเช้า"),
      "care-maintenance": ("Maintenance, fixture stock and refurbishment — perfect on year five.",
                           "บำรุงรักษา สต๊อกเฟอร์นิเจอร์ และงานปรับปรุง — สมบูรณ์แบบแม้ปีที่ห้า"),
    }
    svc_imgs = {"design-engineering":"services-floorplan","fabrication-millwork":"machine-worker",
                "interior-fitout":"sector-white-retail","installation":"workshop-wide","care-maintenance":"hands-detail"}
    explore = "ดูรายละเอียด" if lang == "th" else "Explore"
    svc_cards = "".join(
        f'<a class="service-card" href="services.html#{sid}">'
        f'<div class="sc-img"><img src="{P}assets/img/{svc_imgs[sid]}.jpg" alt="{(nth if lang=="th" else nen)}" loading="lazy"></div>'
        f'<span class="num">{str(i+1).zfill(2)}</span>'
        f'<h3>{(nth if lang=="th" else nen)}</h3><p>{SHORT[sid][1] if lang=="th" else SHORT[sid][0]}</p>'
        f'<span class="sc-link">{explore} →</span></a>'
        for i,(sid,nen,nth,_img,den,dth,_de,_dt) in enumerate(SERVICES))
    tiles_data = [("luxury-retail","cat_retail","chanel-window","tile-a"),("hospitality","cat_hosp","sector-hospitality","tile-b"),
                  ("corporate","cat_corp","sector-corporate","tile-c"),("fnb","cat_fnb","office-lounge","tile-d"),
                  ("galleries","cat_gal","sector-gallery","tile-e")]
    cat_counts = {}
    for m in META: cat_counts[m["cat"]] = cat_counts.get(m["cat"], 0) + 1
    def tile_sub(i, slug):
        n = cat_counts.get(slug, 0)
        if not n: return f'{str(i+1).zfill(2)}'
        word = "โปรเจกต์" if lang == "th" else ("project" if n == 1 else "projects")
        return f'{str(i+1).zfill(2)} · {n} {word}'
    tiles = "".join(
        f'<a class="tile {cls}" href="works.html#{slug}"><img src="{P}assets/img/{img}.jpg" alt="{L[key]}">'
        f'<div class="wash"></div><div class="label"><span class="t-sub">{tile_sub(i,slug)}</span>'
        f'<span class="t-name">{L[key]}</span></div></a>'
        for i,(slug,key,img,cls) in enumerate(tiles_data))
    marquee_cells = "".join(
        f'<div class="cell"><img src="{P}assets/img/clients/{c}.png" alt="{LOGO_NAME[c]}" style="--lh:{round(LOGO_H[c]*0.5)}px" loading="lazy"></div>'
        for c in CLIENT_LOGOS) \
        + "".join(f'<div class="cell"><span>{t}</span></div>' for t in CLIENT_TEXT)
    steps_html = "".join(f'<div class="step reveal"><div class="num">{n}</div><hr><h3>{(tth if lang=="th" else ten)}</h3><p>{(dth if lang=="th" else den)}</p></div>' for n,ten,tth,den,dth in STEPS)
    news3 = "".join(
        f'<a class="news-card reveal" href="article-{a["slug"]}.html">'
        f'<img src="{P}assets/img/{a["img"]}.jpg" alt="{A(a,"t")}" loading="lazy">'
        f'<div class="meta">{acat(a)} · {adate(a)}</div><h3>{A(a,"t")}</h3></a>'
        for a in [ARTICLES[0], ARTICLES[1], ARTICLES[2]])
    desc = ("รับตกแต่งภายใน ผลิตงานรีเทลลักชัวรี ตกแต่งร้านค้า และรับทำบูธอีเวนต์ กรุงเทพฯ — Chanel, Gucci, Burberry ไว้วางใจ · ผู้รับเหมาตกแต่งภายในครบวงจร 20+ ปี · โรงงาน 3 แห่ง · ติดตั้งข้ามคืน"
            if lang=="th" else
            "Bangkok design-build fabricator for luxury retail fit-out, interior design & contracting, shop & retail solutions, and exhibition & event booths. Trusted by Chanel, Gucci, Burberry — 20+ years, 3 factories, overnight installation.")
    idx_title = ("รับตกแต่งภายใน งานรีเทล และบูธอีเวนต์ | " + L["tagline"]) if lang=="th" else \
                ("Retail Fit-Out, Interior Contractor & Event Booths, Bangkok")
    htmlp = head(L, lang, P, "index.html", idx_title, desc, "assets/video/hero-poster.jpg") + header_html(L, lang, P, "index.html", transparent=True) + f"""
<main>
{hero}
  <section class="section positioning">
    <div class="bgimg" style="background-image:url({P}assets/img/craft-bench.jpg)"></div>
    <div class="container reveal">
      <p class="display-l">{L['positioning']}</p>
      <p style="margin-top:40px"><a class="link-brand" href="about.html">{L['more_about']} →</a></p>
    </div>
  </section>
  <section class="stats section">
    <div class="bgimg" style="background-image:url({P}assets/img/factory-aerial.jpg)"></div>
    <div class="container grid">
      <div class="stat"><div class="num"><span data-count="20" data-suffix="+">20+</span></div><div class="lbl">{L['stat1']}</div><div class="sub">{L['stat1s']}</div></div>
      <div class="stat"><div class="num"><span data-count="180" data-suffix="+">180+</span></div><div class="lbl">{L['stat2']}</div><div class="sub">{L['stat2s']}</div></div>
      <div class="stat"><div class="num"><span data-count="11300">11,300</span></div><div class="lbl">{L['stat3']}</div><div class="sub">{L['stat3s']}</div></div>
      <div class="stat"><div class="num"><span data-count="20" data-suffix="+">20+</span></div><div class="lbl">{L['stat4']}</div><div class="sub">{L['stat4s']}</div></div>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <div class="section-header reveal"><div><span class="eyebrow">{L['our_services']}</span><h2>{L['services_h']}</h2></div>
      <a class="link-brand" href="services.html">{L['all_services']} →</a></div>
      <div class="cards-5">{svc_cards}</div>
    </div>
  </section>
  <section class="section" style="background:var(--bg-subtle)">
    <div class="container">
      <div class="section-header reveal"><div><span class="eyebrow">{L['works_eyebrow']}</span><h2>{L['works_h']}</h2></div>
      <a class="link-brand" href="works.html">{L['view_more']} →</a></div>
      <div class="tile-grid">{tiles}</div>
    </div>
  </section>
  <section class="section">
    <div class="container featured reveal">
      <img src="{P}assets/img/chanel-front.jpg" alt="Chanel @ Emsphere">
      <div>
        <span class="eyebrow">{L['featured']}</span>
        <h2 style="margin:12px 0 20px">Chanel @ Emsphere</h2>
        <p class="body-l" style="color:var(--text-secondary)">{L['featured_body']}</p>
        <div class="metrics">
          <div><div class="num">10+</div><div class="lbl">{L['years_partner']}</div></div>
          <div><div class="num">99</div><div class="lbl">{L['sqm']}</div></div>
          <div><div class="num">2025</div><div class="lbl">{L['delivered']}</div></div>
        </div>
        <a class="btn btn-secondary" href="project-chanel-emsphere.html">{L['view_case']} {ARROW}</a>
      </div>
    </div>
  </section>
  <div class="marquee" aria-label="Clients"><div class="marquee-track">{marquee_cells}{marquee_cells}</div></div>
  <section class="section">
    <div class="container">
      <div class="section-header reveal"><div><span class="eyebrow">{L['how_we_work']}</span><h2>{L['process_h']}</h2></div>
      <a class="link-brand" href="services.html">{L['our_process']} →</a></div>
      <div class="process-photos"><img src="{P}assets/img/worker-portrait.jpg" alt=""><img src="{P}assets/img/services-floorplan.jpg" alt=""><img src="{P}assets/img/machine-worker.jpg" alt=""><img src="{P}assets/img/workshop-wide.jpg" alt=""><img src="{P}assets/img/hands-detail.jpg" alt=""></div>
      <div class="process-grid">{steps_html}</div>
    </div>
  </section>
  <section class="section" style="background:var(--bg-subtle)">
    <div class="container">
      <div class="section-header reveal"><div><span class="eyebrow">{L['news_eyebrow']}</span><h2>{L['news_h']}</h2></div>
      <a class="link-brand" href="news.html">{L['all_news']} →</a></div>
      <div class="news-grid">{news3}</div>
    </div>
  </section>
  <section class="band">
    <div class="bgimg" style="background-image:url({P}assets/img/team-dark.jpg)"></div>
    <div class="container">
      <span class="eyebrow" style="color:var(--green-300)">{L['careers_eyebrow']}</span>
      <h2>{L['careers_band']}</h2>
      <a class="btn btn-on-green" href="careers.html">{L['view_openings']} {ARROW}</a>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <div class="section-header reveal"><div><span class="eyebrow">{L['follow']}</span><h2>{L['fb_h']}</h2></div>
      <a class="link-brand" href="{FB}" target="_blank" rel="noopener">FACEBOOK →</a></div>
      <div class="gallery-3"><a href="{FB}" target="_blank" rel="noopener"><img src="{P}assets/img/hands-detail.jpg" alt=""></a><a href="{FB}" target="_blank" rel="noopener"><img src="{P}assets/img/red-lacquer.jpg" alt=""></a><a href="{FB}" target="_blank" rel="noopener"><img src="{P}assets/img/laser-cut.jpg" alt=""></a></div>
    </div>
  </section>
</main>
{cta_band(L)}{dock(P)}{footer(L,lang,P)}"""
    write(lang, "index.html", htmlp)

    # ---- about ----
    diffs_html = "".join(f'<div class="step reveal"><div class="num" style="color:var(--green-300)">{n}</div><hr style="border-color:rgba(255,255,255,.15)"><h3 style="color:#fff">{(tth if lang=="th" else ten)}</h3><p style="color:var(--grey-300)">{(dth if lang=="th" else den)}</p></div>' for n,ten,tth,den,dth in DIFFS)
    team = "".join(f'<div class="team-card reveal"><img src="{P}assets/img/{img}.jpg" alt="{name}"><h3>{name}</h3><p>{(rth if lang=="th" else ren)}</p></div>' for img,name,ren,rth in LEADERS)
    tl = "".join(f'<div class="step reveal"><div class="num" style="font-size:24px;color:var(--text-brand)">{y}</div><hr><p>{(dth if lang=="th" else den)}</p></div>' for y,den,dth in TIMELINE)
    wall = "".join(f'<div style="border:1px solid var(--border-subtle);height:104px;display:flex;align-items:center;justify-content:center"><img src="{P}assets/img/clients/{c}.png" alt="{LOGO_NAME[c]}" loading="lazy" style="height:{round(LOGO_H[c]*0.5)}px;max-width:110px;width:auto;object-fit:contain"></div>' for c in CLIENT_LOGOS) \
        + "".join(f'<div style="border:1px solid var(--border-subtle);height:104px;display:flex;align-items:center;justify-content:center"><span style="font-family:var(--font-display);font-weight:400;font-size:15px;color:var(--text-secondary)">{t}</span></div>' for t in CLIENT_TEXT)
    desc = ("บริษัทเงียบ ๆ เบื้องหลังแบรนด์ที่ดังที่สุด ก่อตั้งปี 2547 ที่กรุงเทพฯ — บุคลากร 180 คน โรงงาน 3 แห่ง ผ่านการตรวจสอบระดับ LVMH" if lang=="th" else
            "The quiet company behind the loudest brands. Founded 2004 in Bangkok — 180 people, 3 factories, LVMH-tier audited.")
    about_title = ("เกี่ยวกับเรา — ผู้ผลิตงานรีเทลลักชัวรีและผู้รับเหมาตกแต่งภายใน" if lang=="th" else "About Us — Luxury Retail Fabricator & Interior Contractor, Thailand")
    htmlp = head(L, lang, P, "about.html", about_title, desc, "assets/img/team-dark.jpg") + header_html(L, lang, P, "about.html", transparent=True) + f"""
<main>
  <section class="page-hero dark">
    <img class="bg" src="{P}assets/img/team-dark.jpg" alt="Happexhibition team">
    <div class="scrim"></div>
    <div class="container">
      <span class="eyebrow" style="color:var(--green-300)">{L['about_eyebrow']}</span>
      <h1 class="display-l on-dark">{L['about_h']}</h1>
    </div>
  </section>
  <section class="section">
    <div class="container about-split">
      <div class="reveal">
        <span class="eyebrow">{L['overview_eyebrow']}</span>
        <h2 style="margin:12px 0 24px">{L['overview_h']}</h2>
        <p class="body-l" style="color:var(--text-secondary);margin-bottom:20px">{L['overview_p1']}</p>
        <p class="body-l" style="color:var(--text-secondary)">{L['overview_p2']}</p>
      </div>
      <blockquote class="reveal">{L['pullquote']}</blockquote>
    </div>
  </section>
  <section class="section" style="background:var(--bg-subtle)">
    <div class="container">
      <div class="section-header reveal"><div><span class="eyebrow">{L['timeline_eyebrow']}</span><h2>{L['timeline_h']}</h2></div></div>
      <div class="process-grid timeline-grid">{tl}</div>
    </div>
  </section>
  <section class="section" style="background:var(--grey-900)">
    <div class="container">
      <div class="section-header reveal"><div><span class="eyebrow">{L['whyus_eyebrow']}</span><h2 class="on-dark">{L['whyus_h']}</h2></div></div>
      <div class="process-grid">{diffs_html}</div>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <div class="section-header reveal"><div><span class="eyebrow">{L['leadership_eyebrow']}</span><h2>{L['leadership_h']}</h2></div></div>
      <div class="team-grid">{team}</div>
    </div>
  </section>
  <section class="section" style="background:var(--bg-subtle)">
    <div class="container">
      <div class="section-header reveal"><div><span class="eyebrow">{L['factory_eyebrow']}</span><h2>{L['factory_h']}</h2></div>
      <a class="link-brand" href="{YT}" target="_blank" rel="noopener">{L['watch_tour']} →</a></div>
      <div class="gallery-3">
        <a href="{YT}" target="_blank" rel="noopener"><img style="aspect-ratio:16/10" src="{P}assets/img/craft-table.jpg" alt="H1"></a>
        <a href="{YT}" target="_blank" rel="noopener"><img style="aspect-ratio:16/10" src="{P}assets/img/welding.jpg" alt="H2"></a>
        <a href="{YT}" target="_blank" rel="noopener"><img style="aspect-ratio:16/10" src="{P}assets/img/factory-exterior.jpg" alt="H3"></a>
      </div>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <div class="section-header reveal"><div><span class="eyebrow">{L['clients_eyebrow']}</span><h2>{L['clients_h']}</h2></div></div>
      <div class="logo-wall">{wall}</div>
    </div>
  </section>
</main>
{cta_band(L)}{dock(P)}{footer(L,lang,P)}"""
    write(lang, "about.html", htmlp)

    # ---- services ----
    nav = "".join(f'<a href="#{sid}">{str(i+1).zfill(2)} — {(nth if lang=="th" else nen)}</a>' for i,(sid,nen,nth,_,_,_,_,_) in enumerate(SERVICES))
    blocks = "".join(
        f'<div class="svc-block" id="{sid}"><img src="{P}assets/img/{img}.jpg" alt="{(nth if lang=="th" else nen)}"><h2>{(nth if lang=="th" else nen)}</h2>'
        f'<p class="desc">{(dth if lang=="th" else den)}</p><ul>' + "".join(f"<li>{d}</li>" for d in (delt if lang=="th" else dele)) + "</ul></div>"
        for sid,nen,nth,img,den,dth,dele,delt in SERVICES)
    cap_html = "".join(f"<div><dt>{(kth if lang=='th' else ken)}</dt><dd>{(vth if lang=='th' else ven)}</dd></div>" for ken,kth,ven,vth in CAP)
    faq = "".join(f"<details{' open' if i==0 else ''}><summary>{(qt if lang=='th' else qe)}</summary><p>{(at if lang=='th' else ae)}</p></details>" for i,(qe,ae,qt,at) in enumerate(FAQ))
    faq_ld = '<script type="application/ld+json">' + json.dumps(
        {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
            {"@type":"Question","name":(qt if lang=="th" else qe),
             "acceptedAnswer":{"@type":"Answer","text":(at if lang=="th" else ae)}} for qe,ae,qt,at in FAQ]},
        ensure_ascii=False) + '</script>'
    desc = ("บริการรับตกแต่งภายในครบวงจร: ออกแบบและวิศวกรรม งานผลิตความละเอียดสูง ตกแต่งร้านค้าและภายใน รับทำบูธอีเวนต์และบูธแสดงสินค้า ติดตั้งข้ามคืน และดูแลรักษา — หนึ่งโรงงาน หนึ่งมาตรฐาน" if lang=="th" else
            "Full-service interior contractor: design & engineering, precision fabrication, shop & interior fit-out, exhibition and event booth making, overnight installation and aftercare — one factory, one standard, one accountable team.")
    svc_title = ("บริการ — รับทำร้านค้า งานผลิต บูธอีเวนต์ และติดตั้ง" if lang=="th" else "Services — Retail Fit-Out, Fabrication, Event Booths & Installation")
    htmlp = head(L, lang, P, "services.html", svc_title, desc, "assets/img/machine-worker.jpg", faq_ld) + header_html(L, lang, P, "services.html") + f"""
<main>
  <section class="page-hero">
    <div class="container">
      <span class="eyebrow">{L['svc_eyebrow']}</span>
      <h1 class="display-l">{L['svc_h']}</h1>
      <p class="body-l muted" style="margin-top:16px">{L['svc_sub']}</p>
    </div>
  </section>
  <section class="section" style="padding-top:24px">
    <div class="container svc-layout">
      <nav class="svc-nav" aria-label="Services">{nav}</nav>
      <div>{blocks}</div>
    </div>
  </section>
  <section class="section" style="background:var(--bg-subtle)">
    <div class="container"><h2 class="reveal" style="margin-bottom:40px">{L['cap_h']}</h2><div class="cap-table">{cap_html}</div></div>
  </section>
  <section class="section">
    <div class="container article-col"><h2 style="margin-bottom:40px">{L['faq_h']}</h2><div class="accordion">{faq}</div></div>
  </section>
</main>
{cta_band(L)}{dock(P)}{footer(L,lang,P)}"""
    write(lang, "services.html", htmlp)

    # ---- works ----
    chips = f'<button class="chip active" data-filter="all">{L["all"]}</button>' + "".join(
        f'<button class="chip" data-filter="{s}">{L[k]}</button>' for s, k in CATS)
    META = all_meta(lang)
    cards = "".join(
        f'<a class="work-card" data-cat="{m["cat"]}" href="project-{m["slug"]}.html">'
        f'<div class="imgwrap"><img src="{P}assets/img/{m["hero"]}.jpg" alt="{m["title"]}" loading="lazy"></div>'
        f'<h3>{m["title"]}</h3><div class="meta">{m["meta"]}</div>'
        f'<span class="cat">{L[CATKEY[m["cat"]]].upper()}</span></a>' for m in META)
    nproj = len(META)
    desc = ("Chanel, Gucci, Van Cleef & Arpels, Burberry, Hourglass, Blue Bottle และอีกมากมาย — ผลงานรีเทล บิวตี้เคาน์เตอร์ และร้านค้าของเราทั่วประเทศ" if lang=="th" else
            "Chanel, Gucci, Van Cleef & Arpels, Burberry, Hourglass, Blue Bottle and more — the company we keep and what they trusted us to build.")
    works_title = ("ผลงาน — รับทำร้านค้า เคาน์เตอร์แบรนด์ และป๊อปอัพ" if lang=="th" else "Works — Luxury Retail Stores, Brand Counters & Pop-ups")
    htmlp = head(L, lang, P, "works.html", works_title, desc) + header_html(L, lang, P, "works.html") + f"""
<main>
  <section class="page-hero">
    <div class="container">
      <span class="eyebrow">{L['works_eyebrow']}</span>
      <h1 class="display-l">{L['works_idx_h']}</h1>
      <p class="muted" style="margin-top:16px" data-result-count>{nproj} {L['projects_word']}</p>
    </div>
  </section>
  <div class="filter-bar"><div class="container">{chips}</div></div>
  <section class="section">
    <div class="container">
      <div class="work-grid">{cards}</div>
      <div data-empty style="display:none;text-align:center;padding:80px 0;background:var(--bg-subtle);margin-top:48px">
        <h3 style="margin-bottom:8px">{L['empty_h']}</h3>
        <p class="muted" style="margin-bottom:24px">{L['empty_p']}</p>
        <a class="btn btn-primary" href="{LINE}" target="_blank" rel="noopener">{L['talk_line']} {ARROW}</a>
      </div>
    </div>
  </section>
</main>
{cta_band(L)}{dock(P)}{footer(L,lang,P)}
<script>const h=location.hash.replace('#','');if(h)document.querySelector(`.chip[data-filter="${{h}}"]`)?.click();</script>"""
    write(lang, "works.html", htmlp)

    # ---- projects (shared nav helpers over the combined ordered list) ----
    POS = {m["slug"]: i for i, m in enumerate(META)}
    def pn(slug):
        i = POS[slug]
        return META[(i-1) % len(META)], META[(i+1) % len(META)]
    def rel3(slug, cat):
        i = POS[slug]
        ring = META[i+1:] + META[:i]
        same = [m for m in ring if m["cat"] == cat]
        return (same + [m for m in ring if m["cat"] != cat])[:3]
    def rel_cards(slug, cat):
        return "".join(
            f'<a class="work-card reveal" href="project-{r["slug"]}.html">'
            f'<div class="imgwrap"><img src="{P}assets/img/{r["hero"]}.jpg" alt="{r["title"]}" loading="lazy"></div>'
            f'<h3>{r["title"]}</h3><div class="meta">{r["meta"]}</div></a>' for r in rel3(slug, cat))
    def more_lbl(cat):
        return (f"More in {L[CATKEY[cat]]}" if lang == "en" else f"ผลงานอื่นในหมวด{L[CATKEY[cat]]}")
    def prevnext_html(slug):
        prev, nxt = pn(slug)
        return f"""
  <nav class="prevnext" aria-label="Projects">
    <a href="project-{prev['slug']}.html"><div class="dir">← {L['prev']}</div><div class="name">{prev['title']}</div></a>
    <a href="project-{nxt['slug']}.html" style="text-align:right"><div class="dir">{L['next']} →</div><div class="name">{nxt['title']}</div></a>
  </nav>"""


    def proj_title(t):
        return t if lang == "en" else f"{t} — ผลงานรับทำร้านค้าและเคาน์เตอร์"
    def proj_ld(title, hero, year, city, page):
        crumbs = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
            {"@type":"ListItem","position":1,"name":("ผลงาน" if lang=="th" else "Works"),"item":f"{BASE}/works.html"},
            {"@type":"ListItem","position":2,"name":title,"item":f"{BASE}/{('th/' if lang=='th' else '')}{page}"}]}
        cw = {"@context":"https://schema.org","@type":"CreativeWork","name":title,
              "image":f"{BASE}/assets/img/{hero}.jpg",
              "creator":{"@type":"Organization","name":"Happ Exhibition Co., Ltd."}}
        if year: cw["dateCreated"] = str(year)
        if city: cw["locationCreated"] = {"@type":"Place","name":city}
        return ('<script type="application/ld+json">'+json.dumps(cw,ensure_ascii=False)+'</script>'
               +'<script type="application/ld+json">'+json.dumps(crumbs,ensure_ascii=False)+'</script>')

    for idx, p in enumerate(PROJECTS):
        rel_html = rel_cards(p["slug"], "luxury-retail")
        pair = ""
        if p["d1"]:
            second = f'<img src="{P}assets/img/{p["d2"]}.jpg" alt="">' if p["d2"] else ""
            pair = f'<div class="img-pair"><img src="{P}assets/img/{p["d1"]}.jpg" alt="">{second}</div>'
        plan = f'<img style="width:100%;margin:16px 0 32px" src="{P}assets/img/{p["plan"]}.jpg" alt="Technical drawing">' if p["plan"] else ""
        pcity = p.get('city_th' if lang=='th' else 'city_en') or L['bangkok']
        pld = proj_ld(p["title"], p["hero"], p["year"], pcity, f"project-{p['slug']}.html")
        htmlp = head(L, lang, P, f"project-{p['slug']}.html", proj_title(p["title"]), T(p,lang)[:150], f"assets/img/{p['hero']}.jpg", pld) + header_html(L, lang, P, f"project-{p['slug']}.html", transparent=True) + f"""
<main>
  <section class="page-hero dark">
    <img class="bg" src="{P}assets/img/{p['hero']}.jpg" alt="{p['title']}">
    <div class="scrim"></div>
    <div class="container">
      <p style="font-size:13px;opacity:.8;margin-bottom:16px"><a href="works.html">{L['nav_works']}</a> / <a href="works.html#luxury-retail">{L['cat_retail']}</a></p>
      <span class="eyebrow" style="color:var(--green-300)">{L['cat_retail'].upper()}</span>
      <h1 class="display-l on-dark" style="margin-top:10px">{p['title']}</h1>
    </div>
  </section>
  <section class="section">
    <div class="container project-body">
      <aside class="fact-rail"><dl>
        <div><dt>{L['client']}</dt><dd>{p['client']}</dd></div>
        <div><dt>{L['venue']}</dt><dd>{p['venue']}</dd></div>
        <div><dt>{L['city']}</dt><dd>{p.get('city_th' if lang=='th' else 'city_en') or L['bangkok']}</dd></div>
        <div><dt>{L['year']}</dt><dd>{p['year']}</dd></div>
        <div><dt>{L['area']}</dt><dd>{p['sqm']} {L['sqm']}</dd></div>
        <div><dt>{L['scope']}</dt><dd>{L['scope_v']}</dd></div>
      </dl></aside>
      <div class="narrative">
        <p>{T(p,lang)}</p>
        {pair}{plan}
        <div style="display:flex;gap:48px;flex-wrap:wrap">
          <div><div style="font-family:var(--font-display);font-weight:400;font-size:36px;color:var(--text-brand)">0</div><div style="font-size:11px;letter-spacing:.08em;color:var(--text-muted);font-weight:500">{L['disruption']}</div></div>
          <div><div style="font-family:var(--font-display);font-weight:400;font-size:36px;color:var(--text-brand)">5</div><div style="font-size:11px;letter-spacing:.08em;color:var(--text-muted);font-weight:500">{L['qc_shipped']}</div></div>
          <div><div style="font-family:var(--font-display);font-weight:400;font-size:36px;color:var(--text-brand)">{p['sqm']}</div><div style="font-size:11px;letter-spacing:.08em;color:var(--text-muted);font-weight:500">{L['sqm_delivered']}</div></div>
        </div>
      </div>
    </div>
  </section>
  {prevnext_html(p['slug'])}
  <section class="section">
    <div class="container"><h2 style="margin-bottom:40px">{more_lbl('luxury-retail')}</h2><div class="news-grid">{rel_html}</div></div>
  </section>
</main>
{cta_band(L)}{dock(P)}{footer(L,lang,P)}"""
        write(lang, f"project-{p['slug']}.html", htmlp)

    # ---- new single-location project pages ----
    def gallery_html(slug, imgs, start):
        rest = imgs[start:]
        if not rest: return ""
        cells = "".join(
            f'<img style="width:100%;object-fit:cover" src="{P}assets/img/works/{slug}/{f}.jpg" alt="{(ath if lang=="th" else aen)}" loading="lazy">'
            for f, aen, ath in rest)
        return f'<div class="art-grid" style="--cols:2">{cells}</div>'

    def fact_rail(rows):
        cells = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows if v)
        return f'<aside class="fact-rail"><dl>{cells}</dl></aside>'

    for p in NEWP:
        slug = p["slug"]; cat = p["cat"]
        hero_f, hero_aen, hero_ath = p["imgs"][0]
        hero = f'works/{slug}/{hero_f}'
        narr = p["narr_th"] if lang == "th" else p["narr_en"]
        ven = p.get("venue_th") if (lang == "th" and p.get("venue_th")) else p["venue"]
        city = p.get("city_th") if lang == "th" else p.get("city_en")
        scope = (p.get("scope") or SCOPE_FULL)[1 if lang == "th" else 0]
        pair = ""
        if len(p["imgs"]) > 1:
            cells = "".join(
                f'<img src="{P}assets/img/works/{slug}/{f}.jpg" alt="{(ath if lang=="th" else aen)}" loading="lazy">'
                for f, aen, ath in p["imgs"][1:3])
            pair = f'<div class="img-pair">{cells}</div>'
        rail = fact_rail([
            (L['client'], p["client"]), (L['venue'], ven), (L['city'], city),
            (L['year'], p.get("year")), (L['scope'], scope)])
        pld = proj_ld(p["title"], hero, p.get("year"), city, f"project-{slug}.html")
        htmlp = head(L, lang, P, f"project-{slug}.html", proj_title(p["title"]), narr[:150], f"assets/img/{hero}.jpg", pld) \
              + header_html(L, lang, P, f"project-{slug}.html", transparent=True) + f"""
<main>
  <section class="page-hero dark">
    <img class="bg" src="{P}assets/img/{hero}.jpg" alt="{(hero_ath if lang=='th' else hero_aen)}">
    <div class="scrim"></div>
    <div class="container">
      <p style="font-size:13px;opacity:.8;margin-bottom:16px"><a href="works.html">{L['nav_works']}</a> / <a href="works.html#{cat}">{L[CATKEY[cat]]}</a></p>
      <span class="eyebrow" style="color:var(--green-300)">{L[CATKEY[cat]].upper()}</span>
      <h1 class="display-l on-dark" style="margin-top:10px">{p['title']}</h1>
    </div>
  </section>
  <section class="section">
    <div class="container project-body">
      {rail}
      <div class="narrative">
        <p>{narr}</p>
        {pair}
        {gallery_html(slug, p["imgs"], 3)}
      </div>
    </div>
  </section>
  {prevnext_html(slug)}
  <section class="section">
    <div class="container"><h2 style="margin-bottom:40px">{more_lbl(cat)}</h2><div class="news-grid">{rel_cards(slug, cat)}</div></div>
  </section>
</main>
{cta_band(L)}{dock(P)}{footer(L,lang,P)}"""
        write(lang, f"project-{slug}.html", htmlp)

    # ---- grouped pages: brand rollouts + VM campaigns ----
    for g in GROUPS:
        slug = g["slug"]; cat = g["cat"]
        hero = f'works/{slug}/{g["hero"]}'
        narr = g["narr_th"] if lang == "th" else g["narr_en"]
        scope = g["scope"][1 if lang == "th" else 0]
        loc_lbl = ("แคมเปญ" if g["kind"] == "vm" else "สถานที่ติดตั้ง") if lang == "th" else \
                  ("Campaigns" if g["kind"] == "vm" else "Locations")
        loc_names = " · ".join((l["name_th"] if lang == "th" else l["name_en"]) for l in g["locs"])
        secs = []
        for l in g["locs"]:
            nm = l["name_th"] if lang == "th" else l["name_en"]
            sub = " · ".join(x for x in [(l.get("city_th") if lang == "th" else l.get("city_en")), l.get("year")] if x)
            cells = "".join(
                f'<img style="width:100%;object-fit:cover" src="{P}assets/img/works/{slug}/{f}.jpg" alt="{(ath if lang=="th" else aen)}" loading="lazy">'
                for f, aen, ath in l["imgs"])
            secs.append(
                f'<div style="margin-bottom:56px"><h2 style="font-size:24px;margin-bottom:4px">{nm}</h2>'
                + (f'<p class="muted" style="margin-bottom:16px;font-size:14px">{sub}</p>' if sub else '<div style="height:12px"></div>')
                + f'<div class="art-grid" style="--cols:2">{cells}</div></div>')
        rail = fact_rail([
            (L['client'], g["client"]), (loc_lbl, f'{len(g["locs"])} — {loc_names}'),
            (L['scope'], scope)])
        pld = proj_ld(g["title"], hero, None, None, f"project-{slug}.html")
        htmlp = head(L, lang, P, f"project-{slug}.html", proj_title(g["title"]), narr[:150], f"assets/img/{hero}.jpg", pld) \
              + header_html(L, lang, P, f"project-{slug}.html", transparent=True) + f"""
<main>
  <section class="page-hero dark">
    <img class="bg" src="{P}assets/img/{hero}.jpg" alt="{g['title']}">
    <div class="scrim"></div>
    <div class="container">
      <p style="font-size:13px;opacity:.8;margin-bottom:16px"><a href="works.html">{L['nav_works']}</a> / <a href="works.html#{cat}">{L[CATKEY[cat]]}</a></p>
      <span class="eyebrow" style="color:var(--green-300)">{L[CATKEY[cat]].upper()}</span>
      <h1 class="display-l on-dark" style="margin-top:10px">{g['title']}</h1>
    </div>
  </section>
  <section class="section">
    <div class="container project-body">
      {rail}
      <div class="narrative">
        <p>{narr}</p>
        {''.join(secs)}
      </div>
    </div>
  </section>
  {prevnext_html(slug)}
  <section class="section">
    <div class="container"><h2 style="margin-bottom:40px">{more_lbl(cat)}</h2><div class="news-grid">{rel_cards(slug, cat)}</div></div>
  </section>
</main>
{cta_band(L)}{dock(P)}{footer(L,lang,P)}"""
        write(lang, f"project-{slug}.html", htmlp)

    # ---- news ----
    feat = ARTICLES[0]
    cards = "".join(
        f'<a class="news-card reveal" href="article-{a["slug"]}.html">'
        + (f'<img src="{P}assets/img/{a["img"]}.jpg" alt="{A(a,"t")}" loading="lazy">' if a.get("img")
           else f'<div style="aspect-ratio:16/9;background:#fff;border:1px solid var(--border-subtle);display:flex;align-items:center;justify-content:center"><img src="{P}assets/img/sto-logo.png" alt="Save Thai Ocean Project" style="height:82%;width:auto;aspect-ratio:1;object-fit:contain"></div>')
        + f'<div class="meta">{acat(a)} · {adate(a)}</div><h3>{A(a,"t")}</h3></a>' for a in ARTICLES[1:])
    desc = ("ข่าวสารและกิจกรรมจาก Happexhibition — โปรเจกต์ โรงงาน ทีมงาน ความยั่งยืน" if lang=="th" else
            "News and activity from Happexhibition — projects, factory, people, sustainability.")
    news_title = ("ข่าวสาร — โปรเจกต์ โรงงาน และความยั่งยืน" if lang=="th" else "News — Projects, Factory & Sustainability")
    htmlp = head(L, lang, P, "news.html", news_title, desc) + header_html(L, lang, P, "news.html") + f"""
<main>
  <section class="page-hero">
    <div class="container"><span class="eyebrow">{L['news_eyebrow']}</span><h1 class="display-l">{L['news_h']}</h1></div>
  </section>
  <section class="section" style="padding-top:24px">
    <div class="container">
      <a class="featured reveal" href="article-{feat['slug']}.html" style="margin-bottom:80px">
        <img style="aspect-ratio:16/9" src="{P}assets/img/{feat['img']}.jpg" alt="{A(feat,'t')}">
        <div>
          <div class="news-card"><div class="meta">{acat(feat)} · {adate(feat)}</div></div>
          <h2 style="margin:8px 0 16px">{A(feat,'t')}</h2>
          <p class="body-l" style="color:var(--text-secondary)">{A(feat,'b1')[:180]}…</p>
        </div>
      </a>
      <div class="news-grid" style="margin-top:64px">{cards}</div>
    </div>
  </section>
</main>
{cta_band(L)}{dock(P)}{footer(L,lang,P)}"""
    write(lang, "news.html", htmlp)

    # ---- articles ----
    for a in ARTICLES:
        title = A(a,"t")
        if a.get("sto"):
            heroblock = f"""<div class="sto-hero"><div class="badge"><img src="{P}assets/img/sto-logo.png" alt="Save Thai Ocean Project"></div>
            <div class="big">฿73,300 {'raised' if lang=='en' else ''}</div><p>{'2,410 turtle cookies · trash pick-up equipment · shore cleanups with Koh Tao Clean Up' if lang=='en' else 'คุกกี้เต่า 2,410 ชิ้น · อุปกรณ์เก็บขยะ · เก็บขยะชายหาดร่วมกับ Koh Tao Clean Up'}</p></div>"""
            extra = f'<p><a class="btn btn-primary" href="https://www.instagram.com/savethaiocean/" target="_blank" rel="noopener">{"Follow @savethaiocean" if lang=="en" else "ติดตาม @savethaiocean"} {ARROW}</a> <a class="btn btn-secondary" href="https://www.facebook.com/savethaiocean" target="_blank" rel="noopener">Facebook</a></p>'
        else:
            heroblock = f'<div class="article-hero"><img src="{P}assets/img/{a["img"]}.jpg" alt="{title}"></div>'
            extra = ""
        grid = ""
        if a["grid"]:
            cols = min(len(a["grid"]),4)
            grid = f'<div class="art-grid" style="--cols:{cols}">' + \
                   "".join(f'<img style="aspect-ratio:1;object-fit:cover;width:100%" src="{P}assets/img/{g}.jpg" alt="">' for g in a["grid"]) + "</div>"
        ld = f"""<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{esc(title)}","datePublished":"{a['iso']}","inLanguage":"{lang}","image":"{BASE}/assets/img/{(a.get('img') or 'sto-logo')}.{'png' if not a.get('img') else 'jpg'}","author":{{"@type":"Organization","name":"Happexhibition"}},"publisher":{{"@type":"Organization","name":"Happexhibition","logo":{{"@type":"ImageObject","url":"{BASE}/assets/img/logo.png"}}}}}}</script>"""
        htmlp = head(L, lang, P, f"article-{a['slug']}.html", title, A(a,"b1")[:150],
                     f"assets/img/{a['img']}.jpg" if a.get("img") else "assets/img/sto-logo.png", ld) + header_html(L, lang, P, f"article-{a['slug']}.html") + f"""
<main>
  <article class="section article-top">
    <div class="container">
      <div class="article-col" style="text-align:center">
        <span class="eyebrow">{acat(a)} · {adate(a)} · {a['mins']} {L['min_read']}</span>
        <h1 style="margin-top:16px">{title}</h1>
      </div>
      {heroblock}
      <div class="article-col">
        <p>{A(a,'b1')}</p>
        <blockquote>“{A(a,'q')}”</blockquote>
        {grid}
        <p>{A(a,'b2')}</p>
        {extra}
        <div class="share-row"><span>{L['share']}</span>
          <a href="https://www.facebook.com/sharer/sharer.php" target="_blank" rel="noopener">Facebook</a>
          <a href="https://www.linkedin.com/sharing/share-offsite/" target="_blank" rel="noopener">LinkedIn</a>
          <a href="https://social-plugins.line.me/lineit/share" target="_blank" rel="noopener">LINE</a>
        </div>
      </div>
    </div>
  </article>
</main>
{cta_band(L)}{dock(P)}{footer(L,lang,P)}"""
        write(lang, f"article-{a['slug']}.html", htmlp)

    # ---- careers ----
    ben = "".join(f'<div class="benefit reveal"><h3>{(tth if lang=="th" else ten)}</h3><p>{(dth if lang=="th" else den)}</p></div>' for ten,tth,den,dth in BENEFITS)
    rows = "".join(f'<a class="job-row" href="role-senior-draftsman.html"><h3>{(tth if lang=="th" else ten)}</h3><span class="meta">{(mth if lang=="th" else men)}</span><span style="color:var(--text-brand)">→</span></a>' for ten,tth,men,mth in ROLES)
    desc = ("ร่วมงานกับ Happexhibition — ผู้ผลิตงานรีเทลลักชัวรีของกรุงเทพฯ" if lang=="th" else
            "Craft knowledge compounds. Join Happexhibition — Bangkok's luxury design-build fabricator.")
    htmlp = head(L, lang, P, "careers.html", L['nav_careers'], desc, "assets/img/team-dark.jpg") + header_html(L, lang, P, "careers.html", transparent=True) + f"""
<main>
  <section class="page-hero dark">
    <img class="bg" src="{P}assets/img/team-dark.jpg" alt="">
    <div class="scrim" style="background:linear-gradient(to bottom,rgba(21,77,52,.55),rgba(4,28,19,.9))"></div>
    <div class="container">
      <span class="eyebrow" style="color:var(--green-300)">{L['careers_eyebrow']}</span>
      <h1 class="display-l on-dark">{L['careers_h']}</h1>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <div class="section-header reveal"><div><h2>{L['why_stay']}</h2></div></div>
      <div class="benefit-grid">{ben}</div>
    </div>
  </section>
  <section class="section" style="padding-top:0">
    <div class="container gallery-3">
      <img src="{P}assets/img/craft-bench.jpg" alt=""><img src="{P}assets/img/red-lacquer.jpg" alt=""><img src="{P}assets/img/workshop-wide.jpg" alt="">
    </div>
  </section>
  <section class="section" style="background:var(--bg-subtle)">
    <div class="container article-col" style="max-width:820px"><h2 style="margin-bottom:32px">{L['open_roles']}</h2>{rows}</div>
  </section>
</main>
{cta_band(L)}{dock(P)}{footer(L,lang,P)}"""
    write(lang, "careers.html", htmlp)

    # ---- role ----
    resp = (["ผลิต shop drawing ที่พร้อมสร้างจริง จากไกด์ไลน์แบรนด์และแนวคิดสถาปนิก","ทำงาน 3 มิติตั้งแต่วันแรก — แก้ปัญหาวัสดุ ความคลาดเคลื่อน และข้อจำกัดหน้างาน","ประสานงานกับแผนกไม้ โลหะ กระจก และงานสีตลอดการผลิต","สนับสนุนการสำรวจหน้างานและเอกสาร as-built"]
            if lang=="th" else
            ["Produce build-ready shop drawings from brand guidelines and architects' intent","Work in 3D from day one — resolve materials, tolerances and site constraints","Coordinate with wood, metal, glass and paint departments through production","Support site surveys and as-built documentation"])
    resp_html = "".join(f"<li>• {r}</li>" for r in resp)
    rtitle = "ช่างเขียนแบบอาวุโส" if lang=="th" else "Senior Draftsman"
    htmlp = head(L, lang, P, "role-senior-draftsman.html", rtitle, L['role_meta']) + header_html(L, lang, P, "role-senior-draftsman.html") + f"""
<main>
  <section class="page-hero">
    <div class="container article-col" style="max-width:820px">
      <p style="font-size:13px;color:var(--text-muted);margin-bottom:12px"><a href="careers.html">{L['nav_careers']}</a> / {rtitle}</p>
      <h1>{rtitle}</h1><p class="muted" style="margin-top:8px">{L['role_meta']}</p>
    </div>
  </section>
  <section class="section" style="padding-top:24px">
    <div class="container article-col" style="max-width:820px">
      <ul style="list-style:none;display:flex;flex-direction:column;gap:10px;color:var(--text-secondary);font-size:16px;margin-bottom:40px">{resp_html}</ul>
      <div style="background:var(--bg-subtle);padding:48px">
        <h2 style="margin-bottom:24px">{L['apply_h']}</h2>
        <form class="form-grid" action="{APPLY_MAILTO}" method="get">
          <div class="field"><label for="a-name">{L['name']} *</label><input id="a-name" required placeholder="{L['ph_name']}"></div>
          <div class="field"><label for="a-email">{L['email']} *</label><input id="a-email" type="email" required placeholder="{L['ph_email']}"></div>
          <div class="field"><label for="a-phone">{L['phone']} *</label><input id="a-phone" placeholder="{L['ph_phone']}"></div>
          <div class="field"><label for="a-msg">{L['message']}</label><textarea id="a-msg" rows="4" placeholder="{L['ph_exp']}"></textarea></div>
          <div class="upload">{L['attach_note']}</div>
          <div><a class="btn btn-primary btn-lg" href="{APPLY_MAILTO}">{L['apply']} {ARROW}</a></div>
        </form>
      </div>
    </div>
  </section>
</main>
{cta_band(L)}{dock(P)}{footer(L,lang,P)}"""
    write(lang, "role-senior-draftsman.html", htmlp)

    # ---- contact ----
    lb = f"""<script type="application/ld+json">{{"@context":"https://schema.org","@type":"LocalBusiness","name":"Happ Exhibition Co., Ltd.","image":"{BASE}/assets/img/factory-exterior.jpg","telephone":"{TEL}","email":"{MAIL}","address":{{"@type":"PostalAddress","streetAddress":"52/8 Moo 11, Ladsawai, Lamlookka","addressLocality":"Pathumthani","postalCode":"12150","addressCountry":"TH"}},"openingHours":"Mo-Sa 08:30-17:30","url":"{BASE}/contact.html","sameAs":["{FB}","{IG}"]}}</script>"""
    desc = ("ติดต่อ บริษัท แฮพ เอ็กซิบิชั่น จำกัด — ปทุมธานี ประเทศไทย โทร +66 81-488-0475" if lang=="th" else
            "Contact Happ Exhibition Co., Ltd. — Pathumthani, Thailand. Call +66 81-488-0475 or add us on LINE @happexhibition.")
    contact_title = ("ติดต่อเรา — ขอใบเสนอราคาตกแต่งร้านและบูธ" if lang=="th" else "Contact — Get a Fit-Out or Booth Quote")
    htmlp = head(L, lang, P, "contact.html", contact_title, desc, "assets/img/factory-exterior.jpg", lb) + header_html(L, lang, P, "contact.html") + f"""
<main>
  <section class="page-hero">
    <div class="container"><span class="eyebrow">{L['contact_eyebrow']}</span><h1 class="display-l">{L['contact_h']}</h1></div>
  </section>
  <section class="section" style="padding-top:32px">
    <div class="container contact-split">
      <form class="form-grid" action="{CONTACT_MAILTO}" method="get">
        <div class="field"><label for="c-name">{L['name']} *</label><input id="c-name" required placeholder="{L['ph_name']}"></div>
        <div class="field"><label for="c-co">{L['company']}</label><input id="c-co" placeholder="{L['ph_company']}"></div>
        <div class="field"><label for="c-email">{L['email']} *</label><input id="c-email" type="email" required placeholder="{L['ph_email']}"></div>
        <div class="field"><label for="c-phone">{L['phone']}</label><input id="c-phone" placeholder="{L['ph_phone']}"></div>
        <div class="field"><label for="c-msg">{L['message']} *</label><textarea id="c-msg" rows="5" required placeholder="{L['ph_msg']}"></textarea>
        <div class="help">{L['reply_1d']}</div></div>
        <div><a class="btn btn-primary btn-lg" href="{CONTACT_MAILTO}">{L['send']} {ARROW}</a></div>
      </form>
      <div>
        <a class="map-embed" href="{MAPS}" target="_blank" rel="noopener"><img src="{P}assets/img/map.jpg" alt="{L['map_alt']}"></a>
        <address style="font-style:normal;font-size:15px;line-height:1.8;margin-top:24px;color:var(--text-secondary)">
          <strong style="color:var(--text-primary)">Happ Exhibition Co., Ltd.</strong><br>
          {L['addr_html']}<br><br>
          {L['ceo_line']}<br>
          <a href="{TELHREF}" style="color:var(--text-brand)">{TEL}</a><br>
          <a href="mailto:{MAIL}" style="color:var(--text-brand)">{MAIL}</a><br>
          LINE: @happexhibition · WeChat: nanathawat<br>
          {L['hours']}
        </address>
        <div class="qr-row">
          <img src="{P}assets/img/line-qr.png" alt="LINE QR — @happexhibition">
          <span style="font-size:14px;color:var(--text-secondary)">{L['scan']}<br><strong>@happexhibition</strong></span>
        </div>
      </div>
    </div>
  </section>
</main>
{cta_band(L)}{dock(P)}{footer(L,lang,P)}"""
    write(lang, "contact.html", htmlp)

    # ---- 404 ----
    htmlp = head(L, lang, P, "404.html", "404", L['nf_h']) + header_html(L, lang, P, "404.html") + f"""
<main class="nf container">
  <div class="code">404</div>
  <h2>{L['nf_h']}</h2>
  <div style="display:flex;gap:12px">
    <a class="btn btn-primary" href="index.html">{L['back_home']}</a>
    <a class="btn btn-secondary" href="works.html">{L['view_works']} {ARROW}</a>
  </div>
</main>
{dock(P)}{footer(L,lang,P)}"""
    write(lang, "404.html", htmlp)

# ==================== SEO FILES ====================
def build_seo():
    pages = ["index.html","about.html","services.html","works.html","news.html","careers.html","role-senior-draftsman.html","contact.html"] \
        + [f"project-{p['slug']}.html" for p in PROJECTS] \
        + [f"project-{p['slug']}.html" for p in NEWP] \
        + [f"project-{g['slug']}.html" for g in GROUPS] \
        + [f"article-{a['slug']}.html" for a in ARTICLES]
    urls = []
    for pg in pages:
        urls.append(f"""  <url><loc>{BASE}/{pg}</loc><lastmod>{LASTMOD}</lastmod>
    <xhtml:link rel="alternate" hreflang="en" href="{BASE}/{pg}"/>
    <xhtml:link rel="alternate" hreflang="th" href="{BASE}/th/{pg}"/>
  </url>
  <url><loc>{BASE}/th/{pg}</loc><lastmod>{LASTMOD}</lastmod>
    <xhtml:link rel="alternate" hreflang="en" href="{BASE}/{pg}"/>
    <xhtml:link rel="alternate" hreflang="th" href="{BASE}/th/{pg}"/>
  </url>""")
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n"
    open(os.path.join(OUT,"sitemap.xml"),"w").write(sm)
    open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    llms = f"""# Happ Exhibition Co., Ltd.

Design-build fabricator in Pathumthani, Thailand (Bangkok metro), founded 2004.
We design, fabricate and install: luxury retail stores and beauty counters,
interior fit-out, exhibition and event booths, pop-up stores, visual
merchandising campaigns and bespoke retail furniture — end to end, with our
own three factories (11,300 sqm) and overnight installation crews. Clients
include Chanel (10+ year partner), Gucci, Burberry, Van Cleef & Arpels,
Shiseido, Clé de Peau Beauté, Hourglass, Paul Smith and Pop Mart. Projects
delivered across Thailand (Bangkok, Chiang Mai, Udon Thani, Phuket, Khon Kaen)
and at airports (Suvarnabhumi, Chiang Mai).

- Services: {BASE}/services.html
- Works (34 case studies): {BASE}/works.html
- About: {BASE}/about.html
- Contact: {BASE}/contact.html — tel +66 81-488-0475, LINE @happexhibition
- Thai version: {BASE}/th/

Languages: English ({BASE}/) and Thai ({BASE}/th/).
"""
    open(os.path.join(OUT,"llms.txt"),"w").write(llms)
    print("sitemap.xml + robots.txt")

build_all("en")
build_all("th")
build_seo()
print("DONE: EN + TH + SEO")
