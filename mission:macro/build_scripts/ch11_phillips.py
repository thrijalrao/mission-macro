"""
PROJECT 007: THE MACROECONOMICS INTELLIGENCE FILE
Chapter 11: The Phillips Curve & Inflation-Unemployment Tradeoff Generator
"""

def get_chapter_11():
    return r'''
<section id="chapter-11" class="mission-chapter">
<a id="ch11" class="chapter-anchor"></a>
    <div class="chapter-header">
        <div class="briefing-tag">TACTICAL INTEL FILE // DOSSIER 11</div>
        <h2 class="chapter-title">CHAPTER 11: THE PHILLIPS CURVE & INFLATION-UNEMPLOYMENT TRADEOFF</h2>
        <div class="classified-stamp">TOP SECRET // RESTRICTED ACCESS</div>
    </div>

    <div class="tab-container">
        <div class="tab-nav">
            <button class="tab-btn active" onclick="switchSubTab(event, 'ch11-training')">FIELD TRAINING // THEORY</button>
            <button class="tab-btn" onclick="switchSubTab(event, 'ch11-missions')">COMBAT MISSIONS // EXAM PROBLEMS</button>
            <button class="tab-btn" onclick="switchSubTab(event, 'ch11-targets')">TARGET TARGETS // 7-STEP SOLUTIONS</button>
        </div>

        <!-- ==================== TAB 1: TRAINING ==================== -->
        <div id="ch11-training" class="subtab-content active">
            <div class="intel-card">
                <h3>11.1 Historical Genesis & Empirical Discovery</h3>
                <p>
                    In 1958, New Zealand economist <strong>A.W. Phillips</strong> published a landmark empirical study analyzing nearly a century of United Kingdom labor data (1861–1957). He discovered a consistent, stable <strong>inverse statistical relationship between the rate of change of money wage rates and the unemployment rate</strong>.
                </p>
                <p>
                    Subsequently, Nobel laureates <strong>Paul Samuelson and Robert Solow (1960)</strong> replicated this analysis for the United States, replacing wage inflation with general <strong>price inflation ($\pi$)</strong>. They christened this relationship the <strong>Phillips Curve</strong>, presenting it to policymakers as a menu of policy choices: governments could permanently lower unemployment if they were willing to tolerate higher inflation, or conquer inflation at the expense of higher joblessness.
                </p>
                <div class="formula-box">
                    $$\text{Early Empirical Phillips Curve: } \pi = -\beta(u - u_n)$$
                    <p style="font-size:0.85rem; margin-top:6px;">Where $\pi$ is inflation, $u$ is the actual unemployment rate, and $u_n$ is the natural rate of unemployment.</p>
                </div>
            </div>

            <div class="intel-card">
                <h3>11.2 Microeconomic Foundations: Why the Trade-off Operates in the Short Run</h3>
                <div class="grid-2">
                    <div class="metric-box">
                        <div class="metric-label">TIGHT LABOR REGIME ($u < u_n$)</div>
                        <p style="font-size:0.85rem; margin-top:8px;">
                            <strong>Why low unemployment causes high inflation:</strong> When aggregate demand surges, firms aggressively expand operations. Labor reserves become scarce. Vacancies multiply, and workers enjoy maximum bargaining leverage. To retain and recruit talent, firms bid up nominal wages ($W \uparrow$). Because wages constitute the largest fraction of production costs, enterprises pass these expenses on to consumers via higher price markups ($P \uparrow$). Hence, $\mathbf{u \downarrow \implies \pi \uparrow}$.
                        </p>
                    </div>
                    <div class="metric-box">
                        <div class="metric-label">SLACK LABOR REGIME ($u > u_n$)</div>
                        <p style="font-size:0.85rem; margin-top:8px;">
                            <strong>Why high unemployment coincides with low inflation:</strong> In a recession, aggregate demand contracts. Firms lay off personnel and freeze recruitment. Millions of workers compete for scarce job openings; worker bargaining power collapses. Nominal wage growth stagnates or turns negative ($W \downarrow$). Facing subdued labor costs and weak consumer demand, firms discount prices to liquidate inventory. Hence, $\mathbf{u \uparrow \implies \pi \downarrow}$.
                        </p>
                    </div>
                </div>
            </div>

            <div class="intel-card">
                <a id="ch11-friedman-phelps"></a>
<h3>11.3 The Friedman-Phelps Critique: The Demise of the Stable Trade-off</h3>
                <p>
                    In the late 1960s, <strong>Milton Friedman</strong> and <strong>Edmund Phelps</strong> independently issued a revolutionary theoretical challenge: the original Phillips Curve suffered from <strong>money illusion</strong>.
                </p>
                <ul style="margin-left:20px; line-height:1.7;">
                    <li><strong>Real Wages Govern Behavior:</strong> Workers do not care about nominal wages ($W$); they care about the purchasing power of their paychecks—the <em>real wage</em> ($W/P$). Similarly, firms base hiring decisions on the real wage.</li>
                    <li><strong>Inflation Expectations Matter:</strong> If the central bank attempts to keep unemployment below its natural rate through perpetual monetary expansion, workers will soon realize that inflation is eroding their purchasing power.</li>
                    <li><strong>Wage Renegotiation:</strong> In subsequent collective bargaining rounds, workers demand nominal wage hikes that incorporate expected future inflation ($\pi^e$).</li>
                    <li><strong>The Neutrality of Money:</strong> Once expected inflation catches up with actual inflation ($\pi^e = \pi$), real wages return to their equilibrium level, firms cut back hiring to the natural baseline, and unemployment returns to $u_n$—but now at a permanently higher rate of inflation!</li>
                </ul>
                <div class="warning-box">
                    <strong>The Friedman-Phelps Verdict:</strong> There is <em>no permanent, long-run trade-off</em> between inflation and unemployment. The government cannot trick the labor market forever. Any attempt to peg unemployment below $u_n$ results in <strong>accelerating inflation</strong>.
                </div>
            </div>

            <div class="intel-card">
                <h3>11.4 The Expectations-Augmented Phillips Curve Equation</h3>
                <p>Modern macroeconomics models inflation using the expectations-augmented specification:</p>
                <div class="formula-box">
                    $$\pi = \pi^e - \beta(u - u_n) + \nu$$
                </div>
                <h4>Detailed Decomposition of Every Variable:</h4>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>Symbol</th>
                            <th>Economic Identity</th>
                            <th>Role & Transmission in the System</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>$\pi$</td>
                            <td><strong>Actual Inflation Rate</strong></td>
                            <td>The percentage change in the general price level over the measurement period.</td>
                        </tr>
                        <tr>
                            <td>$\pi^e$</td>
                            <td><strong>Expected Inflation Rate</strong></td>
                            <td>The forward-looking inflation anticipated by wage-setters and financial markets. A 1% rise in $\pi^e$ shifts the entire SRPC upward vertically by 1%.</td>
                        </tr>
                        <tr>
                            <td>$\beta$</td>
                            <td><strong>Cyclical Sensitivity Parameter</strong></td>
                            <td>Measures the responsiveness of inflation to the unemployment gap. A larger $\beta$ implies that wages and prices react aggressively to labor market slack.</td>
                        </tr>
                        <tr>
                            <td>$(u - u_n)$</td>
                            <td><strong>Unemployment Gap</strong></td>
                            <td>Difference between actual unemployment ($u$) and the Natural Rate of Unemployment ($u_n$ / NAIRU). If $u < u_n$, the gap is negative, exerting upward demand-pull pressure on inflation.</td>
                        </tr>
                        <tr>
                            <td>$\nu$</td>
                            <td><strong>Exogenous Supply Shock</strong></td>
                            <td>Represents sudden shifts in production costs independent of labor market tightness (e.g., OPEC crude oil embargoes, geopolitical supply disruptions, agricultural crop failures). A positive $\nu$ shifts SRPC vertically upward.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="intel-card">
                <a id="ch11-srpc-lrpc"></a>
<h3>11.5 Movements Along vs. Shifts of the Short-Run Phillips Curve (SRPC)</h3>
                <div class="grid-2">
                    <div class="metric-box">
                        <div class="metric-label">MOVEMENTS ALONG THE SRPC</div>
                        <p style="font-size:0.85rem; margin-top:8px;">
                            <strong>Trigger: Demand-Side Shocks (AD Shifts).</strong><br>
                            When fiscal or monetary policy alters Aggregate Demand (e.g., central bank cuts interest rates), output and employment rise while prices increase. The economy slides <strong>upward-left along the existing SRPC</strong> ($u \downarrow, \pi \uparrow$). If AD collapses, the economy slides <strong>downward-right</strong> ($u \uparrow, \pi \downarrow$).
                        </p>
                    </div>
                    <div class="metric-box">
                        <div class="metric-label">SHIFTS OF THE ENTIRE SRPC</div>
                        <p style="font-size:0.85rem; margin-top:8px;">
                            <strong>Trigger: Supply Shocks ($\nu$) or Changes in Expectations ($\Delta \pi^e$).</strong><br>
                            An adverse supply shock (oil spike) or a rise in expected inflation shifts the <strong>entire SRPC upward-right</strong>. At <em>every given level of unemployment</em>, inflation is now higher. Conversely, a favorable technology shock or credibility-driven anchoring of lower inflation expectations shifts SRPC <strong>downward-left</strong>.
                        </p>
                    </div>
                </div>

                <h4>The Long-Run Phillips Curve (LRPC):</h4>
                <p>
                    In the long run, expected inflation fully adjusts to actual inflation ($\pi^e = \pi$) and supply shocks dissipate ($\nu = 0$). Substituting into the formula:
                </p>
                <div class="formula-box">
                    $$\pi = \pi - \beta(u - u_n) \implies 0 = -\beta(u - u_n) \implies u = u_n$$
                </div>
                <p>
                    Therefore, the <strong>Long-Run Phillips Curve (LRPC) is a vertical line at the Natural Rate of Unemployment ($u_n$ or NAIRU)</strong>. Central banks can choose the inflation rate in the long run through monetary policy, but they cannot choose the unemployment rate—it is governed solely by structural labor market realities.
                </p>
            </div>

            <!-- Canvas Lab 6: Phillips Curve Dual Simulator -->
            <div class="intel-card">
                <div class="lab-toolbar-header">
                    <span class="lab-toolbar-badge">TACTICAL LAB 06 // DUAL-PANEL AD-AS & PHILLIPS CURVE SIMULATOR</span>
                    <button class="graph-reset-btn" onclick="resetPhillipsGraph()" type="button" title="Reset Phillips Curve Simulation to Baseline Parameters">
                        <span class="reset-icon">↺</span> RESET SIMULATION TO BASELINE
                    </button>
                </div>
                <h3>11.6 Q-Branch Interactive Laboratory: Dual-Panel AD-AS & Phillips Curve Simulator</h3>
                <p>
                    Experiment with unemployment changes and inflation expectations to witness how the short-run trade-off shifts, while the vertical Long-Run Phillips Curve (LRPC) dictates the structural limit.
                </p>
                <div class="canvas-lab-container" style="height:380px;">
                    <canvas id="phillipsCanvas" class="canvas-screen"></canvas>
                </div>
                <div class="canvas-controls">
                    <div class="control-group">
                        <label>UNEMPLOYMENT RATE (u %):</label>
                        <input type="range" id="pcUSlider" min="2.0" max="10.0" value="4.0" step="0.5">
                    </div>
                    <div class="control-group">
                        <label>EXPECTED INFLATION ($\pi^e$ %):</label>
                        <input type="range" id="pcExpInfSlider" min="0.0" max="10.0" value="4.0" step="0.5">
                    </div>
                    <div class="control-group" style="align-self:flex-end;">
                        <button class="graph-reset-btn" onclick="resetPhillipsGraph()" type="button" title="Reset Simulation to Baseline">↺ RESET SIMULATION</button>
                    </div>
                </div>
                <div class="grid-3" style="margin-top:12px;">
                    <div class="metric-box">
                        <div class="metric-label">ACTUAL INFLATION ($\pi$)</div>
                        <div id="pcActInfReadout" class="metric-val" style="color:#f87171;">8.0%</div>
                    </div>
                    <div class="metric-box">
                        <div class="metric-label">NATURAL RATE (NRU / NAIRU)</div>
                        <div id="pcNruReadout" class="metric-val" style="color:var(--accent-silver);">6.0%</div>
                    </div>
                    <div class="metric-box">
                        <div class="metric-label">TRADEOFF REGIME</div>
                        <div id="pcTradeoffReadout" class="metric-val" style="color:#fbbf24;">Boom / Tight Labor</div>
                    </div>
                </div>
            </div>

            <div class="intel-card">
                <h3>11.7 Disinflation, The Sacrifice Ratio & Central Bank Credibility</h3>
                <p>
                    <strong>Disinflation:</strong> A policy-induced reduction in the rate of inflation (e.g., from 10% down to 4%).
                </p>
                <div class="grid-2">
                    <div class="metric-box">
                        <div class="metric-label">THE SACRIFICE RATIO</div>
                        <div class="formula-box" style="margin:4px 0;">
                            $$\text{Sacrifice Ratio} = \frac{\text{Cumulative \% Loss in Real GDP}}{\text{Percentage Point Reduction in Inflation}}$$
                        </div>
                        <p style="font-size:0.85rem; margin-top:6px;">Measures the painful output and employment loss an economy must endure during the disinflationary transition.</p>
                    </div>
                    <div class="metric-box">
                        <div class="metric-label">THE CREDIBILITY REVOLUTION</div>
                        <p style="font-size:0.85rem; margin-top:8px;">
                            If a central bank enjoys supreme institutional credibility (e.g., Paul Volcker in 1979 or modern inflation-targeting central banks), wage-setters immediately revise their expectations $\pi^e$ downward. The SRPC shifts down rapidly, allowing the central bank to achieve disinflation with <strong>minimal sacrifice of real output and employment</strong>.
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <!-- ==================== TAB 2: MISSIONS ==================== -->
        <div id="ch11-missions" class="subtab-content">
            <div class="mission-briefing">
                <div class="briefing-tag">TACTICAL EVALUATION // CH11 EXAM MISSIONS</div>
                <h3>Phillips Curve Deployments & Inflation Dynamics</h3>
                <p>Engage the following university examination problems across diverse macroeconomic scenarios.</p>
            </div>

            <!-- MISSION 11.1 -->
            <div class="intel-card">
                <div class="mission-status-bar">
                    <span class="difficulty-pill pill-med">LEVEL: ALGEBRAIC EQUATION</span>
                    <span class="mission-id">MISSION 007-11.1</span>
                </div>
                <h4>Tactical Mission: The Republic of Wakanda</h4>
                <p>
                    The central bank of Wakanda estimates the domestic short-run Phillips curve as follows:
                </p>
                <div class="formula-box">
                    $$\pi = \pi^e - 0.75(u - 0.05) + \nu$$
                </div>
                <p>
                    Initially, the natural rate of unemployment is $u_n = 5.0\%$, expected inflation is anchored at $\pi^e = 3.0\%$, and there are no supply shocks ($\nu = 0$).
                </p>
                <p><strong>Your Mission Directives:</strong></p>
                <ol style="margin-left:20px; line-height:1.7;">
                    <li>Calculate the baseline inflation rate when the economy operates at full employment ($u = 5.0\%$).</li>
                    <li>If an autonomous vibranium export boom drives the unemployment rate down to $u = 3.0\%$, calculate the new short-run inflation rate.</li>
                    <li>State clearly whether this scenario represents a movement along the SRPC or a shift of the SRPC, and identify the underlying economic driver.</li>
                </ol>
                <div class="hint-container">
                    <button class="hint-btn" onclick="toggleHint('h11-1-1')">DECRYPT HINT 1</button>
                    <div id="h11-1-1" class="hint-text">Substitute $u = 0.05$ for part 1, and $u = 0.03$ for part 2 into the given equation.</div>
                </div>
                <button class="action-btn" onclick="revealSolution('s11-1')">CONFIRM TARGET IDENTIFICATION // REVEAL SOLUTION</button>
<div id="s11-1" class="solution-card">
                <div class="mission-status-bar">
                    <span class="difficulty-pill pill-med">TARGET 11.1: WAKANDA DEMAND BOOM</span>
                    <span class="mission-id">VERIFIED BY Q-BRANCH</span>
                </div>
                <ol class="step-list">
                    <li class="step-item">
                        <div class="step-title">STEP 1: MISSION BRIEF</div>
                        <p>Determine inflation rates under full employment and during an export-led demand boom for the Republic of Wakanda.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 2: INTELLIGENCE EXTRACTION</div>
                        <p>Equation: $\pi = \pi^e - 0.75(u - u_n) + \nu$. Given: $u_n = 0.05$ (5%), $\pi^e = 0.03$ (3%), $\nu = 0$, boom unemployment $u = 0.03$ (3%).</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 3: FORMULA SELECTION</div>
                        <p>Expectations-augmented Phillips Curve: $\pi = \pi^e - \beta(u - u_n) + \nu$.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 4: EXECUTION</div>
                        <p>
                            <strong>Part 1: Full Employment ($u = 0.05$):</strong><br>
                            $$\pi = 0.03 - 0.75(0.05 - 0.05) + 0 = 0.03 = 3.0\%$$
                            <br>
                            <strong>Part 2: Export Boom ($u = 0.03$):</strong><br>
                            $$\pi = 0.03 - 0.75(0.03 - 0.05) + 0 = 0.03 - 0.75(-0.02) = 0.03 + 0.015 = 0.045 = 4.5\%$$
                        </p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 5: GRAPHICAL ANALYSIS</div>
                        <p>The economy moves <strong>upward-left along the existing short-run Phillips curve ($SRPC_0$)</strong> from the initial point $(u=5\%, \pi=3\%)$ to $(u=3\%, \pi=4.5\%)$.</p>

                        <div class="solution-svg-diagram">
                            <svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
                                <rect width="500" height="240" fill="#08090d" rx="4"/>
                                <line x1="40" y1="200" x2="470" y2="200" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                                <line x1="50" y1="210" x2="50" y2="20" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                                <text x="470" y="222" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" text-anchor="end">UNEMPLOYMENT (u %)</text>
                                <text x="25" y="30" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" transform="rotate(-90 25,30)" text-anchor="end">INFLATION (π %)</text>
                                <line x1="260" y1="30" x2="260" y2="200" stroke="#ffffff" stroke-width="2.5"/>
                                <text x="260" y="22" fill="#ffffff" font-family="var(--font-mono)" font-size="11" text-anchor="middle" font-weight="700">LRPC (u* = 6%)</text>
                                <line x1="100" y1="60" x2="420" y2="180" stroke="#e11d48" stroke-width="2.5"/>
                                <text x="425" y="185" fill="#e11d48" font-family="var(--font-mono)" font-size="11" font-weight="700">SRPC₀ (π^e = 4%)</text>
                                <circle cx="260" cy="120" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="260" cy="120" r="2.5" fill="#d92534"/>
                                <text x="270" y="115" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₀ (u=6%, π=4%)</text>
                                <line x1="50" y1="120" x2="260" y2="120" stroke="rgba(255,255,255,0.2)" stroke-dasharray="2,2"/>
                                <line x1="260" y1="120" x2="260" y2="200" stroke="rgba(255,255,255,0.2)" stroke-dasharray="2,2"/>
                                <text x="42" y="124" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" text-anchor="end">π₀ = 4%</text>
                                <text x="260" y="214" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" text-anchor="middle">u* = 6%</text>
                                <circle cx="180" cy="90" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="180" cy="90" r="2.5" fill="#d92534"/>
                                <text x="140" y="82" fill="#e11d48" font-family="var(--font-mono)" font-size="11" font-weight="700">E₁ (u=4%, π=8%)</text>
                                <line x1="50" y1="90" x2="180" y2="90" stroke="#e11d48" stroke-dasharray="2,2"/>
                                <line x1="180" y1="90" x2="180" y2="200" stroke="#e11d48" stroke-dasharray="2,2"/>
                                <text x="42" y="94" fill="#e11d48" font-family="var(--font-mono)" font-size="10" text-anchor="end">π₁ = 8%</text>
                                <text x="180" y="214" fill="#e11d48" font-family="var(--font-mono)" font-size="10" text-anchor="middle">u₁ = 4%</text>
                            </svg>
                            <span class="solution-svg-caption">FIGURE 11.1: SHORT-RUN PHILLIPS CURVE TRADE-OFF</span>
                        </div>

                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 6: ECONOMIC INTERPRETATION</div>
                        <p>This is a pure <strong>movement along the SRPC</strong> driven by an Aggregate Demand shock (export surge). Strong demand tightens the labor market, bidding down unemployment to 3%. Workers command higher wage increases, which firms pass through as consumer price inflation of 4.5%.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 7: TARGET CONFIRMATION</div>
                        <div class="formula-box">
                            $$\mathbf{\pi_{\text{full}} = 3.0\%, \quad \pi_{\text{boom}} = 4.5\%, \quad \text{Movement along existing SRPC}}$$
                        </div>
                    </li>
                </ol>
            </div>
            </div>

            <!-- MISSION 11.2 -->
            <div class="intel-card">
                <div class="mission-status-bar">
                    <span class="difficulty-pill pill-hard">LEVEL: SUPPLY SHOCK STAGFLATION</span>
                    <span class="mission-id">MISSION 007-11.2</span>
                </div>
                <h4>Tactical Mission: The Kingdom of Avalor</h4>
                <p>
                    Continuing from Wakanda's baseline parameters ($\pi^e = 3.0\%, u_n = 5.0\%, \beta = 0.75$), an international geopolitical conflict shuts down global maritime shipping, imposing an acute cost-push supply shock of $\nu = +2.5\%$. Simultaneously, falling business confidence pushes the domestic unemployment rate up to $u = 7.0\%$.
                </p>
                <p><strong>Your Mission Directives:</strong></p>
                <ol style="margin-left:20px; line-height:1.7;">
                    <li>Calculate the resulting short-run inflation rate in Avalor.</li>
                    <li>Explain why Avalor experiences <em>stagflation</em>.</li>
                    <li>Illustrate whether this event represents a movement along or a shift of the SRPC.</li>
                </ol>
                <div class="hint-container">
                    <button class="hint-btn" onclick="toggleHint('h11-2-1')">DECRYPT HINT 1</button>
                    <div id="h11-2-1" class="hint-text">Substitute $\pi^e = 0.03$, $\beta = 0.75$, $u = 0.07$, $u_n = 0.05$, and $\nu = +0.025$.</div>
                </div>
                <button class="action-btn" onclick="revealSolution('s11-2')">CONFIRM TARGET IDENTIFICATION // REVEAL SOLUTION</button>
<div id="s11-2" class="solution-card">
                <div class="mission-status-bar">
                    <span class="difficulty-pill pill-hard">TARGET 11.2: AVALOR SUPPLY-SHOCK STAGFLATION</span>
                    <span class="mission-id">VERIFIED BY Q-BRANCH</span>
                </div>
                <ol class="step-list">
                    <li class="step-item">
                        <div class="step-title">STEP 1: MISSION BRIEF</div>
                        <p>Quantify the simultaneous inflation and unemployment outcome in Avalor following a maritime shipping cost-push shock.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 2: INTELLIGENCE EXTRACTION</div>
                        <p>$\pi^e = 0.03$ (3%), $u_n = 0.05$, $\beta = 0.75$, $\nu = +0.025$ (+2.5%), $u = 0.07$ (7%).</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 3: FORMULA SELECTION</div>
                        <p>$\pi = \pi^e - \beta(u - u_n) + \nu$.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 4: EXECUTION</div>
                        <p>
                            $$\pi = 0.03 - 0.75(0.07 - 0.05) + 0.025$$
                            $$\pi = 0.03 - 0.75(0.02) + 0.025 = 0.03 - 0.015 + 0.025 = 0.040 = 4.0\%$$
                        </p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 5: GRAPHICAL ANALYSIS</div>
                        <p>The positive supply shock $\nu = +2.5\%$ causes an <strong>upward-right shift of the entire SRPC</strong> from $SRPC_0$ to $SRPC_1$. The economy operates at $(u=7\%, \pi=4\%)$, combining above-normal unemployment with elevated inflation.</p>

                        <div class="solution-svg-diagram">
                            <svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
                                <rect width="500" height="240" fill="#08090d" rx="4"/>
                                <line x1="40" y1="200" x2="470" y2="200" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                                <line x1="50" y1="210" x2="50" y2="20" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                                <text x="470" y="222" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" text-anchor="end">UNEMPLOYMENT (u %)</text>
                                <text x="25" y="30" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" transform="rotate(-90 25,30)" text-anchor="end">INFLATION (π %)</text>
                                <line x1="260" y1="30" x2="260" y2="200" stroke="#ffffff" stroke-width="2.5"/>
                                <text x="260" y="22" fill="#ffffff" font-family="var(--font-mono)" font-size="11" text-anchor="middle" font-weight="700">LRPC (u* = 6%)</text>
                                <line x1="100" y1="90" x2="420" y2="210" stroke="#e11d48" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <text x="425" y="215" fill="#e11d48" font-family="var(--font-mono)" font-size="10">SRPC₀ (Baseline)</text>
                                <line x1="100" y1="40" x2="420" y2="160" stroke="#e11d48" stroke-width="2.5"/>
                                <text x="425" y="165" fill="#e11d48" font-family="var(--font-mono)" font-size="11" font-weight="700">SRPC₁ (Supply Shock)</text>
                                <line x1="320" y1="170" x2="320" y2="120" stroke="#e11d48" stroke-width="2"/>
                                <polygon points="316,120 320,112 324,120" fill="#e11d48"/>
                                <circle cx="260" cy="150" r="5" fill="none" stroke="rgba(255,255,255,0.5)" stroke-width="1.5"/>
                                <text x="270" y="155" fill="rgba(255,255,255,0.6)" font-family="var(--font-mono)" font-size="9">E₀(6%, 4%)</text>
                                <circle cx="260" cy="100" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="260" cy="100" r="2.5" fill="#d92534"/>
                                <line x1="248" y1="100" x2="272" y2="100" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="260" y1="88" x2="260" y2="112" stroke="#d92534" stroke-width="1.2"/>
                                <text x="270" y="95" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E_shock (6%, 7%)</text>
                                <line x1="50" y1="100" x2="260" y2="100" stroke="#e11d48" stroke-dasharray="2,2"/>
                                <text x="42" y="104" fill="#e11d48" font-family="var(--font-mono)" font-size="10" text-anchor="end">π_shock = 7%</text>
                            </svg>
                            <span class="solution-svg-caption">FIGURE 11.2: ADVERSE SUPPLY SHOCK SHIFTS SRPC UPWARD</span>
                        </div>

                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 6: ECONOMIC INTERPRETATION</div>
                        <p>This illustrates classic <strong>stagflation</strong>. The shipping cost shock shifts SRAS leftward, simultaneously causing output contraction (raising unemployment from 5% to 7%) and raising prices. Even though labor market slack dampens wage pressure ($-1.5\%$), the external cost shock ($+2.5\%$) dominates, driving final inflation to 4.0%.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 7: TARGET CONFIRMATION</div>
                        <div class="formula-box">
                            $$\mathbf{\pi = 4.0\%, \quad u = 7.0\%, \quad \text{Upward Shift of the Entire SRPC (Stagflation)}}$$
                        </div>
                    </li>
                </ol>
            </div>
            </div>

            <!-- MISSION 11.3 -->
            <div class="intel-card">
                <div class="mission-status-bar">
                    <span class="difficulty-pill pill-hard">LEVEL: LONG-RUN ADJUSTMENT</span>
                    <span class="mission-id">MISSION 007-11.3</span>
                </div>
                <h4>Tactical Mission: Monetaria's Expectations Trap</h4>
                <p>
                    In the sovereign state of Monetaria, the government attempts to permanently engineer an unemployment rate of $u = 3.5\%$ (below the natural rate $u_n = 5.0\%$) via persistent monetary expansion. The sensitivity parameter is $\beta = 1.0$, and initially $\pi^e_0 = 2.0\%$.
                </p>
                <p><strong>Your Mission Directives:</strong></p>
                <ol style="margin-left:20px; line-height:1.7;">
                    <li>Calculate the actual inflation rate $\pi_1$ generated in Year 1.</li>
                    <li>Assuming adaptive expectations where $\pi^e_t = \pi_{t-1}$, calculate expected inflation $\pi^e_2$ and actual inflation $\pi_2$ in Year 2 if the central bank insists on maintaining $u = 3.5\%$.</li>
                    <li>Explain why the government cannot permanently maintain $u = 3.5\%$ without triggering an explosive inflation spiral.</li>
                </ol>
                <div class="hint-container">
                    <button class="hint-btn" onclick="toggleHint('h11-3-1')">DECRYPT HINT 1</button>
                    <div id="h11-3-1" class="hint-text">Year 1: $\pi_1 = 0.02 - 1.0(0.035 - 0.050) = 0.02 - (-0.015) = 0.035 = 3.5\%$. For Year 2, $\pi^e_2 = 3.5\%$.</div>
                </div>
                <button class="action-btn" onclick="revealSolution('s11-3')">CONFIRM TARGET IDENTIFICATION // REVEAL SOLUTION</button>
<div id="s11-3" class="solution-card">
                <div class="mission-status-bar">
                    <span class="difficulty-pill pill-hard">TARGET 11.3: MONETARIA'S EXPECTATIONS SPIRAL</span>
                    <span class="mission-id">VERIFIED BY Q-BRANCH</span>
                </div>
                <ol class="step-list">
                    <li class="step-item">
                        <div class="step-title">STEP 1: MISSION BRIEF</div>
                        <p>Model the multi-period inflation dynamics when Monetaria attempts to peg unemployment below the natural rate under adaptive expectations.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 2: INTELLIGENCE EXTRACTION</div>
                        <p>$\beta = 1.0$, $u_n = 5.0\%$, target $u = 3.5\%$, initial $\pi^e_1 = 2.0\%$, adaptive expectations: $\pi^e_t = \pi_{t-1}$.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 3: FORMULA SELECTION</div>
                        <p>$\pi_t = \pi^e_t - \beta(u_t - u_n)$.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 4: EXECUTION</div>
                        <p>
                            <strong>Year 1:</strong>
                            $$\pi_1 = 0.02 - 1.0(0.035 - 0.050) = 0.02 - (-0.015) = 0.035 = 3.5\%$$
                            <strong>Year 2:</strong>
                            Wage-setters incorporate past inflation: $\pi^e_2 = \pi_1 = 3.5\%$.
                            $$\pi_2 = 0.035 - 1.0(0.035 - 0.050) = 0.035 + 0.015 = 0.050 = 5.0\%$$
                            <strong>Year 3 (Projection):</strong>
                            $$\pi^e_3 = 5.0\% \implies \pi_3 = 0.050 + 0.015 = 6.5\%$$
                        </p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 5: GRAPHICAL ANALYSIS</div>
                        <p>The SRPC shifts continuously upward from $SRPC_1$ ($\pi^e=2\%$) to $SRPC_2$ ($\pi^e=3.5\%$) to $SRPC_3$ ($\pi^e=5\%$). The long-run path traces out the vertical LRPC at $u_n = 5\%$.</p>

                        <div class="solution-svg-diagram">
                            <svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
                                <rect width="500" height="240" fill="#08090d" rx="4"/>
                                <line x1="40" y1="200" x2="470" y2="200" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                                <line x1="50" y1="210" x2="50" y2="20" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                                <text x="470" y="222" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" text-anchor="end">UNEMPLOYMENT (u %)</text>
                                <text x="25" y="30" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" transform="rotate(-90 25,30)" text-anchor="end">INFLATION (π %)</text>
                                <line x1="240" y1="30" x2="240" y2="200" stroke="#ffffff" stroke-width="2.5"/>
                                <text x="240" y="22" fill="#ffffff" font-family="var(--font-mono)" font-size="11" text-anchor="middle" font-weight="700">LRPC (u* = 5%)</text>
                                <line x1="80" y1="50" x2="400" y2="170" stroke="#e11d48" stroke-width="2.5"/>
                                <text x="405" y="175" fill="#e11d48" font-family="var(--font-mono)" font-size="11" font-weight="700">SRPC(π^e = 8%)</text>
                                <line x1="80" y1="100" x2="400" y2="220" stroke="#10b981" stroke-width="2" stroke-dasharray="3,3"/>
                                <text x="405" y="225" fill="#10b981" font-family="var(--font-mono)" font-size="11">SRPC(π^e = 3%)</text>
                                <circle cx="240" cy="110" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="240" cy="110" r="2.5" fill="#d92534"/>
                                <text x="250" y="105" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₀ (8% Infl.)</text>
                                <circle cx="340" cy="148" r="5" fill="none" stroke="#f59e0b" stroke-width="1.5"/>
                                <text x="350" y="145" fill="#f59e0b" font-family="var(--font-mono)" font-size="10">E_slump (Recession)</text>
                                <circle cx="240" cy="160" r="8" fill="none" stroke="#10b981" stroke-width="2"/>
                                <circle cx="240" cy="160" r="3" fill="#10b981"/>
                                <text x="250" y="165" fill="#10b981" font-family="var(--font-mono)" font-size="11" font-weight="700">E_final (3% Target)</text>
                            </svg>
                            <span class="solution-svg-caption">FIGURE 11.3: DISINFLATION TRAJECTORY & SACRIFICE RATIO</span>
                        </div>

                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 6: ECONOMIC INTERPRETATION</div>
                        <p><strong>The Accelerationist Principle:</strong> Maintaining unemployment permanently below the natural rate requires ever-accelerating rates of monetary growth and inflation. As workers catch up to eroded real wages, they demand higher wages, shifting SRPC upward. To prevent unemployment from returning to 5%, the central bank must generate an even larger positive inflation surprise, creating an unsustainable hyperinflationary spiral.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 7: TARGET CONFIRMATION</div>
                        <div class="formula-box">
                            $$\mathbf{\pi_1 = 3.5\%, \quad \pi^e_2 = 3.5\%, \quad \pi_2 = 5.0\% \quad (\text{Explosive Inflation Acceleration})}$$
                        </div>
                    </li>
                </ol>
            </div>
            </div>

            <!-- MISSION 11.4 -->
            <div class="intel-card">
                <div class="mission-status-bar">
                    <span class="difficulty-pill pill-exam">LEVEL: DISINFLATION & SACRIFICE</span>
                    <span class="mission-id">MISSION 007-11.4</span>
                </div>
                <h4>Tactical Mission: Borealia's Disinflation Campaign</h4>
                <p>
                    The Central Bank of Borealia faces entrenched inflation of $\pi = 9.0\%$. The Monetary Policy Committee is tasked with executing a disinflation policy to lower inflation to target $\pi^* = 3.0\%$ over a 3-year period.
                </p>
                <p>
                    Empirical data reveals that Borealia's sacrifice ratio is <strong>2.5</strong> (meaning 2.5% of one year's real GDP must be foregone for each 1-percentage-point permanent reduction in inflation). Borealia's baseline potential GDP is <strong>\$800 billion</strong>.
                </p>
                <p><strong>Your Mission Directives:</strong></p>
                <ol style="margin-left:20px; line-height:1.7;">
                    <li>Calculate the total cumulative percentage of real GDP that Borealia must sacrifice to achieve the target.</li>
                    <li>Calculate the cumulative monetary dollar loss in real national output.</li>
                    <li>How can central bank transparency, institutional independence, and inflation targeting reduce this sacrifice ratio?</li>
                </ol>
                <div class="hint-container">
                    <button class="hint-btn" onclick="toggleHint('h11-4-1')">DECRYPT HINT 1</button>
                    <div id="h11-4-1" class="hint-text">Target reduction $\Delta \pi = 9\% - 3\% = 6$ percentage points. Cumulative loss = $6 \times 2.5 = 15\%$.</div>
                </div>
                <button class="action-btn" onclick="revealSolution('s11-4')">CONFIRM TARGET IDENTIFICATION // REVEAL SOLUTION</button>
<div id="s11-4" class="solution-card">
                <div class="mission-status-bar">
                    <span class="difficulty-pill pill-exam">TARGET 11.4: BOREALIA DISINFLATION & SACRIFICE</span>
                    <span class="mission-id">VERIFIED BY Q-BRANCH</span>
                </div>
                <ol class="step-list">
                    <li class="step-item">
                        <div class="step-title">STEP 1: MISSION BRIEF</div>
                        <p>Calculate cumulative output sacrifice in percentage and dollar terms for a 6% disinflation in Borealia.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 2: INTELLIGENCE EXTRACTION</div>
                        <p>Initial $\pi_0 = 9\%$, target $\pi^* = 3\%$, Sacrifice Ratio = 2.5, Potential GDP = \$800 Billion.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 3: FORMULA SELECTION</div>
                        <p>
                            $$\text{Required Disinflation } (\Delta \pi) = \pi_0 - \pi^*$$
                            $$\text{Cumulative Output Loss (\%)} = \Delta \pi \times \text{Sacrifice Ratio}$$
                            $$\text{Dollar Loss} = \text{Cumulative Output Loss (\%)} \times \text{Potential GDP}$$
                        </p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 4: EXECUTION</div>
                        <p>
                            $$\Delta \pi = 9.0\% - 3.0\% = 6.0 \text{ percentage points}$$
                            $$\text{Cumulative GDP Sacrifice (\%)} = 6.0 \times 2.5 = 15.0\% \text{ of one year's GDP}$$
                            $$\text{Monetary Loss} = 15\% \times \$800 \text{ Billion} = 0.15 \times 800 = \mathbf{\$120 \text{ Billion}}$$
                        </p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 5: GRAPHICAL ANALYSIS</div>
                        <p>During disinflation, the central bank contracts AD. The economy moves downward-right along the SRPC into recession ($u > u_n$). Gradually, as expectations fall from 9% to 3%, the SRPC shifts downward to anchor at the vertical LRPC.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 6: ECONOMIC INTERPRETATION</div>
                        <p>Borealia must undergo \$120 billion in cumulative lost output (unemployment above natural rate) because wage contracts and inflation expectations are sluggish. However, if the central bank establishes <strong>high credibility</strong> through transparent communication, forward guidance, and a binding inflation-targeting charter, expected inflation drops quickly without requiring prolonged economic contraction—slashing the sacrifice ratio dramatically.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 7: TARGET CONFIRMATION</div>
                        <div class="formula-box">
                            $$\mathbf{\Delta \pi = 6.0\% \implies \text{GDP Sacrifice} = 15.0\% = \$120 \text{ Billion}}$$
                        </div>
                    </li>
                </ol>
            </div>
        </div>
    </div>

    <!-- ==================== TAB 3: TARGETS ==================== -->
        <div id="ch11-targets" class="subtab-content">
            <div class="mission-briefing">
                <div class="briefing-tag">TARGET DEBRIEF // OFFICIAL 7-STEP PROTOCOL</div>
                <h3>Standard Operating Procedure Solutions: The Phillips Curve</h3>
                <p>All 4 mission target debriefings are fully decrypted with technical Phillips Curve diagrams. You can view each solution directly beneath its problem in the <strong>Combat Missions</strong> tab, or use the direct target conduits below:</p>
            </div>

            <div class="grid-2">
                <div class="intel-card">
                    <span class="difficulty-pill pill-hard">TARGET 11.1</span>
                    <h4>Short-Run Phillips Curve Trade-off</h4>
                    <p>Demand stimulus drives unemployment from 6% down to 4%, accelerating inflation to $\pi = 8\%$. Movement up-left along $SRPC_0$.</p>
                    <button class="action-btn" onclick="switchSubTab(event, 'ch11-missions'); revealSolution('s11-1');">ACCESS TARGET 11.1 DEBRIEF</button>
                </div>

                <div class="intel-card">
                    <span class="difficulty-pill pill-hard">TARGET 11.2</span>
                    <h4>Adverse Supply Shock on Phillips Curve</h4>
                    <p>Crude oil price shock ($\Delta v = 3\%$) shifts the entire SRPC curve upward. Inflation reaches 7% with zero reduction in natural unemployment.</p>
                    <button class="action-btn" onclick="switchSubTab(event, 'ch11-missions'); revealSolution('s11-2');">ACCESS TARGET 11.2 DEBRIEF</button>
                </div>

                <div class="intel-card">
                    <span class="difficulty-pill pill-exam">TARGET 11.3</span>
                    <h4>Disinflation Dynamics & The Sacrifice Ratio</h4>
                    <p>Reducing inflation from 8% to 3% yields a cumulative output sacrifice of 12.5% of GDP under a Sacrifice Ratio of 2.5.</p>
                    <button class="action-btn" onclick="switchSubTab(event, 'ch11-missions'); revealSolution('s11-3');">ACCESS TARGET 11.3 DEBRIEF</button>
                </div>

                <div class="intel-card">
                    <span class="difficulty-pill pill-exam">TARGET 11.4</span>
                    <h4>Comprehensive Phillips Curve Evaluation</h4>
                    <p>Evaluating adaptive vs. rational expectations, Lucas Critique, central bank independence, and Okun's Law transmission to output gaps.</p>
                    <button class="action-btn" onclick="switchSubTab(event, 'ch11-missions'); revealSolution('s11-4');">ACCESS TARGET 11.4 DEBRIEF</button>
                </div>
            </div>
        </div>
    </div>
</section>
'''

if __name__ == '__main__':
    print('Testing ch11 module length:', len(get_chapter_11()))
