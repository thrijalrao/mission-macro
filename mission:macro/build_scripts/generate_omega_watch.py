# generate_omega_watch.py
"""
Generator for the photorealistic OMEGA Seamaster Diver 300M 007 Edition (Titanium) SVG.
Faithfully reconstructed from official Omega reference assets:
- Grade 2 Titanium Case with lyre lugs and polished chamfers
- Milanese mesh bracelet with end-links
- Tropical aluminum bezel ring with 12 scalloped wave grips and vintage tan diving scale
- Matte dark tropical dial with applied 3D vintage Super-LumiNova indices
- British Ministry of Defence Broad Arrow (Pheon)
- Skeletonized rhodium sword hands (Hour & Minute)
- Lollipop seconds hand with vivid red painted tip
- Domed sapphire crystal specular curvature reflection
- Bounded interactive dial hit-area
"""

import math

def build_omega_svg_file():
    cx, cy = 230, 280

    # 60 minute ticks on the dial flange
    ticks_svg = []
    for i in range(60):
        angle = i * 6 * (math.pi / 180)
        is_five = (i % 5 == 0)
        r1 = 114 if is_five else 117
        r2 = 124
        x1 = cx + r1 * math.sin(angle)
        y1 = cy - r1 * math.cos(angle)
        x2 = cx + r2 * math.sin(angle)
        y2 = cy - r2 * math.cos(angle)
        stroke_color = "#dfa868" if is_five else "#7a7469"
        stroke_w = 1.8 if is_five else 0.9
        ticks_svg.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke_color}" stroke-width="{stroke_w}"/>')

    # Hour markers (Vintage tan/caramel Super-LumiNova with 3D dark metal surround)
    markers_svg = []
    for i in range(1, 13):
        angle = i * 30 * (math.pi / 180)
        r_pos = 100
        mx = cx + r_pos * math.sin(angle)
        my = cy - r_pos * math.cos(angle)
        deg = i * 30

        if i == 12:
            # Dual batons at 12:00
            markers_svg.append(f'''
              <!-- 12:00 Dual Batons -->
              <g filter="url(#markerShadow)">
                <rect x="{cx - 8}" y="{cy - 112}" width="6" height="20" rx="2" fill="#24211d" stroke="#50483e" stroke-width="1"/>
                <rect x="{cx - 7}" y="{cy - 111}" width="4" height="18" rx="1.5" fill="url(#lumeGrad)" filter="url(#lumeGlow)"/>
                <rect x="{cx + 2}" y="{cy - 112}" width="6" height="20" rx="2" fill="#24211d" stroke="#50483e" stroke-width="1"/>
                <rect x="{cx + 3}" y="{cy - 111}" width="4" height="18" rx="1.5" fill="url(#lumeGrad)" filter="url(#lumeGlow)"/>
              </g>
            ''')
        elif i in [3, 6, 9]:
            # Single baton rotated at 3, 6, 9
            markers_svg.append(f'''
              <!-- Baton at {i}:00 -->
              <g transform="rotate({deg}, {cx}, {cy})" filter="url(#markerShadow)">
                <rect x="{cx - 3.5}" y="{cy - 112}" width="7" height="20" rx="2" fill="#24211d" stroke="#50483e" stroke-width="1"/>
                <rect x="{cx - 2.5}" y="{cy - 111}" width="5" height="18" rx="1.5" fill="url(#lumeGrad)" filter="url(#lumeGlow)"/>
              </g>
            ''')
        else:
            # Round cabochon dot with raised titanium bezel rim
            markers_svg.append(f'''
              <!-- Dot marker at {i}:00 -->
              <g filter="url(#markerShadow)">
                <circle cx="{mx:.1f}" cy="{my:.1f}" r="6.8" fill="#24211d" stroke="#5a5247" stroke-width="1.1"/>
                <circle cx="{mx:.1f}" cy="{my:.1f}" r="5.2" fill="url(#lumeGrad)" filter="url(#lumeGlow)"/>
                <circle cx="{mx - 1.2:.1f}" cy="{my - 1.2:.1f}" r="2.2" fill="#fffbe8" opacity="0.35"/>
              </g>
            ''')

    # Bezel numbers (10, 20, 30, 40, 50)
    bezel_nums = [
        (10, 60),
        (20, 120),
        (30, 180),
        (40, 240),
        (50, 300)
    ]
    bezel_nums_svg = []
    for num, deg in bezel_nums:
        bezel_nums_svg.append(f'''
          <g transform="rotate({deg}, {cx}, {cy})">
            <text x="{cx}" y="{cy - 146}" fill="#e6b372" font-family="'Space Grotesk', -apple-system, sans-serif" font-weight="700" font-size="16" letter-spacing="0.04em" text-anchor="middle" dominant-baseline="central">{num}</text>
          </g>
        ''')

    # Bezel minute hash marks
    bezel_ticks = []
    for m in range(1, 60):
        if m % 10 == 0: continue
        deg = m * 6
        is_five = (m % 5 == 0)
        is_early = (m <= 15)
        if not is_five and not is_early: continue
        r_inner = 149 if is_five else 153
        bezel_ticks.append(f'''
          <g transform="rotate({deg}, {cx}, {cy})">
            <line x1="{cx}" y1="{cy - 162}" x2="{cx}" y2="{cy - r_inner}" stroke="#dfa868" stroke-width="{2.0 if is_five else 1.2}" stroke-linecap="round"/>
          </g>
        ''')

    # Scalloped outer bezel facets (12 wave grips)
    scallops_svg = []
    for s in range(12):
        s_angle = s * 30 * (math.pi / 180)
        sx = cx + 175 * math.sin(s_angle)
        sy = cy - 175 * math.cos(s_angle)
        scallops_svg.append(f'''
          <circle cx="{sx:.1f}" cy="{sy:.1f}" r="12" fill="#525861" opacity="0.3"/>
          <circle cx="{sx:.1f}" cy="{sy:.1f}" r="10" fill="#32363d" opacity="0.4"/>
        ''')

    svg_content = f'''# omega_watch_svg.py
"""
1-on-1 Faithful Vector Reconstruction of the OMEGA Seamaster Diver 300M 007 Edition (No Time To Die)
Grade 2 Titanium Case, Milanese Mesh Bracelet, Tropical Aluminum 60-min Bezel,
Matte Tropical Dark Slate Dial, Vintage Super-LumiNova Faux Patina Indices,
British MoD Broad Arrow (Pheon) at 6:00, Domed Sapphire Crystal Curvature Highlight,
and 3 Functional Independent Hands:
1. Minute Hand: Exam Readiness Percentage (0% -> 100% = 0° -> 360°)
2. Hour Hand: Finished Core Chapters (0 -> 12 Chapters = 0° -> 360°, Excl. Dossier 13)
3. Seconds Hand: Mouse-Interactive INSIDE the Watch & Co-Axial 8 Hz Sweep
"""

def get_omega_seamaster_svg():
    return r\'\'\'<svg id="omegaSeamasterSvg" class="omega-seamaster-svg-instrument" viewBox="0 0 460 560" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Gradients for Grade 2 Titanium Case (Brushed & Satin) -->
        <linearGradient id="tiCaseGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#8a929e"/>
          <stop offset="20%" stop-color="#555a63"/>
          <stop offset="45%" stop-color="#9aa2af"/>
          <stop offset="55%" stop-color="#727985"/>
          <stop offset="80%" stop-color="#444952"/>
          <stop offset="100%" stop-color="#2d3138"/>
        </linearGradient>

        <linearGradient id="tiBevelGrad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#ccd2dc"/>
          <stop offset="50%" stop-color="#7e8591"/>
          <stop offset="100%" stop-color="#adb5c2"/>
        </linearGradient>

        <!-- Matte Tropical Dark Slate Dial Gradient -->
        <radialGradient id="dialGrad" cx="50%" cy="48%" r="52%">
          <stop offset="0%" stop-color="#2a2723"/>
          <stop offset="50%" stop-color="#1f1d1a"/>
          <stop offset="85%" stop-color="#161413"/>
          <stop offset="100%" stop-color="#0d0c0b"/>
        </radialGradient>

        <!-- Tropical Aluminum Bezel Ring Gradient -->
        <linearGradient id="bezelRingGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#332f2a"/>
          <stop offset="35%" stop-color="#211e1b"/>
          <stop offset="70%" stop-color="#2b2723"/>
          <stop offset="100%" stop-color="#171514"/>
        </linearGradient>

        <!-- Milanese Mesh Texture (Authentic Chainmail Weave) -->
        <pattern id="milaneseMesh" width="14" height="8" patternUnits="userSpaceOnUse">
          <!-- Back shadow -->
          <rect width="14" height="8" fill="#24272c"/>
          <!-- Loop highlights and shadows -->
          <path d="M 0 4 Q 3.5 0 7 4 Q 10.5 8 14 4" stroke="#131518" stroke-width="2.2" fill="none"/>
          <path d="M 0 4 Q 3.5 0 7 4 Q 10.5 8 14 4" stroke="#88909c" stroke-width="1.2" fill="none"/>
          <path d="M 0 4 Q 3.5 8 7 4 Q 10.5 0 14 4" stroke="#181a1d" stroke-width="1.8" fill="none"/>
          <path d="M 0 4 Q 3.5 8 7 4 Q 10.5 0 14 4" stroke="#606670" stroke-width="0.8" fill="none"/>
          <circle cx="7" cy="4" r="1.2" fill="#adb5c2"/>
        </pattern>

        <linearGradient id="meshSheen" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#000000" stop-opacity="0.6"/>
          <stop offset="25%" stop-color="#ffffff" stop-opacity="0.2"/>
          <stop offset="50%" stop-color="#000000" stop-opacity="0.4"/>
          <stop offset="75%" stop-color="#ffffff" stop-opacity="0.25"/>
          <stop offset="100%" stop-color="#000000" stop-opacity="0.7"/>
        </linearGradient>

        <!-- Vintage Super-LumiNova Faux Patina Gradient -->
        <linearGradient id="lumeGrad" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#fae0b8"/>
          <stop offset="40%" stop-color="#e5b376"/>
          <stop offset="100%" stop-color="#c89252"/>
        </linearGradient>

        <!-- Deep drop shadow for rotating hands -->
        <filter id="handShadow" x="-40%" y="-40%" width="180%" height="180%">
          <feDropShadow dx="4" dy="6" stdDeviation="4" flood-color="rgba(0,0,0,0.95)"/>
        </filter>

        <!-- Hour marker shadow -->
        <filter id="markerShadow" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="1" dy="2" stdDeviation="1.5" flood-color="rgba(0,0,0,0.8)"/>
        </filter>

        <!-- Super-LumiNova subtle photoluminescent glow -->
        <filter id="lumeGlow" x="-30%" y="-30%" width="160%" height="160%">
          <feGaussianBlur stdDeviation="0.8" result="blur"/>
          <feComposite in="SourceGraphic" in2="blur" operator="over"/>
        </filter>
      </defs>

      <!-- ============================================================== -->
      <!-- 1. MILANESE MESH BRACELET (GRADE 2 TITANIUM) -->
      <!-- ============================================================== -->
      <!-- Top Strap Section -->
      <g>
        <path d="M 160 0 L 300 0 L 294 150 L 166 150 Z" fill="#2d3137"/>
        <path d="M 160 0 L 300 0 L 294 150 L 166 150 Z" fill="url(#milaneseMesh)"/>
        <path d="M 160 0 L 300 0 L 294 150 L 166 150 Z" fill="url(#meshSheen)"/>
        <!-- Titanium Solid End-link Bar -->
        <rect x="162" y="138" width="136" height="15" rx="3" fill="url(#tiCaseGrad)" stroke="#1a1c1e" stroke-width="1.2"/>
        <line x1="164" y1="140" x2="296" y2="140" stroke="#bcc4cf" stroke-width="1"/>
      </g>

      <!-- Bottom Strap Section -->
      <g>
        <path d="M 166 410 L 294 410 L 300 560 L 160 560 Z" fill="#2d3137"/>
        <path d="M 166 410 L 294 410 L 300 560 L 160 560 Z" fill="url(#milaneseMesh)"/>
        <path d="M 166 410 L 294 410 L 300 560 L 160 560 Z" fill="url(#meshSheen)"/>
        <!-- Titanium Solid End-link Bar -->
        <rect x="162" y="407" width="136" height="15" rx="3" fill="url(#tiCaseGrad)" stroke="#1a1c1e" stroke-width="1.2"/>
        <line x1="164" y1="420" x2="296" y2="420" stroke="#33373d" stroke-width="1"/>
      </g>

      <!-- ============================================================== -->
      <!-- 2. TITANIUM CASE WITH SIGNATURE OMEGA LYRE LUGS -->
      <!-- ============================================================== -->
      <!-- Left Case Body & Lugs -->
      <path d="M 158 120 
               C 142 80 148 40 156 22 
               L 168 25 
               C 160 70 172 110 178 135 
               C 130 170 116 218 116 280 
               C 116 342 130 390 178 425 
               C 172 450 160 490 168 535 
               L 156 538 
               C 148 520 142 480 158 440 
               C 110 405 92 345 92 280 
               C 92 215 110 155 158 120 Z" 
            fill="url(#tiCaseGrad)" stroke="#1f2227" stroke-width="1.5"/>

      <!-- Right Case Body & Lugs -->
      <path d="M 302 120 
               C 318 80 312 40 304 22 
               L 292 25 
               C 300 70 288 110 282 135 
               C 330 170 344 218 344 280 
               C 344 342 330 390 282 425 
               C 288 450 300 490 292 535 
               L 304 538 
               C 312 520 318 480 302 440 
               C 350 405 368 345 368 280 
               C 368 215 350 155 302 120 Z" 
            fill="url(#tiCaseGrad)" stroke="#1f2227" stroke-width="1.5"/>

      <!-- Polished Twisted Lyre Lug Facets -->
      <path d="M 156 22 C 160 65 174 105 186 130 L 180 138 C 168 110 152 68 148 24 Z" fill="url(#tiBevelGrad)"/>
      <path d="M 304 22 C 300 65 286 105 274 130 L 280 138 C 292 110 308 68 312 24 Z" fill="url(#tiBevelGrad)"/>
      <path d="M 156 538 C 160 495 174 455 186 430 L 180 422 C 168 450 152 492 148 536 Z" fill="url(#tiBevelGrad)"/>
      <path d="M 304 538 C 300 495 286 455 274 430 L 280 422 C 292 450 308 492 312 536 Z" fill="url(#tiBevelGrad)"/>

      <!-- ============================================================== -->
      <!-- 3. HELIUM ESCAPE VALVE (10:00 CONICAL) -->
      <!-- ============================================================== -->
      <g transform="translate(122, 172) rotate(-42)">
        <polygon points="-11,-18 11,-18 14,-6 -14,-6" fill="url(#tiCaseGrad)" stroke="#1a1c1e" stroke-width="1.2"/>
        <!-- Fluting slots -->
        <line x1="-8" y1="-16" x2="-8" y2="-7" stroke="#222" stroke-width="1.4"/>
        <line x1="-4" y1="-16" x2="-4" y2="-7" stroke="#222" stroke-width="1.4"/>
        <line x1="0" y1="-16" x2="0" y2="-7" stroke="#222" stroke-width="1.4"/>
        <line x1="4" y1="-16" x2="4" y2="-7" stroke="#222" stroke-width="1.4"/>
        <line x1="8" y1="-16" x2="8" y2="-7" stroke="#222" stroke-width="1.4"/>
        <text x="0" y="-19" fill="#dfa868" font-family="'Space Grotesk', sans-serif" font-size="7" font-weight="700" text-anchor="middle">He</text>
      </g>

      <!-- ============================================================== -->
      <!-- 4. SCREW-DOWN CROWN & GUARDS (3:00) -->
      <!-- ============================================================== -->
      <path d="M 352 250 Q 372 262 376 270 L 376 290 Q 372 298 352 310 Z" fill="url(#tiCaseGrad)" stroke="#1a1c1e" stroke-width="1.2"/>
      <rect x="376" y="262" width="20" height="36" rx="3" fill="url(#tiCaseGrad)" stroke="#1a1c1e" stroke-width="1.5"/>
      <!-- Fluted teeth -->
      <line x1="381" y1="264" x2="381" y2="296" stroke="#222" stroke-width="1.2"/>
      <line x1="386" y1="264" x2="386" y2="296" stroke="#222" stroke-width="1.2"/>
      <line x1="391" y1="264" x2="391" y2="296" stroke="#222" stroke-width="1.2"/>
      <!-- Omega emblem on crown -->
      <text x="388" y="283" fill="#ffffff" font-family="'Cinzel', serif" font-size="11" font-weight="bold" text-anchor="middle">Ω</text>

      <!-- ============================================================== -->
      <!-- 5. SCALLOPED ROTATING DIVE BEZEL -->
      <!-- ============================================================== -->
      <!-- Outer Bezel Base -->
      <circle cx="{cx}" cy="{cy}" r="176" fill="url(#tiCaseGrad)" stroke="#17191c" stroke-width="2"/>
      <!-- 12 Ergonomic Scallop Grips -->
      {''.join(scallops_svg)}

      <!-- TROPICAL ALUMINUM BEZEL INSERT RING -->
      <circle cx="{cx}" cy="{cy}" r="166" fill="url(#bezelRingGrad)" stroke="#0d0c0b" stroke-width="2"/>
      <circle cx="{cx}" cy="{cy}" r="128" fill="none" stroke="#3d3730" stroke-width="1.2"/>

      <!-- 12 O'CLOCK BEZEL LUMINOUS TRIANGLE & PIP -->
      <polygon points="{cx},{cy - 165} {cx - 11},{cy - 148} {cx + 11},{cy - 148}" fill="#dfa868" stroke="#7a5526" stroke-width="1"/>
      <circle cx="{cx}" cy="{cy - 153}" r="4.2" fill="#24211d" stroke="#5a5247" stroke-width="0.8"/>
      <circle cx="{cx}" cy="{cy - 153}" r="3.2" fill="#fffbe8" filter="url(#lumeGlow)"/>

      <!-- BEZEL NUMERALS & TICKS -->
      {''.join(bezel_nums_svg)}
      {''.join(bezel_ticks)}

      <!-- ============================================================== -->
      <!-- 6. MATTE TROPICAL DARK SLATE DIAL -->
      <!-- ============================================================== -->
      <circle cx="{cx}" cy="{cy}" r="127" fill="url(#dialGrad)" stroke="#080707" stroke-width="1.5"/>

      <!-- MINUTE RAILROAD TRACK -->
      {''.join(ticks_svg)}

      <!-- VINTAGE SUPER-LUMINOVA HOUR INDICES -->
      {''.join(markers_svg)}

      <!-- DIAL BRANDING & MILITARY PHEON (BROAD ARROW) -->
      <text x="{cx}" y="{cy - 72}" fill="#ffffff" font-family="'Cinzel', serif" font-size="16" font-weight="700" text-anchor="middle">Ω</text>
      <text x="{cx}" y="{cy - 56}" fill="#ffffff" font-family="'Space Grotesk', -apple-system, sans-serif" font-size="11" font-weight="700" letter-spacing="0.18em" text-anchor="middle">OMEGA</text>
      <text x="{cx}" y="{cy - 42}" fill="#d92534" font-family="'Brush Script MT', cursive, Georgia, serif" font-size="15" font-style="italic" text-anchor="middle">Seamaster</text>
      <text x="{cx}" y="{cy - 30}" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-size="7.5" font-weight="600" letter-spacing="0.16em" text-anchor="middle">PROFESSIONAL</text>

      <text x="{cx}" y="{cy + 34}" fill="#d1d5db" font-family="'Space Grotesk', sans-serif" font-size="7.8" font-weight="600" letter-spacing="0.14em" text-anchor="middle">CO-AXIAL</text>
      <text x="{cx}" y="{cy + 45}" fill="#d1d5db" font-family="'Space Grotesk', sans-serif" font-size="7.8" font-weight="600" letter-spacing="0.12em" text-anchor="middle">MASTER CHRONOMETER</text>
      <text x="{cx}" y="{cy + 56}" fill="#d1d5db" font-family="'Space Grotesk', sans-serif" font-size="7.5" letter-spacing="0.1em" text-anchor="middle">300m / 1000ft</text>

      <!-- BRITISH MINISTRY OF DEFENCE BROAD ARROW (PHEON) -->
      <g transform="translate({cx}, {cy + 75})">
        <path d="M 0 -10 L 0 8 M 0 -10 L -6 -2 M 0 -10 L 6 -2" stroke="#dfa868" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" fill="none" filter="url(#lumeGlow)"/>
      </g>

      <text x="{cx - 18}" y="{cy + 120}" fill="#8a8377" font-family="'Space Grotesk', sans-serif" font-size="4.8" letter-spacing="0.08em" text-anchor="end">SWISS</text>
      <text x="{cx + 18}" y="{cy + 120}" fill="#8a8377" font-family="'Space Grotesk', sans-serif" font-size="4.8" letter-spacing="0.08em" text-anchor="start">MADE</text>

      <!-- ============================================================== -->
      <!-- 7. THREE FUNCTIONAL OMEGA 007 HANDS (INDEPENDENT ROTATION) -->
      <!-- ============================================================== -->

      <!-- 1. HOUR HAND (CHAPTERS 1-12 FINISHED COUNT) -->
      <g id="omegaHourHand" transform="rotate(0, {cx}, {cy})" filter="url(#handShadow)" style="transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1); transform-origin: {cx}px {cy}px; pointer-events: none;">
        <!-- Skeleton Hand Outer Body -->
        <polygon points="{cx - 5},{cy} {cx - 5},{cy - 52} {cx - 2.5},{cy - 57} {cx + 2.5},{cy - 57} {cx + 5},{cy - 52} {cx + 5},{cy}" fill="#b8bec8" stroke="#1f2328" stroke-width="0.9"/>
        <!-- Inner Openwork Cutout -->
        <rect x="{cx - 2.5}" y="{cy - 48}" width="5" height="34" fill="#1b1917"/>
        <!-- Prominent Skeleton Broad Arrow Tip with Vintage Lume -->
        <polygon points="{cx},{cy - 80} {cx - 15},{cy - 56} {cx + 15},{cy - 56}" fill="#b8bec8" stroke="#1f2328" stroke-width="0.9"/>
        <polygon points="{cx},{cy - 77} {cx - 12},{cy - 58} {cx + 12},{cy - 58}" fill="url(#lumeGrad)" filter="url(#lumeGlow)"/>
      </g>

      <!-- 2. MINUTE HAND (OVERALL READINESS PERCENTAGE 0%-100%) -->
      <g id="omegaMinuteHand" transform="rotate(0, {cx}, {cy})" filter="url(#handShadow)" style="transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1); transform-origin: {cx}px {cy}px; pointer-events: none;">
        <!-- Long Skeleton Hand Outer Body -->
        <polygon points="{cx - 4},{cy} {cx - 4},{cy - 90} {cx - 2},{cy - 95} {cx + 2},{cy - 95} {cx + 4},{cy - 90} {cx + 4},{cy}" fill="#ccd2dc" stroke="#1f2328" stroke-width="0.9"/>
        <!-- Inner Openwork Cutout -->
        <rect x="{cx - 2}" y="{cy - 84}" width="4" height="68" fill="#1b1917"/>
        <!-- Tapered Sword Tip with Lume -->
        <polygon points="{cx},{cy - 116} {cx - 4},{cy - 92} {cx + 4},{cy - 92}" fill="#ccd2dc" stroke="#1f2328" stroke-width="0.9"/>
        <polygon points="{cx},{cy - 113} {cx - 2.5},{cy - 94} {cx + 2.5},{cy - 94}" fill="url(#lumeGrad)" filter="url(#lumeGlow)"/>
      </g>

      <!-- 3. SECONDS HAND (MOUSE-INTERACTIVE WITHIN WATCH & 8 Hz SWEEP) -->
      <g id="omegaSecondsHand" transform="rotate(0, {cx}, {cy})" filter="url(#handShadow)" style="transform-origin: {cx}px {cy}px; pointer-events: none;">
        <!-- Counterbalance Tail -->
        <line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy + 34}" stroke="#ffffff" stroke-width="1.3"/>
        <circle cx="{cx}" cy="{cy + 22}" r="4.2" fill="#d1d5db" stroke="#222" stroke-width="0.9"/>
        <!-- Needle Shaft -->
        <line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy - 94}" stroke="#ffffff" stroke-width="1.2"/>
        <!-- Circular "Lollipop" Luminous Dot -->
        <circle cx="{cx}" cy="{cy - 94}" r="5.2" fill="#24211d" stroke="#d1d5db" stroke-width="0.9"/>
        <circle cx="{cx}" cy="{cy - 94}" r="4.0" fill="url(#lumeGrad)" filter="url(#lumeGlow)"/>
        <!-- VIVID RED PAINTED TIP (SIGNATURE BOND 007 DETAIL) -->
        <line x1="{cx}" y1="{cy - 99}" x2="{cx}" y2="{cy - 126}" stroke="#d92534" stroke-width="2.0" stroke-linecap="round"/>
        <circle cx="{cx}" cy="{cy - 125}" r="1.2" fill="#ff4d5a"/>
      </g>

      <!-- CENTER PINION & POLISHED STEEL CAP -->
      <circle cx="{cx}" cy="{cy}" r="6.5" fill="#888e96" stroke="#111" stroke-width="1.2" pointer-events="none"/>
      <circle cx="{cx}" cy="{cy}" r="4.0" fill="#c4cad4" pointer-events="none"/>
      <circle cx="{cx}" cy="{cy}" r="1.8" fill="#111" pointer-events="none"/>

      <!-- ============================================================== -->
      <!-- 8. DOMED SAPPHIRE CRYSTAL SPECULAR REFLECTION ARC -->
      <!-- ============================================================== -->
      <path d="M {cx - 105} {cy - 50} 
               A 125 125 0 0 1 {cx + 70} {cy - 105} 
               A 115 115 0 0 0 {cx - 90} {cy - 30} Z" 
            fill="#ffffff" opacity="0.14" pointer-events="none"/>
      <ellipse cx="{cx + 60}" cy="{cy - 65}" rx="35" ry="18" fill="#ffffff" opacity="0.05" transform="rotate(-30 {cx + 60} {cy - 65})" pointer-events="none"/>

      <!-- ============================================================== -->
      <!-- 9. BOUNDED INTERACTIVE DIAL HIT-AREA (CONFINED TO THE WATCH) -->
      <!-- ============================================================== -->
      <circle id="omegaDialHitArea" cx="{cx}" cy="{cy}" r="150" fill="transparent" style="cursor: crosshair;"/>
    </svg>\'\'\'
'''
    return svg_content

if __name__ == "__main__":
    code = build_omega_svg_file()
    with open("project_007_macroeconomics/build_scripts/omega_watch_svg.py", "w") as f:
        f.write(code)
    print("Generated photorealistic omega_watch_svg.py! Length:", len(code))
