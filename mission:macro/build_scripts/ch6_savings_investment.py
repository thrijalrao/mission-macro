# build_scripts/ch6_savings_investment.py
"""
Project 007: Chapter 6 — Savings and Investment in a Closed Economy
Exhaustive academic content strictly from Prof. Sana Tabassum lecture slides,
including the Loanable Funds & Saving-Investment Interactive Canvas Lab.
"""

def get_chapter_6():
    return r"""
<!-- CHAPTER 6: SAVINGS AND INVESTMENT IN A CLOSED ECONOMY -->
<div class="chapter-container" id="chapter-6">
  <a id="ch6" class="chapter-anchor"></a>
  <div class="chapter-header">
    <div class="ch-badge-group">
      <span class="ch-code-pill">DOSSIER 06 // INTEL-LOANABLE-FUNDS</span>
      <h2 class="ch-title">Chapter 6 — Savings & Investment in Closed Economies</h2>
    </div>
    <div class="chapter-actions">
      <button class="ch-mastery-btn" id="ch-mastery-badge-6" onclick="toggleProgressItem(6, 'training', {checked: true})">IN PROGRESS</button>
    </div>
  </div>

  <div class="chapter-nav-tabs">
    <button class="ch-tab-btn active" data-tab="all" onclick="switchChapterTab(6, 'all')">ALL INTEL</button>
    <button class="ch-tab-btn" data-tab="training" onclick="switchChapterTab(6, 'training')">TRAINING (THE BRIEFING)</button>
    <button class="ch-tab-btn" data-tab="missions" onclick="switchChapterTab(6, 'missions')">MISSIONS (ACTIVE OPS)</button>
    <button class="ch-tab-btn" data-tab="targets" onclick="switchChapterTab(6, 'targets')">TARGETS (DEBRIEFING)</button>
  </div>

  <div class="chapter-body">
    <!-- ==================== TRAINING ENVIRONMENT ==================== -->
    <div class="training-section">
      <div class="topic-card">
        <div class="topic-header">
          <h3 class="topic-title">6.1 The Consumption & Savings Architecture</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Unit 2, Slides 3-6</span>
        </div>
        <p class="content-lead">
          The foundation of Keynesian goods-market equilibrium rests on the behavioral relationship between household disposable income ($Y_d$), aggregate consumption ($C$), and national saving ($S$).
        </p>

        <h4 class="section-subtitle">The Consumption Function</h4>
        <p class="content-text">
          The <strong>Consumption Function</strong> expresses the functional relationship between aggregate household consumption and current disposable income:
        </p>
        <div class="formula-card">
          <div class="formula-card-title">Consumption Function Formulation</div>
          <div class="formula-math-display">
            C = C₀ + MPC × Y_d<br>
            [With real interest rate sensitivity: C = C₀ + MPC × (Y − T) − c × r]
          </div>
          <div class="formula-breakdown">
            <ul>
              <li><strong>Disposable Income ($Y_d$):</strong> Income available for spending after payment of net taxes: $Y_d = Y - T$.</li>
              <li><strong>Autonomous Consumption ($C_0$):</strong> Baseline subsistence spending that is <strong>independent of current disposable income</strong>. Even if $Y_d = 0$, survival spending always occurs (financed via dissaving, accumulated wealth, or credit). $C_0$ shifts when consumer confidence or credit access changes.</li>
              <li><strong>Marginal Propensity to Consume (MPC):</strong> The fraction of an extra unit of disposable income that is consumed: $\text{MPC} = \Delta C / \Delta Y_d$. Always $0 < \text{MPC} < 1$.</li>
              <li><strong>Keynes' Psychological Law of Consumption:</strong> <em>"Men are disposed, as a rule and on the average, to increase their consumption as their income increases, but not by as much as the increase in their income."</em> As income grows, consumption increases at a diminishing rate ($\text{MPC}$ falls), and savings rise!</li>
            </ul>
          </div>
        </div>

        <h4 class="section-subtitle">The Savings Function & Sectoral Balances</h4>
        <div class="formula-card">
          <div class="formula-card-title">Savings Function Formulation</div>
          <div class="formula-math-display">
            S = −C₀ + MPS × Y_d<br><br>
            MPC + MPS = 1.00
          </div>
          <div class="formula-breakdown">
            <ul>
              <li><strong>Marginal Propensity to Save (MPS):</strong> $\text{MPS} = \Delta S / \Delta Y_d = 1 - \text{MPC}$. Every rupee of disposable income is either consumed or saved!</li>
              <li><strong>Private Saving ($S_p$):</strong> Income saved by households: $S_p = Y - T - C$.</li>
              <li><strong>Government Saving ($S_g$):</strong> Net fiscal balance: $S_g = T - G$. When $T > G$, government saves (surplus); when $G > T$, government dissaves (deficit).</li>
              <li><strong>National Saving ($S$):</strong> Aggregate saving available to the economy:
                <br>$$S = S_p + S_g = (Y - T - C) + (T - G) = Y - C - G$$
              </li>
            </ul>
          </div>
        </div>
      </div>

      <div class="topic-card">
        <div class="topic-header">
          <a id="ch6-loanable-funds"></a>
          <h3 class="topic-title">6.2 The Investment Function & Goods Market Equilibrium</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Unit 2, Slides 7-9</span>
        </div>
        <p class="content-text">
          <strong>Planned Investment ($I$)</strong> represents total spending by businesses on newly produced capital goods (factories, equipment, tech infrastructure) to expand the economy's productive capacity.
        </p>

        <div class="formula-card">
          <div class="formula-card-title">Planned Investment Function</div>
          <div class="formula-math-display">
            I = I₀ − b × r
          </div>
          <div class="formula-breakdown">
            <ul>
              <li><strong>Autonomous Investment ($I_0$):</strong> Investment spending that is independent of interest rates, determined exogenously by business animal spirits, technological breakthroughs, and long-term optimism.</li>
              <li><strong>Real Interest Rate ($r$):</strong> The true cost of borrowing funds: $r = i - \pi$. A higher real interest rate raises hurdle rates for corporate projects:
                <br>$$r \uparrow \implies I \downarrow \quad \text{and} \quad r \downarrow \implies I \uparrow$$
              </li>
              <li><strong>Interest Sensitivity of Investment ($b$):</strong> Measures the responsiveness of investment to changes in borrowing costs: $b = |\Delta I / \Delta r|$. The larger $b$, the flatter the investment demand curve.</li>
            </ul>
          </div>
        </div>

        <h4 class="section-subtitle">Goods Market Equilibrium & The S = I Identity in a Closed Economy</h4>
        <p class="content-text">
          Goods market equilibrium requires that total production equals total demand:
        </p>
        <div class="step-math">
          Y = C + I + G &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(National Income Identity)<br>
          Subtract C + G from both sides:<br>
          Y − C − G = I<br>
          Since National Saving S = Y − C − G:<br>
          <strong>S = I &nbsp;&nbsp;(In a closed economy, Goods Market Equilibrium occurs where S = I)</strong>
        </div>
      </div>

      <!-- INTERACTIVE GRAPH LAB 2: LOANABLE FUNDS & READY RECKONER -->
      <div class="graph-canvas-box">
        <div class="lab-toolbar-header">
          <span class="lab-toolbar-badge">TACTICAL LAB 02 // LOANABLE FUNDS & SAVINGS-INVESTMENT SIMULATOR</span>
          <button class="graph-reset-btn" onclick="resetLoanableFundsGraph()" type="button" title="Reset Loanable Funds Simulation to Baseline">
            <span class="reset-icon">↺</span> RESET SIMULATION TO BASELINE
          </button>
        </div>
        <div class="graph-top-ctrls" style="margin-top:8px;">
          <div style="display:flex; align-items:center; gap:16px; flex-wrap:wrap; width:100%; justify-content:flex-start;">
            <div class="slider-group">
              <label for="lfSaveShift">SHIFT SAVING SUPPLY (ΔS):</label>
              <input type="range" id="lfSaveShift" min="-50" max="50" value="0" style="width:120px;">
            </div>
            <div class="slider-group">
              <label for="lfInvShift">SHIFT INVESTMENT DEMAND (ΔI):</label>
              <input type="range" id="lfInvShift" min="-50" max="50" value="0" style="width:120px;">
            </div>
          </div>
        </div>
        <div class="canvas-viewport-wrap">
          <canvas id="loanableFundsCanvas"></canvas>
        </div>
        <div class="graph-telemetry-readout">
          <div class="telemetry-item">REAL INTEREST RATE (r*): <span id="lfRReadout" style="color:var(--silver-100);">3.00%</span></div>
          <div class="telemetry-item">EQUILIBRIUM LOANABLE FUNDS (Q*): <span id="lfQReadout" style="color:var(--success-emerald);">1300 units</span></div>
          <div class="telemetry-item">READY RECKONER: <span id="lfReckonerReadout" style="color:var(--silver-300);">Baseline Equilibrium</span></div>
        </div>
      </div>

      <div class="topic-card">
        <div class="topic-header">
          <a id="ch6-ready-reckoner"></a>
          <h3 class="topic-title">6.3 Simultaneous Shifts in S & I: The Ready Reckoner</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Dedicated Deck on Simultaneous Shifts</span>
        </div>
        <p class="content-lead">
          When multiple macroeconomic shocks hit an economy simultaneously, saving supply and investment demand shift at the same time. The <strong>Ready Reckoner</strong> establishes the strict laws governing whether interest rates and loanable funds quantities are determinate or indeterminate.
        </p>

        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th>Scenario & Real-World Trigger</th>
                <th>Shift in Saving (S)</th>
                <th>Shift in Investment (I)</th>
                <th>Effect on Real Interest Rate (r)</th>
                <th>Effect on Loanable Funds (Q)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Scenario 1:</strong> Digital expansion + Precautionary saving boom</td>
                <td>Right →</td>
                <td>Right →</td>
                <td><strong style="color:var(--warning-amber);">INDETERMINATE</strong><br>(r↑ if ΔI > ΔS; r↓ if ΔS > ΔI)</td>
                <td><strong style="color:var(--success-emerald);">DETERMINATE: INCREASES (↑)</strong></td>
              </tr>
              <tr>
                <td><strong>Scenario 2:</strong> Income squeeze + Business pessimism</td>
                <td>Left ←</td>
                <td>Left ←</td>
                <td><strong style="color:var(--warning-amber);">INDETERMINATE</strong><br>(depends on relative shift sizes)</td>
                <td><strong style="color:var(--bond-crimson);">DETERMINATE: DECREASES (↓)</strong></td>
              </tr>
              <tr>
                <td><strong>Scenario 3:</strong> Rapid growth, high consumer optimism + capex boom</td>
                <td>Left ←<br>(C↑ so S↓)</td>
                <td>Right →<br>(strong sales optimism)</td>
                <td><strong style="color:var(--bond-crimson);">DETERMINATE: INCREASES (↑)</strong></td>
                <td><strong style="color:var(--warning-amber);">INDETERMINATE</strong><br>(forces pull Q in opposite directions)</td>
              </tr>
              <tr>
                <td><strong>Scenario 4:</strong> Major financial panic: Precautionary saving + capex freeze</td>
                <td>Right →<br>(fear induces saving)</td>
                <td>Left ←<br>(firms cancel plans)</td>
                <td><strong style="color:var(--success-emerald);">DETERMINATE: DECREASES (↓)</strong></td>
                <td><strong style="color:var(--warning-amber);">INDETERMINATE</strong><br>(forces pull Q in opposite directions)</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="intel-box key-intuition">
          <div class="intel-box-title">The Master Ready Reckoner Axiom</div>
          <p class="content-text" style="margin-bottom:6px;">
            <strong>1. S and I shift in the SAME direction:</strong> Both shifts push equilibrium quantity in the same direction, but exert opposing pressures on interest rates $\implies$ <strong>Quantity is DETERMINATE | Interest Rate is INDETERMINATE</strong>.
          </p>
          <p class="content-text" style="margin-bottom:0;">
            <strong>2. S and I shift in OPPOSITE directions:</strong> Both shifts push the interest rate in the same direction, but exert opposing pressures on loanable funds quantity $\implies$ <strong>Interest Rate is DETERMINATE | Quantity is INDETERMINATE</strong>.
          </p>
        </div>
      </div>

      <div class="topic-card" id="crowding-out-in" data-title="Crowding Out vs Crowding In">
        <a id="section-crowding-out-in"></a><a id="crowding-out"></a><a id="crowding-in"></a>
        <div class="topic-header">
          <h3 class="topic-title">6.4 Crowding Out vs Crowding In: Mechanisms & Context</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Unit 2, Slides 16-18</span>
        </div>
        <p class="content-text">
          A fundamental policy debate in macroeconomics centers on how government fiscal deficit spending affects private corporate investment:
        </p>

        <h4 class="section-subtitle">The Crowding-Out Mechanism (Near Full Employment)</h4>
        <p class="content-text">
          When an economy operates close to full employment ($Y \approx Y^*$), resources (labor and capital) are scarce. If the government launches large infrastructure spending financed by domestic borrowing:
        </p>
        <div class="step-math">
          G ↑ ⇒ Government Saving (S_g) ↓ ⇒ National Saving (S) ↓ ⇒ S curve shifts LEFT<br>
          ⇒ Excess demand for loanable funds ⇒ Real Interest Rate (r) RISES<br>
          ⇒ Private borrowing becomes expensive ⇒ Private Investment (I) FALLS (Crowding Out!)
        </div>

        <h4 class="section-subtitle">The Crowding-In Mechanism (During Slump / Recession)</h4>
        <p class="content-text">
          When an economy has substantial slack capacity, private firms are reluctant to invest due to weak logistics and poor demand. If the government increases productive capital expenditure on critical infrastructure (ports, highways, electricity networks):
        </p>
        <div class="step-math">
          Government Capital Expenditure ↑ ⇒ Logistics costs ↓ & Business operating efficiency ↑<br>
          ⇒ Expected future profitability of private projects ↑ ⇒ Desired Private Investment (I) shifts RIGHT<br>
          ⇒ If I shift outweighs the savings pressure ⇒ Private Investment RISES (Crowding In!)
        </div>

        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th>Dimension</th>
                <th>Crowding Out</th>
                <th>Crowding In</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Core Mechanism</strong></td>
                <td>Government borrowing reduces available loanable funds, driving $r \uparrow$ and shrinking private capex.</td>
                <td>Productive public infrastructure lowers corporate operating costs, boosting private investment profitability.</td>
              </tr>
              <tr>
                <td><strong>Saving Schedule ($S$)</strong></td>
                <td>$S$ shifts Left ($S_g \downarrow$).</td>
                <td>$S$ initially shifts Left, but long-run national income expansion replenishes savings.</td>
              </tr>
              <tr>
                <td><strong>Investment Schedule ($I$)</strong></td>
                <td>Movement upward along the static $I$ curve ($I \downarrow$).</td>
                <td>Autonomous shift RIGHT of the entire investment curve ($I \uparrow$).</td>
              </tr>
              <tr>
                <td><strong>Prevailing Condition</strong></td>
                <td><strong>Near full employment</strong>; tight domestic credit markets.</td>
                <td><strong>Severe recession / slack capacity</strong>; deficient private demand.</td>
              </tr>
              <tr>
                <td><strong>Final Outcome</strong></td>
                <td><strong>Private Investment FALLS ($I \downarrow$)</strong></td>
                <td><strong>Private Investment RISES ($I \uparrow$)</strong></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- ==================== MISSIONS ENVIRONMENT ==================== -->
    <div class="missions-section">
      <div class="mission-card">
        <div class="mission-top-bar">
          <span class="mission-level-badge level-1">LEVEL 1 // FOUNDATION</span>
          <span class="topic-ref-tag">Unit 2 Case Study 1 Novara</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 6.1: Novara Functional Derivations & Tech Surge</h3>
        <p class="mission-question">
          The following macroeconomic data is available for the economy of Novara:
          <br>• When household disposable income ($Y_d$) is ₹1,000 crore, consumption expenditure is ₹800 crore. When disposable income increases to ₹2,000 crore, consumption expenditure rises to ₹1,500 crore.
          <br>• When the real interest rate is 4%, planned investment is ₹720 crore. When the real interest rate rises to 6%, planned investment falls to ₹660 crore. Subsequently, improved production technology raises the expected profitability of capital, and firms increase planned investment by ₹200 crore at every real interest rate.
          <br>• The government announces a ₹300 crore expenditure on public infrastructure.
          <br><br>
          <strong>Your Operational Directives:</strong><br>
          a. Calculate the MPC, MPS, and autonomous consumption ($C_0$).<br>
          b. Derive the algebraic consumption function and saving function.<br>
          c. Determine the values of $I_0$ and $b$, and write the investment function before and after the technology shock.<br>
          d. Represent the increase in planned investment graphically and explain the interest rate response.<br>
          e. Calculate the change in national income resulting from the ₹300 crore infrastructure spending.
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h6_1_1')">Hint 1: MPC Math</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h6_1_2')">Hint 2: Investment b</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h6_1_3')">Hint 3: Multiplier</button>
          </div>
          <div class="hint-content-box" id="h6_1_1">
            <strong>Hint 1:</strong> $\text{MPC} = \Delta C / \Delta Y_d = (1,500 - 800) / (2,000 - 1,000) = 700 / 1,000 = 0.70$. $\text{MPS} = 0.30$.
          </div>
          <div class="hint-content-box" id="h6_1_2">
            <strong>Hint 2:</strong> $b = |\Delta I / \Delta r| = |(660 - 720) / (6 - 4)| = 60 / 2 = 30$. At $r = 4$, $720 = I_0 - 30(4) \implies I_0 = 840$.
          </div>
          <div class="hint-content-box" id="h6_1_3">
            <strong>Hint 3:</strong> $\Delta Y = k_F \times \Delta G = (1 / MPS) \times 300 = (1 / 0.30) \times 300 = 1,000$ crore.
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_6_1', 6)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_6_1">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Derive linear behavioral functions for consumption, savings, and investment in Novara, analyze a tech shock, and compute fiscal multiplier expansion.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • Coordinates 1: $Y_{d1} = 1,000, C_1 = 800$.<br>
                • Coordinates 2: $Y_{d2} = 2,000, C_2 = 1,500$.<br>
                • Investment 1: $r_1 = 4\%, I_1 = 720$.<br>
                • Investment 2: $r_2 = 6\%, I_2 = 660$.<br>
                • Autonomous technology boost $\Delta I_0 = +200$.<br>
                • Government infrastructure $\Delta G = +300$.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA SELECTION</span>
              <div class="step-content">
                • $\text{MPC} = \Delta C / \Delta Y_d$; $\text{MPS} = 1 - \text{MPC}$<br>
                • $C = C_0 + \text{MPC}(Y_d) \implies C_0 = C - \text{MPC}(Y_d)$<br>
                • $S = -C_0 + \text{MPS}(Y_d)$<br>
                • $b = |\Delta I / \Delta r|$; $I = I_0 - br$<br>
                • $\Delta Y = (1 / \text{MPS}) \times \Delta G$
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION</span>
              <div class="step-content">
                <div class="step-math">
                  Part a: MPC, MPS, Autonomous Consumption:<br>
                  • MPC = (1,500 − 800) / (2,000 − 1,000) = 700 / 1,000 = 0.70.<br>
                  • MPS = 1 − 0.70 = 0.30.<br>
                  • Autonomous Consumption (C₀): 800 = C₀ + 0.70(1,000) ⇒ C₀ = 800 − 700 = ₹100 crore.<br><br>
                  Part b: Algebraic Functions:<br>
                  • Consumption Function: C = 100 + 0.70 Y_d.<br>
                  • Saving Function: S = −100 + 0.30 Y_d.<br><br>
                  Part c: Investment Parameters & Functions:<br>
                  • Sensitivity (b) = |(660 − 720) / (6 − 4)| = 60 / 2 = 30.<br>
                  • Initial I₀: 720 = I₀ − 30(4) ⇒ I₀ = 720 + 120 = ₹840 crore.<br>
                  • Initial Investment Function: I = 840 − 30r.<br>
                  • Technology shock increases planned investment by ₹200 cr at all interest rates:<br>
                  New I₀' = 840 + 200 = ₹1,040 crore.<br>
                  • New Investment Function: I' = 1,040 − 30r.<br><br>
                  Part d: Graphical Shift & Interest Rate Effect:<br>
                  The investment schedule shifts horizontally RIGHT by ₹200 crore. In the loanable funds market (with saving unchanged), this rightward shift creates excess demand for funds, pushing the equilibrium real interest rate UP.<br><br>
                  Part e: Change in National Income from Infrastructure:<br>
                  • Expenditure Multiplier (k) = 1 / MPS = 1 / 0.30 = 3.333.<br>
                  • ΔY = k × ΔG = (1 / 0.30) × 300 = +₹1,000 crore.
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                Loanable funds diagram illustrates $I$ shifting right from $I_0 = 840$ to $I_0' = 1,040$. Real interest rate ascends along the upward-sloping saving curve.

                <div class="solution-svg-diagram">
                  <svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
                    <rect width="500" height="240" fill="#08090d" rx="4"/>
                    <line x1="40" y1="200" x2="470" y2="200" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                    <line x1="50" y1="210" x2="50" y2="20" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                    <text x="470" y="222" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" text-anchor="end">LOANABLE FUNDS (Q)</text>
                    <text x="25" y="30" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" transform="rotate(-90 25,30)" text-anchor="end">REAL RATE (r %)</text>
                    <line x1="100" y1="190" x2="420" y2="50" stroke="#60a5fa" stroke-width="2.5"/>
                    <text x="425" y="50" fill="#60a5fa" font-family="var(--font-mono)" font-size="11" font-weight="700">S(r)</text>
                    <line x1="80" y1="50" x2="360" y2="190" stroke="#fb923c" stroke-width="1.8" stroke-dasharray="3,3"/>
                    <text x="365" y="195" fill="#fb923c" font-family="var(--font-mono)" font-size="10">I₀</text>
                    <line x1="160" y1="50" x2="440" y2="190" stroke="#fb923c" stroke-width="2.5"/>
                    <text x="445" y="195" fill="#fb923c" font-family="var(--font-mono)" font-size="11" font-weight="700">I₁ (Tech Boom)</text>
                    <circle cx="220" cy="138" r="5" fill="none" stroke="rgba(255,255,255,0.5)" stroke-width="1.5"/>
                    <text x="170" y="142" fill="rgba(255,255,255,0.6)" font-family="var(--font-mono)" font-size="9">E₀(1300, 3.0%)</text>
                    <circle cx="280" cy="112" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                    <circle cx="280" cy="112" r="2.5" fill="#d92534"/>
                    <line x1="268" y1="112" x2="292" y2="112" stroke="#d92534" stroke-width="1.2"/>
                    <line x1="280" y1="100" x2="280" y2="124" stroke="#d92534" stroke-width="1.2"/>
                    <text x="290" y="106" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₁ (1380, 3.8%)</text>
                    <line x1="50" y1="112" x2="280" y2="112" stroke="#d92534" stroke-dasharray="2,2"/>
                    <line x1="280" y1="112" x2="280" y2="200" stroke="#d92534" stroke-dasharray="2,2"/>
                    <text x="42" y="116" fill="#fb923c" font-family="var(--font-mono)" font-size="10" text-anchor="end">r₁* = 3.8%</text>
                    <text x="280" y="214" fill="#fb923c" font-family="var(--font-mono)" font-size="10" text-anchor="middle">Q₁* = 1380</text>
                  </svg>
                  <span class="solution-svg-caption">FIGURE 6.1: INVESTMENT DEMAND SHIFT IN LOANABLE FUNDS</span>
                </div>

              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                Technological advancements shift the marginal product of capital upward, making investment profitable even at existing interest rates. The infrastructure multiplier of 3.33 magnifies government spending into a ₹1,000 crore national output surge.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                • $\text{MPC} = 0.70; \text{MPS} = 0.30; C_0 = ₹100$ cr.<br>
                • $C = 100 + 0.70Y_d; S = -100 + 0.30Y_d$.<br>
                • Initial $I = 840 - 30r$; New $I' = 1,040 - 30r$.<br>
                • Infrastructure output expansion $\Delta Y = \mathbf{₹1,000}$ crore.
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="mission-card">
        <div class="mission-top-bar">
          <span class="mission-level-badge level-3">LEVEL 3 // ADVANCED EXAMINATION OPERATION</span>
          <span class="topic-ref-tag">SEPTEMBER 2026 MIDSEM EXAM QUESTION 3 (PART A & B1)</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 6.2: Ostara Loanable Funds Simultaneous Shift & Multiplier (Official Gold Standard)</h3>
        <p class="mission-question">
          The economy of Ostara is experiencing rising unemployment and uncertainty about future employment. Households respond by increasing precautionary saving. As a result, planned household savings increases by 12%, and improved business expectations increase planned investment by 8%.
          <br><br>
          The initial loanable-funds schedules are:
          <br>$$S_L = 1000 + 100r$$
          <br>$$I_L = 1600 − 100r$$
          where $S_L$ and $I_L$ are measured in billion ostars and $r$ is the real interest rate expressed in percentage points. Assume that the changes in planned saving and investment shift the respective schedules horizontally by the desired amounts.
          <br>Ostara's current real GDP is 8,640 billion ostars, which is equal to 60% of potential GDP. The marginal propensity to consume is 0.75. Assume no taxes, imports, or crowding out.
          <br><br>
          <strong>Your Operational Directives (Official Midsem Mandate):</strong><br>
          a. Calculate the initial and new equilibrium real interest rate and quantity of loanable funds. Illustrate the changes in an appropriately labelled diagram and explain why the interest rate changes in the observed direction (4 marks).<br>
          b1. Calculate the expenditure multiplier (1 mark).
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h6_2_1')">Hint 1: Baseline Eq</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h6_2_2')">Hint 2: Horizontal Shifts</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h6_2_3')">Hint 3: Why r Rises</button>
          </div>
          <div class="hint-content-box" id="h6_2_1">
            <strong>Hint 1:</strong> Initial: $1000 + 100r = 1600 - 100r \implies 200r = 600 \implies r = 3\%, Q = 1300$.
          </div>
          <div class="hint-content-box" id="h6_2_2">
            <strong>Hint 2:</strong> Saving shift = 12% of 1000 = 120 $\implies S' = 1120 + 100r$. Investment shift = 8% of 1600 = 128 $\implies I' = 1728 - 100r$.
          </div>
          <div class="hint-content-box" id="h6_2_3">
            <strong>Hint 3:</strong> Rightward shift of investment (128) > rightward shift of saving (120), creating net excess demand for funds $\implies r$ rises from 3.00% to 3.04%!
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_6_2', 6)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_6_2">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Official Mid-Term Examination Question 3 (Parts a & b1): Solve initial and shifted loanable funds general equilibrium, explain interest rate direction, and calculate spending multiplier.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • Initial Saving: $S_L = 1000 + 100r$.<br>
                • Initial Investment: $I_L = 1600 - 100r$.<br>
                • Precautionary saving shift = +12% of intercept (1000) = +120 billion ostars.<br>
                • Business expectation investment shift = +8% of intercept (1600) = +128 billion ostars.<br>
                • $MPC = 0.75$.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA SELECTION</span>
              <div class="step-content">
                • Equilibrium Condition: $S_L = I_L$<br>
                • Shifted schedules: $S' = (1000 + 120) + 100r$; $I' = (1600 + 128) - 100r$<br>
                • Expenditure Multiplier: $k = 1 / (1 - MPC)$
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION (OFFICIAL ANSWER KEY METHODOLOGY)</span>
              <div class="step-content">
                <div class="step-math">
                  a. Initial and new loanable-funds equilibrium (4 marks):<br>
                  Initial equilibrium:<br>
                  S = I ⇒ 1000 + 100r = 1600 − 100r ⇒ 200r = 600 ⇒ r = 3%.<br>
                  Initial Equilibrium quantity: S = I = 1000 + 100(3) = 1,300 billion ostars.<br><br>
                  Horizontal shifts:<br>
                  Saving rises by 12% of 1,000 = 120;<br>
                  Investment rises by 8% of 1,600 = 128.<br><br>
                  New schedules:<br>
                  S′ = 1120 + 100r<br>
                  I′ = 1728 − 100r<br><br>
                  New equilibrium:<br>
                  1120 + 100r = 1728 − 100r ⇒ 200r = 608 ⇒ r = 3.04%.<br>
                  New equilibrium quantity = 1120 + 100(3.04) = 1,424 billion ostars.<br><br>
                  Diagram & Direction Justification:<br>
                  Show both S and I shifting right, from S to S′ and I to I′. The equilibrium quantity of loanable funds rises and interest rates also rises as the rightward shift in investment demand (128 billion ostars) is greater than the rightward shift in saving supply (120 billion ostars).<br><br>
                  b1. Expenditure multiplier (1 mark):<br>
                  k = 1 / (1 − MPC) = 1 / (1 − 0.75) = 1 / 0.25 = 4.
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                The diagram exhibits Scenario 1 of the Ready Reckoner: Both curves shift right. Equilibrium quantity expands determinately from 1,300 to 1,424. Because $\Delta I (128) > \Delta S (120)$, the interest rate ticks upward from 3.00% to 3.04%.

                <div class="solution-svg-diagram">
                  <svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
                    <rect width="500" height="240" fill="#08090d" rx="4"/>
                    <line x1="40" y1="200" x2="470" y2="200" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                    <line x1="50" y1="210" x2="50" y2="20" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                    <text x="470" y="222" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" text-anchor="end">LOANABLE FUNDS (Q)</text>
                    <text x="25" y="30" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" transform="rotate(-90 25,30)" text-anchor="end">REAL RATE (r %)</text>
                    <line x1="80" y1="190" x2="380" y2="50" stroke="#60a5fa" stroke-width="1.8" stroke-dasharray="3,3"/>
                    <line x1="140" y1="190" x2="440" y2="50" stroke="#60a5fa" stroke-width="2.5"/>
                    <text x="445" y="50" fill="#60a5fa" font-family="var(--font-mono)" font-size="11" font-weight="700">S₁ (ΔS = +120)</text>
                    <line x1="80" y1="50" x2="360" y2="190" stroke="#fb923c" stroke-width="1.8" stroke-dasharray="3,3"/>
                    <line x1="148" y1="50" x2="428" y2="190" stroke="#fb923c" stroke-width="2.5"/>
                    <text x="433" y="195" fill="#fb923c" font-family="var(--font-mono)" font-size="11" font-weight="700">I₁ (ΔI = +128)</text>
                    <circle cx="230" cy="120" r="5" fill="none" stroke="rgba(255,255,255,0.5)" stroke-width="1.5"/>
                    <text x="180" y="115" fill="rgba(255,255,255,0.6)" font-family="var(--font-mono)" font-size="9">E₀(1300, 3.00%)</text>
                    <circle cx="288" cy="119" r="8" fill="none" stroke="#10b981" stroke-width="2"/>
                    <circle cx="288" cy="119" r="3" fill="#10b981"/>
                    <text x="298" y="114" fill="#10b981" font-family="var(--font-mono)" font-size="11" font-weight="700">E₁ (1424, 3.04%)</text>
                  </svg>
                  <span class="solution-svg-caption">FIGURE 6.2: READY RECKONER SIMULTANEOUS SHIFTS (S & I BOTH RIGHT)</span>
                </div>

              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                Even though households attempted to hoard precautionary cash, corporate animal spirits expanded investment demand by a larger absolute margin (128 vs 120), creating net borrowing competition that drove interest rates higher.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                <strong>OFFICIAL SCORE METRICS:</strong><br>
                • Initial Eq: $r = 3.00\%, Q = 1,300$ billion ostars.<br>
                • New Eq: $r = 3.04\%, Q = 1,424$ billion ostars.<br>
                • Interest Rate explanation: $r$ rises because $\Delta I (128) > \Delta S (120)$.<br>
                • Expenditure Multiplier $k = \mathbf{4.00}$.<br>
                <em>Full 5/5 marks verified.</em>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ==================== TARGETS ENVIRONMENT ==================== -->
    <div class="targets-section">
      <div class="topic-card">
        <div class="topic-header">
          <h3 class="topic-title">Chapter 6 Solutions & Ready Reckoner Master Archive</h3>
          <span class="topic-ref-tag">TARGET PROTOCOL: 7-STEP VERIFICATION</span>
        </div>
        <p class="content-text">
          Review the simultaneous shift dynamics. Remember that in an examination, whenever both curves shift in the same direction, you must compare the horizontal intercepts to determine the movement of $r$!
        </p>
      </div>
    </div>
  </div>
</div>
"""
