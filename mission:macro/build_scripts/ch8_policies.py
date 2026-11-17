# build_scripts/ch8_policies.py
"""
Project 007: Chapter 8 — Fiscal Policy and Monetary Policy
Exhaustive academic content strictly from Prof. Sana Tabassum lecture slides,
including RBI policy rate mechanisms, Nutria CRR cut case, and coordinated policy mix.
"""

def get_chapter_8():
    return r"""
<!-- CHAPTER 8: FISCAL POLICY AND MONETARY POLICY -->
<div class="chapter-container" id="chapter-8">
  <a id="ch8" class="chapter-anchor"></a>
  <div class="chapter-header">
    <div class="ch-badge-group">
      <span class="ch-code-pill">DOSSIER 08 // INTEL-POLICIES</span>
      <h2 class="ch-title">Chapter 8 — Fiscal Policy & Monetary Policy</h2>
    </div>
    <div class="chapter-actions">
      <button class="ch-mastery-btn" id="ch-mastery-badge-8" onclick="toggleProgressItem(8, 'training', {checked: true})">IN PROGRESS</button>
    </div>
  </div>

  <div class="chapter-nav-tabs">
    <button class="ch-tab-btn active" data-tab="all" onclick="switchChapterTab(8, 'all')">ALL INTEL</button>
    <button class="ch-tab-btn" data-tab="training" onclick="switchChapterTab(8, 'training')">TRAINING (THE BRIEFING)</button>
    <button class="ch-tab-btn" data-tab="missions" onclick="switchChapterTab(8, 'missions')">MISSIONS (ACTIVE OPS)</button>
    <button class="ch-tab-btn" data-tab="targets" onclick="switchChapterTab(8, 'targets')">TARGETS (DEBRIEFING)</button>
  </div>

  <div class="chapter-body">
    <!-- ==================== TRAINING ENVIRONMENT ==================== -->
    <div class="training-section">
      <div class="topic-card">
        <div class="topic-header">
          <h3 class="topic-title">8.1 Fiscal Policy: Mandate, Instruments & Transmission</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Business Cycles & IS Decks</span>
        </div>
        <p class="content-lead">
          <strong>Fiscal Policy</strong> is the strategic use of government taxation ($T$), expenditure ($G$), and transfer payments ($TR$) to influence aggregate demand, resource allocation, and macroeconomic stabilization.
        </p>

        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th>Fiscal Posture</th>
                <th>When Deployed</th>
                <th>Policy Levers Executed</th>
                <th>Macroeconomic Transmission Sequence</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Expansionary Fiscal Policy</strong></td>
                <td>During <strong>Recessionary Gaps ($Y < Y^*$)</strong> and cyclical slumps.</td>
                <td>• <strong>Increase Government Spending ($G \uparrow$)</strong><br>• <strong>Cut Taxes ($T \downarrow$)</strong><br>• Increase Transfer Payments ($TR \uparrow$)</td>
                <td>Direct injection into Goods Market $\implies$ Multiplier sequence activated $\implies$ Disposable income ($Y_d$) rises $\implies C \uparrow, AD$ shifts RIGHT $\implies$ Real GDP ($Y$) expands, unemployment falls.</td>
              </tr>
              <tr>
                <td><strong>Contractionary Fiscal Policy</strong></td>
                <td>During <strong>Inflationary Gaps ($Y > Y^*$)</strong> and economic overheating.</td>
                <td>• <strong>Reduce Government Spending ($G \downarrow$)</strong><br>• <strong>Increase Taxes ($T \uparrow$)</strong><br>• Curtail Transfers ($TR \downarrow$)</td>
                <td>Withdraws purchasing power from spending flow $\implies$ Disposable income falls $\implies C \downarrow, AD$ shifts LEFT $\implies$ Aggregate output cools back to potential, dampening inflation.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="topic-card">
        <div class="topic-header">
          <a id="ch8-monetary-policy"></a>
          <h3 class="topic-title">8.2 Monetary Policy: Central Banking Levers & Transmission</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum IS-LM Deck & AD Deck</span>
        </div>
        <p class="content-text">
          <strong>Monetary Policy</strong> is the management of the money supply, interest rates, and banking liquidity by the nation's Central Bank (such as the Reserve Bank of India or US Federal Reserve) to achieve price stability and sustainable growth.
        </p>

        <h4 class="section-subtitle">The Official Hierarchy of Money Aggregates</h4>
        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th>Money Measure</th>
                <th>Official Components Included</th>
                <th>Liquidity Level</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>$M_0$ (High-Powered Money)</strong></td>
                <td>Currency in circulation + Bankers' deposits with RBI + 'Other' deposits with RBI.</td>
                <td>Monetary Base / Reserve Money</td>
              </tr>
              <tr>
                <td><strong>$M_1$ (Narrow Money)</strong></td>
                <td>Currency with the public + Demand deposits with commercial banking system.</td>
                <td><strong>Highest Liquidity</strong></td>
              </tr>
              <tr>
                <td><strong>$M_2$</strong></td>
                <td>$M_1$ + Savings deposits with Post Office Savings Banks.</td>
                <td>High Liquidity</td>
              </tr>
              <tr>
                <td><strong>$M_3$ (Broad Money)</strong></td>
                <td>$M_1$ + Time deposits (fixed deposits) with the commercial banking system.</td>
                <td>Primary Monetary Target (Lower liquidity)</td>
              </tr>
              <tr>
                <td><strong>$M_4$</strong></td>
                <td>$M_3$ + All deposits with Post Office Savings Banks (excluding National Savings Certificates).</td>
                <td>Least Liquid Broad Measure</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h4 class="section-subtitle">Core Central Bank Policy Levers</h4>
        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th>Central Bank Lever</th>
                <th>Definition & Operational Function</th>
                <th>Expansionary Stance</th>
                <th>Contractionary Stance</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Repo Rate (Policy Rate)</strong></td>
                <td>The benchmark interest rate at which the central bank lends short-term funds to commercial banks against government collateral.</td>
                <td><strong>CUT Repo Rate (↓)</strong><br>Lowers commercial bank borrowing costs $\implies$ lending rates drop.</td>
                <td><strong>HIKE Repo Rate (↑)</strong><br>Raises commercial bank borrowing costs $\implies$ loans become expensive.</td>
              </tr>
              <tr>
                <td><strong>Cash Reserve Ratio (CRR)</strong></td>
                <td>The mandatory percentage of net demand and time liabilities that commercial banks must hold in cash reserves with the central bank.</td>
                <td><strong>REDUCE CRR (↓)</strong><br>Releases billions in vault cash into commercial bank lending pipelines.</td>
                <td><strong>INCREASE CRR (↑)</strong><br>Impounds commercial bank liquidity, restricting loan expansion.</td>
              </tr>
              <tr>
                <td><strong>Open Market Operations (OMO)</strong></td>
                <td>Outright central bank purchase or sale of government securities in open capital markets.</td>
                <td><strong>PURCHASE Securities</strong><br>Injects central bank cash into commercial bank reserve accounts.</td>
                <td><strong>SELL Securities</strong><br>Drains cash from the banking system into central bank vaults.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="topic-card">
        <div class="topic-header">
          <h3 class="topic-title">8.3 Master Comparative Policy Matrix</h3>
          <span class="topic-ref-tag">REF: Synthesized from Primary Lecture Frameworks</span>
        </div>
        <p class="content-text">
          Memorize the exact transmission outcomes across all four policy stances for university examinations:
        </p>
        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th>Macroeconomic Variable</th>
                <th>Expansionary Fiscal ($G \uparrow, T \downarrow$)</th>
                <th>Contractionary Fiscal ($G \downarrow, T \uparrow$)</th>
                <th>Expansionary Monetary (Repo $\downarrow$, CRR $\downarrow$)</th>
                <th>Contractionary Monetary (Repo $\uparrow$, CRR $\uparrow$)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Aggregate Output ($Y$)</strong></td>
                <td><strong style="color:var(--success-emerald);">EXPANDS (↑)</strong></td>
                <td><strong style="color:var(--bond-crimson);">CONTRACTS (↓)</strong></td>
                <td><strong style="color:var(--success-emerald);">EXPANDS (↑)</strong></td>
                <td><strong style="color:var(--bond-crimson);">CONTRACTS (↓)</strong></td>
              </tr>
              <tr>
                <td><strong>Price Level ($P$)</strong></td>
                <td><strong style="color:var(--bond-crimson);">RISES (↑)</strong></td>
                <td><strong style="color:var(--success-emerald);">FALLS (↓)</strong></td>
                <td><strong style="color:var(--bond-crimson);">RISES (↑)</strong></td>
                <td><strong style="color:var(--success-emerald);">FALLS (↓)</strong></td>
              </tr>
              <tr>
                <td><strong>Real Interest Rate ($r$)</strong></td>
                <td><strong style="color:var(--bond-crimson);">RISES (↑)</strong><br>(due to borrowing/money demand)</td>
                <td><strong style="color:var(--success-emerald);">FALLS (↓)</strong></td>
                <td><strong style="color:var(--success-emerald);">FALLS (↓)</strong><br>(due to expanded liquidity)</td>
                <td><strong style="color:var(--bond-crimson);">RISES (↑)</strong></td>
              </tr>
              <tr>
                <td><strong>Private Investment ($I$)</strong></td>
                <td><strong style="color:var(--bond-crimson);">FALLS (↓)</strong><br>(Crowded out by higher $r$)</td>
                <td><strong style="color:var(--success-emerald);">RISES (↑)</strong><br>(Crowded in by lower $r$)</td>
                <td><strong style="color:var(--success-emerald);">RISES (↑)</strong><br>(Stimulated by lower $r$)</td>
                <td><strong style="color:var(--bond-crimson);">FALLS (↓)</strong><br>(Choked by higher $r$)</td>
              </tr>
              <tr>
                <td><strong>Unemployment ($u$)</strong></td>
                <td><strong style="color:var(--success-emerald);">FALLS (↓)</strong></td>
                <td><strong style="color:var(--bond-crimson);">RISES (↑)</strong></td>
                <td><strong style="color:var(--success-emerald);">FALLS (↓)</strong></td>
                <td><strong style="color:var(--bond-crimson);">RISES (↑)</strong></td>
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
          <span class="mission-level-badge level-2">LEVEL 2 // STRATEGIC APPLICATION</span>
          <span class="topic-ref-tag">AD-AS Deck Case Study 2 Nutria</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 8.1: Central Bank CRR Cut & Capex Revival in Nutria</h3>
        <p class="mission-question">
          After a soft patch, inflation in the country of Nutria cooled to 3.0%, and capacity utilization fell below potential output. To support demand, the Central Bank of Nutria cut the Cash Reserve Ratio (CRR) by 2%, easing bank liquidity and reducing lending rates. Consequently, commercial firms revived capex plans, and planned private investment increased by 200.
          <br>At the time that the policy was implemented, actual GDP was 8,600 and MPS was 0.20.
          <br><br>
          <strong>Your Operational Directives:</strong><br>
          a. Using the AD–AS framework, show how the policy affects equilibrium output and the price level.<br>
          b. Identify the type of output gap existing before the policy implementation.<br>
          c. Compute the potential GDP ($Y^*$) of the economy, assuming this monetary intervention was calibrated to restore long-run full employment.
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h8_1_1')">Hint 1: Transmission</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h8_1_2')">Hint 2: Multiplier</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h8_1_3')">Hint 3: Potential GDP</button>
          </div>
          <div class="hint-content-box" id="h8_1_1">
            <strong>Hint 1:</strong> CRR cut $\implies$ excess bank reserves $\implies$ market lending rates fall $\implies$ planned investment rises by 200 $\implies AD$ shifts right.
          </div>
          <div class="hint-content-box" id="h8_1_2">
            <strong>Hint 2:</strong> $k_I = 1 / MPS = 1 / 0.20 = 5$. $\Delta Y = 5 \times 200 = 1,000$.
          </div>
          <div class="hint-content-box" id="h8_1_3">
            <strong>Hint 3:</strong> If the 200 capex boost exactly closes the recessionary gap, then Potential GDP = Actual + $\Delta Y = 8,600 + 1,000 = 9,600$.
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_8_1', 8)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_8_1">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Analyze monetary transmission of a 2% CRR cut in Nutria, determine initial output gap, and calculate potential GDP.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • Initial Actual GDP ($Y_0$) = 8,600.<br>
                • Inflation = 3.0% (subdued).<br>
                • CRR cut = 2.0% $\implies$ Private investment increases by $\Delta I = 200$.<br>
                • $MPS = 0.20 \implies MPC = 0.80$.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA SELECTION</span>
              <div class="step-content">
                • Investment Multiplier: $k_I = 1 / MPS$<br>
                • $\Delta Y = k_I \times \Delta I$<br>
                • $\text{Potential GDP } (Y^*) = Y_0 + \Delta Y$
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION</span>
              <div class="step-content">
                <div class="step-math">
                  a. AD–AS Framework Transmission:<br>
                  • Central Bank cuts CRR by 2% ⇒ Required bank reserves decrease, creating substantial excess liquidity in the commercial banking system.<br>
                  • Interbank money market rates and commercial loan lending rates drop.<br>
                  • Lower financing costs encourage corporate capex, expanding private investment by 200.<br>
                  • AD = C + I + G shifts RIGHT.<br>
                  • In the short run, the intersection with upward-sloping SRAS moves to the right: Real Output (Y) rises and the Price Level (P) edges modestly upward.<br><br>
                  b. Identification of Pre-Policy Output Gap:<br>
                  Because capacity utilization was depressed, actual output was below sustainable full-employment output. This is a <strong>Recessionary Output Gap (Negative Output Gap)</strong>.<br><br>
                  c. Computation of Potential GDP:<br>
                  • Multiplier (k_I) = 1 / MPS = 1 / 0.20 = 5.<br>
                  • Expansion in Output: ΔY = k_I × ΔI = 5 × 200 = +1,000.<br>
                  • New Equilibrium GDP = 8,600 + 1,000 = 9,600.<br>
                  • Potential GDP (Y*) = 9,600.<br>
                  • Initial Gap was −1,000 (or −10.42% of potential).
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                AD–AS diagram: Initial equilibrium $E_0$ lies to the left of vertical LRAS at $Y = 8,600$. The CRR-induced capex surge shifts AD rightward, bringing the new short-run equilibrium $E_1$ onto the LRAS curve at $Y^* = 9,600$.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                Because inflation was low (3.0%), the central bank had ample headroom to inject liquidity. The 200 capex injection activated five rounds of multiplier spending, absorbing idle capacity without generating high inflation.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                • Policy effect: AD shifts right $\implies Y \uparrow$ to 9,600, $P$ rises modestly.<br>
                • Gap type: <strong>Recessionary Gap (−1,000 units)</strong>.<br>
                • Potential GDP = <strong>9,600 units</strong>.
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="mission-card">
        <div class="mission-top-bar">
          <span class="mission-level-badge level-3">LEVEL 3 // ADVANCED STRATEGIC MISSION</span>
          <span class="topic-ref-tag">IS-LM Deck RBI Bulletin Case Question 4</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 8.2: Coordinated Policy Mix to Revive Private Investment</h3>
        <p class="mission-question">
          The Indian economy is operating close to its potential output, with national income remaining stable. However, private investment continues to be sluggish. Policymakers aim to encourage private investment without creating additional demand pressures (inflation) in the economy.
          <br><br>
          <strong>Your Operational Directives (Official RBI Case Mandate):</strong><br>
          1. Explain why independent fiscal or independent monetary policy interventions will FAIL to increase private investment while keeping national income unchanged.<br>
          2. Formulate an appropriate coordinated fiscal–monetary policy mix that successfully achieves both objectives simultaneously.<br>
          3. Explain the transmission sequence and illustrate the resulting equilibrium on national income, real interest rates, and private investment.
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h8_2_1')">Hint 1: Single Policy Failure</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h8_2_2')">Hint 2: Coordinated Mix</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h8_2_3')">Hint 3: Interest Rate Key</button>
          </div>
          <div class="hint-content-box" id="h8_2_1">
            <strong>Hint 1:</strong> If you use expansionary fiscal policy ($G \uparrow$), interest rates rise and crowd out investment. If you use expansionary monetary policy alone ($M \uparrow$), output expands beyond potential, causing inflation.
          </div>
          <div class="hint-content-box" id="h8_2_2">
            <strong>Hint 2:</strong> Combine Contractionary Fiscal Policy ($G \downarrow$ or $T \uparrow$) with Expansionary Monetary Policy ($M \uparrow$).
          </div>
          <div class="hint-content-box" id="h8_2_3">
            <strong>Hint 3:</strong> $IS$ shifts left while $LM$ shifts right. Both push real interest rate $r$ DOWN, while their output effects cancel out, leaving $Y$ stable at potential GDP!
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_8_2', 8)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_8_2">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Design an optimal macroeconomic policy mix that expands private corporate investment while preserving national income at potential output ($Y^*$).</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • Target 1: Increase private investment ($I \uparrow$).<br>
                • Target 2: Maintain national income unchanged at potential output ($Y = Y^*$).<br>
                • Constraint: Avoid demand-pull inflation.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA & MODEL SELECTION</span>
              <div class="step-content">
                • Investment function: $I = I_0 - br$ (Private investment rises IF AND ONLY IF interest rate $r$ falls).<br>
                • Framework: IS–LM General Equilibrium.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION (OFFICIAL ANSWER KEY METHODOLOGY)</span>
              <div class="step-content">
                <div class="step-math">
                  1. Failure of Independent Policies:<br>
                  • Independent Fiscal Expansion (G↑): Shifts IS rightward. While this raises income, it drives interest rates UP (r↑), which crowds out private investment! Private investment falls, violating Target 1.<br>
                  • Independent Monetary Expansion (M↑): Shifts LM rightward. While this lowers interest rates (r↓) and stimulates investment, it increases national income beyond potential (Y > Y*), creating an inflationary gap and overheating, violating Target 2.<br><br>
                  2. The Coordinated Policy Mix Formulation:<br>
                  The optimal solution is a <strong>Tight Fiscal Policy coupled with an Easy Monetary Policy</strong>:<br>
                  <strong>• Contractionary Fiscal Policy:</strong> The government reduces spending (G↓) or increases taxes (T↑), shifting the IS curve LEFTWARD (from IS₀ to IS₁).<br>
                  <strong>• Expansionary Monetary Policy:</strong> Simultaneously, the RBI cuts repo rates / increases liquidity, shifting the LM curve RIGHTWARD (from LM₀ to LM₁).<br><br>
                  3. Transmission & Final Equilibrium:<br>
                  • Effect on Interest Rates: Both policies exert unambiguous downward pressure on borrowing costs (IS left lowers r; LM right lowers r). The equilibrium real interest rate plunges from r₀ to r₁.<br>
                  • Effect on Private Investment: Because r falls substantially, borrowing becomes cheap, causing private corporate investment to expand dramatically: I₁ = I₀ − br₁ > I₀.<br>
                  • Effect on National Income: The contractionary impulse of fiscal policy is exactly offset by the expansionary impulse of monetary policy. National income remains stable at potential output: Y₁ = Y₀ = Y*!
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                In the IS–LM diagram, $IS_0$ shifts left to $IS_1$ and $LM_0$ shifts right to $LM_1$. The new intersection point $E_1$ sits vertically directly beneath $E_0$: identical horizontal coordinate ($Y^*$), but drastically lower vertical coordinate ($r_1 < r_0$).
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                This coordinated mix re-engineers the composition of aggregate demand: Government consumption ($G$) is curtailed, freeing up domestic financial savings and physical resources, which are simultaneously mobilized into private capital formation ($I$) via lower interest rates.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                <strong>Policy Mix Formula:</strong> <strong>Contractionary Fiscal ($IS \leftarrow$) + Expansionary Monetary ($LM \rightarrow$)</strong>.<br>
                • National Income ($Y$): <strong>UNCHANGED ($Y = Y^*$)</strong>.<br>
                • Real Interest Rate ($r$): <strong>DECREASES SUBSTANTIALLY</strong>.<br>
                • Private Investment ($I$): <strong>INCREASES EXPONENTIALLY</strong>.
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
          <h3 class="topic-title">Chapter 8 Policy Toolkit & Coordination Dossier</h3>
          <span class="topic-ref-tag">TARGET PROTOCOL: 7-STEP VERIFICATION</span>
        </div>
        <p class="content-text">
          Remember the vital policy takeaway: Fiscal policy affects $Y$ directly via goods-market expenditure, but shifts $r$ in the same direction. Monetary policy affects $r$ directly via money-market liquidity, shifting $r$ in the opposite direction!
        </p>
      </div>
    </div>
  </div>
</div>
"""
