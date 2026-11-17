# build_scripts/ch5_business_cycles.py
"""
Project 007: Chapter 5 — Business Cycles and Output Gaps
Exhaustive academic content strictly from Prof. Sana Tabassum lecture slides,
including the Business Cycle & Output Gap Interactive Canvas Lab.
"""

def get_chapter_5():
    return r"""
<!-- CHAPTER 5: BUSINESS CYCLES AND OUTPUT GAPS -->
<div class="chapter-container" id="chapter-5">
  <a id="ch5" class="chapter-anchor"></a>
  <div class="chapter-header">
    <div class="ch-badge-group">
      <span class="ch-code-pill">DOSSIER 05 // INTEL-CYCLES</span>
      <h2 class="ch-title">Chapter 5 — Business Cycles & Output Gaps</h2>
    </div>
    <div class="chapter-actions">
      <button class="ch-mastery-btn" id="ch-mastery-badge-5" onclick="toggleProgressItem(5, 'training', {checked: true})">IN PROGRESS</button>
    </div>
  </div>

  <div class="chapter-nav-tabs">
    <button class="ch-tab-btn active" data-tab="all" onclick="switchChapterTab(5, 'all')">ALL INTEL</button>
    <button class="ch-tab-btn" data-tab="training" onclick="switchChapterTab(5, 'training')">TRAINING (THE BRIEFING)</button>
    <button class="ch-tab-btn" data-tab="missions" onclick="switchChapterTab(5, 'missions')">MISSIONS (ACTIVE OPS)</button>
    <button class="ch-tab-btn" data-tab="targets" onclick="switchChapterTab(5, 'targets')">TARGETS (DEBRIEFING)</button>
  </div>

  <div class="chapter-body">
    <!-- ==================== TRAINING ENVIRONMENT ==================== -->
    <div class="training-section">
      <div class="topic-card">
        <div class="topic-header">
          <h3 class="topic-title">5.1 Anatomy of the Business Cycle: Phases, Trend & Gaps</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Dedicated Deck, Slides 2-7</span>
        </div>
        <p class="content-lead">
          Economic activity does not expand along a smooth, linear trajectory. Instead, it oscillates in recurrent waves of boom and slowdown termed the <strong>Business Cycle</strong>: <em>"Fluctuations in aggregate economic activity of a country around its long-term potential growth trend."</em>
        </p>

        <h4 class="section-subtitle">The Four Sequential Phases of the Business Cycle</h4>
        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th>Cycle Phase</th>
                <th>Core Characteristics & Economic Trajectory</th>
                <th>Labor & Capacity Metrics</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>1. Expansion (Recovery & Boom)</strong></td>
                <td>Production surges, consumer and business confidence rise, household spending expands, and corporate sales accelerate.</td>
                <td>Firms hire idle labor; employment rises; capacity utilization increases beyond sustainable norms.</td>
              </tr>
              <tr>
                <td><strong>2. Peak</strong></td>
                <td>The highest apex of economic activity in the cycle before the downturn begins. Growth decelerates as capacity bottlenecks bind.</td>
                <td>Unemployment falls below the Natural Rate ($u < NRU$); wage pressures and inflationary heat reach cyclical maximums.</td>
              </tr>
              <tr>
                <td><strong>3. Contraction (Recession)</strong></td>
                <td>Real GDP decelerates and then falls. Business sales drop, investment is shelved, and household incomes shrink. <em>Technical Recession = Two consecutive quarters of negative GDP growth.</em></td>
                <td>Layoffs escalate; unemployment rises above NRU; idle industrial capacity accumulates.</td>
              </tr>
              <tr>
                <td><strong>4. Trough (Depression)</strong></td>
                <td>The bottom turning point where economic decline ceases, inventory liquidation concludes, and the initial spark of recovery begins.</td>
                <td>Unemployment reaches its maximum; price pressures are lowest/deflationary; excess capacity is widespread.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h4 class="section-subtitle">Potential Output ($Y^P / Y^*$) & Sustainable Capacity</h4>
        <p class="content-text">
          <strong>Potential Output ($Y^P / Y^*$)</strong>, also termed <em>Potential GDP</em> or <em>Full-Employment Output</em>, is defined as the <strong>maximum amount of goods and services an economy can produce sustainably over the long term without causing high inflation</strong>.
        </p>
        <ul style="padding-left:20px; color:var(--silver-300); margin-bottom:16px; line-height:1.8;">
          <li><strong>Sustainable Capacity:</strong> Factors of production (labor, physical capital, factory equipment) are operated at normal, safe intensity levels without mechanical breakdown or severe worker overtime fatigue.</li>
          <li><strong>Natural Rate Alignment:</strong> At potential output, cyclical unemployment is exactly zero ($u_{\text{cyclical}} = 0$). Only structural and frictional unemployment remain.</li>
          <li><strong>Price Stability:</strong> Aggregate demand matches sustainable aggregate supply, maintaining stable inflation.</li>
          <li><strong>Productive Determinants:</strong> Potential GDP is determined strictly by the size of the labor force, total accumulated capital stock ($K$), natural resources, and the state of technological productivity.</li>
        </ul>
      </div>

      <!-- INTERACTIVE GRAPH LAB 1: BUSINESS CYCLE -->
      <div class="graph-canvas-box">
        <div class="lab-toolbar-header">
          <span class="lab-toolbar-badge">TACTICAL LAB 01 // BUSINESS CYCLE & OUTPUT GAP ANALYZER</span>
          <button class="graph-reset-btn" onclick="resetBusinessCycleGraph()" type="button" title="Reset Simulation to Baseline Parameters">
            <span class="reset-icon">↺</span> RESET SIMULATION TO BASELINE
          </button>
        </div>
        <div class="graph-top-ctrls" style="margin-top:8px;">
          <div style="display:flex; align-items:center; gap:16px; flex-wrap:wrap; width:100%; justify-content:space-between;">
            <div class="slider-group">
              <label for="bcTimeSlider">CHRONO-SCANNER (t):</label>
              <input type="range" id="bcTimeSlider" min="0" max="100" value="25" style="width:160px;">
            </div>
            <span style="font-family:var(--font-mono); font-size:0.7rem; color:var(--silver-400);">DRAG SLIDER TO SCAN CYCLE HORIZON</span>
          </div>
        </div>
        <div class="canvas-viewport-wrap">
          <canvas id="businessCycleCanvas"></canvas>
        </div>
        <div class="graph-telemetry-readout">
          <div class="telemetry-item">CYCLE PHASE: <span id="bcPhaseReadout" style="color:var(--silver-100);">Expansion</span></div>
          <div class="telemetry-item">OUTPUT GAP: <span id="bcGapReadout" style="color:var(--success-emerald);">+4.2%</span></div>
          <div class="telemetry-item">RECOMMENDED DOCTRINE: <span id="bcPolicyReadout" style="color:var(--silver-300);">Neutral</span></div>
        </div>
      </div>

      <div class="topic-card">
        <div class="topic-header">
          <a id="ch5-output-gap"></a>
          <h3 class="topic-title">5.2 Output Gap Formulation & Policy Intervention Matrix</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Slides 7-9</span>
        </div>
        <p class="content-text">
          The <strong>Output Gap</strong> measures the precise deviation between an economy's actual real production ($Y$) and its sustainable potential output ($Y^*$).
        </p>

        <div class="formula-card">
          <div class="formula-card-title">Formula for Output Gap</div>
          <div class="formula-math-display">
            Output Gap = [(Actual Output Y − Potential Output Y*) / Potential Output Y*] × 100
          </div>
          <div class="formula-breakdown">
            <ul>
              <li><strong>Positive Output Gap ($Y > Y^*$):</strong> <strong>Inflationary Gap / Overheating.</strong> The economy is producing beyond sustainable capacity. Machine utilization is excessive, labor shortages emerge, actual unemployment falls below the natural rate ($u < NRU$), and acute upward wage/price pressures build.</li>
              <li><strong>Negative Output Gap ($Y < Y^*$):</strong> <strong>Recessionary Gap / Idle Capacity.</strong> The economy is producing below potential. Factories stand idle, workers are laid off, actual unemployment exceeds the natural rate ($u > NRU$), and disinflationary/deflationary pressures dominate.</li>
            </ul>
          </div>
        </div>

        <h4 class="section-subtitle">Master Comparison: Negative vs Positive Output Gaps</h4>
        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th>Analytical Basis</th>
                <th>Negative Output Gap (Recessionary Gap)</th>
                <th>Positive Output Gap (Inflationary Gap)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Mathematical Condition</strong></td>
                <td><strong>Actual Output < Potential Output ($Y < Y^*$)</strong></td>
                <td><strong>Actual Output > Potential Output ($Y > Y^*$)</strong></td>
              </tr>
              <tr>
                <td><strong>Business Cycle Position</strong></td>
                <td>Contraction / Recession / Trough</td>
                <td>Boom / Peak / Overheating</td>
              </tr>
              <tr>
                <td><strong>Resource Utilization</strong></td>
                <td>Substantial idle capacity; underutilized physical capital.</td>
                <td>Overworked machinery; unsustainable overtime shifts.</td>
              </tr>
              <tr>
                <td><strong>Employment Status</strong></td>
                <td>High unemployment ($u > NRU$); cyclical joblessness.</td>
                <td>Tight labor market; severe labor shortages ($u < NRU$).</td>
              </tr>
              <tr>
                <td><strong>Price Pressures</strong></td>
                <td>Weak demand depresses prices; disinflation or deflation.</td>
                <td>Strong excess demand enables firms to hike prices; high inflation.</td>
              </tr>
              <tr>
                <td><strong>Core Policy Objective</strong></td>
                <td><strong>Stimulate demand:</strong> Expand real output and employment.</td>
                <td><strong>Restrain demand:</strong> Cool overheating and anchor price stability.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h4 class="section-subtitle">Policy Deployment Matrix: Expansionary vs Contractionary</h4>
        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th>Operational Lever</th>
                <th>Expansionary Policy (During Recessionary Gaps)</th>
                <th>Contractionary Policy (During Inflationary Gaps)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Fiscal Tools</strong></td>
                <td>• <strong>Increase Government Spending ($G \uparrow$)</strong><br>• <strong>Cut Direct/Indirect Taxes ($T \downarrow$)</strong></td>
                <td>• <strong>Reduce Government Spending ($G \downarrow$)</strong><br>• <strong>Raise Taxes ($T \uparrow$)</strong></td>
              </tr>
              <tr>
                <td><strong>Monetary Tools (Central Bank)</strong></td>
                <td>• <strong>Lower Repo Rate</strong> (Policy rate cut)<br>• <strong>Reduce Cash Reserve Ratio (CRR $\downarrow$)</strong><br>• <strong>Open Market Purchases of Securities</strong></td>
                <td>• <strong>Raise Repo Rate</strong> (Policy rate hike)<br>• <strong>Increase Cash Reserve Ratio (CRR $\uparrow$)</strong><br>• <strong>Open Market Sales of Securities</strong></td>
              </tr>
              <tr>
                <td><strong>Transmission Sequence</strong></td>
                <td>Borrowing costs fall $\implies$ Credit flows $\uparrow \implies C \uparrow, I \uparrow \implies AD$ shifts right $\implies Y \uparrow$, employment rises.</td>
                <td>Borrowing costs rise $\implies$ Credit squeezes $\implies C \downarrow, I \downarrow \implies AD$ shifts left $\implies$ Demand cools, inflation slows.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="topic-card">
        <div class="topic-header">
          <a id="ch5-price-stickiness"></a>
          <h3 class="topic-title">5.3 Cyclical Indicators & Sources of Price Stickiness</h3>
          <span class="topic-ref-tag">REF: Business Cycle Extended Deck (Mitchell & Burns, OECD, Alan Blinder)</span>
        </div>
        <p class="content-text">
          Modern macroeconomic reconnaissance utilizes cyclical indicators categorized by direction of movement and timing relative to GDP:
        </p>
        <ul style="padding-left:20px; color:var(--silver-300); margin-bottom:16px; line-height:1.8;">
          <li><strong>Comovement:</strong>
            <br>• <em>Procyclical:</em> Moves in the same direction as GDP (Real consumption, corporate investment, real wages, corporate profits).
            <br>• <em>Countercyclical:</em> Moves in the opposite direction to GDP (Unemployment rate, business bankruptcies).
            <br>• <em>Acyclical:</em> Has no systematic correlation with business cycles.
          </li>
          <li><strong>Timing Relative to Cycle:</strong>
            <br>• <em>Leading Indicators:</em> Reach peaks and troughs <em>before</em> aggregate GDP turns (Stock and bond prices, building permits, OECD Composite Leading Indicators CLI).
            <br>• <em>Coincident Indicators:</em> Turn at the <em>exact same time</em> as aggregate GDP (Real consumer spending, industrial production).
            <br>• <em>Lagging Indicators:</em> Turn <em>after</em> economic turning points have already occurred (Inflation rate, commercial bank interest rates, long-term unemployment duration).
          </li>
        </ul>

        <h4 class="section-subtitle">The Microeconomic Sources of Keynesian Price Stickiness</h4>
        <div class="intel-box key-intuition">
          <div class="intel-box-title">Why Prices Adjust Slowly to Equilibrium</div>
          <p class="content-text">
            While classical economics assumes perfectly flexible prices and the classical dichotomy, Keynesian reality proves that prices are sticky due to:
            <br>1. <strong>Menu Costs:</strong> The literal and administrative expenses incurred in changing price tags, updating catalogs, re-programming billing algorithms, and risking customer alienation.
            <br>2. <strong>Rational Inattention:</strong> Information collection is costly. Firms and consumers make infrequent, staggered price decisions at periodic intervals rather than continuous daily recalculations.
            <br>3. <strong>Staggered Price Setting:</strong> Competing firms adjust contracts and prices at different calendar dates. Fear of being the first to raise prices and lose market share slows down aggregate price level adjustments.
            <br>4. <strong>Empirical Validation:</strong> Alan Blinder's landmark Princeton survey revealed that only 10% of firms change prices weekly, while nearly 40% change prices only once a year!
          </p>
        </div>
      </div>
    </div>

    <!-- ==================== MISSIONS ENVIRONMENT ==================== -->
    <div class="missions-section">
      <div class="mission-card">
        <div class="mission-top-bar">
          <span class="mission-level-badge level-1">LEVEL 1 // FOUNDATION</span>
          <span class="topic-ref-tag">Business Cycles Case Study 1</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 5.1: Arvania Recessionary Gap & Investment Stimulus</h3>
        <p class="mission-question">
          In the economy of Arvania, potential GDP ($Y^*$) is 20,000 arvenies, while actual GDP ($Y$) is 18,000 arvenies. The marginal propensity to save (MPS) is 0.20. Actual investment is 3,600 arvenies.
          <br><br>
          <strong>Your Operational Directives:</strong><br>
          a. Identify the nature and size of the output gap in absolute terms and as a percentage of potential GDP. Calculate the additional investment required to close the output gap completely.<br>
          b. Suppose improved business confidence increases planned investment by 300 arvenies. Calculate the resulting change in equilibrium GDP and determine whether the economy reaches potential output.
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h5_1_1')">Hint 1: Gap Formula</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h5_1_2')">Hint 2: Multiplier</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h5_1_3')">Hint 3: 300 Injection</button>
          </div>
          <div class="hint-content-box" id="h5_1_1">
            <strong>Hint 1:</strong> Gap = Actual − Potential = 18,000 − 20,000 = −2,000 arvenies. As percentage: (−2,000 / 20,000) × 100 = −10%.
          </div>
          <div class="hint-content-box" id="h5_1_2">
            <strong>Hint 2:</strong> Multiplier $k = 1 / MPS = 1 / 0.20 = 5$. Required $\Delta I = \Delta Y / k = 2,000 / 5$.
          </div>
          <div class="hint-content-box" id="h5_1_3">
            <strong>Hint 3:</strong> If $\Delta I = 300$, then $\Delta Y = 300 \times 5 = 1,500$. New $Y = 18,000 + 1,500 = 19,500 < 20,000$.
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_5_1', 5)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_5_1">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Determine Arvania's output gap, calculate investment required to achieve potential GDP, and evaluate a 300 arvenie private capex surge.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • Potential GDP ($Y^*$) = 20,000 arvenies.<br>
                • Actual GDP ($Y$) = 18,000 arvenies.<br>
                • $MPS = 0.20 \implies MPC = 1 - 0.20 = 0.80$.<br>
                • Actual baseline investment = 3,600 arvenies.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA SELECTION</span>
              <div class="step-content">
                • $\text{Absolute Gap} = Y - Y^*$<br>
                • $\text{Percentage Gap} = [(Y - Y^*) / Y^*] × 100$<br>
                • Multiplier $k = 1 / MPS$<br>
                • $\Delta Y = k \times \Delta I \implies \Delta I_{\text{required}} = \Delta Y_{\text{target}} / k$
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION</span>
              <div class="step-content">
                <div class="step-math">
                  Part a: Output Gap & Required Stimulus:<br>
                  • Absolute Gap = 18,000 − 20,000 = −2,000 arvenies.<br>
                  • Percentage Gap = (−2,000 / 20,000) × 100 = −10.00%.<br>
                  • Nature: <strong>Recessionary Output Gap (Negative Output Gap)</strong>. Economy is operating below potential with idle capacity and elevated unemployment.<br>
                  • Spending Multiplier (k) = 1 / MPS = 1 / 0.20 = 5.<br>
                  • Additional investment required to close gap completely:<br>
                  ΔI = ΔY / k = 2,000 / 5 = 400 arvenies.<br><br>
                  Part b: Evaluation of 300 Arvenie Confidence Shock:<br>
                  • ΔY = k × ΔI = 5 × 300 = +1,500 arvenies.<br>
                  • New Equilibrium GDP = 18,000 + 1,500 = 19,500 arvenies.<br>
                  • Comparison with Potential: 19,500 < 20,000 arvenies.<br>
                  • Conclusion: The 300 arvenie investment surge is <strong>INSUFFICIENT</strong> to restore full potential output. A residual recessionary gap of 500 arvenies (−2.5%) remains.
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                In the Keynesian Cross framework, the aggregate expenditure function shifts upward by 300. The 45° line intersection moves from 18,000 to 19,500, falling short of the full employment coordinate $Y^* = 20,000$.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                Because households leak 20% of extra income into savings, a 300 arvenie injection creates ₹1,500 arvenies of induced spending. To fully bridge the remaining 500 arvenie gap, the government must provide an additional 100 arvenies of fiscal stimulus ($100 \times 5 = 500$).
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                • Output Gap = <strong>−2,000 arvenies (−10.00%, Recessionary Gap)</strong>.<br>
                • Required Investment to close gap = <strong>400 arvenies</strong>.<br>
                • Outcome of ΔI = 300: New GDP = 19,500; <strong>Fails to reach potential output</strong> (residual gap of 500 arvenies).
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="mission-card">
        <div class="mission-top-bar">
          <span class="mission-level-badge level-2">LEVEL 2 // STRATEGIC APPLICATION</span>
          <span class="topic-ref-tag">Business Cycles Case Study 2</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 5.2: Demeria Output Gap & Domestic Borrowing Shock</h3>
        <p class="mission-question">
          During the current year, the economy of Demeria recorded output worth 16,000 demries. The National Economic Council estimates that this represents 80% of the level of output that the economy can produce with its existing labour, capital, and technology.
          <br>At the current level of national income, savings amounts to 20%, while the MPC is 0.75. Firms' planned investment expenditure is given by: $I = 4,000 − 100r$. The prevailing real interest rate is 8%.
          <br>In response to current economic conditions, the government announces an additional expenditure of 500 demries.
          <br><br>
          <strong>Your Operational Directives:</strong><br>
          a. Estimate Demeria's sustainable level of output ($Y^*$). Calculate the prevailing output gap, and identify the economy's position in the business cycle.<br>
          b. Evaluate whether the initial 500 demries increase in government expenditure is sufficient to move the economy to its sustainable level of output.<br>
          c. Calculate the initial levels of saving and planned investment and verify whether the loanable funds market is in equilibrium. Suppose the additional government expenditure of 500 demries is financed entirely through domestic borrowing. Using the loanable funds framework, explain the likely effect on the equilibrium real interest rate and planned investment.
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h5_2_1')">Hint 1: Potential Output</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h5_2_2')">Hint 2: Fiscal Multiplier</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h5_2_3')">Hint 3: Loanable Funds</button>
          </div>
          <div class="hint-content-box" id="h5_2_1">
            <strong>Hint 1:</strong> Current output 16,000 = 80% of $Y^* \implies Y^* = 16,000 / 0.80 = 20,000$ demries. Gap = −4,000 demries.
          </div>
          <div class="hint-content-box" id="h5_2_2">
            <strong>Hint 2:</strong> $MPC = 0.75 \implies k = 1 / (1 - 0.75) = 4$. $\Delta Y = 4 \times 500 = 2,000$. New $Y = 18,000 < 20,000$.
          </div>
          <div class="hint-content-box" id="h5_2_3">
            <strong>Hint 3:</strong> At $r = 8\%$, $I = 4,000 - 100(8) = 3,200$. Savings = 20% of 16,000 = 3,200. Loanable funds is initially balanced. Borrowing shifts national saving left.
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_5_2', 5)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_5_2">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Audit Demeria's 80% capacity state, evaluate a 500 demries fiscal stimulus, and analyze loanable funds crowding out under domestic borrowing.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • Current Actual GDP ($Y$) = 16,000 demries.<br>
                • Capacity utilization = 80% of Potential GDP.<br>
                • $MPC = 0.75 \implies MPS = 0.25$.<br>
                • Savings rate = 20% of income; Investment function: $I = 4,000 - 100r$; $r = 8\%$.<br>
                • Proposed Fiscal Stimulus $\Delta G = 500$ demries financed by borrowing.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA SELECTION</span>
              <div class="step-content">
                • Potential Output $Y^* = Y / 0.80$<br>
                • $\text{Output Gap} = [(Y - Y^*) / Y^*] \times 100$<br>
                • Fiscal Multiplier $k_F = 1 / (1 - MPC)$<br>
                • Loanable Funds: $S = I$ at equilibrium.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION</span>
              <div class="step-content">
                <div class="step-math">
                  Part a: Sustainable Output, Gap, and Cycle Position:<br>
                  • Potential Output (Y*) = 16,000 / 0.80 = 20,000 demries.<br>
                  • Output Gap = 16,000 − 20,000 = −4,000 demries.<br>
                  • Percentage Gap = (−4,000 / 20,000) × 100 = −20.00%.<br>
                  • Cycle Position: <strong>Contraction / Recession Phase</strong>. Demeria is suffering from a massive 20% recessionary gap with widespread idle capacity.<br><br>
                  Part b: Sufficiency of 500 Demries Fiscal Stimulus:<br>
                  • Expenditure Multiplier (k) = 1 / (1 − 0.75) = 1 / 0.25 = 4.<br>
                  • Expansion in Output: ΔY = k × ΔG = 4 × 500 = +2,000 demries.<br>
                  • New Real Output = 16,000 + 2,000 = 18,000 demries.<br>
                  • Remaining Gap = 18,000 − 20,000 = −2,000 demries.<br>
                  • Verdict: The 500 demries stimulus is <strong>INSUFFICIENT</strong>. It closes only half the gap. The required stimulus to close the entire 4,000 demrie gap is ΔG = 4,000 / 4 = 1,000 demries.<br><br>
                  Part c: Loanable Funds & Crowding Out:<br>
                  • Initial Planned Investment: I = 4,000 − 100(8) = 4,000 − 800 = 3,200 demries.<br>
                  • Initial National Savings: S = 20% of 16,000 = 3,200 demries.<br>
                  • Since S = I = 3,200 demries, the loanable funds market is in <strong>EQUILIBRIUM</strong>.<br>
                  • Domestic Borrowing Impact: The government borrows 500 demries domestically to finance ΔG, causing a fiscal deficit. Government saving declines ($S_g \downarrow$), reducing national saving ($S = S_p + S_g$). The supply curve of loanable funds shifts LEFT. With investment demand unchanged, this creates an excess demand for loanable funds, driving the equilibrium real interest rate UP ($r \uparrow$). The higher interest rate increases borrowing costs for private firms, causing a movement up along the investment demand schedule and <strong>crowding out private corporate investment ($I \downarrow$)</strong>!
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                In the Loanable Funds diagram, the Saving supply schedule shifts leftward by 500. The intersection with the downward-sloping Investment schedule moves upward and to the left: real interest rate rises above 8%, while equilibrium loanable funds and private investment contract.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                Financing public expenditure via domestic bond sales cannibalizes domestic credit that would otherwise fund private corporate machinery, muting the full expansionary power of the fiscal multiplier.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                • Potential GDP = <strong>20,000 demries</strong>; Gap = <strong>−4,000 demries (−20.00%, Recession)</strong>.<br>
                • Proposed ΔG = 500 achieves ΔY = 2,000; <strong>Insufficient</strong> (leaves −2,000 residual gap).<br>
                • Initial $S = I = 3,200$ (in equilibrium).<br>
                • Domestic borrowing shifts $S$ left $\implies r \uparrow$, causing <strong>crowding out of private investment</strong>.
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="mission-card">
        <div class="mission-top-bar">
          <span class="mission-level-badge level-3">LEVEL 3 // ADVANCED COMPARATIVE MISSION</span>
          <span class="topic-ref-tag">Business Cycles Case Study 3</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 5.3: Arvania vs Beloria Dual Economy Policy Battle</h3>
        <p class="mission-question">
          The following intelligence data is reported for the adjacent economies of Arvania and Beloria:
          <br>• Potential GDP: Arvania = ₹12,000 crore; Beloria = ₹12,000 crore.
          <br>• Actual GDP: Arvania = ₹10,800 crore; Beloria = ₹12,600 crore.
          <br>• Saving: Arvania = ₹3,000 crore; Beloria = ₹3,000 crore.
          <br>• Planned Investment: Arvania = ₹3,000 crore; Beloria = ₹3,000 crore.
          <br>• Real Interest Rate: Arvania = 6%; Beloria = 6%.
          <br>• MPC: Arvania = 0.80; Beloria = 0.60.
          <br><br>
          During the year, both economies implement policy adjustments:
          <br>• In <strong>Arvania</strong>, improved business confidence leads to an autonomous increase in planned investment of ₹400 crore.
          <br>• In <strong>Beloria</strong>, the government implements a contractionary fiscal measure by raising lump-sum taxes by ₹400 crore.
          <br><br>
          <strong>Your Operational Directives:</strong><br>
          a. Calculate the output gap in each economy and identify their respective stages in the business cycle.<br>
          b. Using the Saving–Investment framework, illustrate how the changes affect the saving and investment curves, real interest rates, and loanable funds quantity.<br>
          c. Calculate the change in equilibrium GDP resulting from Arvania's ₹400 crore investment surge and Beloria's ₹400 crore tax hike. Determine the new output gap in each economy and assess whether each economy moves towards, reaches, or moves beyond its potential GDP.
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h5_3_1')">Hint 1: Gaps</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h5_3_2')">Hint 2: Multipliers</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h5_3_3')">Hint 3: Tax Multiplier</button>
          </div>
          <div class="hint-content-box" id="h5_3_1">
            <strong>Hint 1:</strong> Arvania Gap = (10,800 − 12,000) / 12,000 = −10% (Recession). Beloria Gap = (12,600 − 12,000) / 12,000 = +5% (Boom/Overheating).
          </div>
          <div class="hint-content-box" id="h5_3_2">
            <strong>Hint 2:</strong> Arvania: $MPC = 0.80 \implies k_I = 1 / (1 - 0.80) = 5$. $\Delta Y = 5 \times 400 = +2,000$.
          </div>
          <div class="hint-content-box" id="h5_3_3">
            <strong>Hint 3:</strong> Beloria: $MPC = 0.60 \implies k_T = -MPC / (1 - MPC) = -0.60 / 0.40 = -1.5$. $\Delta Y = -1.5 \times (+400) = -600$.
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_5_3', 5)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_5_3">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Perform comparative macroeconomic audit of Arvania and Beloria, analyze loanable funds shifts, calculate multiplier effects, and evaluate gap convergence.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • Arvania: $Y^* = 12,000; Y = 10,800; S = 3,000; I = 3,000; r = 6\%; MPC = 0.80; \Delta I = +400$ cr.<br>
                • Beloria: $Y^* = 12,000; Y = 12,600; S = 3,000; I = 3,000; r = 6\%; MPC = 0.60; \Delta T = +400$ cr.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA SELECTION</span>
              <div class="step-content">
                • $\text{Output Gap} = [(Y - Y^*) / Y^*] \times 100$<br>
                • Investment Multiplier: $k_I = 1 / (1 - MPC)$<br>
                • Tax Multiplier: $k_T = -MPC / (1 - MPC)$<br>
                • $\Delta Y = \text{Multiplier} \times \Delta \text{Injection/Withdrawal}$
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION</span>
              <div class="step-content">
                <div class="step-math">
                  Part a: Output Gaps & Cycle Stages:<br>
                  • Arvania Gap = [(10,800 − 12,000) / 12,000] × 100 = (−1,200 / 12,000) × 100 = −10.00%.<br>
                  Stage: <strong>Recession / Contraction Phase</strong> (Recessionary Gap of ₹1,200 crore).<br><br>
                  • Beloria Gap = [(12,600 − 12,000) / 12,000] × 100 = (+600 / 12,000) × 100 = +5.00%.<br>
                  Stage: <strong>Expansion / Peak Phase</strong> (Inflationary Gap of ₹600 crore).<br><br>
                  Part b: Saving–Investment Loanable Funds Impact:<br>
                  • Arvania: Autonomous investment increases by ₹400 crore. The Investment schedule shifts RIGHT. With the saving schedule unchanged, this creates an excess demand for loanable funds at 6%, driving the real interest rate UP ($r \uparrow$) and increasing the equilibrium quantity of loanable funds.<br>
                  • Beloria: Taxes increase by ₹400 crore. Higher taxes reduce household disposable income ($Y_d \downarrow$), causing private saving to decline by $MPS \times \Delta T = 0.40 \times 400 = 160$ crore, while government saving increases by $\Delta T = 400$ crore. National saving ($S = S_p + S_g$) increases on net by $+240$ crore. The saving curve shifts RIGHT, lowering the equilibrium real interest rate ($r \downarrow$) and expanding loanable funds.<br><br>
                  Part c: Multipliers and Final Gap Outcomes:<br>
                  • Arvania Investment Multiplier: k_I = 1 / (1 − 0.80) = 1 / 0.20 = 5.<br>
                  ΔY = 5 × ₹400 = +₹2,000 crore.<br>
                  New GDP = 10,800 + 2,000 = ₹12,800 crore.<br>
                  New Output Gap = [(12,800 − 12,000) / 12,000] × 100 = (+800 / 12,000) × 100 = +6.67%.<br>
                  Verdict: Arvania <strong>MOVES BEYOND</strong> its potential GDP, converting a −10% recessionary gap into a +6.67% inflationary gap!<br><br>
                  • Beloria Tax Multiplier: k_T = −0.60 / (1 − 0.60) = −0.60 / 0.40 = −1.5.<br>
                  ΔY = −1.5 × ₹400 = −₹600 crore.<br>
                  New GDP = 12,600 − 600 = ₹12,000 crore.<br>
                  New Output Gap = [(12,000 − 12,000) / 12,000] × 100 = 0.00%.<br>
                  Verdict: Beloria's policy is <strong>EXACTLY SUFFICIENT</strong>. It eliminates the inflationary gap and causes the economy to <strong>REACH ITS POTENTIAL GDP PERFECTLY</strong>!
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                In Arvania, the expenditure curve shifts up by 400, overshooting the 45° line potential intersection. In Beloria, the expenditure curve shifts down by $0.60 \times 400 = 240$, locking in at exactly $Y = 12,000$.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                Because Arvania had a high MPC (0.80), the investment multiplier was huge (5), overshooting potential. Beloria's lower MPC (0.60) gave a moderate tax multiplier of -1.5, allowing calibrated precision in eliminating the ₹600 cr inflationary gap.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                • Arvania: Initial gap = <strong>−10.00%</strong>; New GDP = <strong>₹12,800 cr</strong>; <strong>Moves BEYOND potential</strong> (+6.67% inflationary gap).<br>
                • Beloria: Initial gap = <strong>+5.00%</strong>; New GDP = <strong>₹12,000 cr</strong>; <strong>EXACTLY REACHES potential</strong> (0.00% gap).
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
          <h3 class="topic-title">Chapter 5 Solutions & Policy Response Archive</h3>
          <span class="topic-ref-tag">TARGET PROTOCOL: 7-STEP VERIFICATION</span>
        </div>
        <p class="content-text">
          Always check whether a policy stimulus is insufficient, exactly sufficient, or overshoots potential output! Remember that tax multipliers are always negative and smaller in absolute magnitude than government spending multipliers.
        </p>
      </div>
    </div>
  </div>
</div>
"""
