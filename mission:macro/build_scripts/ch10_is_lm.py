"""
PROJECT 007: THE MACROECONOMICS INTELLIGENCE FILE
Chapter 10: The IS-LM Framework & General Equilibrium Generator
"""

def get_chapter_10():
    return r'''
<section id="chapter-10" class="mission-chapter">
<a id="ch10" class="chapter-anchor"></a>
    <div class="chapter-header">
        <div class="briefing-tag">TACTICAL INTEL FILE // DOSSIER 10</div>
        <h2 class="chapter-title">CHAPTER 10: THE IS-LM FRAMEWORK & GENERAL EQUILIBRIUM</h2>
        <div class="classified-stamp">TOP SECRET // RESTRICTED ACCESS</div>
    </div>

    <div class="tab-container">
        <div class="tab-nav">
            <button class="tab-btn active" onclick="switchSubTab(event, 'ch10-training')">FIELD TRAINING // THEORY</button>
            <button class="tab-btn" onclick="switchSubTab(event, 'ch10-missions')">COMBAT MISSIONS // EXAM PROBLEMS</button>
            <button class="tab-btn" onclick="switchSubTab(event, 'ch10-targets')">TARGET TARGETS // 7-STEP SOLUTIONS</button>
        </div>

        <!-- ==================== TAB 1: TRAINING ==================== -->
        <div id="ch10-training" class="subtab-content active">
            <div class="intel-card">
                <h3>10.1 Mission Directive: Simultaneous Dual-Market Equilibrium</h3>
                <p>
                    Up to this point in Q-Branch intelligence analysis, we examined the <strong>Goods Market</strong> (Keynesian Cross, Multipliers) and the <strong>Money Market</strong> ($M_0-M_4$, Central Bank instruments) in isolation. However, in an operational economy, these two markets are <strong>inextricably coupled</strong> through two transmission gears:
                </p>
                <div class="grid-2">
                    <div class="metric-box">
                        <div class="metric-label">TRANSMISSION LINK 1</div>
                        <div class="metric-val" style="color:var(--accent-silver);">Interest Rate ($r$)</div>
                        <p style="font-size:0.85rem; margin-top:8px;">Determined primarily in the Money Market; directly dictates autonomous investment expenditure ($I(r)$) in the Goods Market.</p>
                    </div>
                    <div class="metric-box">
                        <div class="metric-label">TRANSMISSION LINK 2</div>
                        <div class="metric-val" style="color:var(--accent-silver);">Aggregate Output ($Y$)</div>
                        <p style="font-size:0.85rem; margin-top:8px;">Determined in the Goods Market; directly dictates the transactional and precautionary demand for real money balances ($L_1(Y)$) in the Money Market.</p>
                    </div>
                </div>
                <p style="margin-top:14px;">
                    The <strong>IS-LM Model</strong> (pioneered by Sir John Hicks in 1937 based on John Maynard Keynes's <em>General Theory</em>) synthesizes both sectors to locate the unique pair of interest rate ($r^*$) and output ($Y^*$) that establishes simultaneous equilibrium across both the real and monetary sectors of the economy.
                </p>
            </div>

            <div class="intel-card">
                <a id="ch10-is-curve"></a>
<h3>10.2 The IS Curve: Goods Market Equilibrium</h3>
                <p>
                    <strong>Definition:</strong> The <strong>IS curve</strong> (Investment-Saving) represents the locus of all combinations of the real interest rate ($r$) and aggregate output/income ($Y$) where the <strong>Goods Market is in equilibrium</strong> (Aggregate Planned Expenditure = Real Output, or Leakages = Injections).
                </p>
                <h4>Derivation of the IS Curve:</h4>
                <ol style="margin-left:20px; line-height:1.7;">
                    <li><strong>Investment Function:</strong> Planned investment is negatively related to the interest rate: $I = I_0 - b \cdot r$, where $b > 0$ measures the interest sensitivity of investment.</li>
                    <li><strong>Keynesian Equilibrium:</strong> In a closed economy with government:
                        <div class="formula-box">
                            $$Y = C + I + G$$
                            $$Y = [C_0 + c(Y - T)] + [I_0 - br] + G$$
                            $$Y - cY = C_0 - cT + I_0 - br + G$$
                            $$Y(1 - c) = \bar{A} - br \quad \text{where } \bar{A} \equiv C_0 - cT + I_0 + G$$
                            $$Y = \frac{1}{1 - c}[\bar{A} - br] = k_F [\bar{A} - br]$$
                        </div>
                    </li>
                    <li><strong>Slope of the IS Curve:</strong> Expressing $r$ as a function of $Y$:
                        $$r = \frac{\bar{A}}{b} - \frac{1 - c}{b} Y = \frac{\bar{A}}{b} - \frac{1}{b \cdot k_F} Y$$
                        Because $b > 0$ and $(1-c) > 0$, the slope $\frac{dr}{dY} = -\frac{1-c}{b} < 0$. The IS curve is strictly <strong>downward sloping</strong>.
                    </li>
                </ol>
                <div class="warning-box">
                    <strong>Economic Intuition of Downward Slope:</strong> When interest rates drop ($r \downarrow$), corporate financing costs fall $\implies$ planned investment rises ($I \uparrow$) $\implies$ aggregate demand exceeds output $\implies$ through the multiplier cascade, equilibrium national output expands ($Y \uparrow$). Hence, lower interest rates require higher output to restore goods market balance.
                </div>

                <h4>Disequilibrium in the Goods Market (Off-IS Dynamics):</h4>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>Position Relative to IS</th>
                            <th>Current Output vs Equilibrium</th>
                            <th>Economic Condition</th>
                            <th>Market Adjustment Mechanism</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong style="color:var(--accent-crimson);">Points Above IS</strong></td>
                            <td>At given $Y$, interest rate $r$ is too high; or at given $r$, output $Y$ is too large.</td>
                            <td><strong>Excess Supply of Goods (ESG)</strong><br>($Y > AD$)</td>
                            <td>Unplanned inventory accumulation ($I_{unplanned} > 0$). Firms cut production until output contracts back to IS ($Y \downarrow$).</td>
                        </tr>
                        <tr>
                            <td><strong style="color:var(--accent-silver);">Points Below IS</strong></td>
                            <td>At given $Y$, interest rate $r$ is too low; or at given $r$, output $Y$ is too low.</td>
                            <td><strong>Excess Demand of Goods (EDG)</strong><br>($AD > Y$)</td>
                            <td>Unplanned inventory depletion ($I_{unplanned} < 0$). Firms increase hiring and output until $Y$ expands to IS ($Y \uparrow$).</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="intel-card">
                <a id="ch10-lm-curve"></a>
<h3>10.3 The LM Curve: Money Market Equilibrium</h3>
                <p>
                    <strong>Definition:</strong> The <strong>LM curve</strong> (Liquidity Preference-Money Supply) represents the locus of all combinations of interest rate ($r$) and income ($Y$) where the <strong>Money Market is in equilibrium</strong> (Real Money Demand = Real Money Supply).
                </p>
                <h4>Derivation of the LM Curve:</h4>
                <ol style="margin-left:20px; line-height:1.7;">
                    <li><strong>Real Money Supply:</strong> Exogenously fixed by the Central Bank and price level $P$:
                        $$\left(\frac{M}{P}\right)^s = \frac{\bar{M}}{P}$$
                    </li>
                    <li><strong>Real Money Demand (Liquidity Preference):</strong> Comprises transactional demand (proportional to income $Y$) and speculative demand (inversely related to interest rate $r$):
                        $$\left(\frac{M}{P}\right)^d = L(Y, r) = k Y - h r$$
                        Where $k > 0$ represents income sensitivity of money demand, and $h > 0$ represents interest sensitivity of money demand.
                    </li>
                    <li><strong>Equilibrium Condition:</strong>
                        <div class="formula-box">
                            $$\frac{\bar{M}}{P} = k Y - h r$$
                            $$h r = k Y - \frac{\bar{M}}{P}$$
                            $$r = \frac{k}{h} Y - \frac{1}{h}\left(\frac{\bar{M}}{P}\right)$$
                        </div>
                    </li>
                    <li><strong>Slope of the LM Curve:</strong> $\frac{dr}{dY} = \frac{k}{h} > 0$. The LM curve is strictly <strong>upward sloping</strong>.
                    </li>
                </ol>
                <div class="warning-box">
                    <strong>Economic Intuition of Upward Slope:</strong> When real output expands ($Y \uparrow$), households and enterprises execute more transactions $\implies$ transactional money demand surges $\implies$ at a fixed real money supply ($\bar{M}/P$), people liquidate bonds to obtain cash $\implies$ bond prices crash $\implies$ market interest rates spike ($r \uparrow$) until speculative demand falls enough to restore money market equilibrium.
                </div>

                <h4>Disequilibrium in the Money Market (Off-LM Dynamics):</h4>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>Position Relative to LM</th>
                            <th>Current Interest Rate vs Equilibrium</th>
                            <th>Economic Condition</th>
                            <th>Market Adjustment Mechanism</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong style="color:var(--accent-silver);">Points Above LM</strong></td>
                            <td>At given $Y$, interest rate $r$ is too high $\implies$ money demand is depressed ($L < M/P$).</td>
                            <td><strong>Excess Supply of Money (ESM)</strong><br>(Excess Demand for Bonds)</td>
                            <td>Agents use excess cash to buy bonds $\implies$ bond prices bid up $\implies$ interest rates fall ($r \downarrow$) rapidly back to LM.</td>
                        </tr>
                        <tr>
                            <td><strong style="color:var(--accent-crimson);">Points Below LM</strong></td>
                            <td>At given $Y$, interest rate $r$ is too low $\implies$ money demand exceeds supply ($L > M/P$).</td>
                            <td><strong>Excess Demand for Money (EDM)</strong><br>(Excess Supply of Bonds)</td>
                            <td>Agents sell bonds to obtain cash $\implies$ bond prices collapse $\implies$ interest rates surge ($r \uparrow$) rapidly back to LM.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Canvas Lab 5: Interactive IS-LM Simulator -->
            <div class="intel-card">
                <div class="lab-toolbar-header">
                    <span class="lab-toolbar-badge">TACTICAL LAB 05 // IS–LM DUAL GENERAL EQUILIBRIUM SIMULATOR</span>
                    <button class="graph-reset-btn" onclick="resetIsLmGraph()" type="button" title="Reset IS-LM Simulation to Baseline Parameters">
                        <span class="reset-icon">↺</span> RESET SIMULATION TO BASELINE
                    </button>
                </div>
                <h3>10.4 Q-Branch Interactive Laboratory: IS-LM General Equilibrium Simulator</h3>
                <p>Manipulate autonomous fiscal spending, the nominal money supply, and test the Zero Lower Bound (Liquidity Trap) or Coordinated Policy Mix to monitor equilibrium shifts, interest rates, and private investment crowding out.</p>
                <div class="canvas-lab-container" style="height:380px;">
                    <canvas id="isLmCanvas" class="canvas-screen"></canvas>
                </div>
                <div class="canvas-controls">
                    <div class="control-group">
                        <label>FISCAL STANCE ($\Delta G$ / IS SHIFT):</label>
                        <input type="range" id="islmGSlider" min="-600" max="600" value="0" step="50">
                    </div>
                    <div class="control-group">
                        <label>MONETARY LIQUIDITY ($\Delta M$ / LM SHIFT):</label>
                        <input type="range" id="islmMSlider" min="-600" max="600" value="0" step="50">
                    </div>
                    <div class="control-group" style="flex-direction:row; align-items:center; gap:8px; flex-wrap:wrap;">
                        <button class="action-btn" id="islmZlbBtn" onclick="toggleLiquidityTrap(this)" style="padding:6px 12px; font-size:0.75rem;">LIQUIDITY TRAP (ZLB)</button>
                        <button class="action-btn" id="islmCoordBtn" onclick="toggleCoordinatedMix(this)" style="padding:6px 12px; font-size:0.75rem;">COORDINATED MIX</button>
                        <button class="graph-reset-btn" onclick="resetIsLmGraph()" type="button" title="Reset Simulation to Baseline">↺ RESET SIMULATION</button>
                    </div>
                </div>
                <div class="grid-3" style="margin-top:12px;">
                    <div class="metric-box">
                        <div class="metric-label">EQUILIBRIUM OUTPUT ($Y^*$)</div>
                        <div id="islmYReadout" class="metric-val" style="color:var(--accent-silver);">3000 units</div>
                    </div>
                    <div class="metric-box">
                        <div class="metric-label">INTEREST RATE ($r^*$)</div>
                        <div id="islmRReadout" class="metric-val" style="color:#60a5fa;">10.0%</div>
                    </div>
                    <div class="metric-box">
                        <div class="metric-label">PRIVATE INVESTMENT ($I^*$)</div>
                        <div id="islmIReadout" class="metric-val" style="color:#10b981;">600 units</div>
                    </div>
                </div>
            </div>

            <div class="intel-card">
                <a id="ch10-liquidity-trap"></a>
<h3>10.5 The Liquidity Trap & The Zero Lower Bound (ZLB)</h3>
                <p>
                    <strong>Definition:</strong> A <strong>Liquidity Trap</strong> is a severe macroeconomic pathological state wherein nominal interest rates approach zero (the Zero Lower Bound), and the speculative demand for money becomes <strong>infinitely elastic</strong> (horizontal LM curve).
                </p>
                <div class="grid-2">
                    <div class="metric-box">
                        <div class="metric-label">MONETARY POLICY IMPOTENCE</div>
                        <p style="font-size:0.85rem; margin-top:8px;">
                            When $r \approx 0$, bond prices are at their mathematical maximum. Investors expect bond prices can only fall, so they hoard all additional cash injections as pure liquidity rather than purchasing bonds. $\Delta M \implies \Delta r = 0 \implies \Delta I = 0 \implies \Delta Y = 0$. <strong>Monetary policy completely misfires.</strong>
                        </p>
                    </div>
                    <div class="metric-box">
                        <div class="metric-label">FISCAL POLICY SUPREMACY</div>
                        <p style="font-size:0.85rem; margin-top:8px;">
                            Because the LM curve is horizontal, fiscal expansion ($\Delta G > 0$) shifts the IS curve rightward <strong>without driving up interest rates</strong> ($r$ remains pinned at zero). Consequently, private investment experiences <strong>zero crowding out</strong>, and the fiscal multiplier achieves its full theoretical potential ($k_F = 1 / (1-MPC)$).
                        </p>
                    </div>
                </div>

                <h4>Historical Case Studies of Liquidity Traps:</h4>
                <ul style="margin-left:20px; line-height:1.7;">
                    <li><strong>The Great Depression (1929–1939):</strong> US Federal Reserve discount rates collapsed near 0%, but commercial banks held massive excess reserves; recovery occurred only through massive New Deal and WWII fiscal expenditures.</li>
                    <li><strong>Japan's "Lost Decades" (1990–2010s):</strong> Following the collapse of the Nikkei equity and real estate bubble in 1990, the Bank of Japan cut policy rates to 0% by 1999. Despite floodings of bank reserves, private credit stagnated due to corporate balance-sheet repair.</li>
                    <li><strong>Global Financial Crisis (2008–2015):</strong> US Federal Reserve and European Central Bank hit the ZLB ($0-0.25\%$), necessitating forward guidance and Quantitative Easing (asset purchases).</li>
                </ul>
            </div>

            <div class="intel-card">
                <h3>10.6 Central Banking: The Monetary Policy (MP) Curve & Taylor Principle</h3>
                <p>
                    Modern central banks (including the RBI and the Federal Reserve) do not target a fixed monetary aggregate $M_1/M_3$. Instead, they set the <strong>overnight interbank policy rate</strong> (e.g., RBI Repo Rate) using an endogenous reaction function:
                </p>
                <div class="formula-box">
                    $$r = \bar{r} + \lambda \pi$$
                    <p style="font-size:0.85rem; margin-top:6px;">Where $\bar{r}$ is the autonomous policy stance, $\pi$ is inflation, and $\lambda$ is the responsiveness parameter.</p>
                </div>
                <p>
                    <strong>The Taylor Principle:</strong> To stabilize inflation, central banks must raise nominal interest rates by <em>more than one-for-one</em> with inflation ($\Delta i > \Delta \pi$). This guarantees that the <strong>real interest rate rises</strong> ($r = i - \pi \uparrow$), dampening aggregate demand and choking off inflationary pressures.
                </p>
                <h4>Derivation of the Aggregate Demand (AD) Curve from MP-IS:</h4>
                <p>
                    Equating the IS curve ($Y = \bar{A} - b r$) with the central bank's MP curve ($r = \bar{r} + \lambda \pi$):
                </p>
                <div class="formula-box">
                    $$Y = \bar{A} - b(\bar{r} + \lambda \pi) = [\bar{A} - b\bar{r}] - (b\lambda)\pi$$
                    $$\text{Example: If } Y = 12 - 2r \text{ and } r = 0.5 + 0.25\pi \implies Y = 12 - 2(0.5 + 0.25\pi) = 11 - 0.5\pi$$
                </div>
                <p>
                    This confirms an inverse relationship between inflation $\pi$ and real output $Y$, establishing the <strong>downward-sloping Aggregate Demand (AD) curve</strong> in modern monetary frameworks.
                </p>
            </div>
        </div>

        <!-- ==================== TAB 2: MISSIONS ==================== -->
        <div id="ch10-missions" class="subtab-content">
            <div class="mission-briefing">
                <div class="briefing-tag">TACTICAL EVALUATION // CH10 EXAM MISSIONS</div>
                <h3>IS-LM Numerical Deployments & Central Bank Case Studies</h3>
                <p>Solve the following official examination problems derived from the RBI Bulletin and End-Semester Archives.</p>
            </div>

            <!-- MISSION 10.1 -->
            <div class="intel-card">
                <div class="mission-status-bar">
                    <span class="difficulty-pill pill-hard">LEVEL: ADVANCED NUMERICAL</span>
                    <span class="mission-id">MISSION 007-10.1</span>
                </div>
                <h4>Official RBI Bulletin Case Study: Baseline General Equilibrium</h4>
                <p>
                    An intelligence dispatch from the Reserve Bank of India research bureau models the macroeconomy with the following structural behavioral equations:
                </p>
                <div class="formula-box">
                    $$IS_0: Y = 4000 - 100r$$
                    $$LM_0: Y = 2000 + 100r$$
                    $$I_0: I = 1000 - 40r$$
                </div>
                <p><strong>Your Mission Directives:</strong></p>
                <ol style="margin-left:20px; line-height:1.7;">
                    <li>Calculate the simultaneous equilibrium interest rate ($r^*$) and national income ($Y^*$).</li>
                    <li>Calculate the equilibrium level of private corporate investment ($I^*$).</li>
                </ol>

                <div class="hint-container">
                    <button class="hint-btn" onclick="toggleHint('h10-1-1')">DECRYPT HINT 1: Equilibrium Principle</button>
                    <div id="h10-1-1" class="hint-text">Equate $Y_{IS} = Y_{LM}$ to solve for the single market-clearing interest rate $r^*$.</div>
                    <button class="hint-btn" onclick="toggleHint('h10-1-2')">DECRYPT HINT 2: Substitution</button>
                    <div id="h10-1-2" class="hint-text">$4000 - 100r = 2000 + 100r \implies 200r = 2000 \implies r = 10\%$. Substitute into $Y$ and $I$.</div>
                </div>
                <button class="action-btn" onclick="revealSolution('s10-1')">CONFIRM TARGET IDENTIFICATION // REVEAL SOLUTION</button>
<div id="s10-1" class="solution-card">
                <div class="mission-status-bar">
                    <span class="difficulty-pill pill-hard">TARGET 10.1: BASELINE IS-LM EQUILIBRIUM</span>
                    <span class="mission-id">VERIFIED BY Q-BRANCH</span>
                </div>
                <ol class="step-list">
                    <li class="step-item">
                        <div class="step-title">STEP 1: MISSION BRIEF</div>
                        <p>Locate the baseline simultaneous equilibrium values for interest rate ($r^*$), national income ($Y^*$), and private investment ($I^*$).</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 2: INTELLIGENCE EXTRACTION</div>
                        <p>$IS_0: Y = 4000 - 100r$, $LM_0: Y = 2000 + 100r$, $I_0: I = 1000 - 40r$.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 3: FORMULA SELECTION</div>
                        <p>Simultaneous Equilibrium condition: $Y_{IS} = Y_{LM}$.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 4: EXECUTION</div>
                        <p>
                            $$4000 - 100r = 2000 + 100r$$
                            $$200r = 2000 \implies r^* = 10\%$$
                            Substitute $r^* = 10$ into $IS_0$:
                            $$Y^* = 4000 - 100(10) = 4000 - 1000 = 3000$$
                            (Verification with $LM_0$: $Y^* = 2000 + 100(10) = 3000$).<br>
                            Substitute $r^* = 10$ into the investment function:
                            $$I^* = 1000 - 40(10) = 1000 - 400 = 600$$
                        </p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 5: GRAPHICAL ANALYSIS</div>
                        <p>The downward-sloping $IS_0$ intersects the upward-sloping $LM_0$ at the unique coordinate $(Y=3000, r=10\%)$. Both the goods and money markets clear with zero unplanned inventories and zero excess cash balances.</p>

                        <div class="solution-svg-diagram">
                            <svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
                                <rect width="500" height="240" fill="#08090d" rx="4"/>
                                <line x1="40" y1="200" x2="470" y2="200" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                                <line x1="50" y1="210" x2="50" y2="20" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                                <text x="470" y="222" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" text-anchor="end">OUTPUT (Y)</text>
                                <text x="25" y="30" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" transform="rotate(-90 25,30)" text-anchor="end">RATE (r %)</text>
                                <line x1="100" y1="50" x2="400" y2="190" stroke="#38bdf8" stroke-width="2.5"/>
                                <text x="405" y="195" fill="#38bdf8" font-family="var(--font-mono)" font-size="11" font-weight="700">IS₀ (Y = 4000 - 100r)</text>
                                <line x1="100" y1="190" x2="400" y2="50" stroke="#f59e0b" stroke-width="2.5"/>
                                <text x="405" y="50" fill="#f59e0b" font-family="var(--font-mono)" font-size="11" font-weight="700">LM₀ (Y = 2000 + 100r)</text>
                                <line x1="50" y1="120" x2="250" y2="120" stroke="rgba(255,255,255,0.3)" stroke-dasharray="3,3"/>
                                <line x1="250" y1="120" x2="250" y2="200" stroke="rgba(255,255,255,0.3)" stroke-dasharray="3,3"/>
                                <text x="42" y="124" fill="#38bdf8" font-family="var(--font-mono)" font-size="10" text-anchor="end">r* = 10%</text>
                                <text x="250" y="214" fill="#38bdf8" font-family="var(--font-mono)" font-size="10" text-anchor="middle">Y* = 3000</text>
                                <circle cx="250" cy="120" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="250" cy="120" r="2.5" fill="#d92534"/>
                                <line x1="238" y1="120" x2="262" y2="120" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="250" y1="108" x2="250" y2="132" stroke="#d92534" stroke-width="1.2"/>
                                <text x="260" y="114" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₀ (3000, 10%)</text>
                            </svg>
                            <span class="solution-svg-caption">FIGURE 10.1: BASELINE GENERAL EQUILIBRIUM AT E₀</span>
                        </div>

                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 6: ECONOMIC INTERPRETATION</div>
                        <p>At an interest rate of 10%, planned aggregate expenditure matches output of 3,000, and corporate entities demand 600 units of capital goods. The financial market equilibrates money demand with money supply.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 7: TARGET CONFIRMATION</div>
                        <div class="formula-box">
                            $$\mathbf{r^* = 10\%, \quad Y^* = 3000, \quad I^* = 600}$$
                        </div>
                    </li>
                </ol>
            </div>
            </div>

            <!-- MISSION 10.2 -->
            <div class="intel-card">
                <div class="mission-status-bar">
                    <span class="difficulty-pill pill-hard">LEVEL: NUMERICAL SHOCK</span>
                    <span class="mission-id">MISSION 007-10.2</span>
                </div>
                <h4>RBI Bulletin Part 2: Monetary Tightening Transmission</h4>
                <p>
                    To curb inflationary momentum, the Central Bank executes an open market sale of government securities, contracting the money supply such that the new LM curve becomes:
                </p>
                <div class="formula-box">
                    $$LM_1: Y = 1600 + 100r \quad (\text{with } IS_0: Y = 4000 - 100r)$$
                </div>
                <p><strong>Your Mission Directives:</strong></p>
                <ol style="margin-left:20px; line-height:1.7;">
                    <li>Compute the new equilibrium interest rate ($r_1^*$) and national output ($Y_1^*$).</li>
                    <li>Determine the new level of private investment ($I_1^*$).</li>
                    <li>Compute the exact amount of private investment crowded out or curtailed by the monetary contraction.</li>
                </ol>
                <div class="hint-container">
                    <button class="hint-btn" onclick="toggleHint('h10-2-1')">DECRYPT HINT 1</button>
                    <div id="h10-2-1" class="hint-text">Set $4000 - 100r = 1600 + 100r$. Solve for $r$, then compute $I = 1000 - 40r$.</div>
                </div>
                <button class="action-btn" onclick="revealSolution('s10-2')">CONFIRM TARGET IDENTIFICATION // REVEAL SOLUTION</button>
<div id="s10-2" class="solution-card">
                <div class="mission-status-bar">
                    <span class="difficulty-pill pill-hard">TARGET 10.2: MONETARY CONTRACTION</span>
                    <span class="mission-id">VERIFIED BY Q-BRANCH</span>
                </div>
                <ol class="step-list">
                    <li class="step-item">
                        <div class="step-title">STEP 1: MISSION BRIEF</div>
                        <p>Quantify the macroeconomic impact of an open market sale shifting the LM curve to $LM_1: Y = 1600 + 100r$.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 2: INTELLIGENCE EXTRACTION</div>
                        <p>$IS_0: Y = 4000 - 100r$, $LM_1: Y = 1600 + 100r$, Baseline $I_0^* = 600$.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 3: FORMULA SELECTION</div>
                        <p>Equilibrium condition: $Y_{IS0} = Y_{LM1}$. Investment crowding out: $\Delta I = I_1^* - I_0^*$.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 4: EXECUTION</div>
                        <p>
                            $$4000 - 100r = 1600 + 100r$$
                            $$200r = 2400 \implies r_1^* = 12\%$$
                            Substitute into $IS_0$:
                            $$Y_1^* = 4000 - 100(12) = 2800$$
                            Substitute into investment function:
                            $$I_1^* = 1000 - 40(12) = 1000 - 480 = 520$$
                            Investment reduction:
                            $$\Delta I = 520 - 600 = -80$$
                        </p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 5: GRAPHICAL ANALYSIS</div>
                        <p>$LM_0$ shifts leftward/upward to $LM_1$. The economy moves upward-left along $IS_0$ from $(3000, 10\%)$ to $(2800, 12\%)$. Output contracts while interest rates rise.</p>

                        <div class="solution-svg-diagram">
                            <svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
                                <rect width="500" height="240" fill="#08090d" rx="4"/>
                                <line x1="40" y1="200" x2="470" y2="200" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                                <line x1="50" y1="210" x2="50" y2="20" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                                <text x="470" y="222" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" text-anchor="end">OUTPUT (Y)</text>
                                <text x="25" y="30" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" transform="rotate(-90 25,30)" text-anchor="end">RATE (r %)</text>
                                <line x1="100" y1="50" x2="400" y2="190" stroke="#38bdf8" stroke-width="2.5"/>
                                <text x="405" y="195" fill="#38bdf8" font-family="var(--font-mono)" font-size="11" font-weight="700">IS₀</text>
                                <line x1="130" y1="190" x2="430" y2="50" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <text x="435" y="50" fill="#f59e0b" font-family="var(--font-mono)" font-size="10">LM₀</text>
                                <line x1="70" y1="190" x2="370" y2="50" stroke="#f59e0b" stroke-width="2.5"/>
                                <text x="375" y="50" fill="#f59e0b" font-family="var(--font-mono)" font-size="11" font-weight="700">LM₁ (Tightening)</text>
                                <line x1="280" y1="120" x2="220" y2="120" stroke="#f59e0b" stroke-width="1.8"/>
                                <polygon points="220,116 212,120 220,124" fill="#f59e0b"/>
                                <circle cx="280" cy="134" r="5" fill="none" stroke="rgba(255,255,255,0.5)" stroke-width="1.5"/>
                                <text x="288" y="132" fill="rgba(255,255,255,0.6)" font-family="var(--font-mono)" font-size="9">E₀(3000, 10%)</text>
                                <circle cx="220" cy="106" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="220" cy="106" r="2.5" fill="#d92534"/>
                                <line x1="208" y1="106" x2="232" y2="106" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="220" y1="94" x2="220" y2="118" stroke="#d92534" stroke-width="1.2"/>
                                <text x="230" y="100" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₁ (2800, 12%)</text>
                                <line x1="50" y1="106" x2="220" y2="106" stroke="#d92534" stroke-dasharray="3,3"/>
                                <line x1="220" y1="106" x2="220" y2="200" stroke="#d92534" stroke-dasharray="3,3"/>
                                <text x="42" y="110" fill="#f59e0b" font-family="var(--font-mono)" font-size="10" text-anchor="end">r₁* = 12%</text>
                                <text x="220" y="214" fill="#f59e0b" font-family="var(--font-mono)" font-size="10" text-anchor="middle">Y₁* = 2800</text>
                            </svg>
                            <span class="solution-svg-caption">FIGURE 10.2: MONETARY CONTRACTION SHIFT (LM₀ → LM₁)</span>
                        </div>

                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 6: ECONOMIC INTERPRETATION</div>
                        <p>Central bank contraction of real money supply induces excess demand for money. Commercial entities liquidate bonds, driving interest rates up from 10% to 12%. Higher capital costs discourage private capital projects, shrinking investment by 80 units and compressing national income by 200 units.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 7: TARGET CONFIRMATION</div>
                        <div class="formula-box">
                            $$\mathbf{r_1^* = 12\%, \quad Y_1^* = 2800, \quad I_1^* = 520, \quad \text{Investment Reduction} = 80 \text{ units}}$$
                        </div>
                    </li>
                </ol>
            </div>
            </div>

            <!-- MISSION 10.3 -->
            <div class="intel-card">
                <div class="mission-status-bar">
                    <span class="difficulty-pill pill-hard">LEVEL: CROWDING OUT QUANTIFICATION</span>
                    <span class="mission-id">MISSION 007-10.3</span>
                </div>
                <h4>RBI Bulletin Part 3: Sovereign Infrastructure Spending & Crowding Out</h4>
                <p>
                    Starting from the initial baseline ($IS_0$ and $LM_0$), the government embarks on a major national highway modernization project, boosting autonomous spending. The IS curve shifts rightward to:
                </p>
                <div class="formula-box">
                    $$IS_1: Y = 4600 - 100r \quad (\text{with } LM_0: Y = 2000 + 100r)$$
                </div>
                <p><strong>Your Mission Directives:</strong></p>
                <ol style="margin-left:20px; line-height:1.7;">
                    <li>Calculate the new equilibrium interest rate ($r_2^*$) and national income ($Y_2^*$).</li>
                    <li>Calculate private investment ($I_2^*$) under this fiscal expansion.</li>
                    <li>Quantify the exact amount of private investment crowded out compared to the baseline $I_0^* = 600$.</li>
                    <li>Trace the economic transmission mechanism responsible for this crowding out.</li>
                </ol>
                <div class="hint-container">
                    <button class="hint-btn" onclick="toggleHint('h10-3-1')">DECRYPT HINT 1</button>
                    <div id="h10-3-1" class="hint-text">$4600 - 100r = 2000 + 100r \implies 200r = 2600 \implies r = 13\%$. Substitute to find $Y$ and $I$.</div>
                </div>
                <button class="action-btn" onclick="revealSolution('s10-3')">CONFIRM TARGET IDENTIFICATION // REVEAL SOLUTION</button>
<div id="s10-3" class="solution-card">
                <div class="mission-status-bar">
                    <span class="difficulty-pill pill-hard">TARGET 10.3: FISCAL EXPANSION & CROWDING OUT</span>
                    <span class="mission-id">VERIFIED BY Q-BRANCH</span>
                </div>
                <ol class="step-list">
                    <li class="step-item">
                        <div class="step-title">STEP 1: MISSION BRIEF</div>
                        <p>Calculate equilibrium values and private investment crowding out following fiscal expansion to $IS_1: Y = 4600 - 100r$.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 2: INTELLIGENCE EXTRACTION</div>
                        <p>$IS_1: Y = 4600 - 100r$, $LM_0: Y = 2000 + 100r$, Baseline $I_0^* = 600$, $r_0^* = 10\%$.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 3: FORMULA SELECTION</div>
                        <p>Equilibrium condition: $Y_{IS1} = Y_{LM0}$. Crowding out: $Crowding\_Out = I_0^* - I_2^*$.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 4: EXECUTION</div>
                        <p>
                            $$4600 - 100r = 2000 + 100r$$
                            $$200r = 2600 \implies r_2^* = 13\%$$
                            Substitute into $LM_0$:
                            $$Y_2^* = 2000 + 100(13) = 3300$$
                            Substitute into investment function:
                            $$I_2^* = 1000 - 40(13) = 1000 - 520 = 480$$
                            Crowding-out calculation:
                            $$I_0^* - I_2^* = 600 - 480 = 120 \text{ units}$$
                        </p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 5: GRAPHICAL ANALYSIS</div>
                        <p>$IS_0$ shifts rightward to $IS_1$ by 600 units horizontally. However, the economy moves upward-right along $LM_0$ to $(3300, 13\%)$. The interest rate spikes by 300 basis points.</p>

                        <div class="solution-svg-diagram">
                            <svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
                                <rect width="500" height="240" fill="#08090d" rx="4"/>
                                <line x1="40" y1="200" x2="470" y2="200" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                                <line x1="50" y1="210" x2="50" y2="20" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                                <text x="470" y="222" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" text-anchor="end">OUTPUT (Y)</text>
                                <text x="25" y="30" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" transform="rotate(-90 25,30)" text-anchor="end">RATE (r %)</text>
                                <line x1="80" y1="190" x2="420" y2="50" stroke="#f59e0b" stroke-width="2.5"/>
                                <text x="425" y="50" fill="#f59e0b" font-family="var(--font-mono)" font-size="11" font-weight="700">LM₀</text>
                                <line x1="80" y1="50" x2="360" y2="190" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <text x="365" y="195" fill="#38bdf8" font-family="var(--font-mono)" font-size="10">IS₀</text>
                                <line x1="160" y1="50" x2="440" y2="190" stroke="#38bdf8" stroke-width="2.5"/>
                                <text x="445" y="195" fill="#38bdf8" font-family="var(--font-mono)" font-size="11" font-weight="700">IS₁ (ΔG > 0)</text>
                                <circle cx="220" cy="132" r="5" fill="none" stroke="rgba(255,255,255,0.5)" stroke-width="1.5"/>
                                <text x="180" y="145" fill="rgba(255,255,255,0.6)" font-family="var(--font-mono)" font-size="9">E₀(3000, 10%)</text>
                                <circle cx="300" cy="99" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="300" cy="99" r="2.5" fill="#d92534"/>
                                <line x1="288" y1="99" x2="312" y2="99" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="300" y1="87" x2="300" y2="111" stroke="#d92534" stroke-width="1.2"/>
                                <text x="310" y="95" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₂ (3300, 13%)</text>
                                <circle cx="360" cy="132" r="4" fill="none" stroke="#ef4444" stroke-width="1.5"/>
                                <text x="360" y="145" fill="#ef4444" font-family="var(--font-mono)" font-size="9" text-anchor="middle">Y_Keynes (3600)</text>
                                <line x1="300" y1="185" x2="360" y2="185" stroke="#ef4444" stroke-width="1.5"/>
                                <text x="330" y="178" fill="#ef4444" font-family="var(--font-mono)" font-size="8" text-anchor="middle">CROWDED OUT (ΔI = -120)</text>
                            </svg>
                            <span class="solution-svg-caption">FIGURE 10.3: FISCAL EXPANSION & PRIVATE INVESTMENT CROWDING OUT</span>
                        </div>

                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 6: ECONOMIC INTERPRETATION</div>
                        <p>
                            <strong>Transmission Mechanism of Crowding Out:</strong><br>
                            1. Higher sovereign spending ($\Delta G$) initially boosts aggregate expenditure and income ($\Delta Y$).<br>
                            2. Rising income triggers heightened transactional demand for liquidity ($M^d \uparrow$).<br>
                            3. Because the central bank holds money supply constant along $LM_0$, agents sell bonds to obtain transactions balances, crushing bond prices.<br>
                            4. Interest rates climb from 10% to 13%.<br>
                            5. Elevated financing costs force private corporations to cancel capital expenditure, causing investment to fall from 600 to 480 (120 units crowded out).<br>
                            6. Hence, output rises to only 3300 rather than 3600 (the full Keynesian multiplier output).
                        </p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 7: TARGET CONFIRMATION</div>
                        <div class="formula-box">
                            $$\mathbf{r_2^* = 13\%, \quad Y_2^* = 3300, \quad I_2^* = 480, \quad \text{Crowded-Out Investment} = 120 \text{ units}}$$
                        </div>
                    </li>
                </ol>
            </div>
            </div>

            <!-- MISSION 10.4 -->
            <div class="intel-card">
                <div class="mission-status-bar">
                    <span class="difficulty-pill pill-exam">LEVEL: POLICY COORDINATION</span>
                    <span class="mission-id">MISSION 007-10.4</span>
                </div>
                <h4>RBI Bulletin Part 4: Accommodative Policy Mix (Zero Crowding Out)</h4>
                <p>
                    Recognizing that higher interest rates damp private investment, the Treasury and Central Bank agree on a coordinated policy package. While government infrastructure spending pushes the IS curve to $IS_1: Y = 4600 - 100r$, the Central Bank accommodates this expansion by increasing the money supply to $LM_2: Y = 2600 + 100r$.
                </p>
                <p><strong>Your Mission Directives:</strong></p>
                <ol style="margin-left:20px; line-height:1.7;">
                    <li>Compute the resulting equilibrium interest rate ($r_3^*$) and output ($Y_3^*$).</li>
                    <li>Calculate private investment ($I_3^*$) and compare it with the initial baseline.</li>
                    <li>Explain why monetary accommodation neutralizes the crowding-out effect.</li>
                </ol>
                <div class="hint-container">
                    <button class="hint-btn" onclick="toggleHint('h10-4-1')">DECRYPT HINT 1</button>
                    <div id="h10-4-1" class="hint-text">$4600 - 100r = 2600 + 100r \implies 200r = 2000 \implies r = 10\%$. Notice $r$ returns to baseline!</div>
                </div>
                <button class="action-btn" onclick="revealSolution('s10-4')">CONFIRM TARGET IDENTIFICATION // REVEAL SOLUTION</button>
<div id="s10-4" class="solution-card">
                <div class="mission-status-bar">
                    <span class="difficulty-pill pill-exam">TARGET 10.4: COORDINATED FISCAL-MONETARY MIX</span>
                    <span class="mission-id">VERIFIED BY Q-BRANCH</span>
                </div>
                <ol class="step-list">
                    <li class="step-item">
                        <div class="step-title">STEP 1: MISSION BRIEF</div>
                        <p>Evaluate macroeconomic equilibrium under simultaneous fiscal stimulus ($IS_1$) and monetary accommodation ($LM_2$).</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 2: INTELLIGENCE EXTRACTION</div>
                        <p>$IS_1: Y = 4600 - 100r$, $LM_2: Y = 2600 + 100r$, $I = 1000 - 40r$.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 3: FORMULA SELECTION</div>
                        <p>Simultaneous equilibrium: $Y_{IS1} = Y_{LM2}$.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 4: EXECUTION</div>
                        <p>
                            $$4600 - 100r = 2600 + 100r$$
                            $$200r = 2000 \implies r_3^* = 10\%$$
                            Substitute into $IS_1$:
                            $$Y_3^* = 4600 - 100(10) = 3600$$
                            Substitute into investment:
                            $$I_3^* = 1000 - 40(10) = 600$$
                            Crowding-out:
                            $$I_0^* - I_3^* = 600 - 600 = 0 \text{ units!}$$
                        </p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 5: GRAPHICAL ANALYSIS</div>
                        <p>$IS_0$ shifts right to $IS_1$, and $LM_0$ shifts right to $LM_2$ by exactly the same magnitude. The new intersection is at $(3600, 10\%)$—interest rates remain unchanged at 10%.</p>

                        <div class="solution-svg-diagram">
                            <svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
                                <rect width="500" height="240" fill="#08090d" rx="4"/>
                                <line x1="40" y1="200" x2="470" y2="200" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                                <line x1="50" y1="210" x2="50" y2="20" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                                <text x="470" y="222" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" text-anchor="end">OUTPUT (Y)</text>
                                <text x="25" y="30" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" transform="rotate(-90 25,30)" text-anchor="end">RATE (r %)</text>
                                <line x1="80" y1="50" x2="360" y2="190" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <line x1="160" y1="50" x2="440" y2="190" stroke="#38bdf8" stroke-width="2.5"/>
                                <text x="445" y="195" fill="#38bdf8" font-family="var(--font-mono)" font-size="11" font-weight="700">IS₁ (ΔG > 0)</text>
                                <line x1="80" y1="190" x2="380" y2="50" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <line x1="160" y1="190" x2="460" y2="50" stroke="#f59e0b" stroke-width="2.5"/>
                                <text x="465" y="50" fill="#f59e0b" font-family="var(--font-mono)" font-size="11" font-weight="700">LM₂ (Accommodative)</text>
                                <circle cx="220" cy="132" r="5" fill="none" stroke="rgba(255,255,255,0.5)" stroke-width="1.5"/>
                                <text x="175" y="128" fill="rgba(255,255,255,0.6)" font-family="var(--font-mono)" font-size="9">E₀(3000, 10%)</text>
                                <line x1="220" y1="132" x2="340" y2="132" stroke="#10b981" stroke-width="2" stroke-dasharray="3,3"/>
                                <circle cx="340" cy="132" r="8" fill="none" stroke="#10b981" stroke-width="2"/>
                                <circle cx="340" cy="132" r="3" fill="#10b981"/>
                                <line x1="328" y1="132" x2="352" y2="132" stroke="#10b981" stroke-width="1.2"/>
                                <line x1="340" y1="120" x2="340" y2="144" stroke="#10b981" stroke-width="1.2"/>
                                <text x="350" y="125" fill="#10b981" font-family="var(--font-mono)" font-size="11" font-weight="700">E₃ (3600, 10%) ZERO CROWDING OUT</text>
                                <line x1="50" y1="132" x2="340" y2="132" stroke="rgba(255,255,255,0.2)" stroke-dasharray="2,2"/>
                                <line x1="340" y1="132" x2="340" y2="200" stroke="#10b981" stroke-dasharray="2,2"/>
                                <text x="42" y="136" fill="#10b981" font-family="var(--font-mono)" font-size="10" text-anchor="end">r* = 10%</text>
                                <text x="340" y="214" fill="#10b981" font-family="var(--font-mono)" font-size="10" text-anchor="middle">Y* = 3600</text>
                            </svg>
                            <span class="solution-svg-caption">FIGURE 10.4: COORDINATED FISCAL-MONETARY POLICY MIX</span>
                        </div>

                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 6: ECONOMIC INTERPRETATION</div>
                        <p>By injecting liquidity in tandem with the government's capex push, the Central Bank accommodates the surge in transactional money demand without allowing bond prices to fall. Market interest rates remain locked at 10%, private corporate investment is 100% shielded from crowding out, and the economy achieves its full potential Keynesian expansion to $Y=3600$.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">STEP 7: TARGET CONFIRMATION</div>
                        <div class="formula-box">
                            $$\mathbf{r_3^* = 10\%, \quad Y_3^* = 3600, \quad I_3^* = 600, \quad \text{Crowding Out} = 0}$$
                        </div>
                    </li>
                </ol>
            </div>
            </div>

            <!-- MISSION 10.5 -->
            <div class="intel-card">
                <div class="mission-status-bar">
                    <span class="difficulty-pill pill-exam">LEVEL: COMPREHENSIVE CASE STUDY</span>
                    <span class="mission-id">MISSION 007-10.5</span>
                </div>
                <h4>Tactical Case Study: The Bank of Japan & The Liquidity Trap (6 Directives)</h4>
                <p>
                    Following the 1990 asset bubble collapse, Japan entered decades of economic stagnation. The Bank of Japan lowered the policy rate to 0%, but commercial lending and private investment failed to respond vigorously. Answer the following 6 examination questions:
                </p>
                <ol style="margin-left:20px; line-height:1.7;">
                    <li>Describe the exact economic condition known as the <em>Liquidity Trap</em> and illustrate its LM curve.</li>
                    <li>Why did lowering nominal interest rates to the Zero Lower Bound fail to stimulate aggregate demand?</li>
                    <li>Explain the structural balance-sheet causes of Japan's corporate savings behavior during this period.</li>
                    <li>What unconventional tools did the Bank of Japan deploy under Quantitative and Qualitative Easing (QQE)?</li>
                    <li>Why was fiscal stimulus effective in expanding output, and what were its consequences for Japanese sovereign debt?</li>
                    <li>What critical lessons does Japan's experience offer for central banks operating near the ZLB?</li>
                </ol>
                <button class="action-btn" onclick="revealSolution('s10-5')">CONFIRM TARGET IDENTIFICATION // REVEAL SOLUTION</button>
<div id="s10-5" class="solution-card">
                <div class="mission-status-bar">
                    <span class="difficulty-pill pill-exam">TARGET 10.5: JAPAN & LIQUIDITY TRAP DEBRIEF</span>
                    <span class="mission-id">VERIFIED BY Q-BRANCH</span>
                </div>
                <ol class="step-list">
                    <li class="step-item">
                        <div class="step-title">1. NATURE OF THE LIQUIDITY TRAP & LM SHAPE</div>
                        <p>A liquidity trap is a pathological regime where nominal interest rates hit the Zero Lower Bound (ZLB). The speculative demand for money becomes infinitely interest-elastic ($h \to \infty$), rendering the <strong>LM curve completely horizontal</strong>. People are indifferent between holding cash and holding zero-yielding short-term government debt.</p>

                        <div class="solution-svg-diagram">
                            <svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
                                <rect width="500" height="240" fill="#08090d" rx="4"/>
                                <line x1="40" y1="200" x2="470" y2="200" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                                <line x1="50" y1="210" x2="50" y2="20" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                                <text x="470" y="222" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" text-anchor="end">OUTPUT (Y)</text>
                                <text x="25" y="30" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" transform="rotate(-90 25,30)" text-anchor="end">RATE (r %)</text>
                                <path d="M 50 180 L 250 180 L 440 60" fill="none" stroke="#f59e0b" stroke-width="3"/>
                                <text x="445" y="60" fill="#f59e0b" font-family="var(--font-mono)" font-size="11" font-weight="700">LM (Flat at ZLB)</text>
                                <line x1="70" y1="90" x2="210" y2="200" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <text x="215" y="200" fill="#38bdf8" font-family="var(--font-mono)" font-size="10">IS₀</text>
                                <line x1="140" y1="90" x2="280" y2="200" stroke="#38bdf8" stroke-width="2.5"/>
                                <text x="285" y="200" fill="#38bdf8" font-family="var(--font-mono)" font-size="11" font-weight="700">IS₁</text>
                                <circle cx="178" cy="180" r="6" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="178" cy="180" r="2" fill="#d92534"/>
                                <text x="186" y="174" fill="#ffffff" font-family="var(--font-mono)" font-size="10" font-weight="700">E₀</text>
                                <circle cx="248" cy="180" r="8" fill="none" stroke="#10b981" stroke-width="2"/>
                                <circle cx="248" cy="180" r="3" fill="#10b981"/>
                                <text x="256" y="174" fill="#10b981" font-family="var(--font-mono)" font-size="11" font-weight="700">E₁ (Full k_G Power)</text>
                                <text x="60" y="172" fill="#f59e0b" font-family="var(--font-mono)" font-size="9">r_min ≈ 0%</text>
                            </svg>
                            <span class="solution-svg-caption">FIGURE 10.5: LIQUIDITY TRAP & FISCAL MULTIPLIER EFFICACY</span>
                        </div>

                    </li>
                    <li class="step-item">
                        <div class="step-title">2. FAILURE OF MONETARY POLICY AT THE ZLB</div>
                        <p>Conventional open market operations expand the money supply by buying bonds. But at the ZLB, bond yields cannot drop below zero. Injecting reserves simply increases bank excess liquidity; banks hoard cash rather than lending, and borrowing costs cannot fall further. Transmission to investment and consumption breaks down completely ($\Delta M \implies \Delta r = 0 \implies \Delta I = 0$).</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">3. STRUCTURAL CAUSES: BALANCE-SHEET RECESSION</div>
                        <p>As analyzed by Richard Koo, Japanese corporations were not profit-maximizing; they were <strong>debt-minimizing</strong>. The collapse of commercial real estate and equity values left corporate balance sheets deeply insolvent. Cash flows were channeled into repaying debt rather than borrowing to invest, rendering lower interest rates completely ineffective.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">4. UNCONVENTIONAL TOOLS UNDER QQE & ABENOMICS</div>
                        <p>Central banks deployed: (a) <strong>Quantitative Easing (QE)</strong>—massive balance sheet expansion purchasing Japanese Government Bonds (JGBs); (b) <strong>Qualitative Easing</strong>—purchasing risky assets such as ETFs and J-REITs to suppress risk premia; (c) <strong>Negative Interest Rate Policy (NIRP)</strong> (-0.1% on excess reserves); and (d) <strong>Yield Curve Control (YCC)</strong>—pegging 10-year sovereign yields at approximately 0% to shape long-term borrowing rates.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">5. FISCAL POLICY EFFICACY & SOVEREIGN DEBT</div>
                        <p>Because the LM curve was horizontal, fiscal policy suffered <strong>zero crowding out</strong>. Government construction and infrastructure spending generated genuine demand and sustained GDP, preventing a full-scale 1930s-style depression. However, sustained fiscal deficits accumulated Japan's gross government debt to over 260% of GDP, the highest in the developed world.</p>
                    </li>
                    <li class="step-item">
                        <div class="step-title">6. LESSONS FOR CONTEMPORARY CENTRAL BANKING</div>
                        <p>1. Central banks must act preemptively and aggressively before inflation expectations become entrenched below zero.<br>2. Escaping a liquidity trap requires synchronized monetary-fiscal coordination.<br>3. Structural reforms and banking system recapitalization are mandatory—monetary alchemy alone cannot cure balance-sheet insolvency.</p>
                    </li>
                </ol>
            </div>
        </div>
    </div>

    <!-- ==================== TAB 3: TARGETS ==================== -->
        <div id="ch10-targets" class="subtab-content">
            <div class="mission-briefing">
                <div class="briefing-tag">TARGET DEBRIEF // OFFICIAL 7-STEP PROTOCOL</div>
                <h3>Standard Operating Procedure Solutions: IS-LM General Equilibrium</h3>
                <p>All 5 mission target debriefings are fully decrypted and equipped with technical equilibrium diagrams. You can view each solution directly beneath its problem in the <strong>Combat Missions</strong> tab, or use the direct target conduits below:</p>
            </div>

            <div class="grid-2">
                <div class="intel-card">
                    <span class="difficulty-pill pill-hard">TARGET 10.1</span>
                    <h4>Baseline IS-LM Equilibrium ($E_0$)</h4>
                    <p>Equilibrium values: $r^* = 10\%$, $Y^* = 3000$, $I^* = 600$. Goods and money markets clear simultaneously with zero unplanned inventory accumulation.</p>
                    <button class="action-btn" onclick="switchSubTab(event, 'ch10-missions'); revealSolution('s10-1');">ACCESS TARGET 10.1 DEBRIEF</button>
                </div>

                <div class="intel-card">
                    <span class="difficulty-pill pill-hard">TARGET 10.2</span>
                    <h4>Monetary Contraction Transmission</h4>
                    <p>Open market bond sale shifts LM leftward: $r_1^* = 12\%$, $Y_1^* = 2800$, $I_1^* = 520$. Private investment is curtailed by 80 units due to higher borrowing costs.</p>
                    <button class="action-btn" onclick="switchSubTab(event, 'ch10-missions'); revealSolution('s10-2');">ACCESS TARGET 10.2 DEBRIEF</button>
                </div>

                <div class="intel-card">
                    <span class="difficulty-pill pill-hard">TARGET 10.3</span>
                    <h4>Fiscal Expansion & Private Crowding Out</h4>
                    <p>Infrastructure spending shifts IS rightward: $r_2^* = 13\%$, $Y_2^* = 3300$, $I_2^* = 480$. Exactly 120 units of private investment are crowded out ($600 - 480 = 120$).</p>
                    <button class="action-btn" onclick="switchSubTab(event, 'ch10-missions'); revealSolution('s10-3');">ACCESS TARGET 10.3 DEBRIEF</button>
                </div>

                <div class="intel-card">
                    <span class="difficulty-pill pill-exam">TARGET 10.4</span>
                    <h4>Accommodative Monetary-Fiscal Mix</h4>
                    <p>Coordinated policy package: Central bank accommodation locks interest rates at $r^* = 10\%$, expanding output to $Y^* = 3600$ with <strong>zero crowding out</strong>.</p>
                    <button class="action-btn" onclick="switchSubTab(event, 'ch10-missions'); revealSolution('s10-4');">ACCESS TARGET 10.4 DEBRIEF</button>
                </div>

                <div class="intel-card" style="grid-column: span 2;">
                    <span class="difficulty-pill pill-exam">TARGET 10.5</span>
                    <h4>Bank of Japan & Liquidity Trap Case Study</h4>
                    <p>6-directive evaluation of the Zero Lower Bound, balance-sheet recession dynamics, unconventional central banking (QQE, NIRP, YCC), and unconstrained fiscal multiplier efficacy.</p>
                    <button class="action-btn" onclick="switchSubTab(event, 'ch10-missions'); revealSolution('s10-5');">ACCESS TARGET 10.5 DEBRIEF</button>
                </div>
            </div>
        </div>
    </div>
</section>
'''

if __name__ == '__main__':
    print('Testing ch10 module length:', len(get_chapter_10()))
