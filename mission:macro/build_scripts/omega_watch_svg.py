# omega_watch_svg.py
"""
PROJECT 007: 1-on-1 Faithful Vector Reconstruction of the OMEGA Seamaster Diver 300M 007 Edition (No Time To Die)
Strictly abiding by the official omegawatches.com reference image:
- 007 Striped NATO strap (dark brown, grey & beige) with titanium keeper loops (007) and OMEGA buckle bar
- Grade 2 Titanium Case with signature curved lyre lugs
- Prominent Screw-down Winding Crown with protective guards at 3:00 (knurled teeth + embossed Ω)
- Prominent Conical Helium Escape Valve at 10:00 (knurled teeth + engraved 'He')
- Scalloped rotating titanium dive bezel (12 ergonomic wave grips)
- Tropical dark brown aluminum bezel insert:
  * 12:00 Luminous Triangle pointing DOWNWARDS towards the dial with Super-LumiNova pearl pip
  * 0-15 minute individual tick marks
  * Bold numerals (10, 20, 30, 40, 50) and 5-min batons (15, 25, 35, 45, 55) in vintage tan lume
- Matte tropical dark chocolate dial:
  * Aged radium Super-LumiNova markers (batons at 12, 3, 6, 9; dots at 1, 2, 4, 5, 7, 8, 10, 11)
  * Dial branding: Ω, OMEGA, red script Seamaster, PROFESSIONAL, CO-AXIAL MASTER CHRONOMETER 300m/1000ft
  * British Ministry of Defence Broad Arrow (Pheon) at 6:00 and SWISS MADE
- 3 Functional Independent Hands centered at local origin (0, 0) inside translate(230, 280):
  1. Minute Hand: Exam Readiness Percentage (0% -> 100% = 0° -> 360°)
  2. Hour Hand: Finished Core Chapters (0 -> 12 Chapters = 0° -> 360°, Excl. Dossier 13)
  3. Seconds Hand: Mouse-Interactive INSIDE the Watch dial & authentic 8 Hz Co-Axial sweep
"""

import math

