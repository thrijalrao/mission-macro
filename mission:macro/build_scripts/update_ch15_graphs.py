import re

with open('project_007_macroeconomics/build_scripts/ch15_endsem_simulations.py', 'r', encoding='utf-8') as f:
    text = f.read()

graphs = {
    'p1_q1_sol': r'''
                        <!-- Conceptual Graph: Sticky Input Prices & SRAS Slope -->
                        <div style="margin-top:14px; background:#07080b; border:1px solid rgba(255,255,255,0.1); padding:14px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); display:block; margin-bottom:8px;">STICKY INPUT PRICES & PROFIT MARGIN EXPANSION ALONG SRAS</span>
                            <svg viewBox="0 0 520 220" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="60" y1="180" x2="480" y2="180" stroke="#444" stroke-width="1.5"/>
                                <line x1="60" y1="20" x2="60" y2="180" stroke="#444" stroke-width="1.5"/>
                                <text x="485" y="184" fill="#aaa" font-family="var(--font-mono)" font-size="10">Y (Output)</text>
                                <text x="25" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">Price P</text>

                                <!-- LRAS -->
                                <line x1="250" y1="20" x2="250" y2="180" stroke="#eab308" stroke-width="2"/>
                                <text x="255" y="35" fill="#eab308" font-family="var(--font-mono)" font-size="10" font-weight="700">LRAS (Y*)</text>

                                <!-- SRAS Curve (Upward Sloping) -->
                                <line x1="120" y1="160" x2="420" y2="50" stroke="#fb923c" stroke-width="2.5"/>
                                <text x="425" y="55" fill="#fb923c" font-family="var(--font-mono)" font-size="10" font-weight="700">SRAS (W=W₀ Sticky)</text>

                                <!-- Baseline P0, Y* -->
                                <line x1="60" y1="110" x2="250" y2="110" stroke="rgba(255,255,255,0.2)" stroke-dasharray="2,2"/>
                                <circle cx="250" cy="110" r="6" fill="#38bdf8"/>
                                <text x="235" y="105" fill="#38bdf8" font-family="var(--font-mono)" font-size="10">E₀(P₀, Y*)</text>
                                <text x="35" y="114" fill="#aaa" font-family="var(--font-mono)" font-size="10">P₀</text>

                                <!-- Higher Price P1 -> Output Y1 with Red Target Crosshair -->
                                <line x1="60" y1="70" x2="360" y2="70" stroke="rgba(255,255,255,0.2)" stroke-dasharray="2,2"/>
                                <line x1="360" y1="70" x2="360" y2="180" stroke="rgba(255,255,255,0.2)" stroke-dasharray="2,2"/>
                                <circle cx="360" cy="70" r="8" fill="none" stroke="#d92534" stroke-width="2"/>
                                <circle cx="360" cy="70" r="2.5" fill="#d92534"/>
                                <line x1="350" y1="70" x2="370" y2="70" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="360" y1="60" x2="360" y2="80" stroke="#d92534" stroke-width="1.2"/>
                                <text x="370" y="70" fill="#d92534" font-family="var(--font-mono)" font-size="10" font-weight="700">E₁(P₁, Y₁ &gt; Y*)</text>
                                <text x="35" y="74" fill="#d92534" font-family="var(--font-mono)" font-size="10">P₁</text>
                                <text x="350" y="195" fill="#d92534" font-family="var(--font-mono)" font-size="10">Y₁</text>

                                <!-- Profit Margin Bracket -->
                                <path d="M 50 110 L 40 90 L 50 70" stroke="#10b981" stroke-width="1.5" fill="none"/>
                                <text x="4" y="93" fill="#10b981" font-family="var(--font-mono)" font-size="8">ΔProfit Margin</text>
                            </svg>
                        </div>''',

    'p1_q3_sol': r'''
                        <!-- Conceptual Graph: Financial Crowding Out vs Infrastructure Crowding In -->
                        <div style="margin-top:14px; background:#07080b; border:1px solid rgba(255,255,255,0.1); padding:14px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); display:block; margin-bottom:8px;">LOANABLE FUNDS: FINANCIAL CROWDING OUT VS INFRASTRUCTURE CROWDING IN</span>
                            <svg viewBox="0 0 520 220" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="60" y1="180" x2="480" y2="180" stroke="#444" stroke-width="1.5"/>
                                <line x1="60" y1="20" x2="60" y2="180" stroke="#444" stroke-width="1.5"/>
                                <text x="485" y="184" fill="#aaa" font-family="var(--font-mono)" font-size="10">Q (Funds)</text>
                                <text x="35" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">r (%)</text>

                                <!-- Supply Curve S -->
                                <line x1="100" y1="160" x2="420" y2="40" stroke="#38bdf8" stroke-width="2"/>
                                <text x="425" y="45" fill="#38bdf8" font-family="var(--font-mono)" font-size="10">S_LF</text>

                                <!-- D0 Private Investment Demand -->
                                <line x1="100" y1="40" x2="380" y2="160" stroke="#fb923c" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <text x="385" y="165" fill="#fb923c" font-family="var(--font-mono)" font-size="9">D₀ (I_pvt)</text>

                                <!-- D1 Sovereign Borrowing (Crowding Out) -->
                                <line x1="150" y1="40" x2="430" y2="160" stroke="#d92534" stroke-width="2.2"/>
                                <text x="435" y="165" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">D₁ (I + G-T)</text>

                                <!-- Initial E0 -->
                                <circle cx="240" cy="110" r="5" fill="#38bdf8"/>
                                <text x="230" y="100" fill="#38bdf8" font-family="var(--font-mono)" font-size="9">E₀(r₀)</text>

                                <!-- Crowding Out Equilibrium E_out with Target Crosshair -->
                                <circle cx="280" cy="90" r="8" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="280" cy="90" r="2.5" fill="#d92534"/>
                                <line x1="270" y1="90" x2="290" y2="90" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="280" y1="80" x2="280" y2="100" stroke="#d92534" stroke-width="1.2"/>
                                <text x="288" y="85" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">E_out: r₁ &gt; r₀ (I_pvt chokes)</text>

                                <!-- Infrastructure Crowding In Shift D2 -->
                                <line x1="210" y1="30" x2="470" y2="140" stroke="#10b981" stroke-width="2.2"/>
                                <circle cx="330" cy="70" r="8" fill="none" stroke="#10b981" stroke-width="2"/>
                                <circle cx="330" cy="70" r="2.5" fill="#10b981"/>
                                <text x="340" y="65" fill="#10b981" font-family="var(--font-mono)" font-size="9" font-weight="700">E_in: Infra Complementarity</text>
                            </svg>
                        </div>''',

    'p1_q6_sol': r'''
                        <!-- Conceptual Graph: Automotive GVA Double Deflation vs Single Deflation -->
                        <div style="margin-top:14px; background:#07080b; border:1px solid rgba(255,255,255,0.1); padding:14px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); display:block; margin-bottom:8px;">AUTOMOTIVE GVA: INPUT INFLATION WEDGE & DOUBLE DEFLATION</span>
                            <svg viewBox="0 0 520 220" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="60" y1="180" x2="480" y2="180" stroke="#444" stroke-width="1.5"/>
                                <line x1="60" y1="20" x2="60" y2="180" stroke="#444" stroke-width="1.5"/>
                                <text x="485" y="184" fill="#aaa" font-family="var(--font-mono)" font-size="10">Metric</text>
                                <text x="25" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">₹ Crores</text>

                                <!-- 2021 Base Year: ₹400 Cr -->
                                <rect x="110" y="110" width="50" height="70" fill="#38bdf8" rx="3"/>
                                <text x="135" y="100" fill="#38bdf8" font-family="var(--font-mono)" font-size="10" text-anchor="middle">₹400 Cr</text>
                                <text x="135" y="195" fill="#aaa" font-family="var(--font-mono)" font-size="10" text-anchor="middle">2021 Base</text>

                                <!-- 2026 Single Deflation: ₹450 Cr (+12.5%) -->
                                <rect x="230" y="95" width="50" height="85" fill="#f59e0b" rx="3"/>
                                <text x="255" y="85" fill="#f59e0b" font-family="var(--font-mono)" font-size="10" text-anchor="middle">₹450 Cr</text>
                                <text x="255" y="195" fill="#f59e0b" font-family="var(--font-mono)" font-size="9" text-anchor="middle">Single (+12.5%)</text>

                                <!-- 2026 Double Deflation: ₹600 Cr (+50.0%) with Target Crosshair -->
                                <rect x="350" y="50" width="50" height="130" fill="#10b981" rx="3"/>
                                <text x="375" y="40" fill="#10b981" font-family="var(--font-mono)" font-size="10" text-anchor="middle">₹600 Cr</text>
                                <text x="375" y="195" fill="#10b981" font-family="var(--font-mono)" font-size="9" text-anchor="middle" font-weight="700">Double (+50.0%)</text>

                                <!-- Red Target Crosshair on True Double Deflation Height -->
                                <circle cx="375" cy="50" r="8" fill="none" stroke="#d92534" stroke-width="2"/>
                                <circle cx="375" cy="50" r="2.5" fill="#d92534"/>
                                <line x1="365" y1="50" x2="385" y2="50" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="375" y1="40" x2="375" y2="60" stroke="#d92534" stroke-width="1.2"/>
                                <text x="410" y="55" fill="#d92534" font-family="var(--font-mono)" font-size="9">True Physical Volume</text>
                            </svg>
                        </div>''',

    'p2_q1_sol': r'''
                        <!-- Conceptual Graph: Long-Run AD-AS Self-Correction Mechanism -->
                        <div style="margin-top:14px; background:#07080b; border:1px solid rgba(255,255,255,0.1); padding:14px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); display:block; margin-bottom:8px;">LONG-RUN AD-AS SELF-CORRECTION MECHANISM</span>
                            <svg viewBox="0 0 520 230" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="60" y1="190" x2="480" y2="190" stroke="#444" stroke-width="1.5"/>
                                <line x1="60" y1="20" x2="60" y2="190" stroke="#444" stroke-width="1.5"/>
                                <text x="485" y="194" fill="#aaa" font-family="var(--font-mono)" font-size="10">Y (Real Output)</text>
                                <text x="25" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">Price P</text>

                                <!-- LRAS at Y* -->
                                <line x1="300" y1="20" x2="300" y2="190" stroke="#eab308" stroke-width="2"/>
                                <text x="305" y="35" fill="#eab308" font-family="var(--font-mono)" font-size="10" font-weight="700">LRAS (Y*)</text>

                                <!-- AD 0 & AD 1 Shocked -->
                                <line x1="160" y1="40" x2="450" y2="170" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <line x1="90" y1="40" x2="380" y2="170" stroke="#38bdf8" stroke-width="2.2"/>
                                <text x="385" y="170" fill="#38bdf8" font-family="var(--font-mono)" font-size="9">AD₁ (Recession)</text>

                                <!-- SRAS 0 -->
                                <line x1="90" y1="170" x2="400" y2="50" stroke="#fb923c" stroke-width="2"/>
                                <text x="405" y="55" fill="#fb923c" font-family="var(--font-mono)" font-size="9">SRAS₀ (W₀)</text>

                                <!-- SRAS 1 Self-Correction Downward (W decreases) -->
                                <line x1="150" y1="180" x2="450" y2="60" stroke="#10b981" stroke-width="2.2"/>
                                <text x="455" y="65" fill="#10b981" font-family="var(--font-mono)" font-size="9" font-weight="700">SRAS₁ (W↓)</text>

                                <!-- E1 Short-Run Recession Point -->
                                <circle cx="210" cy="120" r="6" fill="#f59e0b"/>
                                <text x="155" y="115" fill="#f59e0b" font-family="var(--font-mono)" font-size="9">E₁ (Y₁ &lt; Y*)</text>

                                <!-- E_LR Long-Run Restored with Red Target Crosshair -->
                                <line x1="60" y1="135" x2="300" y2="135" stroke="rgba(255,255,255,0.2)" stroke-dasharray="2,2"/>
                                <circle cx="300" cy="135" r="9" fill="none" stroke="#d92534" stroke-width="2"/>
                                <circle cx="300" cy="135" r="3" fill="#d92534"/>
                                <line x1="288" y1="135" x2="312" y2="135" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="300" y1="123" x2="300" y2="147" stroke="#d92534" stroke-width="1.2"/>
                                <text x="312" y="130" fill="#d92534" font-family="var(--font-mono)" font-size="10" font-weight="700">E_LR (Y*, P₂ &lt; P₀)</text>
                                <text x="35" y="139" fill="#d92534" font-family="var(--font-mono)" font-size="10">P₂</text>
                            </svg>
                        </div>''',

    'p2_q4_sol': r'''
                        <!-- Conceptual Graph: Liquidity Trap & Horizontal LM -->
                        <div style="margin-top:14px; background:#07080b; border:1px solid rgba(255,255,255,0.1); padding:14px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); display:block; margin-bottom:8px;">ZERO LOWER BOUND: HORIZONTAL LM & MAXIMUM FISCAL MULTIPLIER</span>
                            <svg viewBox="0 0 520 220" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="60" y1="180" x2="480" y2="180" stroke="#444" stroke-width="1.5"/>
                                <line x1="60" y1="20" x2="60" y2="180" stroke="#444" stroke-width="1.5"/>
                                <text x="485" y="184" fill="#aaa" font-family="var(--font-mono)" font-size="10">Y (Output)</text>
                                <text x="35" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">r (%)</text>

                                <!-- LM Curve with Horizontal ZLB Section -->
                                <line x1="60" y1="175" x2="320" y2="175" stroke="#10b981" stroke-width="3"/>
                                <line x1="320" y1="175" x2="440" y2="50" stroke="#10b981" stroke-width="2.5"/>
                                <text x="330" y="165" fill="#10b981" font-family="var(--font-mono)" font-size="9" font-weight="700">LM (Horizontal at r = 0%)</text>

                                <!-- IS 0 -->
                                <line x1="90" y1="60" x2="220" y2="180" stroke="#fb923c" stroke-width="2"/>
                                <text x="225" y="170" fill="#fb923c" font-family="var(--font-mono)" font-size="9">IS₀</text>

                                <!-- IS 1 (Fiscal Stimulus ΔG) -->
                                <line x1="170" y1="60" x2="300" y2="180" stroke="#38bdf8" stroke-width="2.5"/>
                                <text x="305" y="170" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700">IS₁ (ΔG)</text>

                                <!-- Target Crosshairs on E0 and E1 -->
                                <circle cx="215" cy="175" r="5" fill="#fb923c"/>
                                <text x="195" y="195" fill="#aaa" font-family="var(--font-mono)" font-size="9">Y₀</text>

                                <circle cx="295" cy="175" r="8" fill="none" stroke="#d92534" stroke-width="2"/>
                                <circle cx="295" cy="175" r="2.5" fill="#d92534"/>
                                <line x1="285" y1="175" x2="305" y2="175" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="295" y1="165" x2="295" y2="185" stroke="#d92534" stroke-width="1.2"/>
                                <text x="290" y="195" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">Y₁ = Y₀ + k·ΔG</text>

                                <!-- Arrow showing zero crowding out -->
                                <path d="M 225 165 L 285 165" stroke="#10b981" stroke-width="2" marker-end="url(#arrow)" fill="none"/>
                                <text x="230" y="155" fill="#10b981" font-family="var(--font-mono)" font-size="8">Δr = 0 (Zero Crowding Out)</text>
                            </svg>
                        </div>''',

    'p2_q6_sol': r'''
                        <!-- Conceptual Graph: Keynesian Cross with Multi-Tier Leakages -->
                        <div style="margin-top:14px; background:#07080b; border:1px solid rgba(255,255,255,0.1); padding:14px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); display:block; margin-bottom:8px;">KEYNESIAN CROSS: LEAKAGES (TAXES & IMPORTS) FLATTEN AE SLOPE</span>
                            <svg viewBox="0 0 520 220" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="60" y1="180" x2="480" y2="180" stroke="#444" stroke-width="1.5"/>
                                <line x1="60" y1="20" x2="60" y2="180" stroke="#444" stroke-width="1.5"/>
                                <text x="485" y="184" fill="#aaa" font-family="var(--font-mono)" font-size="10">Y (National Income)</text>
                                <text x="25" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">AE</text>

                                <!-- 45 Degree Line -->
                                <line x1="60" y1="180" x2="440" y2="30" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3"/>
                                <text x="445" y="35" fill="#64748b" font-family="var(--font-mono)" font-size="9">Y = AE (45° Line)</text>

                                <!-- Closed Economy AE (Steeper, slope 0.8, k=5) -->
                                <line x1="60" y1="130" x2="420" y2="40" stroke="#fb923c" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <text x="425" y="45" fill="#fb923c" font-family="var(--font-mono)" font-size="9">AE (Closed, k=5)</text>

                                <!-- Open Economy AE with Tax & Imports (Flatter, slope 0.5, k=2) -->
                                <line x1="60" y1="110" x2="440" y2="80" stroke="#38bdf8" stroke-width="2.5"/>
                                <text x="445" y="85" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700">AE (t=0.25, m=0.10, k=2)</text>

                                <!-- Target Crosshair on Equilibrium Y* = 3140 -->
                                <line x1="310" y1="90" x2="310" y2="180" stroke="rgba(255,255,255,0.2)" stroke-dasharray="2,2"/>
                                <circle cx="310" cy="90" r="8" fill="none" stroke="#d92534" stroke-width="2"/>
                                <circle cx="310" cy="90" r="2.5" fill="#d92534"/>
                                <line x1="300" y1="90" x2="320" y2="90" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="310" y1="80" x2="310" y2="100" stroke="#d92534" stroke-width="1.2"/>
                                <text x="315" y="80" fill="#d92534" font-family="var(--font-mono)" font-size="10" font-weight="700">E* (Y* = 3,140)</text>
                                <text x="300" y="195" fill="#aaa" font-family="var(--font-mono)" font-size="10">3,140</text>
                            </svg>
                        </div>''',

    'p3_q1_sol': r'''
                        <!-- Conceptual Graph: Demonetisation in IS-LM -->
                        <div style="margin-top:14px; background:#07080b; border:1px solid rgba(255,255,255,0.1); padding:14px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); display:block; margin-bottom:8px;">DEMONETISATION IN IS-LM: CASH SQUEEZE & DEPOSIT SURGE TRANSMISSION</span>
                            <svg viewBox="0 0 520 220" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="60" y1="180" x2="480" y2="180" stroke="#444" stroke-width="1.5"/>
                                <line x1="60" y1="20" x2="60" y2="180" stroke="#444" stroke-width="1.5"/>
                                <text x="485" y="184" fill="#aaa" font-family="var(--font-mono)" font-size="10">Y (Output)</text>
                                <text x="35" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">r (%)</text>

                                <!-- LM 0 Baseline -->
                                <line x1="120" y1="170" x2="380" y2="50" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <text x="385" y="55" fill="#38bdf8" font-family="var(--font-mono)" font-size="9">LM₀ (Baseline)</text>

                                <!-- LM 1 Crash (Short-Run Cash Invalidation) -->
                                <line x1="70" y1="170" x2="330" y2="50" stroke="#d92534" stroke-width="2.2"/>
                                <text x="210" y="45" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">LM_crash (86% Cash De-legalised)</text>

                                <!-- LM 2 Deposit Easing (Medium Run) -->
                                <line x1="180" y1="170" x2="440" y2="50" stroke="#10b981" stroke-width="2.2"/>
                                <text x="445" y="55" fill="#10b981" font-family="var(--font-mono)" font-size="9">LM_ease (CASA Deposits & MCLR Cut)</text>

                                <!-- IS Curve -->
                                <line x1="100" y1="50" x2="400" y2="170" stroke="#fb923c" stroke-width="2"/>

                                <!-- Shock Point with Target Crosshair -->
                                <circle cx="205" cy="95" r="8" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="205" cy="95" r="2.5" fill="#d92534"/>
                                <line x1="195" y1="95" x2="215" y2="95" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="205" y1="85" x2="205" y2="105" stroke="#d92534" stroke-width="1.2"/>
                                <text x="140" y="85" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">Short-Run Contraction</text>

                                <!-- Recovery Point E2 -->
                                <circle cx="310" cy="135" r="7" fill="none" stroke="#10b981" stroke-width="2"/>
                                <text x="320" y="145" fill="#10b981" font-family="var(--font-mono)" font-size="9" font-weight="700">Lower Lending Rates</text>
                            </svg>
                        </div>''',

    'p3_q2_sol': r'''
                        <!-- Conceptual Graph: Twin Deficits Balance -->
                        <div style="margin-top:14px; background:#07080b; border:1px solid rgba(255,255,255,0.1); padding:14px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); display:block; margin-bottom:8px;">TWIN DEFICITS IDENTITY: FISCAL GAP SPILLOVER INTO EXTERNAL DEFICIT</span>
                            <svg viewBox="0 0 520 220" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="60" y1="180" x2="480" y2="180" stroke="#444" stroke-width="1.5"/>
                                <line x1="60" y1="20" x2="60" y2="180" stroke="#444" stroke-width="1.5"/>
                                <text x="485" y="184" fill="#aaa" font-family="var(--font-mono)" font-size="10">Fiscal Deficit (G - T)</text>
                                <text x="20" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">Trade Deficit (M - X)</text>

                                <!-- 45-degree transmission ray when S=I is constant -->
                                <line x1="100" y1="150" x2="400" y2="40" stroke="#38bdf8" stroke-width="2.2"/>
                                <text x="405" y="45" fill="#38bdf8" font-family="var(--font-mono)" font-size="9">Δ(M - X) = Δ(G - T) [Ray of Twin Deficits]</text>

                                <!-- Target Crosshair on Twin Deficit Coordination -->
                                <circle cx="280" cy="85" r="8" fill="none" stroke="#d92534" stroke-width="2"/>
                                <circle cx="280" cy="85" r="2.5" fill="#d92534"/>
                                <line x1="270" y1="85" x2="290" y2="85" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="280" y1="75" x2="280" y2="95" stroke="#d92534" stroke-width="1.2"/>
                                <text x="290" y="80" fill="#d92534" font-family="var(--font-mono)" font-size="10" font-weight="700">Twin Deficit Equilibrium</text>

                                <!-- Dashed balance lines -->
                                <line x1="60" y1="85" x2="280" y2="85" stroke="rgba(255,255,255,0.2)" stroke-dasharray="2,2"/>
                                <line x1="280" y1="85" x2="280" y2="180" stroke="rgba(255,255,255,0.2)" stroke-dasharray="2,2"/>
                                <text x="15" y="90" fill="#d92534" font-family="var(--font-mono)" font-size="9">CAD</text>
                                <text x="265" y="195" fill="#d92534" font-family="var(--font-mono)" font-size="9">Fiscal Deficit</text>
                            </svg>
                        </div>''',

    'p3_q3_sol': r'''
                        <!-- Conceptual Graph: Paradox of Thrift -->
                        <div style="margin-top:14px; background:#07080b; border:1px solid rgba(255,255,255,0.1); padding:14px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); display:block; margin-bottom:8px;">KEYNESIAN PARADOX OF THRIFT: REALIZED SAVINGS INVARIANCE</span>
                            <svg viewBox="0 0 520 220" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="60" y1="180" x2="480" y2="180" stroke="#444" stroke-width="1.5"/>
                                <line x1="60" y1="20" x2="60" y2="180" stroke="#444" stroke-width="1.5"/>
                                <text x="485" y="184" fill="#aaa" font-family="var(--font-mono)" font-size="10">Y (National Income)</text>
                                <text x="25" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">S, I</text>

                                <!-- Autonomous Investment Line (Horizontal) -->
                                <line x1="80" y1="110" x2="440" y2="110" stroke="#fb923c" stroke-width="2.5"/>
                                <text x="445" y="113" fill="#fb923c" font-family="var(--font-mono)" font-size="10" font-weight="700">I = I_bar</text>

                                <!-- Initial Saving S0 -->
                                <line x1="120" y1="180" x2="400" y2="40" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <text x="405" y="45" fill="#38bdf8" font-family="var(--font-mono)" font-size="9">S₀ = -C₀ + sY</text>

                                <!-- Shifted Saving S1 (Thrift Surge) -->
                                <line x1="70" y1="160" x2="350" y2="20" stroke="#38bdf8" stroke-width="2.5"/>
                                <text x="355" y="25" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700">S₁ (Thrift Surge +ΔS₀)</text>

                                <!-- E0 Equilibrium -->
                                <circle cx="260" cy="110" r="5" fill="#38bdf8"/>
                                <text x="260" y="130" fill="#aaa" font-family="var(--font-mono)" font-size="9">E₀(Y₀)</text>

                                <!-- E1 Equilibrium with Target Crosshair -->
                                <circle cx="180" cy="110" r="8" fill="none" stroke="#d92534" stroke-width="2"/>
                                <circle cx="180" cy="110" r="2.5" fill="#d92534"/>
                                <line x1="170" y1="110" x2="190" y2="110" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="180" y1="100" x2="180" y2="120" stroke="#d92534" stroke-width="1.2"/>
                                <text x="145" y="95" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">E₁: S' = S₀ = I_bar (Y collapses!)</text>

                                <!-- Income Collapse Vector -->
                                <path d="M 250 110 L 195 110" stroke="#d92534" stroke-width="2.2" marker-end="url(#arrow)" fill="none"/>
                            </svg>
                        </div>'''
}

# Insert each graph before the EXAMINER MARK BREAKDOWN inside each solution
for tid, svg_code in graphs.items():
    sol_str = f'id="{tid}"'
    pos_sol = text.find(sol_str)
    if pos_sol != -1:
        # Find next EXAMINER MARK BREAKDOWN after pos_sol
        pos_breakdown = text.find('EXAMINER MARK BREAKDOWN', pos_sol)
        if pos_breakdown != -1:
            # find the opening <div style= before pos_breakdown
            pos_div = text.rfind('<div style="background:rgba(255,255,255,0.03)', pos_sol, pos_breakdown)
            if pos_div != -1:
                text = text[:pos_div] + svg_code + '\n                        ' + text[pos_div:]
                print(f"Inserted graph for {tid} successfully!")
            else:
                print(f"Warning: opening div before breakdown not found for {tid}")
        else:
            print(f"Warning: breakdown not found for {tid}")
    else:
        print(f"Warning: {tid} not found")

with open('project_007_macroeconomics/build_scripts/ch15_endsem_simulations.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved updated ch15_endsem_simulations.py successfully!")
