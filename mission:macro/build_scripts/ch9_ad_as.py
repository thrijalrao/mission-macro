# build_scripts/ch9_ad_as.py
"""
Project 007: Chapter 9 — Aggregate Demand and Aggregate Supply (AD–AS)
Exhaustive academic coverage strictly from Prof. Sana Tabassum lecture slides,
including the dedicated Types of Shocks section, Self-Correction vs Policy Intervention,
AD-AS Interactive Canvas Lab, and Case Studies (Ardonia, Caledonia, Maha Kumbh Mela).
"""

def get_chapter_9():
    return r"""
<!-- CHAPTER 9: AGGREGATE DEMAND AND AGGREGATE SUPPLY (AD-AS) -->
<div class="chapter-container" id="chapter-9">
  <a id="ch9" class="chapter-anchor"></a>
  <div class="chapter-header">
    <div class="ch-badge-group">
      <span class="ch-code-pill">DOSSIER 09 // INTEL-AD-AS-TACTICAL</span>
      <h2 class="ch-title">Chapter 9 — Aggregate Demand & Supply (AD–AS)</h2>
    </div>
    <div class="chapter-actions">
      <button class="ch-mastery-btn" id="ch-mastery-badge-9" onclick="toggleProgressItem(9, 'training', {checked: true})">IN PROGRESS</button>
    </div>
  </div>

  <div class="chapter-nav-tabs">
    <button class="ch-tab-btn active" data-tab="all" onclick="switchChapterTab(9, 'all')">ALL INTEL</button>
    <button class="ch-tab-btn" data-tab="training" onclick="switchChapterTab(9, 'training')">TRAINING (THE BRIEFING)</button>
    <button class="ch-tab-btn" data-tab="missions" onclick="switchChapterTab(9, 'missions')">MISSIONS (ACTIVE OPS)</button>
    <button class="ch-tab-btn" data-tab="targets" onclick="switchChapterTab(9, 'targets')">TARGETS (DEBRIEFING)</button>
  </div>

  <div class="chapter-body">
    <!-- ==================== TRAINING ENVIRONMENT ==================== -->
    <div class="training-section">
      <div class="topic-card" id="ad-framework">
        <a id="section-ad-framework"></a>
        <div class="topic-header">
          <h3 class="topic-title">9.1 The Aggregate Demand (AD) Framework & Downward Slope</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum AD-AS Deck, Slides 2-5</span>
        </div>
        <p class="content-lead">
          The <strong>Aggregate Demand–Aggregate Supply (AD–AS)</strong> framework is the core analytical engine of macroeconomics. It determines the nation's overall price level ($P$) and equilibrium real output ($Y$), tracking how economic activity reacts to external shocks and government stabilization policies.
        </p>

        <h4 class="section-subtitle">Aggregate Demand (AD) Curve Defined</h4>
        <p class="content-text">
          <strong>Aggregate Demand (AD)</strong> refers to the <em>"Total spending on domestic final goods and services in an economy at a given price level and time."</em>
        </p>
        <div class="formula-card">
          <div class="formula-card-title">Components of Aggregate Demand</div>
          <div class="formula-math-display">
            AD = C + I + G + (NX)
          </div>
          <div class="formula-breakdown">
            <ul>
              <li><strong>Axes:</strong> Vertical axis plots the <strong>Overall Price Level ($P$)</strong> (GDP Deflator or CPI); Horizontal axis plots <strong>Real GDP / Aggregate Output ($Y$)</strong>.</li>
              <li><strong>IS–LM Foundation:</strong> Every point on the AD curve represents simultaneous general equilibrium in both the goods market and the money market ($IS = LM$).</li>
              <li><strong>Movement Along vs Shift:</strong> A change in the general price level ($P$) causes a <strong>movement along</strong> the AD curve. A change in any autonomous spending component ($C, I, G, T, M_s$) causes a <strong>shift of the entire AD curve</strong>!</li>
            </ul>
          </div>
        </div>

        <h4 class="section-subtitle">Why Does the Aggregate Demand Curve Slope Downward?</h4>
        <p class="content-text">
          In microeconomics, a demand curve slopes downward due to substitution toward other goods. In macroeconomics, there are no "other goods" outside aggregate output! AD slopes downward due to two powerful transmission mechanisms:
        </p>
        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th>Transmission Effect</th>
                <th>Formal Name & Originator</th>
                <th>Step-by-Step Economic Transmission Mechanism</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>1. Wealth Effect</strong></td>
                <td><strong>Pigou Effect / Real Balance Effect</strong><br>(Arthur Pigou)</td>
                <td>
                  Price Level Falls ($P \downarrow$)<br>
                  $\implies$ Real purchasing power of nominal money balances rises ($\frac{M}{P} \uparrow$)<br>
                  $\implies$ Households feel wealthier in real terms<br>
                  $\implies$ Autonomous consumption spending rises ($C \uparrow$)<br>
                  $\implies$ <strong>Aggregate Output Demanded Expands ($Y \uparrow$)</strong>.
                </td>
              </tr>
              <tr>
                <td><strong>2. Interest Rate Effect</strong></td>
                <td><strong>Keynes Effect</strong><br>(John Maynard Keynes)</td>
                <td>
                  Price Level Falls ($P \downarrow$)<br>
                  $\implies$ Households require less cash to purchase daily goods<br>
                  $\implies$ Transaction money demand falls ($M_d \downarrow$)<br>
                  $\implies$ Excess money supply drives market interest rates down ($r \downarrow$)<br>
                  $\implies$ Corporate borrowing becomes cheaper, boosting capex ($I \uparrow$) and credit consumption ($C \uparrow$)<br>
                  $\implies$ <strong>Aggregate Output Demanded Expands ($Y \uparrow$)</strong>.
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="topic-card" id="sticky-input-prices" data-title="Sticky Input Prices Theory & SRAS">
        <a id="section-sticky-input-prices"></a><a id="sticky-wages"></a><a id="sras-lras"></a>
        <div class="topic-header">
          <h3 class="topic-title">9.2 Aggregate Supply: Short-Run (SRAS) vs Long-Run (LRAS)</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Slides 6-12</span>
        </div>
        <p class="content-text">
          <strong>Aggregate Supply (AS)</strong> represents the total quantity of goods and services that domestic producers are willing and able to produce at different overall price levels. Macroeconomics establishes an unyielding distinction between the short-run and long-run supply response:
        </p>

        <h4 class="section-subtitle">1. The Sticky Input Prices Theory: Why SRAS Slopes Upward</h4>
        <p class="content-text">
          In macroeconomic theory (Prof. Sana Tabassum Unit 3), the upward slope of the <strong>Short-Run Aggregate Supply (SRAS)</strong> curve is governed by the <strong>Sticky Input Prices & Sticky Wages Theory</strong>. When the aggregate price level ($P$) changes, product output prices change quickly, but <strong>input prices (wages, raw materials, rents) are sticky/rigid in the short run</strong>.
        </p>
        <div class="intel-box key-intuition">
          <div class="intel-box-title">The Four Pillars of Sticky Input Prices in the Short Run</div>
          <ul style="padding-left:20px; color:var(--silver-200); line-height:1.8;">
            <li><strong>1. Sticky Nominal Wages:</strong> Multi-year employment contracts, labor union collective bargaining agreements, and minimum wage legislation prevent wages from adjusting instantaneously. Furthermore, firms avoid nominal wage cuts to protect employee morale and productivity (efficiency wage theory).</li>
            <li><strong>2. Sticky Intermediate Goods & Raw Material Contracts:</strong> Procurement agreements, commodity forward contracts, and wholesale delivery arrangements fix component prices over quarterly or annual billing cycles.</li>
            <li><strong>3. Sticky Facility Rents & Capital Leases:</strong> Commercial real estate lease agreements legally lock in fixed operational occupancy costs for 3–5 years.</li>
            <li><strong>4. Sticky Contracted Services & Menu Costs:</strong> Fixed-fee enterprise retainers (IT, legal, logistics) and menu costs (the administrative friction of revising price schedules) deter frequent input price re-indexing.</li>
          </ul>
          <div class="formula-box" style="margin-top:12px;">
            $$\text{Unit Profit Margin} = \text{Selling Price per Unit } (P) - \text{Sticky Input Cost per Unit } (W)$$
            $$\text{When } P \uparrow \text{ while } W \text{ remains sticky} \implies \text{Profit Margin Expands} \implies \text{Firms increase hiring \& overtime} \implies \mathbf{Y \uparrow \text{ (Upward Sloping SRAS)}}$$
          </div>
        </div>

        <h4 class="section-subtitle">2. Long-Run Aggregate Supply (LRAS): Vertical at Potential Output</h4>
        <p class="content-text">
          In the long run, <strong>all wage contracts expire and all input prices fully adjust</strong> to changing price levels. The LRAS curve is a <strong>vertical line parallel to the price axis at Potential Output ($Y^*$)</strong>.
        </p>
        <div class="step-math">
          Why LRAS is Vertical (The Long-Run Adjustment Transmission):<br>
          1. Aggregate demand rises ⇒ Selling prices rise (P↑).<br>
          2. Input prices are initially sticky ⇒ Profit margins rise ⇒ Firms temporarily produce beyond potential (Y > Y*).<br>
          3. Unemployment plunges below the Natural Rate (u < NRU) ⇒ Severe labor shortages emerge.<br>
          4. Workers observe higher cost of living and demand wage hikes ⇒ Suppliers renegotiate higher raw material contracts.<br>
          5. Higher wages and input costs raise production costs ⇒ Profit margins collapse back to normal.<br>
          6. Firms curtail production back to sustainable capacity ⇒ <strong>Output returns to Potential (Y = Y*) and unemployment returns to NRU!</strong>
        </div>

        <h4 class="section-subtitle">SRAS vs LRAS: Master Comparison</h4>
        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th>Dimension</th>
                <th>Short-Run Aggregate Supply (SRAS)</th>
                <th>Long-Run Aggregate Supply (LRAS)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Economic Meaning</strong></td>
                <td>Relationship between price level and output when production costs are sticky.</td>
                <td>Sustainable output of the economy when all wages and input costs have completely adjusted.</td>
              </tr>
              <tr>
                <td><strong>Time Horizon</strong></td>
                <td>Short run (factor prices rigid/sticky).</td>
                <td>Long run (all factor prices completely flexible).</td>
              </tr>
              <tr>
                <td><strong>Geometric Shape</strong></td>
                <td><strong>Upward sloping.</strong> Higher prices incentivize temporary production surges.</td>
                <td><strong>Vertical line at $Y^*$ (parallel to Y-axis).</strong> Output determined by productivity.</td>
              </tr>
              <tr>
                <td><strong>Effect of Price Level</strong></td>
                <td>Price changes cause <strong>movement along</strong> the upward-sloping curve.</td>
                <td>Price changes have <strong>zero effect</strong> on potential output ($Y^*$).</td>
              </tr>
              <tr>
                <td><strong>Primary Shift Factors</strong></td>
                <td>Temporary raw material/oil prices, business taxes/tariffs, weather, short-run productivity.</td>
                <td>Structural changes: Factor quantity (labor force, capital), factor quality (education, health), technology, efficiency.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- INTERACTIVE GRAPH LAB 4: TACTICAL AD-AS -->
      <div class="graph-canvas-box">
        <div class="lab-toolbar-header">
          <span class="lab-toolbar-badge">TACTICAL LAB 04 // AD–AS TACTICAL SHOCK SIMULATOR</span>
          <button class="graph-reset-btn" onclick="resetAdAsGraph()" type="button" title="Reset AD-AS Simulation to Baseline">
            <span class="reset-icon">↺</span> RESET SIMULATION TO BASELINE
          </button>
        </div>
        <div class="graph-top-ctrls" style="margin-top:8px;">
          <span class="graph-title-label">SELECT EXTERNAL SHOCK:</span>
          <div class="graph-interactive-ctrls">
            <button class="graph-btn adas-scen-btn active" onclick="setAdAsScenario('ad_pos', this)">AD+ (BOOM)</button>
            <button class="graph-btn adas-scen-btn" onclick="setAdAsScenario('ad_neg', this)">AD− (RECESSION)</button>
            <button class="graph-btn adas-scen-btn" onclick="setAdAsScenario('sras_neg', this)">SRAS− (STAGFLATION)</button>
            <button class="graph-btn adas-scen-btn" onclick="setAdAsScenario('sras_pos', this)">SRAS+ (OIL RELIEF)</button>
            <button class="graph-btn adas-scen-btn" onclick="setAdAsScenario('lras_pos', this)">LRAS+ (AI/KUMBH)</button>
          </div>
        </div>
        <div style="display:flex; gap:10px; margin-bottom:12px; flex-wrap:wrap;">
          <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--silver-400); align-self:center;">RESOLUTION MECHANISM:</span>
          <button class="graph-btn adas-mech-btn active" onclick="setAdAsMechanism('short_run', this)">SHORT-RUN EQUILIBRIUM</button>
          <button class="graph-btn adas-mech-btn" onclick="setAdAsMechanism('self_correction', this)">LONG-RUN SELF-CORRECTION (SRAS MOVES)</button>
          <button class="graph-btn adas-mech-btn" onclick="setAdAsMechanism('policy_intervention', this)">POLICY INTERVENTION (AD MOVES)</button>
        </div>
        <div class="canvas-viewport-wrap">
          <canvas id="adAsCanvas"></canvas>
        </div>
        <div class="intel-box" style="margin-top:14px; margin-bottom:0; background:rgba(0,0,0,0.5);">
          <div class="intel-box-title" style="color:var(--silver-200);">TACTICAL SITREP & ECONOMIC MECHANICS</div>
          <p class="content-text" id="adAsDescText" style="margin-bottom:0;">
            Positive Demand Shock: AD shifts right. Output expands above potential ($Y > Y^*$), price level rises ($P \uparrow$). An inflationary gap is opened.
          </p>
        </div>
      </div>

      <div class="topic-card" id="ad-as-shocks">
        <a id="section-ad-as-shocks"></a><a id="stagflation"></a><a id="self-correction"></a>
        <div class="topic-header">
          <h3 class="topic-title">9.3 Mandatory Section: Dedicated Shocks Taxonomy & Self-Correction</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Dedicated Shock Matrix</span>
        </div>
        <p class="content-lead">
          University examination boards heavily test the student's mastery over all six canonical demand and supply shocks. Memorize the exact transmission sequences, directional shifts, and long-run adjustments:
        </p>

        <h4 class="section-subtitle">1. Positive Demand Shock (Demand-Pull Inflation)</h4>
        <div class="step-math">
          Causes: Surge in business confidence, consumer optimism, expansionary fiscal stimulus (G↑, T↓), or monetary easing.<br>
          Curve Shift: AD shifts RIGHT from AD₀ to AD₁.<br>
          Short-Run Impact: Output rises above potential (Y₁ > Y*); Price level rises (P₁ > P₀); Unemployment falls below natural rate (u < NRU). Inflationary Gap!<br>
          Self-Correction Mechanism: Tight labor market pushes nominal wages up → Higher production costs cause SRAS to shift LEFT to SRAS₁ → Economy returns to potential output (Y*), but the price level is permanently HIGHER (P₂ > P₁)!<br>
          Policy Intervention Alternative: Contractionary fiscal/monetary policy shifts AD back LEFT to AD₀, restoring Y* faster with lower price level.
        </div>

        <h4 class="section-subtitle">2. Negative Demand Shock (Recessionary Slump)</h4>
        <div class="step-math">
          Causes: Financial panic, collapse in consumer sentiment, austerity fiscal cuts, or monetary tightening.<br>
          Curve Shift: AD shifts LEFT from AD₀ to AD₁.<br>
          Short-Run Impact: Output falls below potential (Y₁ < Y*); Price level falls (P₁ < P₀); Unemployment rises above natural rate (u > NRU). Recessionary Gap!<br>
          Self-Correction Mechanism: High unemployment and idle capacity put downward pressure on wages and input prices → Lower production costs cause SRAS to shift RIGHT to SRAS₁ → Economy returns to potential output (Y*), and the price level is permanently LOWER!<br>
          Policy Intervention Alternative: Expansionary stimulus shifts AD back RIGHT to AD₀, restoring potential output rapidly before painful prolonged wage cuts.
        </div>

        <h4 class="section-subtitle">3. Negative Temporary Supply Shock (Cost-Push Inflation / Stagflation)</h4>
        <div class="step-math">
          Causes: Geopolitical conflict disrupting oil supplies, raw material price spikes, natural disasters.<br>
          Curve Shift: SRAS shifts LEFT from SRAS₀ to SRAS₁ (LRAS unchanged because productive capacity is intact).<br>
          Short-Run Impact: Output falls below potential (Y₁ < Y*); Price level RISES (P₁ > P₀); Unemployment rises (u > NRU). The deadly cocktail of STAGFLATION!<br>
          Self-Correction Mechanism: Persistent high unemployment eventually forces wage growth to slow and input costs to fall → SRAS shifts back RIGHT to SRAS₀ → Economy returns to original potential output (Y*) and original price level (P₀).<br>
          Policy Dilemma: Monetary expansion shifts AD right (eliminates unemployment but causes hyperinflation); Monetary contraction lowers prices but deepens output depression. Standard demand-side policies CANNOT solve adverse supply shocks!
        </div>

        <h4 class="section-subtitle">4. Positive Temporary Supply Shock (Supply-Side Cost Relief)</h4>
        <div class="step-math">
          Causes: Temporary drop in global oil prices, favorable bumper agricultural harvest, short-term tariff reductions.<br>
          Curve Shift: SRAS shifts RIGHT from SRAS₀ to SRAS₁.<br>
          Short-Run Impact: Output rises above potential (Y₁ > Y*); Price level falls (P₁ < P₀); Unemployment falls (u < NRU).<br>
          Self-Correction: Tight labor market gradually pushes wages back up as temporary relief reverses → SRAS drifts back LEFT to SRAS₀.
        </div>

        <h4 class="section-subtitle">5. Positive Permanent Supply Shock (Long-Run Productive Expansion)</h4>
        <div class="step-math">
          Causes: Nationwide infrastructure modernization (highways, ports, reliable power), AI diffusion, technological innovation, larger skilled labor force.<br>
          Curve Shifts: BOTH LRAS and SRAS shift RIGHTWARD permanently!<br>
          Macroeconomic Result: Economy attains a permanently higher potential GDP (Y*₁ > Y*₀), lower sustainable price level, and lower natural rate of unemployment!
        </div>

        <h4 class="section-subtitle">6. Negative Permanent Supply Shock (Structural Decay)</h4>
        <div class="step-math">
          Causes: Rapidly ageing population shrinking the labor force, permanent war destruction of capital, punitive environmental regulations shutting industries.<br>
          Curve Shifts: BOTH LRAS and SRAS shift LEFTWARD permanently!<br>
          Macroeconomic Result: Economy is permanently trapped at a lower potential GDP, higher permanent price level, and higher structural unemployment.
        </div>

        <h4 class="section-subtitle">Master Shocks Reference Matrix</h4>
        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th rowspan="2">Type of Macroeconomic Shock</th>
                <th colspan="4" style="text-align:center; border-bottom:1px solid var(--border-strong);">Short-Run Equilibrium</th>
                <th colspan="4" style="text-align:center; border-bottom:1px solid var(--border-strong);">Long-Run Self-Corrected Outcome</th>
              </tr>
              <tr>
                <th>Output</th>
                <th>Prices</th>
                <th>Unemp.</th>
                <th>Inflation</th>
                <th>Output</th>
                <th>Prices</th>
                <th>Unemp.</th>
                <th>Inflation</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Negative Demand Shock</strong></td>
                <td>Below Y*</td>
                <td>Falls</td>
                <td>Rises</td>
                <td>Falls</td>
                <td>Returns to Y*</td>
                <td>Lower than baseline</td>
                <td>Returns to NRU</td>
                <td>Lower than baseline</td>
              </tr>
              <tr>
                <td><strong>Positive Demand Shock</strong></td>
                <td>Above Y*</td>
                <td>Rises</td>
                <td>Falls</td>
                <td>Rises</td>
                <td>Returns to Y*</td>
                <td>Higher than baseline</td>
                <td>Returns to NRU</td>
                <td>Higher than baseline</td>
              </tr>
              <tr>
                <td><strong>Negative Temp. Supply Shock (Stagflation)</strong></td>
                <td>Below Y*</td>
                <td>Rises</td>
                <td>Rises</td>
                <td>Rises</td>
                <td>Returns to Y*</td>
                <td>Returns to baseline</td>
                <td>Returns to NRU</td>
                <td>Returns to stable rate</td>
              </tr>
              <tr>
                <td><strong>Positive Temp. Supply Shock</strong></td>
                <td>Above Y*</td>
                <td>Falls</td>
                <td>Falls</td>
                <td>Falls</td>
                <td>Returns to Y*</td>
                <td>Returns to baseline</td>
                <td>Returns to NRU</td>
                <td>Returns to stable rate</td>
              </tr>
              <tr>
                <td><strong>Positive Permanent Supply Shock</strong></td>
                <td>Permanently Higher</td>
                <td>Falls</td>
                <td>Falls</td>
                <td>Falls</td>
                <td>Higher Y*</td>
                <td>Permanently Lower</td>
                <td>Lower NRU</td>
                <td>Stable low rate</td>
              </tr>
              <tr>
                <td><strong>Negative Permanent Supply Shock</strong></td>
                <td>Permanently Lower</td>
                <td>Rises</td>
                <td>Rises</td>
                <td>Rises</td>
                <td>Lower Y*</td>
                <td>Permanently Higher</td>
                <td>Higher NRU</td>
                <td>Higher rate</td>
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
          <span class="mission-level-badge level-2">LEVEL 2 // STRATEGIC EVALUATION</span>
          <span class="topic-ref-tag">AD-AS Case Study 1 Ardonia</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 9.1: Ardonia Confidence Boom & Monetary Intervention</h3>
        <p class="mission-question">
          Ardonia initially operates at its potential GDP of ₹10,000 crore, with an overall price index of 100. A sustained improvement in business confidence encourages firms to expand investments, and rising consumer confidence leads to higher household spending.
          <br>As economic activity increases, actual GDP expands to ₹11,000 crore, accompanied by a rise in the price index to 125. While some economists expect market forces to gradually restore long-run equilibrium, others argue that waiting could prolong inflationary pressures. The central bank is considering stabilizing measures.
          <br><br>
          <strong>Your Operational Directives:</strong><br>
          a. Using the AD–AS framework, analyze the impact on short-run equilibrium. Identify the type of shock and illustrate changes in AD, real output, and price level.<br>
          b. Calculate the output gap in absolute terms and as a percentage of potential GDP. Identify the gap nature and business cycle phase.<br>
          c. Suppose the central bank does not intervene. Explain the sequence of self-correction adjustments returning the economy to long-run equilibrium.<br>
          d. Alternatively, suppose the central bank intervenes before self-correction takes effect to restore initial equilibrium. Recommend an appropriate monetary policy response.<br>
          e. Compare intervention with self-correction in terms of curve shifts, equilibrium output, price level, and unemployment.
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h9_1_1')">Hint 1: Shock Type</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h9_1_2')">Hint 2: Gap Math</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h9_1_3')">Hint 3: Comparison</button>
          </div>
          <div class="hint-content-box" id="h9_1_1">
            <strong>Hint 1:</strong> Confidence surge = Positive Demand Shock $\implies AD$ shifts right. Short-run $Y = 11,000, P = 125$.
          </div>
          <div class="hint-content-box" id="h9_1_2">
            <strong>Hint 2:</strong> Gap = (11,000 − 10,000) / 10,000 = +10.00% (Inflationary Gap, Expansion/Boom phase).
          </div>
          <div class="hint-content-box" id="h9_1_3">
            <strong>Hint 3:</strong> Self-correction moves SRAS left $\implies P$ rises further (e.g. to 140). Policy intervention moves AD left $\implies P$ falls back to 100!
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_9_1', 9)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_9_1">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Analyze Ardonia's positive demand shock, calculate output gap, explain self-correction vs contractionary monetary policy, and deliver a comparative assessment.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • Initial state: $Y^* = ₹10,000$ crore; $P_0 = 100$.<br>
                • Shock: Business and consumer confidence surge.<br>
                • Short-run outcome: Actual GDP $Y_1 = ₹11,000$ crore; $P_1 = 125$.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA SELECTION</span>
              <div class="step-content">
                • $\text{Absolute Output Gap} = Y - Y^*$<br>
                • $\text{Percentage Output Gap} = [(Y - Y^*) / Y^*] \times 100$<br>
                • Framework: AD–AS Short-Run & Long-Run Equilibrium.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION (OFFICIAL ANSWER KEY METHODOLOGY)</span>
              <div class="step-content">
                <div class="step-math">
                  a. Short-Run Equilibrium Analysis:<br>
                  • Shock Type: <strong>Positive Demand Shock</strong>.<br>
                  • Higher consumer optimism and business confidence increase autonomous consumption and investment.<br>
                  • AD curve shifts RIGHTWARD from AD₀ to AD₁.<br>
                  • Along the upward-sloping SRAS curve, equilibrium output expands from ₹10,000 cr to ₹11,000 cr, and overall price level escalates from 100 to 125.<br><br>
                  b. Output Gap Calculation & Business Cycle Stage:<br>
                  • Absolute Output Gap = 11,000 − 10,000 = +₹1,000 crore.<br>
                  • Percentage Output Gap = (+1,000 / 10,000) × 100 = +10.00%.<br>
                  • Nature: <strong>Inflationary Output Gap (Positive Output Gap)</strong>.<br>
                  • Phase: <strong>Expansion / Peak (Boom) Phase</strong>. Economy is overheating beyond sustainable capacity with actual unemployment below the natural rate (u < NRU).<br><br>
                  c. Self-Correcting Mechanism (No Central Bank Action):<br>
                  • Because Y > Y*, the labor market is excessively tight (u < NRU), creating worker shortages.<br>
                  • In the short run, wages were sticky. Over time, workers observe higher inflation (price index 125) and demand higher nominal wages.<br>
                  • Rising labor and raw material costs increase unit production costs, causing the <strong>SRAS curve to shift LEFTWARD</strong>.<br>
                  • As SRAS shifts left, output moves down along AD₁ back to potential GDP (₹10,000 cr), and unemployment returns to NRU.<br>
                  • <strong>Crucial Consequence:</strong> The price level climbs even higher (above 125)!<br><br>
                  d. Central Bank Policy Intervention Response:<br>
                  • To restore equilibrium without self-correction inflation, the central bank must execute <strong>Contractionary Monetary Policy</strong>:<br>
                  • Levers: Raise Repo Rate (Policy rate hike), Increase CRR, Sell government securities via OMO.<br>
                  • Effect: Commercial bank liquidity contracts, borrowing rates rise, cooling C and I. The <strong>AD curve shifts LEFTWARD back from AD₁ to AD₀</strong>.<br>
                  • Real output returns to ₹10,000 crore, and the price level returns to its original stable baseline of 100!<br><br>
                  e. Comparative Synthesis Matrix:<br>
                  • Curve Movement: Self-correction shifts SRAS left; Policy intervention shifts AD left.<br>
                  • Speed: Self-correction is SLOW (sticky contracts); Policy intervention is RAPID.<br>
                  • Final Price Level: Self-correction locks in a permanently HIGHER price level (>125); Policy intervention restores the LOW original price level (100).<br>
                  • Output & Unemployment: Both ultimately return output to Y* (₹10,000 cr) and unemployment to NRU.
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                <p>The AD–AS diagram displays initial $E_0 (100, 10000) \to$ Short-run overheating $E_1 (125, 11000)$. Under self-correction, $E_1 \to E_2 (140, 10000)$ via leftward SRAS shift. Under monetary intervention, $E_1 \to E_0 (100, 10000)$ via leftward AD shift.</p>
                <div class="solution-svg-diagram">
                  <svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg">
                    <rect width="540" height="280" fill="#08090d" rx="6" stroke="rgba(255,255,255,0.08)"/>
                    <line x1="50" y1="240" x2="510" y2="240" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                    <line x1="60" y1="250" x2="60" y2="25" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                    <text x="510" y="255" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" text-anchor="end">REAL OUTPUT / GDP (Y)</text>
                    <text x="25" y="35" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" transform="rotate(-90 25,35)" text-anchor="end">PRICE LEVEL (P)</text>

                    <!-- LRAS vertical at Y* = 10,000 (x=240) -->
                    <line x1="240" y1="240" x2="240" y2="35" stroke="#cbd5e1" stroke-width="2.2" stroke-dasharray="5,4"/>
                    <text x="240" y="28" fill="#e2e8f0" font-family="var(--font-mono)" font-size="11" font-weight="700" text-anchor="middle">LRAS (Y* = 10k)</text>

                    <!-- SRAS0 upward sloping (x: 100->420, y: 220->60) -->
                    <line x1="100" y1="220" x2="420" y2="60" stroke="#10b981" stroke-width="2.2"/>
                    <text x="425" y="60" fill="#10b981" font-family="var(--font-mono)" font-size="10" font-weight="700">SRAS₀ (W₀)</text>

                    <!-- SRAS1 (shifted left/up during self-correction) -->
                    <line x1="70" y1="180" x2="390" y2="20" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4,3"/>
                    <text x="395" y="24" fill="#f43f5e" font-family="var(--font-mono)" font-size="10" font-weight="700">SRAS₁ (W₁ > W₀)</text>

                    <!-- AD0 downward sloping (x: 100->420, y: 60->220) -->
                    <line x1="100" y1="60" x2="420" y2="220" stroke="#38bdf8" stroke-width="2"/>
                    <text x="425" y="224" fill="#38bdf8" font-family="var(--font-mono)" font-size="10" font-weight="700">AD₀ (Baseline)</text>

                    <!-- AD1 shifted rightward (x: 180->500, y: 60->220) -->
                    <line x1="180" y1="60" x2="500" y2="220" stroke="#06b6d4" stroke-width="2.5"/>
                    <text x="505" y="224" fill="#06b6d4" font-family="var(--font-mono)" font-size="10" font-weight="700">AD₁ (Demand Shock)</text>

                    <!-- Shift arrow AD0 -> AD1 -->
                    <line x1="280" y1="165" x2="330" y2="165" stroke="#06b6d4" stroke-width="1.8"/>
                    <polygon points="334,165 326,161 326,169" fill="#06b6d4"/>
                    <text x="305" y="158" fill="#06b6d4" font-family="var(--font-mono)" font-size="9" text-anchor="middle">ΔAD > 0</text>

                    <!-- Self-Correction shift arrow SRAS0 -> SRAS1 -->
                    <line x1="280" y1="110" x2="250" y2="90" stroke="#f43f5e" stroke-width="1.5"/>
                    <polygon points="246,87 254,87 250,95" fill="#f43f5e"/>
                    <text x="238" y="105" fill="#f43f5e" font-family="var(--font-mono)" font-size="8">Wage-Push</text>

                    <!-- E0 Baseline (240, 140) -->
                    <circle cx="240" cy="140" r="5" fill="none" stroke="rgba(255,255,255,0.7)" stroke-width="1.5"/>
                    <text x="230" y="152" fill="rgba(255,255,255,0.8)" font-family="var(--font-mono)" font-size="9" text-anchor="end">E₀ (100, 10k)</text>
                    <line x1="60" y1="140" x2="240" y2="140" stroke="rgba(255,255,255,0.15)" stroke-dasharray="2,2"/>
                    <text x="55" y="143" fill="#94a3b8" font-family="var(--font-mono)" font-size="9" text-anchor="end">P₀=100</text>

                    <!-- E1 Short-Run Overheating Equilibrium (320, 100) with Red Crosshair -->
                    <line x1="320" y1="240" x2="320" y2="100" stroke="rgba(217,37,52,0.4)" stroke-dasharray="2,2"/>
                    <line x1="60" y1="100" x2="320" y2="100" stroke="rgba(217,37,52,0.4)" stroke-dasharray="2,2"/>
                    <circle cx="320" cy="100" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                    <circle cx="320" cy="100" r="2.5" fill="#d92534"/>
                    <line x1="308" y1="100" x2="332" y2="100" stroke="#d92534" stroke-width="1.2"/>
                    <line x1="320" y1="88" x2="320" y2="112" stroke="#d92534" stroke-width="1.2"/>
                    <text x="330" y="96" fill="#ffffff" font-family="var(--font-mono)" font-size="10" font-weight="700">E₁ (125, 11k)</text>
                    <text x="55" y="103" fill="#ef4444" font-family="var(--font-mono)" font-size="9" text-anchor="end">P₁=125</text>
                    <text x="320" y="254" fill="#ef4444" font-family="var(--font-mono)" font-size="9" text-anchor="middle">Y₁=11k</text>

                    <!-- E2 Long-Run Self-Correction (240, 70) -->
                    <circle cx="240" cy="70" r="5" fill="none" stroke="#f59e0b" stroke-width="1.8"/>
                    <text x="230" y="66" fill="#f59e0b" font-family="var(--font-mono)" font-size="9" text-anchor="end">E₂ (140, 10k) [Self-Corr]</text>
                    <line x1="60" y1="70" x2="240" y2="70" stroke="rgba(245,158,11,0.4)" stroke-dasharray="2,2"/>
                    <text x="55" y="73" fill="#f59e0b" font-family="var(--font-mono)" font-size="9" text-anchor="end">P₂=140</text>

                    <!-- Inflationary Gap Bracket on X-axis between 240 and 320 -->
                    <line x1="240" y1="248" x2="320" y2="248" stroke="#ef4444" stroke-width="2"/>
                    <line x1="240" y1="244" x2="240" y2="252" stroke="#ef4444" stroke-width="2"/>
                    <line x1="320" y1="244" x2="320" y2="252" stroke="#ef4444" stroke-width="2"/>
                    <text x="280" y="268" fill="#ef4444" font-family="var(--font-mono)" font-size="8.5" text-anchor="middle">INFLATIONARY GAP (+1,000 cr)</text>
                    <text x="240" y="254" fill="#94a3b8" font-family="var(--font-mono)" font-size="9" text-anchor="middle">Y*=10k</text>
                  </svg>
                  <span class="solution-svg-caption">FIGURE 9.1: ARDONIA POSITIVE DEMAND SHOCK, INFLATIONARY GAP & SELF-CORRECTION VS CONTRACTIONARY POLICY</span>
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                While market forces eventually restore full employment on their own, they do so through the painful penalty of permanent inflation. Active central bank intervention preserves price stability.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                • Shock: Positive Demand Shock ($AD \rightarrow$).<br>
                • Output Gap = <strong>+₹1,000 cr (+10.00%, Inflationary Gap)</strong>.<br>
                • Self-correction outcome: $Y \to Y^*$, but price level rises further (>125).<br>
                • Policy response: <strong>Contractionary Monetary Policy (Repo Rate Hike)</strong> $\implies AD \leftarrow$, restoring $Y^* = 10,000$ and $P = 100$.
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="mission-card">
        <div class="mission-top-bar">
          <span class="mission-level-badge level-3">LEVEL 3 // ADVANCED EXAMINATION OPERATION</span>
          <span class="topic-ref-tag">AD-AS Case Study 2 Caledonia</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 9.2: Caledonia Oil Shock, Stagflation & Central Bank Dilemma</h3>
        <p class="mission-question">
          At the beginning of 2026, Caledonia's economy was operating at its potential GDP of ₹12,000 crore, with an overall price index of 100 and an unemployment rate of 5%, equal to its natural rate of unemployment (NRU).
          <br>During Q2 2026, escalating geopolitical tensions disrupted global energy supplies, causing crude oil prices to surge. As Caledonia depended heavily on imported petroleum, manufacturing, transportation, and power costs escalated. By quarter-end, the overall price index rose to 120, while real GDP declined to ₹10,800 crore. Several firms reduced production and laid off workers, pushing unemployment to 7%. The long-term productive capacity remained unchanged.
          <br>The central bank faced a severe policy dilemma: some policymakers advocated hiking interest rates to control inflation, while others recommended lowering interest rates to stimulate output.
          <br><br>
          <strong>Your Operational Directives (Official 6-Part Mandate):</strong><br>
          a. Using the AD–AS framework, identify the nature of the economic shock. Explain its impact on SRAS, real GDP, and price level.<br>
          b. Calculate Caledonia's output gap in absolute terms and as a percentage of potential GDP. Identify the gap nature and explain how unemployment relates to potential output.<br>
          c. Identify and explain the economic phenomenon illustrated by declining real GDP alongside rising prices.<br>
          d. Suppose the central bank adopts an expansionary monetary policy to completely eliminate the recessionary gap. Analyze the changes in AD, real GDP, price level, and unemployment. Discuss the trade-off.<br>
          e. Alternatively, suppose the central bank adopts a contractionary monetary policy to control inflation. Analyze the changes in equilibrium.<br>
          f. Explain why, as long as the adverse supply shock persists, neither monetary policy can restore both potential output and the original price level of 100!
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h9_2_1')">Hint 1: Shock Type</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h9_2_2')">Hint 2: Stagflation</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h9_2_3')">Hint 3: Policy Dilemma</button>
          </div>
          <div class="hint-content-box" id="h9_2_1">
            <strong>Hint 1:</strong> Imported oil price hike = Negative Temporary Supply Shock $\implies$ SRAS shifts left.
          </div>
          <div class="hint-content-box" id="h9_2_2">
            <strong>Hint 2:</strong> Stagnation (GDP falls, $u$ rises to 7%) + Inflation ($P$ rises to 120) = STAGFLATION.
          </div>
          <div class="hint-content-box" id="h9_2_3">
            <strong>Hint 3:</strong> Monetary policy shifts AD, but the root disruption is on the supply side (SRAS). Shifting AD cannot fix both coordinates simultaneously.
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_9_2', 9)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_9_2">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Analyze Caledonia's adverse oil supply shock, compute output gap, identify stagflation, and dissect the central bank's monetary policy dilemma.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • Initial state: $Y^* = ₹12,000$ cr; $P_0 = 100; u_0 = 5\% = NRU$.<br>
                • External Shock: Geopolitical crude oil disruption; input and transport costs surge.<br>
                • Post-Shock state: $Y_1 = ₹10,800$ cr; $P_1 = 120; u_1 = 7\%$.<br>
                • Productive capacity ($Y^*$) remains unchanged.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA SELECTION</span>
              <div class="step-content">
                • Output Gap = $[(Y - Y^*) / Y^*] \times 100$<br>
                • Framework: AD–AS Supply Shock & Policy Dilemma Dynamics.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION (OFFICIAL ANSWER KEY METHODOLOGY)</span>
              <div class="step-content">
                <div class="step-math">
                  a. Nature of Economic Shock & Transmission:<br>
                  • Shock Type: <strong>Negative Temporary Supply Shock (Adverse Supply Shock)</strong>.<br>
                  • Surging oil prices dramatically increase input and logistics costs across industries.<br>
                  • Short-Run Aggregate Supply (SRAS) shifts LEFTWARD from SRAS₀ to SRAS₁.<br>
                  • Intersection with unchanged AD moves left and up: Real GDP falls to ₹10,800 cr and the price index jumps to 120.<br><br>
                  b. Output Gap & Unemployment Analysis:<br>
                  • Absolute Output Gap = 10,800 − 12,000 = −₹1,200 crore.<br>
                  • Percentage Output Gap = (−1,200 / 12,000) × 100 = −10.00%.<br>
                  • Nature: <strong>Recessionary Output Gap (Negative Output Gap)</strong>.<br>
                  • Unemployment Relationship: Because actual GDP is below potential, firms cut output and lay off labor. Actual unemployment (7%) exceeds the Natural Rate of Unemployment (5%) by exactly 2 percentage points of cyclical joblessness.<br><br>
                  c. Identification of Economic Phenomenon:<br>
                  • The phenomenon is <strong>STAGFLATION</strong> (a portmanteau of Stagnant Output / High Unemployment plus Inflation).<br><br>
                  d. Central Bank Expansionary Monetary Policy (Fight Unemployment):<br>
                  • Central bank cuts repo rate / pumps liquidity ⇒ AD shifts RIGHTWARD to AD₁.<br>
                  • Real GDP expands back to potential output (₹12,000 cr), and unemployment drops back to NRU (5%).<br>
                  • <strong>The Severe Trade-off:</strong> The price level escalates even further (from 120 to perhaps 135)! The central bank cures joblessness only by igniting runaway inflation.<br><br>
                  e. Central Bank Contractionary Monetary Policy (Fight Inflation):<br>
                  • Central bank hikes repo rate aggressively ⇒ AD shifts LEFTWARD to AD₂.<br>
                  • Price index is successfully driven back down toward 100.<br>
                  • <strong>The Severe Trade-off:</strong> Real GDP collapses even deeper (below ₹10,800 cr), and unemployment climbs higher (above 7%). Fighting inflation deepens the recession into a depression!<br><br>
                  f. The Policy Inability Proof:<br>
                  Why neither monetary policy can simultaneously restore Y* and P = 100:<br>
                  Monetary policy instruments (repo rates, reserve ratios, OMO) are strictly <strong>DEMAND-SIDE LEVERS</strong> that can only shift the Aggregate Demand curve. However, the root disruption in Caledonia is a <strong>SUPPLY-SIDE SHIFT</strong> of the SRAS curve.<br>
                  Because the shifted SRAS₁ curve lies to the left of the original equilibrium, any intersection with AD along SRAS₁ involves an inescapable trade-off: moving toward higher output requires accepting a higher price level, while moving toward lower prices requires accepting a lower output level! Only supply-side interventions (energy subsidies, technological efficiency, or the reversal of oil prices) can shift SRAS back to SRAS₀ and restore both coordinates simultaneously.
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                <p>In the AD–AS diagram, SRAS shifts left to $SRAS_1$. The point $(P=100, Y=12000)$ no longer lies on the supply curve. Shifting AD can choose any point along $SRAS_1$, but cannot reach $(100, 12000)$ while $SRAS_1$ remains displaced!</p>
                <div class="solution-svg-diagram">
                  <svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg">
                    <rect width="540" height="280" fill="#08090d" rx="6" stroke="rgba(255,255,255,0.08)"/>
                    <line x1="50" y1="240" x2="510" y2="240" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                    <line x1="60" y1="250" x2="60" y2="25" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                    <text x="510" y="255" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" text-anchor="end">REAL OUTPUT / GDP (Y)</text>
                    <text x="25" y="35" fill="#94a3b8" font-family="var(--font-mono)" font-size="10" transform="rotate(-90 25,35)" text-anchor="end">PRICE LEVEL (P)</text>

                    <!-- LRAS vertical at Y* = 12,000 (x=330) -->
                    <line x1="330" y1="240" x2="330" y2="35" stroke="#cbd5e1" stroke-width="2.2" stroke-dasharray="5,4"/>
                    <text x="330" y="28" fill="#e2e8f0" font-family="var(--font-mono)" font-size="11" font-weight="700" text-anchor="middle">LRAS (Y* = 12k)</text>

                    <!-- AD0 downward sloping (x: 120->460, y: 50->220) -->
                    <line x1="120" y1="50" x2="460" y2="220" stroke="#38bdf8" stroke-width="2.2"/>
                    <text x="465" y="224" fill="#38bdf8" font-family="var(--font-mono)" font-size="10" font-weight="700">AD₀ (Baseline)</text>

                    <!-- SRAS0 upward sloping (x: 120->460, y: 220->50) -->
                    <line x1="120" y1="220" x2="460" y2="50" stroke="#10b981" stroke-width="2"/>
                    <text x="465" y="54" fill="#10b981" font-family="var(--font-mono)" font-size="10" font-weight="700">SRAS₀ (Baseline)</text>

                    <!-- SRAS1 (shifted left/up by Oil Shock) (x: 70->410, y: 180->10) -->
                    <line x1="70" y1="180" x2="410" y2="10" stroke="#ef4444" stroke-width="2.5"/>
                    <text x="415" y="16" fill="#ef4444" font-family="var(--font-mono)" font-size="10" font-weight="700">SRAS₁ (Crude Shock)</text>

                    <!-- Shift arrow SRAS0 -> SRAS1 -->
                    <line x1="320" y1="100" x2="270" y2="80" stroke="#ef4444" stroke-width="1.8"/>
                    <polygon points="266,78 274,77 271,85" fill="#ef4444"/>
                    <text x="295" y="70" fill="#ef4444" font-family="var(--font-mono)" font-size="8.5" text-anchor="middle">Oil Cost Shock (SRAS ←)</text>

                    <!-- E0 Baseline (330, 135) -->
                    <circle cx="330" cy="135" r="5" fill="none" stroke="rgba(255,255,255,0.7)" stroke-width="1.5"/>
                    <text x="345" y="145" fill="rgba(255,255,255,0.8)" font-family="var(--font-mono)" font-size="9">E₀ (100, 12k)</text>
                    <line x1="60" y1="135" x2="330" y2="135" stroke="rgba(255,255,255,0.15)" stroke-dasharray="2,2"/>
                    <text x="55" y="138" fill="#94a3b8" font-family="var(--font-mono)" font-size="9" text-anchor="end">P₀=100</text>
                    <text x="330" y="254" fill="#94a3b8" font-family="var(--font-mono)" font-size="9" text-anchor="middle">Y*=12k</text>

                    <!-- E1 Stagflation Equilibrium (240, 95) with Red Crosshair -->
                    <line x1="240" y1="240" x2="240" y2="95" stroke="rgba(217,37,52,0.4)" stroke-dasharray="2,2"/>
                    <line x1="60" y1="95" x2="240" y2="95" stroke="rgba(217,37,52,0.4)" stroke-dasharray="2,2"/>
                    <circle cx="240" cy="95" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                    <circle cx="240" cy="95" r="2.5" fill="#d92534"/>
                    <line x1="228" y1="95" x2="252" y2="95" stroke="#d92534" stroke-width="1.2"/>
                    <line x1="240" y1="83" x2="240" y2="107" stroke="#d92534" stroke-width="1.2"/>
                    <text x="215" y="85" fill="#ffffff" font-family="var(--font-mono)" font-size="10" font-weight="700">E₁ (120, 10.8k)</text>
                    <text x="215" y="97" fill="#ef4444" font-family="var(--font-mono)" font-size="9">[STAGFLATION: Y↓, P↑]</text>
                    <text x="55" y="98" fill="#ef4444" font-family="var(--font-mono)" font-size="9" text-anchor="end">P₁=120</text>
                    <text x="240" y="254" fill="#ef4444" font-family="var(--font-mono)" font-size="9" text-anchor="middle">Y₁=10.8k</text>

                    <!-- Policy trade-off options dotted lines -->
                    <!-- AD_stimulus: passes through (330, 50) -->
                    <line x1="210" y1="20" x2="490" y2="160" stroke="#06b6d4" stroke-width="1.5" stroke-dasharray="3,3"/>
                    <text x="495" y="160" fill="#06b6d4" font-family="var(--font-mono)" font-size="8">AD (Expansion)</text>
                    <circle cx="330" cy="50" r="4" fill="none" stroke="#06b6d4" stroke-width="1.5"/>
                    <text x="340" y="52" fill="#06b6d4" font-family="var(--font-mono)" font-size="8">Fix Y (P=135!)</text>

                    <!-- AD_cooling: passes through (160, 135) -->
                    <line x1="50" y1="80" x2="330" y2="220" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="3,3"/>
                    <text x="335" y="224" fill="#a855f7" font-family="var(--font-mono)" font-size="8">AD (Contraction)</text>
                    <circle cx="160" cy="135" r="4" fill="none" stroke="#a855f7" stroke-width="1.5"/>
                    <text x="145" y="148" fill="#a855f7" font-family="var(--font-mono)" font-size="8" text-anchor="end">Fix P (Deep Slump Y=9.8k)</text>

                    <!-- Recessionary Gap Bracket on X-axis between 240 and 330 -->
                    <line x1="240" y1="248" x2="330" y2="248" stroke="#ef4444" stroke-width="2"/>
                    <line x1="240" y1="244" x2="240" y2="252" stroke="#ef4444" stroke-width="2"/>
                    <line x1="330" y1="244" x2="330" y2="252" stroke="#ef4444" stroke-width="2"/>
                    <text x="285" y="268" fill="#ef4444" font-family="var(--font-mono)" font-size="8.5" text-anchor="middle">RECESSIONARY GAP (−1,200 cr, u=7%)</text>
                  </svg>
                  <span class="solution-svg-caption">FIGURE 9.2: CALEDONIA GEOPOLITICAL OIL SHOCK, STAGFLATION & CENTRAL BANK DUAL-MANDATE DILEMMA</span>
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                Adverse supply shocks strip central banks of their traditional power, confronting monetary authorities with an irreconcilable conflict between price stability and employment mandates.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                • Shock: <strong>Negative Temporary Supply Shock</strong>.<br>
                • Output Gap: <strong>−₹1,200 cr (−10.00%, Recessionary Gap)</strong>.<br>
                • Phenomenon: <strong>STAGFLATION</strong>.<br>
                • Monetary Policy Verdict: Ineffective at dual stabilization because AD shifts cannot remedy an SRAS displacement.
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
          <h3 class="topic-title">Chapter 9 Shocks & AD-AS Verification Archive</h3>
          <span class="topic-ref-tag">TARGET PROTOCOL: 7-STEP VERIFICATION</span>
        </div>
        <p class="content-text">
          Remember: Demand shocks move output and price level in the SAME direction ($Y \uparrow, P \uparrow$ or $Y \downarrow, P \downarrow$). Supply shocks move output and price level in OPPOSITE directions ($Y \downarrow, P \uparrow$ or $Y \uparrow, P \downarrow$)!
        </p>
      </div>
    </div>
  </div>
</div>
"""