def get_omega_seamaster_svg():
    cx, cy = 230, 280

    # 12-scallop bezel outline polygon
    scallop_pts = []
    for i in range(24):
        angle_deg = i * 15 - 90
        rad = math.radians(angle_deg)
        r = 160 if (i % 2 == 0) else 153.5
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        scallop_pts.append(f"{round(x, 1)},{round(y, 1)}")
    scallop_polygon = " ".join(scallop_pts)

    # Bezel minute ticks (1 to 14 minutes, with 5 min bolder; 15, 25, 35, 45, 55 batons)
    bezel_ticks = []
    for m in range(1, 15):
        if m == 5:
            bezel_ticks.append(f'<g transform="rotate({m*6}, {cx}, {cy})"><line x1="{cx}" y1="126" x2="{cx}" y2="144" stroke="#dfa868" stroke-width="1.8" stroke-linecap="round"/></g>')
        elif m == 10:
            pass  # 10 is the numeral
        else:
            bezel_ticks.append(f'<g transform="rotate({m*6}, {cx}, {cy})"><line x1="{cx}" y1="128" x2="{cx}" y2="140" stroke="#dfa868" stroke-width="1.1" stroke-linecap="round"/></g>')
    for m in [15, 25, 35, 45, 55]:
        bezel_ticks.append(f'<g transform="rotate({m*6}, {cx}, {cy})"><line x1="{cx}" y1="125" x2="{cx}" y2="144" stroke="#dfa868" stroke-width="2.6" stroke-linecap="round"/></g>')
    bezel_ticks_markup = "\n".join(bezel_ticks)

    # Dial minute track (60 tick lines around dial perimeter)
    dial_ticks = []
    for m in range(60):
        if m % 5 == 0:
            dial_ticks.append(f'<g transform="rotate({m*6}, {cx}, {cy})"><line x1="{cx}" y1="162" x2="{cx}" y2="168" stroke="#dfa868" stroke-width="1.3" stroke-linecap="round"/></g>')
        else:
            dial_ticks.append(f'<g transform="rotate({m*6}, {cx}, {cy})"><line x1="{cx}" y1="163" x2="{cx}" y2="166.5" stroke="#8a8377" stroke-width="0.8"/></g>')
    dial_ticks_markup = "\n".join(dial_ticks)

    # Dial hour markers (dual baton at 12; single batons at 3, 6, 9; dots elsewhere)
    dial_markers = []
    for h in range(1, 13):
        deg = h * 30
        rad = math.radians(deg - 90)
        dist = 94
        mx = round(cx + dist * math.cos(rad), 1)
        my = round(cy + dist * math.sin(rad), 1)
        if h == 12:
            dial_markers.append(f'''<g filter="url(#markerShadow)">
              <rect x="{cx - 7}" y="174" width="5.5" height="17" rx="1.5" fill="#24211d" stroke="#50483e" stroke-width="0.9"/>
              <rect x="{cx - 6.2}" y="175" width="3.9" height="15" rx="1.2" fill="url(#lumeGrad)" filter="url(#lumeGlow)"/>
              <rect x="{cx + 1.5}" y="174" width="5.5" height="17" rx="1.5" fill="#24211d" stroke="#50483e" stroke-width="0.9"/>
              <rect x="{cx + 2.3}" y="175" width="3.9" height="15" rx="1.2" fill="url(#lumeGrad)" filter="url(#lumeGlow)"/>
            </g>''')
        elif h in [3, 6, 9]:
            dial_markers.append(f'''<g transform="rotate({deg}, {cx}, {cy})" filter="url(#markerShadow)">
              <rect x="{cx - 3}" y="174" width="6" height="17" rx="1.5" fill="#24211d" stroke="#50483e" stroke-width="0.9"/>
              <rect x="{cx - 2.1}" y="175" width="4.2" height="15" rx="1.2" fill="url(#lumeGrad)" filter="url(#lumeGlow)"/>
            </g>''')
        else:
            dial_markers.append(f'''<g filter="url(#markerShadow)">
              <circle cx="{mx}" cy="{my}" r="6.0" fill="#24211d" stroke="#5a5247" stroke-width="0.9"/>
              <circle cx="{mx}" cy="{my}" r="4.6" fill="url(#lumeGrad)" filter="url(#lumeGlow)"/>
              <circle cx="{round(mx-1, 1)}" cy="{round(my-1, 1)}" r="1.8" fill="#fffbe8" opacity="0.35"/>
            </g>''')
    dial_markers_markup = "\n".join(dial_markers)

    return f'''<svg id="omegaSeamasterSvg" class="omega-seamaster-svg-instrument" viewBox="0 0 460 560" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
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

        <!-- Matte Tropical Dark Chocolate Dial Gradient -->
        <radialGradient id="dialGrad" cx="50%" cy="48%" r="52%">
          <stop offset="0%" stop-color="#2a2622"/>
          <stop offset="50%" stop-color="#1f1d19"/>
          <stop offset="85%" stop-color="#161412"/>
          <stop offset="100%" stop-color="#0e0d0b"/>
        </radialGradient>

        <!-- Tropical Dark Brown Aluminum Bezel Ring Gradient -->
        <radialGradient id="bezelRingGrad" cx="50%" cy="50%" r="50%">
          <stop offset="70%" stop-color="#231f1c"/>
          <stop offset="85%" stop-color="#2c2723"/>
          <stop offset="100%" stop-color="#161412"/>
        </radialGradient>

        <!-- Authentic 007 Ballistic Nylon Woven Twill Weave -->
        <pattern id="natoWeave" width="4" height="4" patternUnits="userSpaceOnUse">
          <line x1="0" y1="0" x2="4" y2="4" stroke="rgba(0,0,0,0.3)" stroke-width="0.8"/>
          <line x1="0" y1="4" x2="4" y2="0" stroke="rgba(0,0,0,0.15)" stroke-width="0.6"/>
          <line x1="0" y1="2" x2="4" y2="2" stroke="rgba(255,255,255,0.08)" stroke-width="0.5"/>
        </pattern>

        <!-- Cylindrical Fabric Shading Gradient -->
        <linearGradient id="natoSheen" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#000000" stop-opacity="0.55"/>
          <stop offset="6%" stop-color="#000000" stop-opacity="0.12"/>
          <stop offset="50%" stop-color="#ffffff" stop-opacity="0.09"/>
          <stop offset="94%" stop-color="#000000" stop-opacity="0.12"/>
          <stop offset="100%" stop-color="#000000" stop-opacity="0.6"/>
        </linearGradient>

        <!-- Vintage Super-LumiNova Faux Patina Gradient -->
        <linearGradient id="lumeGrad" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#fae0b8"/>
          <stop offset="40%" stop-color="#e5b376"/>
          <stop offset="100%" stop-color="#c89252"/>
        </linearGradient>

        <!-- Brushed Grade 2 Titanium Hand Metal Gradient -->
        <linearGradient id="tiHandGrad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#dde3ed"/>
          <stop offset="25%" stop-color="#9aa2af"/>
          <stop offset="60%" stop-color="#69707b"/>
          <stop offset="85%" stop-color="#a8b0bd"/>
          <stop offset="100%" stop-color="#464c56"/>
        </linearGradient>

        <!-- Deep drop shadow for rotating hands -->
        <filter id="handShadow" x="-40%" y="-40%" width="180%" height="180%">
          <feDropShadow dx="3" dy="5" stdDeviation="3.5" flood-color="rgba(0,0,0,0.92)"/>
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
      <!-- 1. ICONIC 007 BOND 5-STRIPE NATO STRAP (DARK BROWN, GREY & BEIGE) -->
      <!-- ============================================================== -->
      <!-- Top Strap Section -->
      <g id="natoStrapTop">
        <rect x="168" y="0" width="124" height="150" fill="#1c1d1f"/>
        <rect x="168" y="0" width="18" height="150" fill="#1a1b1d"/>
        <rect x="186" y="0" width="18" height="150" fill="#5c5d60"/>
        <rect x="204" y="0" width="2" height="150" fill="#181716"/>
        <rect x="206" y="0" width="17" height="150" fill="#bfa588"/>
        <line x1="214.5" y1="0" x2="214.5" y2="150" stroke="#7a6752" stroke-width="0.8" stroke-dasharray="3,2"/>
        <rect x="223" y="0" width="14" height="150" fill="#23201d"/>
        <rect x="237" y="0" width="17" height="150" fill="#bfa588"/>
        <line x1="245.5" y1="0" x2="245.5" y2="150" stroke="#7a6752" stroke-width="0.8" stroke-dasharray="3,2"/>
        <rect x="254" y="0" width="2" height="150" fill="#181716"/>
        <rect x="256" y="0" width="18" height="150" fill="#5c5d60"/>
        <rect x="274" y="0" width="18" height="150" fill="#1a1b1d"/>
        <rect x="168" y="0" width="124" height="150" fill="url(#natoWeave)" opacity="0.45"/>
        <rect x="168" y="0" width="124" height="150" fill="url(#natoSheen)"/>
        <line x1="169" y1="0" x2="169" y2="150" stroke="#0a0a0b" stroke-width="1.2"/>
        <line x1="291" y1="0" x2="291" y2="150" stroke="#0a0a0b" stroke-width="1.2"/>
      </g>

      <!-- Bottom Strap Section -->
      <g id="natoStrapBottom">
        <rect x="168" y="410" width="124" height="150" fill="#1c1d1f"/>
        <rect x="168" y="410" width="18" height="150" fill="#1a1b1d"/>
        <rect x="186" y="410" width="18" height="150" fill="#5c5d60"/>
        <rect x="204" y="410" width="2" height="150" fill="#181716"/>
        <rect x="206" y="410" width="17" height="150" fill="#bfa588"/>
        <line x1="214.5" y1="410" x2="214.5" y2="560" stroke="#7a6752" stroke-width="0.8" stroke-dasharray="3,2"/>
        <rect x="223" y="410" width="14" height="150" fill="#23201d"/>
        <rect x="237" y="410" width="17" height="150" fill="#bfa588"/>
        <line x1="245.5" y1="410" x2="245.5" y2="560" stroke="#7a6752" stroke-width="0.8" stroke-dasharray="3,2"/>
        <rect x="254" y="410" width="2" height="150" fill="#181716"/>
        <rect x="256" y="410" width="18" height="150" fill="#5c5d60"/>
        <rect x="274" y="410" width="18" height="150" fill="#1a1b1d"/>
        <rect x="168" y="410" width="124" height="150" fill="url(#natoWeave)" opacity="0.45"/>
        <rect x="168" y="410" width="124" height="150" fill="url(#natoSheen)"/>
        <line x1="169" y1="410" x2="169" y2="560" stroke="#0a0a0b" stroke-width="1.2"/>
        <line x1="291" y1="410" x2="291" y2="560" stroke="#0a0a0b" stroke-width="1.2"/>
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
      <!-- 3. SCALLOPED DIVE BEZEL BASE (12 WAVE SCALLOPS) -->
      <!-- ============================================================== -->
      <!-- 12-Scallop Bezel Outer Ring Base -->
      <polygon points="{scallop_polygon}" fill="url(#tiCaseGrad)" stroke="#17191c" stroke-width="1.8"/>
      <!-- Inner Bezel Base Ring -->
      <circle cx="{cx}" cy="{cy}" r="152" fill="#2d3138" stroke="#121315" stroke-width="1.2"/>

      <!-- ============================================================== -->
      <!-- 4. SCREW-DOWN WINDING CROWN & CROWN GUARDS (3:00) -->
      <!-- Rendered ON TOP of case & bezel so it is 100% visible on right -->
      <!-- ============================================================== -->
      <g id="omegaCrownGroup">
        <!-- Upper Crown Guard -->
        <path d="M 368 246 Q 384 254 394 263 L 382 268 Q 372 260 366 254 Z" fill="url(#tiCaseGrad)" stroke="#181a1d" stroke-width="1.2"/>
        <!-- Lower Crown Guard -->
        <path d="M 366 306 Q 372 300 382 292 L 394 297 Q 384 306 368 314 Z" fill="url(#tiCaseGrad)" stroke="#181a1d" stroke-width="1.2"/>
        <!-- Crown Tube / Stem -->
        <rect x="382" y="271" width="6" height="18" fill="#1b1c1e"/>
        <!-- Knurled Titanium Crown Body -->
        <rect x="386" y="266" width="18" height="28" rx="2" fill="url(#tiCaseGrad)" stroke="#16181b" stroke-width="1.4"/>
        <!-- Fluted Knurling Teeth -->
        <line x1="390" y1="267" x2="390" y2="293" stroke="#161719" stroke-width="1.3"/>
        <line x1="394" y1="267" x2="394" y2="293" stroke="#161719" stroke-width="1.3"/>
        <line x1="398" y1="267" x2="398" y2="293" stroke="#161719" stroke-width="1.3"/>
        <line x1="402" y1="267" x2="402" y2="293" stroke="#161719" stroke-width="1.3"/>
        <!-- Crown Outer End Cap with Embossed Omega Logo -->
        <path d="M 404 268 Q 412 272 412 280 Q 412 288 404 292 Z" fill="url(#tiBevelGrad)" stroke="#16181b" stroke-width="1.2"/>
        <text x="408" y="283.5" fill="#ffffff" font-family="'Cinzel', serif" font-size="9" font-weight="900" text-anchor="middle" dominant-baseline="central">Ω</text>
      </g>

      <!-- ============================================================== -->
      <!-- 5. HELIUM ESCAPE VALVE (10:00 CONICAL) -->
      <!-- Rendered ON TOP of case so it is 100% visible on upper-left -->
      <!-- ============================================================== -->
      <g id="omegaHeliumValve" transform="translate(102, 206) rotate(-38)">
        <rect x="-7" y="-5" width="14" height="6" fill="#1a1c1e"/>
        <polygon points="-12,-20 12,-20 15,-5 -15,-5" fill="url(#tiCaseGrad)" stroke="#16181b" stroke-width="1.3"/>
        <!-- Fluted Grip Teeth -->
        <line x1="-8" y1="-19" x2="-10" y2="-6" stroke="#222" stroke-width="1.3"/>
        <line x1="-4" y1="-19" x2="-5" y2="-6" stroke="#222" stroke-width="1.3"/>
        <line x1="0" y1="-19" x2="0" y2="-6" stroke="#222" stroke-width="1.3"/>
        <line x1="4" y1="-19" x2="5" y2="-6" stroke="#222" stroke-width="1.3"/>
        <line x1="8" y1="-19" x2="10" y2="-6" stroke="#222" stroke-width="1.3"/>
        <!-- Engraved Outer Cap with 'He' -->
        <ellipse cx="0" cy="-20" rx="12" ry="4" fill="url(#tiBevelGrad)" stroke="#16181b" stroke-width="1.2"/>
        <text x="0" y="-19.5" fill="#dfa868" font-family="'Space Grotesk', sans-serif" font-size="6.8" font-weight="700" text-anchor="middle" dominant-baseline="central">He</text>
      </g>

      <!-- ============================================================== -->
      <!-- 6. TROPICAL DARK BROWN ALUMINUM BEZEL INSERT RING -->
      <!-- ============================================================== -->
      <!-- Dark Brown Bezel Insert Track -->
      <circle cx="{cx}" cy="{cy}" r="150" fill="url(#bezelRingGrad)" stroke="#0e0d0c" stroke-width="1.8"/>
      <!-- Inner Bezel Metal Border -->
      <circle cx="{cx}" cy="{cy}" r="121" fill="none" stroke="#3d3730" stroke-width="1.2"/>

      <!-- 12:00 LUMINOUS TRIANGLE (POINTING DOWNWARDS TOWARDS THE DIAL) -->
      <!-- Base at top y=126, vertex pointing down at y=150 into dial! -->
      <polygon points="{cx - 13},126 {cx + 13},126 {cx},150" fill="none" stroke="#dfa868" stroke-width="2.2" stroke-linejoin="round"/>
      <!-- Super-LumiNova Pearl Pip inside the triangle -->
      <circle cx="{cx}" cy="137" r="4.8" fill="#24211d" stroke="#5a5247" stroke-width="1.1"/>
      <circle cx="{cx}" cy="137" r="3.6" fill="#fffbe8" filter="url(#lumeGlow)"/>

      <!-- BEZEL MINUTE TICKS (0 to 15 min & 5-min batons) -->
      {bezel_ticks_markup}

      <!-- BEZEL NUMERALS (10, 20, 30, 40, 50 in bold vintage tan lume) -->
      <g transform="rotate(60, {cx}, {cy})">
        <text x="{cx}" y="144" fill="#dfa868" font-family="'Space Grotesk', -apple-system, sans-serif" font-weight="800" font-size="16" letter-spacing="0.04em" text-anchor="middle" dominant-baseline="central">10</text>
      </g>
      <g transform="rotate(120, {cx}, {cy})">
        <text x="{cx}" y="144" fill="#dfa868" font-family="'Space Grotesk', -apple-system, sans-serif" font-weight="800" font-size="16" letter-spacing="0.04em" text-anchor="middle" dominant-baseline="central">20</text>
      </g>
      <g transform="rotate(180, {cx}, {cy})">
        <text x="{cx}" y="144" fill="#dfa868" font-family="'Space Grotesk', -apple-system, sans-serif" font-weight="800" font-size="16" letter-spacing="0.04em" text-anchor="middle" dominant-baseline="central">30</text>
      </g>
      <g transform="rotate(240, {cx}, {cy})">
        <text x="{cx}" y="144" fill="#dfa868" font-family="'Space Grotesk', -apple-system, sans-serif" font-weight="800" font-size="16" letter-spacing="0.04em" text-anchor="middle" dominant-baseline="central">40</text>
      </g>
      <g transform="rotate(300, {cx}, {cy})">
        <text x="{cx}" y="144" fill="#dfa868" font-family="'Space Grotesk', -apple-system, sans-serif" font-weight="800" font-size="16" letter-spacing="0.04em" text-anchor="middle" dominant-baseline="central">50</text>
      </g>

      <!-- ============================================================== -->
      <!-- 7. MATTE TROPICAL DARK CHOCOLATE DIAL FACE -->
      <!-- ============================================================== -->
      <circle cx="{cx}" cy="{cy}" r="120" fill="url(#dialGrad)" stroke="#080707" stroke-width="1.5"/>

      <!-- DIAL MINUTE TRACK (60 TICKS) -->
      {dial_ticks_markup}

      <!-- VINTAGE SUPER-LUMINOVA HOUR INDICES -->
      {dial_markers_markup}

      <!-- DIAL BRANDING (12:00) -->
      <text x="{cx}" y="208" fill="#ffffff" font-family="'Cinzel', serif" font-size="16" font-weight="700" text-anchor="middle">Ω</text>
      <text x="{cx}" y="224" fill="#ffffff" font-family="'Space Grotesk', -apple-system, sans-serif" font-size="11" font-weight="700" letter-spacing="0.18em" text-anchor="middle">OMEGA</text>
      <text x="{cx}" y="238" fill="#d92534" font-family="'Brush Script MT', cursive, Georgia, serif" font-size="15" font-style="italic" text-anchor="middle">Seamaster</text>
      <text x="{cx}" y="250" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-size="7.5" font-weight="600" letter-spacing="0.16em" text-anchor="middle">PROFESSIONAL</text>

      <!-- LOWER DIAL TELEMETRY & MILITARY PHEON (6:00) -->
      <text x="{cx}" y="312" fill="#d1d5db" font-family="'Space Grotesk', sans-serif" font-size="7.6" font-weight="600" letter-spacing="0.14em" text-anchor="middle">CO-AXIAL</text>
      <text x="{cx}" y="324" fill="#d1d5db" font-family="'Space Grotesk', sans-serif" font-size="7.0" font-weight="600" letter-spacing="0.14em" text-anchor="middle">MASTER CHRONOMETER</text>
      <text x="{cx}" y="336" fill="#d1d5db" font-family="'Space Grotesk', sans-serif" font-size="6.6" letter-spacing="0.12em" text-anchor="middle">300m / 1000ft</text>

      <!-- BRITISH MINISTRY OF DEFENCE BROAD ARROW (PHEON) -->
      <g transform="translate({cx}, 353)">
        <path d="M 0 -10 L 0 8 M 0 -10 L -6 -2 M 0 -10 L 6 -2" stroke="#dfa868" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" fill="none" filter="url(#lumeGlow)"/>
      </g>

      <text x="{cx - 18}" y="396" fill="#8a8377" font-family="'Space Grotesk', sans-serif" font-size="4.8" letter-spacing="0.08em" text-anchor="end">SWISS</text>
      <text x="{cx + 18}" y="396" fill="#8a8377" font-family="'Space Grotesk', sans-serif" font-size="4.8" letter-spacing="0.08em" text-anchor="start">MADE</text>

      <!-- ============================================================== -->
      <!-- 8. THREE FUNCTIONAL OMEGA 007 HANDS (INDEPENDENT ROTATION) -->
      <!-- Centered at local origin (0,0) inside parent translate(230,280) -->
      <!-- Guaranteed to never drift or exit the dial across all browsers -->
      <!-- ============================================================== -->
      <g id="omegaHandsStage" transform="translate({cx}, {cy})" pointer-events="none">

        <!-- 1. HOUR HAND (AUTHENTIC SEAMASTER SKELETON BROAD ARROW) -->
        <g id="omegaHourHand" transform="rotate(0)" filter="url(#handShadow)">
          <!-- Base Circular Ring/Collar -->
          <circle cx="0" cy="0" r="7.5" fill="url(#tiHandGrad)" stroke="#1a1c1f" stroke-width="0.8"/>
          <circle cx="0" cy="0" r="5.2" fill="none" stroke="#25292f" stroke-width="0.6"/>

          <!-- True Openwork Skeleton Frame (fill-rule evenodd for physical cutout) -->
          <path d="M -3.8 0 
                   L -3.8 -33 
                   L -8.2 -33 
                   L -6.5 -36.5 
                   L 0 -62 
                   L 6.5 -36.5 
                   L 8.2 -33 
                   L 3.8 -33 
                   L 3.8 0 
                   Z 
                   M -1.8 -7 
                   L 1.8 -7 
                   L 1.8 -30 
                   L -1.8 -30 
                   Z" 
                fill="url(#tiHandGrad)" 
                fill-rule="evenodd" 
                stroke="#181a1d" 
                stroke-width="0.8" 
                stroke-linejoin="round"/>

          <!-- Left Rail Specular Highlight (Catching Light) -->
          <line x1="-3.4" y1="-1" x2="-3.4" y2="-32.5" stroke="#eef2f8" stroke-width="0.7" opacity="0.8"/>
          <!-- Right Rail Ambient Shadow (Depth) -->
          <line x1="3.4" y1="-1" x2="3.4" y2="-32.5" stroke="#383d46" stroke-width="0.7"/>

          <!-- Inner Cutout Chamfer Borders -->
          <line x1="-1.4" y1="-7" x2="-1.4" y2="-30" stroke="#33373f" stroke-width="0.5"/>
          <line x1="1.4" y1="-7" x2="1.4" y2="-30" stroke="#cbd2de" stroke-width="0.5" opacity="0.7"/>

          <!-- Broad Arrow Head Luminous Cell -->
          <!-- Outer Chamfer Border -->
          <polygon points="-6.0,-35.5 0,-58.5 6.0,-35.5" fill="#24211d" stroke="#50483e" stroke-width="0.8"/>
          <!-- Aged Super-LumiNova Faux Patina Infill -->
          <polygon points="-5.0,-36 0,-56.5 5.0,-36" fill="url(#lumeGrad)" filter="url(#lumeGlow)"/>
          <!-- Domed Lume Specular Highlight -->
          <line x1="-2.0" y1="-38" x2="0" y2="-52" stroke="#fffbe8" stroke-width="0.8" opacity="0.45" stroke-linecap="round"/>
        </g>

        <!-- 2. MINUTE HAND (AUTHENTIC SEAMASTER SKELETON SWORD HAND) -->
        <g id="omegaMinuteHand" transform="rotate(0)" filter="url(#handShadow)">
          <!-- Base Circular Ring/Collar -->
          <circle cx="0" cy="0" r="7.0" fill="url(#tiHandGrad)" stroke="#1a1c1f" stroke-width="0.8"/>
          <circle cx="0" cy="0" r="4.8" fill="none" stroke="#25292f" stroke-width="0.6"/>

          <!-- True Openwork Skeleton Frame (fill-rule evenodd for physical cutout) -->
          <path d="M -3.2 0 
                   L -3.2 -67 
                   L -5.2 -67 
                   L 0 -94 
                   L 5.2 -67 
                   L 3.2 -67 
                   L 3.2 0 
                   Z 
                   M -1.5 -7 
                   L 1.5 -7 
                   L 1.5 -64 
                   L -1.5 -64 
                   Z" 
                fill="url(#tiHandGrad)" 
                fill-rule="evenodd" 
                stroke="#181a1d" 
                stroke-width="0.8" 
                stroke-linejoin="round"/>

          <!-- Left Rail Specular Highlight (Catching Light) -->
          <line x1="-2.8" y1="-1" x2="-2.8" y2="-66" stroke="#eef2f8" stroke-width="0.7" opacity="0.8"/>
          <!-- Right Rail Ambient Shadow (Depth) -->
          <line x1="2.8" y1="-1" x2="2.8" y2="-66" stroke="#383d46" stroke-width="0.7"/>

          <!-- Inner Cutout Chamfer Borders -->
          <line x1="-1.2" y1="-7" x2="-1.2" y2="-64" stroke="#33373f" stroke-width="0.5"/>
          <line x1="1.2" y1="-7" x2="1.2" y2="-64" stroke="#cbd2de" stroke-width="0.5" opacity="0.7"/>

          <!-- Sword Tip Luminous Cell -->
          <!-- Outer Chamfer Border -->
          <polygon points="-4.0,-69 0,-90.5 4.0,-69" fill="#24211d" stroke="#50483e" stroke-width="0.8"/>
          <!-- Aged Super-LumiNova Faux Patina Infill -->
          <polygon points="-3.2,-69.5 0,-88.5 3.2,-69.5" fill="url(#lumeGrad)" filter="url(#lumeGlow)"/>
          <!-- Domed Lume Specular Highlight -->
          <line x1="-1.2" y1="-72" x2="0" y2="-84" stroke="#fffbe8" stroke-width="0.7" opacity="0.45" stroke-linecap="round"/>
        </g>

        <!-- 3. SECONDS HAND (AUTHENTIC BOND LOLLIPOP WITH RED TIP) -->
        <g id="omegaSecondsHand" transform="rotate(0)" filter="url(#handShadow)">
          <!-- Circular Center Pivot Boss -->
          <circle cx="0" cy="0" r="2.8" fill="#e2e7ef" stroke="#25292f" stroke-width="0.6"/>

          <!-- Counterbalance Tail -->
          <line x1="0" y1="0" x2="0" y2="28" stroke="#ffffff" stroke-width="1.1"/>
          <!-- Openwork Counterweight Ring -->
          <circle cx="0" cy="18" r="4.2" fill="url(#tiHandGrad)" stroke="#1a1c1f" stroke-width="0.8"/>
          <circle cx="0" cy="18" r="2.0" fill="#1b1c1e"/>

          <!-- Needle Shaft -->
          <line x1="0" y1="0" x2="0" y2="-69" stroke="#ffffff" stroke-width="1.1"/>

          <!-- Circular "Lollipop" Luminous Dot -->
          <circle cx="0" cy="-69" r="5.2" fill="#24211d" stroke="#50483e" stroke-width="0.9"/>
          <circle cx="0" cy="-69" r="4.0" fill="url(#lumeGrad)" filter="url(#lumeGlow)"/>
          <circle cx="-1.0" cy="-70" r="1.3" fill="#fffbe8" opacity="0.45"/>

          <!-- Signature Vivid Red Painted Tip -->
          <line x1="0" y1="-74.5" x2="0" y2="-102" stroke="#d92534" stroke-width="1.9" stroke-linecap="round"/>
          <circle cx="0" cy="-102" r="1.1" fill="#ff4d5a"/>
          <circle cx="0" cy="-101" r="0.5" fill="#ffffff" opacity="0.6"/>
        </g>

        <!-- CENTER PINION & MULTI-TIER POLISHED STEEL CAP -->
        <circle cx="0" cy="0" r="6.2" fill="url(#tiCaseGrad)" stroke="#16181b" stroke-width="1.0"/>
        <circle cx="0" cy="0" r="4.4" fill="url(#tiBevelGrad)" stroke="#222" stroke-width="0.5"/>
        <circle cx="0" cy="0" r="2.8" fill="#dce2eb"/>
        <circle cx="0" cy="0" r="1.3" fill="#121316"/>
      </g>

      <!-- ============================================================== -->
      <!-- 9. DOMED SAPPHIRE CRYSTAL SPECULAR REFLECTION ARC -->
      <!-- ============================================================== -->
      <path d="M 135 230 
               A 115 115 0 0 1 295 180 
               A 105 105 0 0 0 148 248 Z" 
            fill="#ffffff" opacity="0.14" pointer-events="none"/>
      <ellipse cx="285" cy="220" rx="30" ry="15" fill="#ffffff" opacity="0.05" transform="rotate(-30 285 220)" pointer-events="none"/>

      <!-- ============================================================== -->
      <!-- 10. BRUSHED TITANIUM NATO HARDWARE (KEEPERS & OMEGA BUCKLE) -->
      <!-- ============================================================== -->
      <!-- Top Titanium Keeper Loop (Above 12:00) -->
      <g id="natoTopKeeper">
        <rect x="162" y="10" width="136" height="16" rx="3.5" fill="url(#tiCaseGrad)" stroke="#1a1c1e" stroke-width="1.2"/>
        <rect x="168" y="14" width="124" height="8" rx="2" fill="#121315" opacity="0.6"/>
        <line x1="165" y1="12" x2="295" y2="12" stroke="#d5dbe5" stroke-width="0.9" opacity="0.7"/>
        <line x1="165" y1="24" x2="295" y2="24" stroke="#16181b" stroke-width="0.9"/>
      </g>

      <!-- Middle Titanium Keeper Loop (Below 6:00, Engraved 007) -->
      <g id="natoMidKeeper">
        <rect x="162" y="468" width="136" height="16" rx="3.5" fill="url(#tiCaseGrad)" stroke="#1a1c1e" stroke-width="1.2"/>
        <line x1="165" y1="470" x2="295" y2="470" stroke="#d5dbe5" stroke-width="0.9" opacity="0.7"/>
        <line x1="165" y1="482" x2="295" y2="482" stroke="#16181b" stroke-width="0.9"/>
        <text x="{cx}" y="479" fill="#9da4af" font-family="'Space Grotesk', sans-serif" font-size="7.5" font-weight="700" letter-spacing="0.18em" text-anchor="middle" dominant-baseline="central">007</text>
      </g>

      <!-- Bottom Titanium Buckle Bar (Engraved OMEGA) -->
      <g id="natoBottomBuckle">
        <rect x="160" y="522" width="140" height="22" rx="4" fill="url(#tiCaseGrad)" stroke="#16181b" stroke-width="1.3"/>
        <line x1="163" y1="524" x2="297" y2="524" stroke="#e0e5ed" stroke-width="1.0" opacity="0.8"/>
        <line x1="163" y1="542" x2="297" y2="542" stroke="#141517" stroke-width="1.0"/>
        <text x="{cx}" y="533" fill="#adb5c2" font-family="'Space Grotesk', -apple-system, sans-serif" font-size="9.5" font-weight="700" letter-spacing="0.22em" text-anchor="middle" dominant-baseline="central">OMEGA</text>
      </g>

      <!-- Rounded Folded Fabric Tail at Bottom (Hemmed Edge) -->
      <path d="M 168 544 L 168 554 Q 168 560 174 560 L 286 560 Q 292 560 292 554 L 292 544 Z" fill="#1c1d1f"/>
      <path d="M 168 544 L 168 554 Q 168 560 174 560 L 286 560 Q 292 560 292 554 L 292 544 Z" fill="url(#natoWeave)" opacity="0.45"/>
      <path d="M 172 556 Q {cx} 557 288 556" stroke="#4a4237" stroke-width="1.2" stroke-dasharray="3,2" fill="none"/>

      <!-- ============================================================== -->
      <!-- 11. BOUNDED INTERACTIVE DIAL HIT-AREA (CONFINED TO THE WATCH DIAL) -->
      <!-- ============================================================== -->
      <circle id="omegaDialHitArea" cx="{cx}" cy="{cy}" r="120" fill="rgba(0,0,0,0.001)" pointer-events="all" style="cursor: crosshair; pointer-events: all;"/>
    </svg>'''
