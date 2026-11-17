import re

with open('project_007_macroeconomics/build_scripts/ch14_midsem_case_studies.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Subtab 2 Q2: Add Double Deflation divergence graph before the closing </div> of DEBRIEF Q2
q2_graph_svg = r'''
                        <!-- Conceptual Graph: Double Deflation vs Single Deflation -->
                        <div style="margin-top:14px; background:#07080b; border:1px solid rgba(255,255,255,0.1); padding:16px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); display:block; margin-bottom:8px;">ZEPHYRA GVA: DOUBLE DEFLATION VS SINGLE DEFLATION TRAJECTORY</span>
                            <svg viewBox="0 0 540 260" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="60" y1="220" x2="500" y2="220" stroke="#444" stroke-width="1.5"/>
                                <line x1="60" y1="20" x2="60" y2="220" stroke="#444" stroke-width="1.5"/>
                                <text x="505" y="225" fill="#aaa" font-family="var(--font-mono)" font-size="11">Year</text>
                                <text x="25" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="11">Real GVA (₹ Cr)</text>

                                <!-- Base Year 2020: 600 Cr -->
                                <circle cx="160" cy="140" r="6" fill="#38bdf8"/>
                                <text x="160" y="240" fill="#aaa" font-family="var(--font-mono)" font-size="11" text-anchor="middle">2020 (Base)</text>
                                <text x="145" y="135" fill="#38bdf8" font-family="var(--font-mono)" font-size="11" font-weight="700">₹600 Cr</text>

                                <!-- Single Deflation Flat Line to 2025: 600 Cr (0% growth) -->
                                <line x1="160" y1="140" x2="400" y2="140" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>
                                <circle cx="400" cy="140" r="7" fill="none" stroke="#f59e0b" stroke-width="2"/>
                                <circle cx="400" cy="140" r="2.5" fill="#f59e0b"/>
                                <text x="410" y="145" fill="#f59e0b" font-family="var(--font-mono)" font-size="10">Single Deflation: ₹600 Cr (0.0% Growth)</text>

                                <!-- Double Deflation Upward Line to 2025: 720 Cr (+20% growth) -->
                                <line x1="160" y1="140" x2="400" y2="60" stroke="#10b981" stroke-width="2.5"/>
                                <!-- Red Target Crosshair on True Equilibrium E_true -->
                                <line x1="60" y1="60" x2="400" y2="60" stroke="rgba(255,255,255,0.2)" stroke-dasharray="2,2"/>
                                <line x1="400" y1="60" x2="400" y2="220" stroke="rgba(255,255,255,0.2)" stroke-dasharray="2,2"/>
                                <circle cx="400" cy="60" r="9" fill="none" stroke="#d92534" stroke-width="2"/>
                                <circle cx="400" cy="60" r="3" fill="#d92534"/>
                                <line x1="388" y1="60" x2="412" y2="60" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="400" y1="48" x2="400" y2="72" stroke="#d92534" stroke-width="1.2"/>
                                <text x="412" y="55" fill="#10b981" font-family="var(--font-mono)" font-size="11" font-weight="700">Double Deflation: ₹720 Cr (+20.0%)</text>
                                <text x="400" y="240" fill="#aaa" font-family="var(--font-mono)" font-size="11" text-anchor="middle">2025</text>
                                <text x="25" y="65" fill="#10b981" font-family="var(--font-mono)" font-size="10">₹720</text>
                                <text x="25" y="145" fill="#38bdf8" font-family="var(--font-mono)" font-size="10">₹600</text>

                                <!-- Divergence bracket / label -->
                                <path d="M 405 70 L 415 100 L 405 130" stroke="#d92534" stroke-width="1.5" fill="none"/>
                                <text x="425" y="103" fill="#d92534" font-family="var(--font-mono)" font-size="9">Input Inflation Wedge (P_in=1.50 vs P_out=1.20)</text>
                            </svg>
                        </div>
'''

# Find Q2 end (before DEBRIEF Q3)
pos_q3 = text.find('<!-- DEBRIEF Q3 -->')
if pos_q3 != -1:
    # insert before the last </div> before pos_q3
    pos_last_div = text.rfind('</div>', 0, pos_q3)
    text = text[:pos_last_div] + q2_graph_svg + text[pos_last_div:]
    print("Inserted Q2 Double Deflation graph successfully!")
else:
    print("Warning: DEBRIEF Q3 not found")

# Graphs for 10 Cases in Subtab 3
case_graphs = {
    1: r'''
                        <!-- Case 1 Graph -->
                        <div style="margin-top:12px; background:#07080b; border:1px solid rgba(255,255,255,0.08); padding:12px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); display:block; margin-bottom:6px;">MCA-21 COMMODITY PRICE COLLAPSE & GVA DISTORTION</span>
                            <svg viewBox="0 0 500 200" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="50" y1="170" x2="460" y2="170" stroke="#444" stroke-width="1.2"/>
                                <line x1="50" y1="20" x2="50" y2="170" stroke="#444" stroke-width="1.2"/>
                                <text x="465" y="174" fill="#aaa" font-family="var(--font-mono)" font-size="10">Period</text>
                                <text x="20" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">Growth Rate (%)</text>
                                <!-- Single Deflation Artificially High -->
                                <path d="M 60 140 Q 250 30 440 40" stroke="#f59e0b" stroke-width="2" fill="none"/>
                                <text x="445" y="45" fill="#f59e0b" font-family="var(--font-mono)" font-size="9">Single Deflated GVA (+8.5%)</text>
                                <!-- Double Deflation True Physical Volume -->
                                <path d="M 60 140 Q 250 110 440 120" stroke="#10b981" stroke-width="2.2" fill="none"/>
                                <text x="445" y="125" fill="#10b981" font-family="var(--font-mono)" font-size="9">Double Deflated GVA (+3.2%)</text>
                                <!-- Real Volume IIP -->
                                <path d="M 60 140 Q 250 120 440 130" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3" fill="none"/>
                                <text x="445" y="145" fill="#38bdf8" font-family="var(--font-mono)" font-size="9">IIP Industrial Volume (+2.8%)</text>
                                <!-- Target crosshair on True Growth -->
                                <circle cx="340" cy="115" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="340" cy="115" r="2.5" fill="#d92534"/>
                                <line x1="330" y1="115" x2="350" y2="115" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="340" y1="105" x2="340" y2="125" stroke="#d92534" stroke-width="1.2"/>
                                <text x="330" y="98" fill="#d92534" font-family="var(--font-mono)" font-size="9">True Physical Volume</text>
                            </svg>
                        </div>''',

    2: r'''
                        <!-- Case 2 Graph -->
                        <div style="margin-top:12px; background:#07080b; border:1px solid rgba(255,255,255,0.08); padding:12px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); display:block; margin-bottom:6px;">PARADOX OF THRIFT: PRECAUTIONARY SAVING SURGE & OUTPUT COLLAPSE</span>
                            <svg viewBox="0 0 500 200" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="50" y1="170" x2="460" y2="170" stroke="#444" stroke-width="1.2"/>
                                <line x1="50" y1="20" x2="50" y2="170" stroke="#444" stroke-width="1.2"/>
                                <text x="465" y="174" fill="#aaa" font-family="var(--font-mono)" font-size="10">Y (Output)</text>
                                <text x="25" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">S, I</text>
                                <!-- Investment Line Horizontal -->
                                <line x1="60" y1="110" x2="440" y2="110" stroke="#fb923c" stroke-width="2"/>
                                <text x="445" y="113" fill="#fb923c" font-family="var(--font-mono)" font-size="10">I = I₀</text>
                                <!-- Initial Saving S0 -->
                                <line x1="100" y1="170" x2="380" y2="50" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <text x="385" y="55" fill="#38bdf8" font-family="var(--font-mono)" font-size="9">S₀</text>
                                <!-- Shifted Saving S1 -->
                                <line x1="60" y1="150" x2="340" y2="30" stroke="#38bdf8" stroke-width="2.2"/>
                                <text x="345" y="35" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700">S₁ (Precautionary)</text>
                                <!-- E0 -->
                                <circle cx="240" cy="110" r="6" fill="#38bdf8"/>
                                <text x="235" y="130" fill="#aaa" font-family="var(--font-mono)" font-size="9">E₀ (Y₀)</text>
                                <!-- E1 with Red Crosshair Target -->
                                <circle cx="160" cy="110" r="8" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="160" cy="110" r="2.5" fill="#d92534"/>
                                <line x1="150" y1="110" x2="170" y2="110" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="160" y1="100" x2="160" y2="120" stroke="#d92534" stroke-width="1.2"/>
                                <text x="145" y="130" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">E₁ (Y₁ &lt; Y₀)</text>
                                <!-- Collapse arrow -->
                                <path d="M 230 110 L 175 110" stroke="#d92534" stroke-width="2" marker-end="url(#arrow)" fill="none"/>
                            </svg>
                        </div>''',

    3: r'''
                        <!-- Case 3 Graph -->
                        <div style="margin-top:12px; background:#07080b; border:1px solid rgba(255,255,255,0.08); padding:12px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); display:block; margin-bottom:6px;">STIMULUS OVERSHOOT & INFLATIONARY GAP</span>
                            <svg viewBox="0 0 500 200" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="50" y1="170" x2="460" y2="170" stroke="#444" stroke-width="1.2"/>
                                <line x1="50" y1="20" x2="50" y2="170" stroke="#444" stroke-width="1.2"/>
                                <text x="465" y="174" fill="#aaa" font-family="var(--font-mono)" font-size="10">Y (Real Output)</text>
                                <text x="30" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">Price P</text>
                                <!-- LRAS -->
                                <line x1="250" y1="20" x2="250" y2="170" stroke="#eab308" stroke-width="2"/>
                                <text x="255" y="35" fill="#eab308" font-family="var(--font-mono)" font-size="9">LRAS (Y*)</text>
                                <!-- SRAS -->
                                <line x1="100" y1="160" x2="400" y2="50" stroke="#fb923c" stroke-width="2"/>
                                <text x="405" y="55" fill="#fb923c" font-family="var(--font-mono)" font-size="9">SRAS</text>
                                <!-- AD 0 -->
                                <line x1="100" y1="60" x2="360" y2="160" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <!-- AD 1 Overshoot -->
                                <line x1="180" y1="40" x2="440" y2="150" stroke="#d92534" stroke-width="2.2"/>
                                <text x="445" y="150" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">AD₁ (Stimulus)</text>
                                <!-- Target Crosshair on Inflationary Equilibrium -->
                                <circle cx="310" cy="85" r="8" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="310" cy="85" r="2.5" fill="#d92534"/>
                                <line x1="300" y1="85" x2="320" y2="85" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="310" y1="75" x2="310" y2="95" stroke="#d92534" stroke-width="1.2"/>
                                <text x="315" y="75" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">E₁ (Y &gt; Y* Gap)</text>
                            </svg>
                        </div>''',

    4: r'''
                        <!-- Case 4 Graph -->
                        <div style="margin-top:12px; background:#07080b; border:1px solid rgba(255,255,255,0.08); padding:12px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); display:block; margin-bottom:6px;">1973 OPEC OIL EMBARGO: COST-PUSH STAGFLATION</span>
                            <svg viewBox="0 0 500 200" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="50" y1="170" x2="460" y2="170" stroke="#444" stroke-width="1.2"/>
                                <line x1="50" y1="20" x2="50" y2="170" stroke="#444" stroke-width="1.2"/>
                                <text x="465" y="174" fill="#aaa" font-family="var(--font-mono)" font-size="10">Y (Output)</text>
                                <text x="30" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">Price P</text>
                                <!-- AD -->
                                <line x1="100" y1="50" x2="400" y2="160" stroke="#38bdf8" stroke-width="2"/>
                                <text x="405" y="160" fill="#38bdf8" font-family="var(--font-mono)" font-size="9">AD</text>
                                <!-- SRAS 0 -->
                                <line x1="120" y1="160" x2="420" y2="60" stroke="#fb923c" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <!-- SRAS 1 Shock -->
                                <line x1="70" y1="130" x2="370" y2="30" stroke="#d92534" stroke-width="2.5"/>
                                <text x="375" y="35" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">SRAS₁ (Oil Shock)</text>
                                <!-- E0 Equilibrium -->
                                <circle cx="260" cy="110" r="5" fill="#38bdf8"/>
                                <text x="268" y="120" fill="#aaa" font-family="var(--font-mono)" font-size="9">E₀ (P₀, Y*)</text>
                                <!-- E1 Stagflation with Target Crosshair -->
                                <circle cx="200" cy="85" r="8" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="200" cy="85" r="2.5" fill="#d92534"/>
                                <line x1="190" y1="85" x2="210" y2="85" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="200" y1="75" x2="200" y2="95" stroke="#d92534" stroke-width="1.2"/>
                                <text x="140" y="80" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">E₁ (P↑, Y↓)</text>
                            </svg>
                        </div>''',

    5: r'''
                        <!-- Case 5 Graph -->
                        <div style="margin-top:12px; background:#07080b; border:1px solid rgba(255,255,255,0.08); padding:12px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); display:block; margin-bottom:6px;">BANK OF JAPAN: LIQUIDITY TRAP & ZERO LOWER BOUND</span>
                            <svg viewBox="0 0 500 200" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="50" y1="170" x2="460" y2="170" stroke="#444" stroke-width="1.2"/>
                                <line x1="50" y1="20" x2="50" y2="170" stroke="#444" stroke-width="1.2"/>
                                <text x="465" y="174" fill="#aaa" font-family="var(--font-mono)" font-size="10">Y (Income)</text>
                                <text x="30" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">r (%)</text>
                                <!-- Horizontal LM at ZLB -->
                                <line x1="50" y1="165" x2="350" y2="165" stroke="#10b981" stroke-width="3"/>
                                <line x1="350" y1="165" x2="440" y2="50" stroke="#10b981" stroke-width="2.5"/>
                                <text x="360" y="155" fill="#10b981" font-family="var(--font-mono)" font-size="9" font-weight="700">LM (Horizontal at ZLB)</text>
                                <!-- IS 0 -->
                                <line x1="80" y1="50" x2="240" y2="170" stroke="#fb923c" stroke-width="2"/>
                                <text x="245" y="165" fill="#fb923c" font-family="var(--font-mono)" font-size="9">IS₀</text>
                                <!-- IS 1 Fiscal Stimulus -->
                                <line x1="160" y1="50" x2="320" y2="170" stroke="#38bdf8" stroke-width="2.2"/>
                                <text x="325" y="165" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700">IS₁ (Fiscal)</text>
                                <!-- Target Crosshair on Stimulus Point -->
                                <circle cx="310" cy="165" r="8" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="310" cy="165" r="2.5" fill="#d92534"/>
                                <line x1="300" y1="165" x2="320" y2="165" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="310" y1="155" x2="310" y2="175" stroke="#d92534" stroke-width="1.2"/>
                                <text x="315" y="145" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">Full Multiplier (Zero Crowding Out)</text>
                            </svg>
                        </div>''',

    6: r'''
                        <!-- Case 6 Graph -->
                        <div style="margin-top:12px; background:#07080b; border:1px solid rgba(255,255,255,0.08); padding:12px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); display:block; margin-bottom:6px;">VOLCKER DISINFLATION: PHILLIPS CURVE SACRIFICE TRAJECTORY</span>
                            <svg viewBox="0 0 500 200" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="50" y1="170" x2="460" y2="170" stroke="#444" stroke-width="1.2"/>
                                <line x1="50" y1="20" x2="50" y2="170" stroke="#444" stroke-width="1.2"/>
                                <text x="465" y="174" fill="#aaa" font-family="var(--font-mono)" font-size="10">u (%)</text>
                                <text x="30" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">π (%)</text>
                                <!-- LRPC -->
                                <line x1="200" y1="20" x2="200" y2="170" stroke="#eab308" stroke-width="2"/>
                                <text x="205" y="35" fill="#eab308" font-family="var(--font-mono)" font-size="9">LRPC (u_n=6%)</text>
                                <!-- SRPC High -->
                                <line x1="100" y1="40" x2="400" y2="140" stroke="#d92534" stroke-width="2"/>
                                <text x="405" y="140" fill="#d92534" font-family="var(--font-mono)" font-size="9">SRPC (10% Exp)</text>
                                <!-- SRPC Low -->
                                <line x1="100" y1="90" x2="400" y2="170" stroke="#10b981" stroke-width="2"/>
                                <text x="405" y="170" fill="#10b981" font-family="var(--font-mono)" font-size="9">SRPC (3% Exp)</text>
                                <!-- Crosshair on Volcker Recession Point -->
                                <circle cx="320" cy="115" r="8" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="320" cy="115" r="2.5" fill="#d92534"/>
                                <line x1="310" y1="115" x2="330" y2="115" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="320" y1="105" x2="320" y2="125" stroke="#d92534" stroke-width="1.2"/>
                                <text x="325" y="105" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">1982 Sacrifice (u=10.8%)</text>
                            </svg>
                        </div>''',

    7: r'''
                        <!-- Case 7 Graph -->
                        <div style="margin-top:12px; background:#07080b; border:1px solid rgba(255,255,255,0.08); padding:12px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); display:block; margin-bottom:6px;">CLINTON-GREENSPAN MIX (1993): FISCAL CONTRACTION + MONETARY EASING</span>
                            <svg viewBox="0 0 500 200" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="50" y1="170" x2="460" y2="170" stroke="#444" stroke-width="1.2"/>
                                <line x1="50" y1="20" x2="50" y2="170" stroke="#444" stroke-width="1.2"/>
                                <text x="465" y="174" fill="#aaa" font-family="var(--font-mono)" font-size="10">Y (GDP)</text>
                                <text x="30" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">r (%)</text>
                                <!-- IS 0 to IS 1 (Inward) -->
                                <line x1="140" y1="40" x2="400" y2="160" stroke="#fb923c" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <line x1="80" y1="40" x2="340" y2="160" stroke="#fb923c" stroke-width="2.2"/>
                                <text x="345" y="160" fill="#fb923c" font-family="var(--font-mono)" font-size="9">IS₁ (Deficit Cut)</text>
                                <!-- LM 0 to LM 1 (Outward) -->
                                <line x1="80" y1="150" x2="340" y2="50" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <line x1="140" y1="160" x2="400" y2="60" stroke="#38bdf8" stroke-width="2.2"/>
                                <text x="405" y="65" fill="#38bdf8" font-family="var(--font-mono)" font-size="9">LM₁ (Fed Easing)</text>
                                <!-- Target Crosshair on Final E1 -->
                                <circle cx="260" cy="120" r="8" fill="none" stroke="#10b981" stroke-width="2"/>
                                <circle cx="260" cy="120" r="2.5" fill="#10b981"/>
                                <line x1="250" y1="120" x2="270" y2="120" stroke="#10b981" stroke-width="1.2"/>
                                <line x1="260" y1="110" x2="260" y2="130" stroke="#10b981" stroke-width="1.2"/>
                                <text x="268" y="115" fill="#10b981" font-family="var(--font-mono)" font-size="9" font-weight="700">E₁: Low r, Stable Y</text>
                            </svg>
                        </div>''',

    8: r'''
                        <!-- Case 8 Graph -->
                        <div style="margin-top:12px; background:#07080b; border:1px solid rgba(255,255,255,0.08); padding:12px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); display:block; margin-bottom:6px;">DEMONETISATION SHOCK: TRANSACTION VELOCITY & CASH FREEZE</span>
                            <svg viewBox="0 0 500 200" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="50" y1="170" x2="460" y2="170" stroke="#444" stroke-width="1.2"/>
                                <line x1="50" y1="20" x2="50" y2="170" stroke="#444" stroke-width="1.2"/>
                                <text x="465" y="174" fill="#aaa" font-family="var(--font-mono)" font-size="10">Y (Output)</text>
                                <text x="30" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">r (%)</text>
                                <!-- LM Shock Inward -->
                                <line x1="160" y1="160" x2="400" y2="40" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <line x1="90" y1="160" x2="330" y2="40" stroke="#d92534" stroke-width="2.5"/>
                                <text x="220" y="45" fill="#d92534" font-family="var(--font-mono)" font-size="9">LM_crunch (Cash Frozen)</text>
                                <!-- IS Curve -->
                                <line x1="100" y1="40" x2="380" y2="160" stroke="#fb923c" stroke-width="2"/>
                                <!-- Red Target Crosshair on Shock -->
                                <circle cx="210" cy="85" r="8" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="210" cy="85" r="2.5" fill="#d92534"/>
                                <line x1="200" y1="85" x2="220" y2="85" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="210" y1="75" x2="210" y2="95" stroke="#d92534" stroke-width="1.2"/>
                                <text x="145" y="80" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">Informal Contraction</text>
                            </svg>
                        </div>''',

    9: r'''
                        <!-- Case 9 Graph -->
                        <div style="margin-top:12px; background:#07080b; border:1px solid rgba(255,255,255,0.08); padding:12px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); display:block; margin-bottom:6px;">KUMBH MELA: AUTONOMOUS CONSUMPTION JUMP IN KEYNESIAN CROSS</span>
                            <svg viewBox="0 0 500 200" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="50" y1="170" x2="460" y2="170" stroke="#444" stroke-width="1.2"/>
                                <line x1="50" y1="20" x2="50" y2="170" stroke="#444" stroke-width="1.2"/>
                                <text x="465" y="174" fill="#aaa" font-family="var(--font-mono)" font-size="10">Y (Regional Output)</text>
                                <text x="25" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">AE</text>
                                <!-- 45 Degree Line -->
                                <line x1="50" y1="170" x2="430" y2="30" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3"/>
                                <text x="435" y="35" fill="#64748b" font-family="var(--font-mono)" font-size="9">Y = AE (45°)</text>
                                <!-- AE 0 -->
                                <line x1="50" y1="120" x2="420" y2="60" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <!-- AE 1 Kumbh Surge -->
                                <line x1="50" y1="90" x2="420" y2="30" stroke="#10b981" stroke-width="2.5"/>
                                <text x="425" y="30" fill="#10b981" font-family="var(--font-mono)" font-size="9" font-weight="700">AE₁ (ΔC₀ Surge)</text>
                                <!-- Target Crosshair on Expanded Regional Equilibrium -->
                                <circle cx="310" cy="72" r="8" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="310" cy="72" r="2.5" fill="#d92534"/>
                                <line x1="300" y1="72" x2="320" y2="72" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="310" y1="62" x2="310" y2="82" stroke="#d92534" stroke-width="1.2"/>
                                <text x="315" y="65" fill="#10b981" font-family="var(--font-mono)" font-size="9" font-weight="700">ΔY = k·ΔC₀</text>
                            </svg>
                        </div>''',

    10: r'''
                        <!-- Case 10 Graph -->
                        <div style="margin-top:12px; background:#07080b; border:1px solid rgba(255,255,255,0.08); padding:12px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); display:block; margin-bottom:6px;">WEIMAR HYPERINFLATION & THE FISHER EFFECT SPIRAL</span>
                            <svg viewBox="0 0 500 200" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="50" y1="170" x2="460" y2="170" stroke="#444" stroke-width="1.2"/>
                                <line x1="50" y1="20" x2="50" y2="170" stroke="#444" stroke-width="1.2"/>
                                <text x="465" y="174" fill="#aaa" font-family="var(--font-mono)" font-size="10">Time (Months 1923)</text>
                                <text x="20" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">i, π (%)</text>
                                <!-- Exponential nominal rate curve -->
                                <path d="M 60 160 Q 280 150 420 30" stroke="#d92534" stroke-width="2.8" fill="none"/>
                                <text x="425" y="30" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">Nominal Rate i = r + πᵉ</text>
                                <!-- Real Money Demand Collapsing -->
                                <path d="M 60 40 Q 280 140 420 165" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3" fill="none"/>
                                <text x="425" y="165" fill="#38bdf8" font-family="var(--font-mono)" font-size="9">Real Balances (M/P)</text>
                                <!-- Target crosshair on hyperinflation explosion -->
                                <circle cx="380" cy="55" r="8" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="380" cy="55" r="2.5" fill="#d92534"/>
                                <line x1="370" y1="55" x2="390" y2="55" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="380" y1="45" x2="380" y2="65" stroke="#d92534" stroke-width="1.2"/>
                                <text x="310" y="45" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">Velocity V → ∞</text>
                            </svg>
                        </div>'''
}

# Insert each graph before closing </div> of caseX-sol
for c_num, svg_code in case_graphs.items():
    sol_id = f'id="case{c_num}-sol"'
    pos = text.find(sol_id)
    if pos != -1:
        # Find closing </div> for this div
        div_end = text.find('</div>', pos)
        if div_end != -1:
            text = text[:div_end] + svg_code + '\n                    ' + text[div_end:]
            print(f"Inserted Case {c_num} graph successfully!")
        else:
            print(f"Warning: closing div for Case {c_num} not found")
    else:
        print(f"Warning: Case {c_num} sol not found")

with open('project_007_macroeconomics/build_scripts/ch14_midsem_case_studies.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved updated ch14_midsem_case_studies.py successfully!")
