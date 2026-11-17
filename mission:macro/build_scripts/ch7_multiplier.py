# build_scripts/ch7_multiplier.py
"""
Project 007: Chapter 7 — The Multiplier Effect
Exhaustive academic content strictly from Prof. Sana Tabassum lecture slides,
including Multiplier Cascade Interactive Engine and Mid-Term Exam Question 3 (Parts B2-B3).
"""

def get_chapter_7():
    return r"""
<!-- CHAPTER 7: THE MULTIPLIER EFFECT -->
<div class="chapter-container" id="chapter-7">
  <a id="ch7" class="chapter-anchor"></a>
  <div class="chapter-header">
    <div class="ch-badge-group">
      <span class="ch-code-pill">DOSSIER 07 // INTEL-MULTIPLIER</span>
      <h2 class="ch-title">Chapter 7 — The Multiplier Effect & Fiscal Mechanics</h2>
    </div>
    <div class="chapter-actions">
      <button class="ch-mastery-btn" id="ch-mastery-badge-7" onclick="toggleProgressItem(7, 'training', {checked: true})">IN PROGRESS</button>
    </div>
  </div>

  <div class="chapter-nav-tabs">
    <button class="ch-tab-btn active" data-tab="all" onclick="switchChapterTab(7, 'all')">ALL INTEL</button>
    <button class="ch-tab-btn" data-tab="training" onclick="switchChapterTab(7, 'training')">TRAINING (THE BRIEFING)</button>
    <button class="ch-tab-btn" data-tab="missions" onclick="switchChapterTab(7, 'missions')">MISSIONS (ACTIVE OPS)</button>
    <button class="ch-tab-btn" data-tab="targets" onclick="switchChapterTab(7, 'targets')">TARGETS (DEBRIEFING)</button>
  </div>

  <div class="chapter-body">
    <!-- ==================== TRAINING ENVIRONMENT ==================== -->
    <div class="training-section">
      <div class="topic-card">
        <div class="topic-header">
          <h3 class="topic-title">7.1 Economic Intuition & The Round-by-Round Transmission Ripple</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Unit 2, Slides 12-14 & IS Deck</span>
        </div>
        <p class="content-lead">
          The <strong>Multiplier Effect</strong> refers to the economic phenomenon whereby an <em>"initial autonomous increase in spending or investment generates a much larger cumulative expansion in final national income."</em>
        </p>
        <p class="content-text">
          Why does this multiplication occur? Because in an interdependent economy, <strong>one person's spending becomes another person's income</strong>. When a new injection enters the economy, it triggers a chain-reaction ripple of successive expenditure rounds:
        </p>

        <div class="intel-box key-intuition">
          <div class="intel-box-title">The Ripple Architecture (e.g., Government Power Station Project of €10 Billion)</div>
          <p class="content-text">
            <strong>Initial Injection:</strong> The government commissions €10 billion to build nuclear power facilities.<br>
            <strong>Round 1 (Factor Income Creation):</strong> Contractors, engineers, and steelworkers receive €10 billion in new wages and revenues.<br>
            <strong>Round 2 (Induced Consumption):</strong> If $\text{MPC} = 0.75$, workers spend 75% (€7.5 billion) on food, clothing, housing, and entertainment. The remaining 25% (€2.5 billion) leaks out as savings.<br>
            <strong>Round 3 (Second-Order Income):</strong> Retailers and suppliers earn €7.5 billion and subsequently spend 75% of that (€5.625 billion), while €1.875 billion leaks into savings.<br>
            <strong>Cumulative Convergence:</strong> This geometric spending progression continues across infinite rounds:
            $$\Delta Y = 10 \times \left(1 + 0.75 + 0.75^2 + 0.75^3 + \dots\right) = 10 \times \frac{1}{1 - 0.75} = 10 \times 4 = €40 \text{ billion!}$$
          </p>
        </div>
      </div>

      <!-- INTERACTIVE GRAPH LAB 3: MULTIPLIER CASCADE -->
      <div class="graph-canvas-box">
        <div class="lab-toolbar-header">
          <span class="lab-toolbar-badge">TACTICAL LAB 03 // MULTIPLIER CASCADE RIPPLE ENGINE</span>
          <button class="graph-reset-btn" onclick="resetMultiplierCascade()" type="button" title="Reset Multiplier Simulation to Baseline">
            <span class="reset-icon">↺</span> RESET SIMULATION TO BASELINE
          </button>
        </div>
        <div class="graph-top-ctrls" style="margin-top:8px;">
          <div style="display:flex; align-items:center; gap:16px; flex-wrap:wrap; width:100%; justify-content:flex-start;">
            <div class="slider-group">
              <label for="multMpcSlider">MPC (PROPENSITY):</label>
              <input type="range" id="multMpcSlider" min="0.5" max="0.9" step="0.05" value="0.75" style="width:110px;">
            </div>
            <div class="slider-group">
              <label for="multInjSlider">INITIAL INJECTION (ΔJ):</label>
              <input type="range" id="multInjSlider" min="50" max="500" step="50" value="100" style="width:110px;">
            </div>
          </div>
        </div>
        <div class="graph-telemetry-readout" style="margin-bottom:14px;">
          <div class="telemetry-item">MULTIPLIER (k): <span id="multKReadout" style="color:var(--silver-100);">4.00</span></div>
          <div class="telemetry-item">CUMULATIVE EXPANSION (ΔY): <span id="multTotalYReadout" style="color:var(--success-emerald);">₹400.0 cr</span></div>
        </div>
        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th>Progression Round</th>
                <th>Induced Spending (ΔC)</th>
                <th>Leakage / Savings (ΔS)</th>
                <th>Cumulative Output (ΔY)</th>
                <th>Convergence Tracker</th>
              </tr>
            </thead>
            <tbody id="multiplierRoundsTable">
              <!-- Dynamically rendered by engine_js.py -->
            </tbody>
          </table>
        </div>
      </div>

      <div class="topic-card">
        <div class="topic-header">
          <a id="ch7-multiplier-taxonomy"></a>
          <h3 class="topic-title">7.2 Master Multiplier Taxonomies & Algebraic Formulations</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Slides 14-15 & IS Deck</span>
        </div>
        <p class="content-text">
          Never assume that all multipliers are identical. The lecture slides establish distinct formulations for each policy and expenditure lever:
        </p>

        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th>Multiplier Type</th>
                <th>Mathematical Formula</th>
                <th>Algebraic Sign</th>
                <th>Economic Transmission Rationale</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Investment Multiplier ($k_I$)</strong></td>
                <td><strong>$k_I = \frac{1}{1 - MPC} = \frac{1}{MPS}$</strong></td>
                <td>Positive (+)</td>
                <td>A change in private business capital expenditure directly enters the goods market in full in Round 1.</td>
              </tr>
              <tr>
                <td><strong>Government Expenditure Multiplier ($k_F$)</strong></td>
                <td><strong>$k_F = \frac{1}{1 - MPC} = \frac{1}{MPS}$</strong></td>
                <td>Positive (+)</td>
                <td>Direct government purchase of newly produced goods and infrastructure ($G$). Exactly equal to $k_I$.</td>
              </tr>
              <tr>
                <td><strong>Tax Multiplier ($k_T$)</strong></td>
                <td><strong>$k_T = \frac{-MPC}{1 - MPC} = \frac{-MPC}{MPS}$</strong></td>
                <td><strong style="color:var(--bond-crimson);">Negative (−)</strong></td>
                <td>Taxes inversely affect disposable income ($T \uparrow \implies Y_d \downarrow \implies C \downarrow \implies Y \downarrow$).</td>
              </tr>
              <tr>
                <td><strong>Transfer Payment Multiplier ($k_{TR}$)</strong></td>
                <td><strong>$k_{TR} = \frac{MPC}{1 - MPC}$</strong></td>
                <td>Positive (+)</td>
                <td>Pensions and welfare increase disposable income. Households spend fraction $MPC$ in Round 1.</td>
              </tr>
              <tr>
                <td><strong>Balanced Budget Multiplier ($k_{BB}$)</strong></td>
                <td><strong>$k_{BB} = k_F + k_T = 1.00$</strong></td>
                <td>Positive (+1)</td>
                <td>If $\Delta G = \Delta T$, national income expands by exactly $1 \times \Delta G$ because the government spent 100% of $G$, whereas households would have saved a fraction of $T$!</td>
              </tr>
              <tr>
                <td><strong>Open Economy Multiplier ($k_{\text{open}}$)</strong></td>
                <td><strong>$k = \frac{1}{MPS + MPT + MPM} = \frac{1}{MPW}$</strong></td>
                <td>Positive (+)</td>
                <td>Income leaks through savings ($MPS$), taxes ($MPT$), and imports ($MPM$). Total Marginal Propensity to Withdraw ($MPW$) shrinks the multiplier!</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="intel-box trap">
          <div class="intel-box-title">Examination Trap: Why the Tax Multiplier is Smaller than the Spending Multiplier</div>
          <p class="content-text" style="margin-bottom:0;">
            Notice that $|k_T| = k_F - 1$. For example, if $MPC = 0.80$, then $k_F = 5$ while $k_T = -4$. <strong>Why?</strong> When the government spends ₹100 on infrastructure, the entire ₹100 is immediately injected into the goods market in Round 1. When the government cuts taxes by ₹100, households do not spend all of it—they save $MPS \times 100 = ₹20$, spending only $MPC \times 100 = ₹80$ in Round 1! Because Round 1 spending is smaller, the cumulative output expansion is lower by exactly the initial tax cut amount.
          </p>
        </div>

        <h4 class="section-subtitle">The Accelerator Principle</h4>
        <p class="content-text">
          The <strong>Accelerator Principle</strong> relates the rate of change of aggregate demand to the rate of change in investment. It demonstrates that a small percentage increase in consumer demand can trigger a massive percentage surge in capital equipment investment when existing capacity thresholds are breached:
        </p>
        <div class="intel-box key-intuition">
          <div class="intel-box-title">The Lecture Capacity Threshold Example</div>
          <p class="content-text" style="margin-bottom:0;">
            A manufacturing plant operates a machine producing 1,000 units/week. Current demand is 800 units. A 10% demand rise to 880 requires zero new investment. In year two, demand rises to 1,056 units—capacity is breached. By year three, demand reaches 1,250 units (+25%). To supply this, the firm MUST purchase an entire new machine (+100% investment increase!). A 25% change in final demand triggered an accelerated 100% surge in capital investment!
          </p>
        </div>
      </div>
    </div>

    <!-- ==================== MISSIONS ENVIRONMENT ==================== -->
    <div class="missions-section">
      <div class="mission-card">
        <div class="mission-top-bar">
          <span class="mission-level-badge level-1">LEVEL 1 // FOUNDATION</span>
          <span class="topic-ref-tag">IS Curve Deck Practice Problem 1</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 7.1: Linear Keynesian System Equilibrium & Deficit Audit</h3>
        <p class="mission-question">
          The government of a country introduces a fiscal policy aimed at boosting economic activity by increasing its spending. It decides to invest ₹20 in public infrastructure while collecting only ₹10 through taxes. The consumption behaviour of households is given by the function:
          <br>$$C = 20 + 0.80 Y_d \quad \text{where } Y_d = Y − Tx$$
          Other macroeconomic parameters are: Planned Investment $I = 50$, Government spending $G = 20$, and Taxes $Tx = 10$.
          <br><br>
          <strong>Your Operational Directives:</strong><br>
          A. Find equilibrium output ($Y$).<br>
          B. Find consumption ($C$) and saving ($S$) at equilibrium output.<br>
          C. Show the equality of leakages and injections from the spending flow at equilibrium.<br>
          D. How is the ₹20 government expenditure financed, and what type of budget does this represent?
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h7_1_1')">Hint 1: Goods Market</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h7_1_2')">Hint 2: Disposable Income</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h7_1_3')">Hint 3: Leakages</button>
          </div>
          <div class="hint-content-box" id="h7_1_1">
            <strong>Hint 1:</strong> $Y = C + I + G = [20 + 0.80(Y - 10)] + 50 + 20$.
          </div>
          <div class="hint-content-box" id="h7_1_2">
            <strong>Hint 2:</strong> $Y = 20 + 0.80Y - 8 + 70 = 82 + 0.80Y \implies 0.20Y = 82 \implies Y = 410$.
          </div>
          <div class="hint-content-box" id="h7_1_3">
            <strong>Hint 3:</strong> Leakages = $S + Tx$; Injections = $I + G$.
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_7_1', 7)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_7_1">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Solve equilibrium national income for the linear 3-sector Keynesian model, compute consumption and saving, prove leakage-injection equality, and analyze fiscal deficit financing.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • $C = 20 + 0.80(Y - Tx)$<br>
                • $I = 50; G = 20; Tx = 10$.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA SELECTION</span>
              <div class="step-content">
                • $Y = C + I + G$<br>
                • $S = Y_d - C$<br>
                • $\text{Leakages} = S + Tx$; $\text{Injections} = I + G$
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION</span>
              <div class="step-content">
                <div class="step-math">
                  A. Equilibrium Output:<br>
                  Y = [20 + 0.80(Y − 10)] + 50 + 20<br>
                  Y = 20 + 0.80Y − 8 + 70<br>
                  Y = 82 + 0.80Y<br>
                  Y − 0.80Y = 82 ⇒ 0.20Y = 82 ⇒ Y = 82 / 0.20 = 410.<br><br>
                  B. Consumption and Saving at Equilibrium:<br>
                  Y_d = Y − Tx = 410 − 10 = 400.<br>
                  Consumption (C) = 20 + 0.80(400) = 20 + 320 = 340.<br>
                  Saving (S) = Y_d − C = 400 − 340 = 60.<br>
                  (Verification: S = −20 + 0.20(400) = −20 + 80 = 60).<br><br>
                  C. Equality of Leakages and Injections:<br>
                  Total Leakages (L) = S + Tx = 60 + 10 = 70.<br>
                  Total Injections (J) = I + G = 50 + 20 = 70.<br>
                  Since L = J = 70, the spending flow is in perfect equilibrium!<br><br>
                  D. Budget Financing:<br>
                  Government spending is ₹20 while tax revenue is only ₹10.<br>
                  Fiscal Balance = Tx − G = 10 − 20 = −10.<br>
                  This represents a <strong>DEFICIT BUDGET</strong> of ₹10.<br>
                  Financing: The government finances the ₹10 deficit by borrowing from the financial market (issuing government bonds that absorb ₹10 of private household savings). Notice that private saving of ₹60 exactly funds private investment of ₹50 PLUS the government deficit of ₹10: $S = I + (G - Tx) \implies 60 = 50 + 10$!
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                Keynesian Cross: Planned expenditure line $E = 82 + 0.80Y$ intersects the 45° line at $Y = 410$.

                <div class="solution-svg-diagram">
                  <svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
                    <rect width="500" height="240" fill="#08090d" rx="4"/>
                    <line x1="40" y1="200" x2="470" y2="200" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                    <line x1="50" y1="210" x2="50" y2="20" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                    <text x="470" y="222" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" text-anchor="end">OUTPUT (Y)</text>
                    <text x="25" y="30" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" transform="rotate(-90 25,30)" text-anchor="end">EXPENDITURE (AE)</text>
                    <line x1="50" y1="200" x2="250" y2="20" stroke="#ffffff" stroke-width="2"/>
                    <text x="255" y="20" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">Y = AE (45° Line)</text>
                    <line x1="50" y1="140" x2="420" y2="60" stroke="#a855f7" stroke-width="2.5"/>
                    <text x="425" y="60" fill="#a855f7" font-family="var(--font-mono)" font-size="11" font-weight="700">AE = 82 + 0.80Y</text>
                    <circle cx="160" cy="101" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                    <circle cx="160" cy="101" r="2.5" fill="#d92534"/>
                    <line x1="148" y1="101" x2="172" y2="101" stroke="#d92534" stroke-width="1.2"/>
                    <line x1="160" y1="89" x2="160" y2="113" stroke="#d92534" stroke-width="1.2"/>
                    <text x="170" y="95" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E* (Y* = 410)</text>
                    <line x1="50" y1="101" x2="160" y2="101" stroke="#d92534" stroke-dasharray="2,2"/>
                    <line x1="160" y1="101" x2="160" y2="200" stroke="#d92534" stroke-dasharray="2,2"/>
                    <text x="160" y="214" fill="#38bdf8" font-family="var(--font-mono)" font-size="10" text-anchor="middle">Y* = 410</text>
                  </svg>
                  <span class="solution-svg-caption">FIGURE 7.1: KEYNESIAN CROSS 45° EQUILIBRIUM</span>
                </div>

              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                The ₹10 fiscal deficit injected purchasing power into the private sector, allowing equilibrium output to reach 410 without choking off private investment.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                • Equilibrium Output $Y = \mathbf{410}$.<br>
                • Consumption $C = \mathbf{340}$; Saving $S = \mathbf{60}$.<br>
                • Injections = Leakages = $\mathbf{70}$.<br>
                • Budget: Deficit of ₹10, financed by domestic bond borrowing.
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="mission-card">
        <div class="mission-top-bar">
          <span class="mission-level-badge level-3">LEVEL 3 // ADVANCED EXAMINATION OPERATION</span>
          <span class="topic-ref-tag">SEPTEMBER 2026 MIDSEM EXAM QUESTION 3 (PARTS B2 & B3)</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 7.2: Ostara Output Gap Closure & Overshooting Audit (Official Gold Standard)</h3>
        <p class="mission-question">
          Recall the economy of Ostara from Mission 6.2:
          <br>• Current real GDP = 8,640 billion ostars (equal to 60% of potential GDP).
          <br>• Expenditure multiplier $k = 4$ ($MPC = 0.75$).
          <br>• As a result of private sector adjustments, planned investment increased by 8% of 1,600 = 128 billion ostars.
          <br>• The government proposes increasing expenditure by 1,600 billion ostars, claiming that this will exactly eliminate the output gap.
          <br><br>
          <strong>Your Operational Directives (Official Midsem Mandate):</strong><br>
          1. Estimate the resulting change in equilibrium output following the private-sector adjustment described above (1 mark).<br>
          2. Assess whether the proposed increase in government expenditure of 1,600 billion ostars is sufficient to eliminate the output gap. Based on your calculations, determine the exact increase in government expenditure required to close the output gap completely (2 marks).
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h7_2_1')">Hint 1: Private Expansion</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h7_2_2')">Hint 2: Potential GDP</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h7_2_3')">Hint 3: Overshooting Math</button>
          </div>
          <div class="hint-content-box" id="h7_2_1">
            <strong>Hint 1:</strong> $\Delta Y_{\text{private}} = k \times \Delta I = 4 \times 128 = +512$ billion ostars.
          </div>
          <div class="hint-content-box" id="h7_2_2">
            <strong>Hint 2:</strong> Potential GDP = 8,640 / 0.60 = 14,400. Remaining gap after private boost = 14,400 − (8,640 + 512) = 5,248.
          </div>
          <div class="hint-content-box" id="h7_2_3">
            <strong>Hint 3:</strong> Proposed $\Delta G = 1,600 \implies \Delta Y = 4 \times 1,600 = 6,400$. Overshoots 5,248 by 1,152! Required $\Delta G = 5,248 / 4 = 1,312$.
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_7_2', 7)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_7_2">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Official Mid-Term Examination Question 3 (Parts b2 & b3): Calculate output expansion from private investment, evaluate government stimulus overshooting, and derive required calibrated $\Delta G$.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • Current real GDP ($Y_0$) = 8,640 billion ostars (60% of potential GDP).<br>
                • Multiplier ($k$) = 4.<br>
                • Private investment increase ($\Delta I$) = 128 billion ostars.<br>
                • Proposed government stimulus ($\Delta G_{\text{proposed}}$) = 1,600 billion ostars.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA SELECTION</span>
              <div class="step-content">
                • $\Delta Y_{\text{private}} = k \times \Delta I$<br>
                • $\text{Potential GDP} = Y_0 / 0.60$<br>
                • $\text{Remaining Gap} = \text{Potential GDP} - (Y_0 + \Delta Y_{\text{private}})$<br>
                • $\Delta G_{\text{required}} = \text{Remaining Gap} / k$
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION (OFFICIAL ANSWER KEY METHODOLOGY)</span>
              <div class="step-content">
                <div class="step-math">
                  b2. Change in equilibrium output from private-sector adjustment (1 mark):<br>
                  Increase in planned investment = 8% of 1,600 = 128 billion ostars.<br>
                  ΔY = k × ΔI = 4 × 128 = +512 billion ostars.<br>
                  New real GDP after private-sector adjustment = 8,640 + 512 = 9,152 billion ostars.<br><br>
                  b3. Government expenditure and the output gap (2 marks):<br>
                  Potential GDP = 8,640 / 0.60 = 14,400 billion ostars.<br>
                  Initial output gap = 14,400 − 8,640 = 5,760 billion ostars.<br>
                  After the private-sector output increase of 512, remaining gap = 14,400 − 9,152 = 5,248 billion ostars.<br><br>
                  Evaluation of Proposed Stimulus:<br>
                  Proposed ΔG = 1,600 ⇒ ΔY = 4 × 1,600 = 6,400 billion ostars.<br>
                  Therefore, the proposal is more than sufficient and would overshoot the remaining gap by:<br>
                  6,400 − 5,248 = 1,152 billion ostars.<br><br>
                  Required Calibrated Stimulus:<br>
                  Therefore, the required increase in government expenditure = 5,248 / 4 = 1,312 billion ostars.
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                In the Keynesian Cross diagram, the initial equilibrium at 8,640 shifts to 9,152 via private capex. An injection of 1,600 would push output to 15,552, creating a severe inflationary gap of 1,152. Calibrating $\Delta G$ to 1,312 lands output precisely on $Y^* = 14,400$.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                The government's proposal failed to account for the private sector's endogenous recovery (+512 billion ostars) and applied a crude uncalibrated injection that would trigger severe demand-pull inflation.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                <strong>OFFICIAL SCORE METRICS:</strong><br>
                1. Private sector output increase = <strong>+512 billion ostars</strong> (New GDP = 9,152).<br>
                2. Potential GDP = <strong>14,400 billion ostars</strong>; Remaining Gap = <strong>5,248 billion ostars</strong>.<br>
                3. Proposed $\Delta G = 1,600$ <strong>overshoots by 1,152 billion ostars</strong>.<br>
                4. Required calibrated $\Delta G = \mathbf{1,312}$ billion ostars.<br>
                <em>Full 3/3 marks verified.</em>
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
          <h3 class="topic-title">Chapter 7 Multiplier Toolkit & Verification Archive</h3>
          <span class="topic-ref-tag">TARGET PROTOCOL: 7-STEP VERIFICATION</span>
        </div>
        <p class="content-text">
          Master the sequence: When private sector shifts happen concurrently with public policy, ALWAYS calculate the private adjustment first, compute the residual remaining output gap, and only then divide by the multiplier to find the required government spending!
        </p>
      </div>
    </div>
  </div>
</div>
"""
