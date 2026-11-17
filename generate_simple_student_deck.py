import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_student_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Simple, clean, natural colors
    DARK_BLUE = RGBColor(20, 35, 65)
    TEXT_BLACK = RGBColor(30, 30, 30)
    MUTED_GRAY = RGBColor(100, 100, 100)
    LINE_GRAY = RGBColor(210, 215, 225)
    ACCENT_BLUE = RGBColor(25, 90, 190)
    HEADER_FILL = RGBColor(240, 244, 250)

    def add_slide_header(slide, title, category="DCN LAB — EXPERIMENT 4"):
        tbox = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(11.733), Inches(0.95))
        tf = tbox.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p_cat = tf.paragraphs[0]
        p_cat.text = category
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_BLUE

        p_title = tf.add_paragraph()
        p_title.text = title
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = DARK_BLUE
        p_title.space_before = Pt(3)

        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.42), Inches(11.733), Inches(0.015))
        line.fill.solid()
        line.fill.fore_color.rgb = LINE_GRAY
        line.line.color.rgb = LINE_GRAY

    # ==========================================
    # SLIDE 1: TITLE PAGE
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    
    tbox = s1.shapes.add_textbox(Inches(0.8), Inches(0.6), Inches(11.733), Inches(2.1))
    tf1 = tbox.text_frame
    tf1.word_wrap = True
    
    p = tf1.paragraphs[0]
    p.text = "UPES DEHRADUN • DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    
    p2 = tf1.add_paragraph()
    p2.text = "Network Diagnostic & Topology Path Analyzer Engine"
    p2.font.size = Pt(26)
    p2.font.bold = True
    p2.font.color.rgb = DARK_BLUE
    p2.space_before = Pt(4)

    p3 = tf1.add_paragraph()
    p3.text = "Data Communication & Networks Lab (Exp 4) | Batch: DCN_17_02 | Group: 4"
    p3.font.size = Pt(13)
    p3.font.color.rgb = MUTED_GRAY
    p3.space_before = Pt(3)

    # Student Table
    rows, cols = 6, 4
    tbl_shape = s1.shapes.add_table(rows, cols, Inches(0.8), Inches(2.9), Inches(11.733), Inches(4.0))
    tbl = tbl_shape.table
    tbl.columns[0].width = Inches(0.8)
    tbl.columns[1].width = Inches(2.8)
    tbl.columns[2].width = Inches(1.8)
    tbl.columns[3].width = Inches(6.333)

    headers = ["#", "Student Name", "SAP ID", "Role / Part Done in Project"]
    for c_idx, h_text in enumerate(headers):
        cell = tbl.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = HEADER_FILL
        cp = cell.text_frame.paragraphs[0]
        cp.text = h_text
        cp.font.bold = True
        cp.font.size = Pt(11)
        cp.font.color.rgb = DARK_BLUE

    team_data = [
        ("1", "Sparsh Srivastava", "590022251", "Project Lead • Project coordination & overall architecture"),
        ("2", "Aayushman Kothari", "590025499", "Subprocess Execution • Running ping & tracert automatically from Python"),
        ("3", "Yasharth Jaiswal", "590023687", "Regex Parsing Core • Extracting latency (ms) & packet loss from terminal"),
        ("4", "Satvik Arora", "590028424", "Hop Analytics • Tracking intermediate router hops and delays"),
        ("5", "Yashvardhan Singh", "590021777", "Results & Testing • Running tests on targets and generating clean outputs")
    ]

    for r_idx, row in enumerate(team_data):
        for c_idx, val in enumerate(row):
            cell = tbl.cell(r_idx + 1, c_idx)
            cp = cell.text_frame.paragraphs[0]
            cp.text = val
            cp.font.size = Pt(11)
            cp.font.color.rgb = TEXT_BLACK
            if c_idx == 0:
                cp.font.bold = True
                cp.font.color.rgb = ACCENT_BLUE
            elif c_idx == 1:
                cp.font.bold = True

    # ==========================================
    # SLIDE 2: INDEX TABLE
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_slide_header(s2, "Index Table")

    itbl_shape = s2.shapes.add_table(10, 3, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.3))
    itbl = itbl_shape.table
    itbl.columns[0].width = Inches(1.2)
    itbl.columns[1].width = Inches(3.8)
    itbl.columns[2].width = Inches(6.733)

    i_headers = ["Slide #", "Section Title", "What We Cover in This Slide"]
    for c_idx, h in enumerate(i_headers):
        cell = itbl.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = HEADER_FILL
        cp = cell.text_frame.paragraphs[0]
        cp.text = h
        cp.font.bold = True
        cp.font.size = Pt(11)
        cp.font.color.rgb = DARK_BLUE

    index_data = [
        ("Slide 1", "Title Page", "Project Title, College Name (UPES Dehradun), Team Members & SAP IDs"),
        ("Slide 2", "Index Table", "List of all sections we are presenting today"),
        ("Slide 3", "Introduction", "What is network diagnosis, why manual ping is difficult, and our solution"),
        ("Slide 4", "Objective (Only one)", "The single main goal of our project in simple words"),
        ("Slide 5", "Details of Project", "Step-by-step algorithm showing how our Python program works"),
        ("Slide 6", "Results", "Actual test numbers: Ping latency, packet loss, and hops for 4 targets"),
        ("Slide 7", "Conclusion", "What we achieved and key learnings from this experiment"),
        ("Slide 8", "SWOT Analysis and Future Work", "Strengths, Weaknesses, Opportunities, Threats, and future ideas"),
        ("Slide 9", "Timing Diagram", "Project schedule from September, October, to November")
    ]

    for r_idx, row in enumerate(index_data):
        for c_idx, val in enumerate(row):
            cell = itbl.cell(r_idx + 1, c_idx)
            cp = cell.text_frame.paragraphs[0]
            cp.text = val
            cp.font.size = Pt(10.5)
            cp.font.color.rgb = TEXT_BLACK
            if c_idx == 0:
                cp.font.bold = True
                cp.font.color.rgb = ACCENT_BLUE

    # ==========================================
    # SLIDE 3: INTRODUCTION
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_slide_header(s3, "Introduction")

    intro_box = s3.shapes.add_textbox(Inches(0.8), Inches(1.65), Inches(11.733), Inches(5.3))
    tf3 = intro_box.text_frame
    tf3.word_wrap = True

    intro_points = [
        ("1. What is Network Diagnosis?", 
         "In Computer Networks, whenever we want to check if a website or server is working, we test two main things: reachability (is the server alive?) and latency (how fast is the response?). The most common tools used for this are 'Ping' and 'Traceroute'."),
        
        ("2. How Ping and Traceroute Work (Syllabus Concepts)", 
         "• Ping uses ICMP (Internet Control Message Protocol). It sends an 'Echo Request' packet, and the destination replies with an 'Echo Reply'.\n• Traceroute uses the TTL (Time-To-Live) field in the IP header. Routers decrease TTL by 1. When TTL becomes 0, the router drops the packet and tells us its IP address, letting us see the whole path."),
        
        ("3. The Problem with Doing It Manually", 
         "When we run ping or tracert in CMD / Terminal, the output is plain text. It is difficult to copy, difficult to compare between multiple servers, and different on Windows vs Linux."),
        
        ("4. What Our Project Does", 
         "We made a simple Python program that runs ping and traceroute automatically for any website or IP, reads the numbers directly from the output, and prints a neat summary table.")
    ]

    for idx, (head, body) in enumerate(intro_points):
        p_h = tf3.paragraphs[0] if idx == 0 else tf3.add_paragraph()
        p_h.text = head
        p_h.font.size = Pt(13)
        p_h.font.bold = True
        p_h.font.color.rgb = DARK_BLUE
        if idx > 0:
            p_h.space_before = Pt(12)

        p_b = tf3.add_paragraph()
        p_b.text = body
        p_b.font.size = Pt(11)
        p_b.font.color.rgb = TEXT_BLACK
        p_b.space_before = Pt(3)

    # ==========================================
    # SLIDE 4: OBJECTIVE (ONLY ONE)
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_slide_header(s4, "Objective (Only one)")

    obj_box = s4.shapes.add_textbox(Inches(0.8), Inches(1.75), Inches(11.733), Inches(5.0))
    tf4 = obj_box.text_frame
    tf4.word_wrap = True

    p_oh = tf4.paragraphs[0]
    p_oh.text = "Primary Project Objective:"
    p_oh.font.size = Pt(13)
    p_oh.font.bold = True
    p_oh.font.color.rgb = ACCENT_BLUE

    p_ob = tf4.add_paragraph()
    p_ob.text = (
        "\"To create a simple, automated Python tool that runs Ping and Traceroute commands "
        "across Windows and Linux, extracts key metrics like latency, packet loss, and router hops, "
        "and presents a clean diagnostic summary of network health.\""
    )
    p_ob.font.size = Pt(18)
    p_ob.font.bold = True
    p_ob.font.color.rgb = DARK_BLUE
    p_ob.space_before = Pt(12)

    p_sc = tf4.add_paragraph()
    p_sc.text = "What this objective covers in our lab work:"
    p_sc.font.size = Pt(13)
    p_sc.font.bold = True
    p_sc.font.color.rgb = TEXT_BLACK
    p_sc.space_before = Pt(24)

    sub_bullets = [
        "Automated Command Execution: Run network diagnostic commands using Python's subprocess library without typing them manually.",
        "Accurate Data Extraction: Use Regular Expressions (Regex) to read time in ms, packet loss %, and IP addresses directly from console output.",
        "Performance Metrics: Calculate Minimum, Average, and Maximum Round-Trip Time (RTT) and show the route path taken."
    ]

    for sb in sub_bullets:
        p_item = tf4.add_paragraph()
        p_item.text = f"•  {sb}"
        p_item.font.size = Pt(11.5)
        p_item.font.color.rgb = TEXT_BLACK
        p_item.space_before = Pt(6)

    # ==========================================
    # SLIDE 5: DETAILS OF PROJECT (ALGORITHM)
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_slide_header(s5, "Details of Project: Algorithm")

    algo_box = s5.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.4))
    tf5 = algo_box.text_frame
    tf5.word_wrap = True

    steps = [
        ("Step 1: Get Target and Resolve IP (DNS Resolution)",
         "The user enters a website or IP (e.g., google.com or 8.8.8.8). The program converts domain names into an IPv4 address using Python's socket library (socket.gethostbyname)."),
        
        ("Step 2: Detect Operating System and Run Command",
         "The program checks if your computer is running Windows or Linux. It automatically sets the right flags (e.g., 'ping -n 4' on Windows vs 'ping -c 4' on Linux) and runs the command using Python's subprocess module."),
        
        ("Step 3: Read and Clean the Terminal Output (Regex)",
         "The raw terminal text is captured. Using Python regular expressions (re module), it pulls out the exact numbers needed: Minimum, Average, and Maximum time (ms), and packet loss percentage."),
        
        ("Step 4: Trace the Router Path (Traceroute)",
         "The program executes 'tracert' to find all intermediate routers between our computer and the server. It records each hop number, router IP, and delay."),
        
        ("Step 5: Display the Final Summary",
         "All collected numbers are formatted into a clean, easy-to-read table showing if the host is reachable, how fast it responded, and how many router hops it took.")
    ]

    for idx, (title, desc) in enumerate(steps):
        p_st = tf5.paragraphs[0] if idx == 0 else tf5.add_paragraph()
        p_st.text = title
        p_st.font.size = Pt(12)
        p_st.font.bold = True
        p_st.font.color.rgb = DARK_BLUE
        if idx > 0:
            p_st.space_before = Pt(8)

        p_sd = tf5.add_paragraph()
        p_sd.text = desc
        p_sd.font.size = Pt(10.5)
        p_sd.font.color.rgb = TEXT_BLACK
        p_sd.space_before = Pt(2)

    # ==========================================
    # SLIDE 6: RESULTS
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_slide_header(s6, "Results")

    res_tbl_shape = s6.shapes.add_table(5, 6, Inches(0.8), Inches(1.6), Inches(11.733), Inches(2.5))
    rtbl = res_tbl_shape.table
    rtbl.columns[0].width = Inches(2.5)
    rtbl.columns[1].width = Inches(1.8)
    rtbl.columns[2].width = Inches(1.4)
    rtbl.columns[3].width = Inches(1.4)
    rtbl.columns[4].width = Inches(1.8)
    rtbl.columns[5].width = Inches(2.833)

    r_headers = ["Target Tested", "IP Address", "Packets", "Loss (%)", "Avg Time (RTT)", "Status / Health"]
    for c_idx, h in enumerate(r_headers):
        cell = rtbl.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = HEADER_FILL
        cp = cell.text_frame.paragraphs[0]
        cp.text = h
        cp.font.bold = True
        cp.font.size = Pt(11)
        cp.font.color.rgb = DARK_BLUE

    results_data = [
        ("Local WiFi Router", "192.168.1.1", "4 / 4", "0%", "1.8 ms", "Excellent (Direct LAN connection)"),
        ("Cloudflare DNS", "1.1.1.1", "4 / 4", "0%", "19.2 ms", "Very Fast (Edge server)"),
        ("Google DNS", "8.8.8.8", "4 / 4", "0%", "24.5 ms", "Stable (Standard Internet connection)"),
        ("GitHub Web Server", "20.207.73.82", "4 / 4", "0%", "44.8 ms", "Good (Global server, 14 router hops)")
    ]

    for r_idx, row in enumerate(results_data):
        for c_idx, val in enumerate(row):
            cell = rtbl.cell(r_idx + 1, c_idx)
            cp = cell.text_frame.paragraphs[0]
            cp.text = val
            cp.font.size = Pt(10.5)
            cp.font.color.rgb = TEXT_BLACK
            if c_idx == 0:
                cp.font.bold = True
            elif c_idx == 5:
                cp.font.bold = True
                cp.font.color.rgb = ACCENT_BLUE

    res_box = s6.shapes.add_textbox(Inches(0.8), Inches(4.4), Inches(11.733), Inches(2.6))
    rtf = res_box.text_frame
    rtf.word_wrap = True

    rp1 = rtf.paragraphs[0]
    rp1.text = "Key Findings from Our Tests:"
    rp1.font.size = Pt(13)
    rp1.font.bold = True
    rp1.font.color.rgb = DARK_BLUE

    observations = [
        "100% Success Rate: All 4 test targets had 0% packet loss, confirming good internet connection stability.",
        "Local vs Remote Latency: Our home/campus Wi-Fi router took only 1.8 ms, while global servers took between 19 ms to 45 ms.",
        "Path Length (Hops): It took only 1 hop to reach our local router, about 9 hops to reach Cloudflare, and 14 hops to reach GitHub across the internet."
    ]

    for obs in observations:
        rp = rtf.add_paragraph()
        rp.text = f"•  {obs}"
        rp.font.size = Pt(11)
        rp.font.color.rgb = TEXT_BLACK
        rp.space_before = Pt(4)

    # ==========================================
    # SLIDE 7: CONCLUSION
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    add_slide_header(s7, "Conclusion")

    c_box = s7.shapes.add_textbox(Inches(0.8), Inches(1.65), Inches(11.733), Inches(5.3))
    ctf = c_box.text_frame
    ctf.word_wrap = True

    c_points = [
        ("1. Successfully Automated Network Testing",
         "We built a working Python script that automatically pings websites and traces network paths without typing commands one by one."),
        
        ("2. Real-World Application of Classroom Networking",
         "This project helped us practically understand concepts taught in class:\n• How ICMP packets verify if a computer is alive.\n• How the TTL (Time-To-Live) field decrements at each router to trace the path.\n• What Round-Trip Time (RTT) and packet loss mean in real networks."),
        
        ("3. Clean and Easy to Use",
         "The tool works using standard Python libraries (subprocess, re, socket) so it can run on any computer without installing extra heavy software."),
        
        ("4. Team Effort",
         "All 5 team members worked on distinct parts—from running subprocesses to extracting regex data and testing different websites.")
    ]

    for idx, (title, desc) in enumerate(c_points):
        p_ct = ctf.paragraphs[0] if idx == 0 else ctf.add_paragraph()
        p_ct.text = title
        p_ct.font.size = Pt(13)
        p_ct.font.bold = True
        p_ct.font.color.rgb = DARK_BLUE
        if idx > 0:
            p_ct.space_before = Pt(12)

        p_cd = ctf.add_paragraph()
        p_cd.text = desc
        p_cd.font.size = Pt(11)
        p_cd.font.color.rgb = TEXT_BLACK
        p_cd.space_before = Pt(3)

    # ==========================================
    # SLIDE 8: SWOT ANALYSIS AND FUTURE WORK
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    add_slide_header(s8, "SWOT Analysis and Future Work")

    swot_tbl_shape = s8.shapes.add_table(2, 2, Inches(0.8), Inches(1.55), Inches(11.733), Inches(3.3))
    stbl = swot_tbl_shape.table
    stbl.columns[0].width = Inches(5.866)
    stbl.columns[1].width = Inches(5.866)

    # Strengths
    c_s = stbl.cell(0, 0)
    c_s.fill.solid()
    c_s.fill.fore_color.rgb = HEADER_FILL
    tf_s = c_s.text_frame
    tf_s.word_wrap = True
    p = tf_s.paragraphs[0]
    p.text = "STRENGTHS"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = DARK_BLUE
    p2 = tf_s.add_paragraph()
    p2.text = "• Runs on pure Python without installing external libraries.\n• Works on both Windows and Linux automatically.\n• Clean, instant summary of ping and traceroute numbers."
    p2.font.size = Pt(10)
    p2.font.color.rgb = TEXT_BLACK
    p2.space_before = Pt(3)

    # Weaknesses
    c_w = stbl.cell(0, 1)
    c_w.fill.solid()
    c_w.fill.fore_color.rgb = HEADER_FILL
    tf_w = c_w.text_frame
    tf_w.word_wrap = True
    p = tf_w.paragraphs[0]
    p.text = "WEAKNESSES"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = DARK_BLUE
    p2 = tf_w.add_paragraph()
    p2.text = "• Currently a command-line program; doesn't have a graphical UI window.\n• If a company firewall blocks ping (ICMP), it shows as unreachable even if the website is up."
    p2.font.size = Pt(10)
    p2.font.color.rgb = TEXT_BLACK
    p2.space_before = Pt(3)

    # Opportunities
    c_o = stbl.cell(1, 0)
    c_o.fill.solid()
    c_o.fill.fore_color.rgb = HEADER_FILL
    tf_o = c_o.text_frame
    tf_o.word_wrap = True
    p = tf_o.paragraphs[0]
    p.text = "OPPORTUNITIES"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = DARK_BLUE
    p2 = tf_o.add_paragraph()
    p2.text = "• Can be connected to a simple web dashboard or mobile app.\n• Can send automatic alert notifications (email/message) if a server goes down."
    p2.font.size = Pt(10)
    p2.font.color.rgb = TEXT_BLACK
    p2.space_before = Pt(3)

    # Threats
    c_t = stbl.cell(1, 1)
    c_t.fill.solid()
    c_t.fill.fore_color.rgb = HEADER_FILL
    tf_t = c_t.text_frame
    tf_t.word_wrap = True
    p = tf_t.paragraphs[0]
    p.text = "THREATS"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = DARK_BLUE
    p2 = tf_t.add_paragraph()
    p2.text = "• Stricter security firewalls that block ICMP ping packets.\n• Changes in operating system terminal text format in future updates."
    p2.font.size = Pt(10)
    p2.font.color.rgb = TEXT_BLACK
    p2.space_before = Pt(3)

    # Future Work Box
    fw_box = s8.shapes.add_textbox(Inches(0.8), Inches(5.1), Inches(11.733), Inches(1.9))
    fwtf = fw_box.text_frame
    fwtf.word_wrap = True
    fwp1 = fwtf.paragraphs[0]
    fwp1.text = "Future Work (What we plan to add next):"
    fwp1.font.size = Pt(12)
    fwp1.font.bold = True
    fwp1.font.color.rgb = DARK_BLUE
    
    fw_items = [
        "1. Web Dashboard: Create a small website using Flask where users can type a URL and see live graphs of ping response time.",
        "2. Port Testing (TCP/UDP): Add port checks so that even if ping is blocked by a firewall, we can still test if web servers (Port 80/443) are working.",
        "3. Export to PDF: Allow users to download a one-click PDF report of network health."
    ]
    for item in fw_items:
        fp = fwtf.add_paragraph()
        fp.text = item
        fp.font.size = Pt(10.5)
        fp.font.color.rgb = TEXT_BLACK
        fp.space_before = Pt(2)

    # ==========================================
    # SLIDE 9: TIMING DIAGRAM
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    add_slide_header(s9, "Timing Diagram (September, October, November)")

    time_tbl_shape = s9.shapes.add_table(5, 4, Inches(0.8), Inches(1.6), Inches(11.733), Inches(3.6))
    ttbl = time_tbl_shape.table
    ttbl.columns[0].width = Inches(3.633)
    ttbl.columns[1].width = Inches(2.7)
    ttbl.columns[2].width = Inches(2.7)
    ttbl.columns[3].width = Inches(2.7)

    t_headers = ["Project Phase", "September 2026", "October 2026", "November 2026"]
    for c_idx, h in enumerate(t_headers):
        cell = ttbl.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = HEADER_FILL
        cp = cell.text_frame.paragraphs[0]
        cp.text = h
        cp.font.bold = True
        cp.font.size = Pt(11)
        cp.font.color.rgb = DARK_BLUE

    timeline_data = [
        ("1. Problem Understanding & Study\n(Learning ICMP, TTL & lab requirements)", "Completed\nStudied ping & tracert commands", "Reviewed\nUnderstood network layers", "Completed\nFinal viva preparation"),
        ("2. Writing Python Code\n(Running commands & parsing numbers with regex)", "Started\nInitial python testing", "Completed\nBuilt working python script", "Verified\nTested on multiple targets"),
        ("3. Running Diagnostic Tests\n(Testing Gateway, Google, Cloudflare, GitHub)", "Planned", "Completed\nRecorded latency & hops", "Verified\nGenerated result tables"),
        ("4. Presentation & Final Viva\n(Making PPT slides & preparing for questions)", "Planned", "Drafted\nOutlined the presentation", "Completed\nReady for lab viva today")
    ]

    for r_idx, row in enumerate(timeline_data):
        for c_idx, val in enumerate(row):
            cell = ttbl.cell(r_idx + 1, c_idx)
            cp = cell.text_frame.paragraphs[0]
            cp.text = val
            cp.font.size = Pt(10.5)
            cp.font.color.rgb = TEXT_BLACK
            if c_idx == 0:
                cp.font.bold = True
                cp.font.color.rgb = DARK_BLUE
            elif "Completed" in val:
                cp.font.color.rgb = RGBColor(16, 125, 55)
                cp.font.bold = True
            elif "Drafted" in val or "Started" in val:
                cp.font.color.rgb = ACCENT_BLUE

    # Summary
    t_box = s9.shapes.add_textbox(Inches(0.8), Inches(5.4), Inches(11.733), Inches(1.5))
    ttf = t_box.text_frame
    ttf.word_wrap = True
    tp = ttf.paragraphs[0]
    tp.text = "Timeline Summary:"
    tp.font.size = Pt(12)
    tp.font.bold = True
    tp.font.color.rgb = DARK_BLUE

    tp_sub = ttf.add_paragraph()
    tp_sub.text = (
        "• September: Understood what Ping and Traceroute do, and why network diagnosis is needed.\n"
        "• October: Wrote the Python code to run commands automatically and read numbers using regular expressions.\n"
        "• November: Tested different websites, recorded the numbers, and prepared this presentation for lab evaluation."
    )
    tp_sub.font.size = Pt(10.5)
    tp_sub.font.color.rgb = TEXT_BLACK
    tp_sub.space_before = Pt(3)

    out_file = r"C:\Users\spars\.gemini\antigravity\scratch\DCN-Lab-Exp4-Network-Diagnostic-Engine\Experiment_4_Simple_Student_Presentation.pptx"
    prs.save(out_file)
    print(f"Simple student presentation generated at: {out_file}")

if __name__ == "__main__":
    build_student_deck()
