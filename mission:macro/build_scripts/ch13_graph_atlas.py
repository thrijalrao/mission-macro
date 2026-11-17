"""
PROJECT 007: THE MACROECONOMICS INTELLIGENCE FILE
Chapter 13 Exclusive Module: Master Graphical Intelligence Atlas
16 Comprehensive Vector Conceptual Blueprints of Macroeconomic Shifts & Transmission Mechanisms
Authoritative Reference: TAPMI BBA Macroeconomics Syllabus (Prof. Sana Tabassum & Prof. Abhishek Kumar Rohit)
"""

def get_graphical_atlas_html():
    return r'''
    <div class="graphical-atlas-container">
      <div class="atlas-header-banner">
        <div class="atlas-badge">TOP SECRET // REVISION COMPENDIUM</div>
        <h2 class="atlas-title">007 MASTER GRAPHICAL INTELLIGENCE ATLAS</h2>
        <p class="atlas-subtitle">
          16 Authoritative Vector Conceptual Blueprints: Before & After Shifting Curves, Equilibrium Target Crosshairs, Transmission Sequences & Exam Pitfalls.
        </p>
      </div>

      <!-- QUICK NAVIGATION MATRIX -->
      <div class="atlas-quick-nav">
        <span class="quick-nav-label">SELECT BLUEPRINT REGIME:</span>
        <a href="#atlas-sec-islm" class="quick-nav-pill">I. IS-LM GENERAL EQUILIBRIUM (7 SCENARIOS)</a>
        <a href="#atlas-sec-adas" class="quick-nav-pill">II. AD-AS SHOCKS & SELF-CORRECTION (5 SCENARIOS)</a>
        <a href="#atlas-sec-markets" class="quick-nav-pill">III. GOODS & MONEY MARKETS (3 SCENARIOS)</a>
        <a href="#atlas-sec-phillips" class="quick-nav-pill">IV. THE PHILLIPS CURVE & EXPECTATIONS</a>
      </div>

      <!-- ========================================================================= -->
      <!-- SECTION I: THE IS-LM GENERAL EQUILIBRIUM FRAMEWORK -->
      <!-- ========================================================================= -->
      <div class="atlas-section-group" id="atlas-sec-islm">
        <div class="atlas-group-header">
          <span class="group-num">REGIME I</span>
          <h3 class="group-title">THE IS-LM GENERAL EQUILIBRIUM FRAMEWORK (GOODS & MONEY MARKET INTERACTION)</h3>
          <p class="group-desc">Authoritative Reference: Prof. Sana Tabassum IS-LM Deck. General equilibrium occurs where the Goods Market (IS) and Money Market (LM) clear simultaneously at interest rate $r^*$ and output $Y^*$.</p>
        </div>

        <!-- SCENARIO 1: EXPANSIONARY FISCAL POLICY & CROWDING OUT -->
        <div class="atlas-card" id="atlas-scen-1">
          <div class="atlas-card-header">
            <span class="scen-badge">BLUEPRINT 01 // FISCAL STIMULUS</span>
            <h4 class="scen-title">Expansionary Fiscal Policy ($\uparrow G$ or $\downarrow T$) & The Crowding-Out Mechanism</h4>
            <span class="scen-ref">REF: Unit 3, Slides 18-24</span>
          </div>

          <div class="atlas-grid">
            <div class="atlas-svg-panel">
              <svg viewBox="0 0 540 320" xmlns="http://www.w3.org/2000/svg" class="atlas-svg">
                <!-- Grid background -->
                <rect width="540" height="320" fill="#090a0f" rx="6"/>
                <line x1="50" y1="270" x2="510" y2="270" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <line x1="60" y1="280" x2="60" y2="30" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <!-- Axis labels -->
                <text x="510" y="295" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" text-anchor="end">REAL OUTPUT (Y)</text>
                <text x="25" y="45" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" transform="rotate(-90 25,45)" text-anchor="end">INTEREST RATE (r %)</text>

                <!-- LM Curve (Fixed) -->
                <line x1="100" y1="250" x2="440" y2="70" stroke="#f59e0b" stroke-width="2.5"/>
                <text x="445" y="70" fill="#f59e0b" font-family="var(--font-mono)" font-size="12" font-weight="700">LM₀</text>

                <!-- Baseline IS0 Curve -->
                <line x1="100" y1="70" x2="400" y2="250" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>
                <text x="405" y="255" fill="#38bdf8" font-family="var(--font-mono)" font-size="12">IS₀</text>

                <!-- Shifted IS1 Curve -->
                <line x1="180" y1="70" x2="480" y2="250" stroke="#38bdf8" stroke-width="2.5"/>
                <text x="485" y="255" fill="#38bdf8" font-family="var(--font-mono)" font-size="12" font-weight="700">IS₁ (ΔG > 0)</text>

                <!-- Shift Arrow -->
                <line x1="280" y1="120" x2="330" y2="120" stroke="#38bdf8" stroke-width="2"/>
                <polygon points="330,116 338,120 330,124" fill="#38bdf8"/>

                <!-- Projections & Crosshair E0 -->
                <line x1="60" y1="178" x2="242" y2="178" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <line x1="242" y1="178" x2="242" y2="270" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <text x="50" y="182" fill="#94a3b8" font-family="var(--font-mono)" font-size="11" text-anchor="end">r₀</text>
                <text x="242" y="286" fill="#94a3b8" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Y₀</text>

                <!-- Crosshair E0 -->
                <circle cx="242" cy="178" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="242" cy="178" r="2.5" fill="#d92534"/>
                <line x1="230" y1="178" x2="254" y2="178" stroke="#d92534" stroke-width="1.2"/>
                <line x1="242" y1="166" x2="242" y2="190" stroke="#d92534" stroke-width="1.2"/>
                <text x="252" y="172" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₀</text>

                <!-- E1: intersection of IS1 & LM0 -->
                <line x1="60" y1="140" x2="312" y2="140" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <line x1="312" y1="140" x2="312" y2="270" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <text x="50" y="144" fill="#38bdf8" font-family="var(--font-mono)" font-size="11" text-anchor="end">r₁</text>
                <text x="312" y="286" fill="#38bdf8" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Y₁</text>

                <!-- Crosshair E1 -->
                <circle cx="312" cy="140" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="312" cy="140" r="2.5" fill="#d92534"/>
                <line x1="300" y1="140" x2="324" y2="140" stroke="#d92534" stroke-width="1.2"/>
                <line x1="312" y1="128" x2="312" y2="152" stroke="#d92534" stroke-width="1.2"/>
                <text x="322" y="134" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₁</text>

                <!-- Full Multiplier Point (Hypothetical without crowding out) -->
                <line x1="390" y1="178" x2="390" y2="270" stroke="#ef4444" stroke-dasharray="2,2"/>
                <circle cx="390" cy="178" r="4" fill="none" stroke="#ef4444" stroke-width="1.5"/>
                <text x="390" y="286" fill="#ef4444" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Y_Keynes</text>

                <!-- Crowding out horizontal bracket -->
                <line x1="312" y1="258" x2="390" y2="258" stroke="#ef4444" stroke-width="1.5"/>
                <text x="351" y="252" fill="#ef4444" font-family="var(--font-mono)" font-size="9" text-anchor="middle">CROWDED OUT</text>
              </svg>
            </div>

            <div class="atlas-text-panel">
              <div class="intel-block">
                <span class="block-tag">EXAM SITUATION / SCENARIO TRIGGER</span>
                <p>The Ministry of Finance passes a massive ₹50,000 crore infrastructure stimulus package ($\Delta G > 0$) funded by domestic borrowing, or slashes corporate tax rates ($\Delta T < 0$).</p>
              </div>

              <div class="intel-block">
                <span class="block-tag">MARKET-BY-MARKET TRANSMISSION CHAIN</span>
                <ol class="transmission-list">
                  <li><strong>Goods Market Shock:</strong> Autonomous expenditure increases. Planned spending exceeds output ($AE > Y$). Firms expand production via the Keynesian multiplier. The <strong>IS curve shifts horizontally right</strong> by $\Delta Y = k_G \times \Delta G = \frac{1}{1-MPC} \Delta G$.</li>
                  <li><strong>Money Market Reaction:</strong> As national income surges ($Y \uparrow$), transaction demand for money increases ($M_d = kY - hr$). With nominal money supply fixed by the Central Bank ($M/P$ constant), agents experience an <em>excess demand for money</em>.</li>
                  <li><strong>Interest Rate Adjustment:</strong> Agents sell government bonds to obtain liquidity. Bond prices collapse, bidding market interest rates upward ($r_0 \to r_1$).</li>
                  <li><strong>Feedback on Private Sector:</strong> Rising borrowing costs make capital investment projects unviable. Private firms curtail planned investment ($\Delta I = -b \cdot \Delta r < 0$).</li>
                  <li><strong>Final Equilibrium ($E_1$):</strong> The economy settles at $(Y_1, r_1)$. Real output rises, but by less than the full simple multiplier due to <strong>partial crowding out</strong> ($Y_1 < Y_{Keynes}$).</li>
                </ol>
              </div>

              <div class="scorecard-table-wrap">
                <table class="scorecard-table">
                  <thead>
                    <tr><th>Variable</th><th>Pre-Shock ($E_0$)</th><th>Post-Shock ($E_1$)</th><th>Directional Net Impact</th></tr>
                  </thead>
                  <tbody>
                    <tr><td>National Output ($Y$)</td><td>$Y_0$</td><td>$Y_1$</td><td class="pos-val">EXPANDS ($\uparrow$)</td></tr>
                    <tr><td>Interest Rate ($r$)</td><td>$r_0$</td><td>$r_1$</td><td class="pos-val">RISES ($\uparrow$)</td></tr>
                    <tr><td>Private Investment ($I$)</td><td>$I_0$</td><td>$I_1$</td><td class="neg-val">CROWDED OUT ($\downarrow$)</td></tr>
                    <tr><td>Private Consumption ($C$)</td><td>$C_0$</td><td>$C_1$</td><td class="pos-val">INCREASES ($\uparrow$)</td></tr>
                  </tbody>
                </table>
              </div>

              <div class="trap-warning-box">
                <span class="trap-tag">EXAMINER TRAP WARNING:</span>
                Never equate the horizontal shift of the IS curve with the actual increase in equilibrium GDP. The horizontal shift equals $\frac{\Delta G}{1 - MPC}$, but the actual expansion is dampened by the LM slope because interest rates rise along LM.
              </div>
            </div>
          </div>
        </div>

        <!-- SCENARIO 2: CONTRACTIONARY FISCAL POLICY & CROWDING IN -->
        <div class="atlas-card" id="atlas-scen-2">
          <div class="atlas-card-header">
            <span class="scen-badge">BLUEPRINT 02 // FISCAL CONSOLIDATION</span>
            <h4 class="scen-title">Contractionary Fiscal Policy ($\downarrow G$ or $\uparrow T$) & The Crowding-In Effect</h4>
            <span class="scen-ref">REF: Unit 3, Slides 25-28</span>
          </div>

          <div class="atlas-grid">
            <div class="atlas-svg-panel">
              <svg viewBox="0 0 540 320" xmlns="http://www.w3.org/2000/svg" class="atlas-svg">
                <rect width="540" height="320" fill="#090a0f" rx="6"/>
                <line x1="50" y1="270" x2="510" y2="270" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <line x1="60" y1="280" x2="60" y2="30" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <text x="510" y="295" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" text-anchor="end">REAL OUTPUT (Y)</text>
                <text x="25" y="45" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" transform="rotate(-90 25,45)" text-anchor="end">INTEREST RATE (r %)</text>

                <!-- LM Curve -->
                <line x1="100" y1="250" x2="440" y2="70" stroke="#f59e0b" stroke-width="2.5"/>
                <text x="445" y="70" fill="#f59e0b" font-family="var(--font-mono)" font-size="12" font-weight="700">LM₀</text>

                <!-- Initial IS0 -->
                <line x1="180" y1="70" x2="480" y2="250" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>
                <text x="485" y="255" fill="#38bdf8" font-family="var(--font-mono)" font-size="12">IS₀</text>

                <!-- Shifted IS1 -->
                <line x1="100" y1="70" x2="400" y2="250" stroke="#38bdf8" stroke-width="2.5"/>
                <text x="405" y="255" fill="#38bdf8" font-family="var(--font-mono)" font-size="12" font-weight="700">IS₁ (ΔG < 0)</text>

                <!-- Left Shift Arrow -->
                <line x1="330" y1="120" x2="280" y2="120" stroke="#38bdf8" stroke-width="2"/>
                <polygon points="280,116 272,120 280,124" fill="#38bdf8"/>

                <!-- Projections & Crosshair E0 -->
                <line x1="60" y1="140" x2="312" y2="140" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <line x1="312" y1="140" x2="312" y2="270" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <text x="50" y="144" fill="#94a3b8" font-family="var(--font-mono)" font-size="11" text-anchor="end">r₀</text>
                <text x="312" y="286" fill="#94a3b8" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Y₀</text>

                <circle cx="312" cy="140" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="312" cy="140" r="2.5" fill="#d92534"/>
                <line x1="300" y1="140" x2="324" y2="140" stroke="#d92534" stroke-width="1.2"/>
                <line x1="312" y1="128" x2="312" y2="152" stroke="#d92534" stroke-width="1.2"/>
                <text x="322" y="134" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₀</text>

                <!-- Crosshair E1 -->
                <line x1="60" y1="178" x2="242" y2="178" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <line x1="242" y1="178" x2="242" y2="270" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <text x="50" y="182" fill="#38bdf8" font-family="var(--font-mono)" font-size="11" text-anchor="end">r₁</text>
                <text x="242" y="286" fill="#38bdf8" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Y₁</text>

                <circle cx="242" cy="178" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="242" cy="178" r="2.5" fill="#d92534"/>
                <line x1="230" y1="178" x2="254" y2="178" stroke="#d92534" stroke-width="1.2"/>
                <line x1="242" y1="166" x2="242" y2="190" stroke="#d92534" stroke-width="1.2"/>
                <text x="252" y="172" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₁</text>
              </svg>
            </div>

            <div class="atlas-text-panel">
              <div class="intel-block">
                <span class="block-tag">EXAM SITUATION / SCENARIO TRIGGER</span>
                <p>Government undertakes fiscal austerity (reduces defense or welfare spending, or hikes personal income taxes to curb sovereign debt).</p>
              </div>

              <div class="intel-block">
                <span class="block-tag">TRANSMISSION SEQUENCE & ECONOMIC MECHANICS</span>
                <p>1. <strong>IS Shifts Left:</strong> Drop in aggregate planned expenditure causes involuntary inventory accumulation. Firms lay off workers and reduce production ($Y \downarrow$).<br>
                2. <strong>Money Market Reaction:</strong> Lower income decreases transaction demand for money. Excess supply of money induces households to purchase bonds.<br>
                3. <strong>Interest Rate Falls:</strong> Bond prices rise, driving market interest rates down ($r_0 \to r_1$).<br>
                4. <strong>Crowding-In Effect:</strong> Lower borrowing costs stimulate private business capital expenditure and corporate borrowing ($I \uparrow$). This "crowding-in" partially cushions the GDP decline.</p>
              </div>

              <div class="scorecard-table-wrap">
                <table class="scorecard-table">
                  <thead><tr><th>Variable</th><th>Equilibrium Direction</th><th>Analytical Cause</th></tr></thead>
                  <tbody>
                    <tr><td>Real GDP ($Y$)</td><td class="neg-val">CONTRACTS ($\downarrow$)</td><td>Autonomous spending reduction</td></tr>
                    <tr><td>Interest Rate ($r$)</td><td class="neg-val">FALLS ($\downarrow$)</td><td>Depressed transaction cash demand</td></tr>
                    <tr><td>Private Investment ($I$)</td><td class="pos-val">CROWDED IN ($\uparrow$)</td><td>Cheaper commercial borrowing rates</td></tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>

        <!-- SCENARIO 3: EXPANSIONARY MONETARY POLICY -->
        <div class="atlas-card" id="atlas-scen-3">
          <div class="atlas-card-header">
            <span class="scen-badge">BLUEPRINT 03 // MONETARY EASING</span>
            <h4 class="scen-title">Expansionary Monetary Policy ($\uparrow M/P$, Repo Cut, OMO Purchases)</h4>
            <span class="scen-ref">REF: Unit 3, Slides 29-34</span>
          </div>

          <div class="atlas-grid">
            <div class="atlas-svg-panel">
              <svg viewBox="0 0 540 320" xmlns="http://www.w3.org/2000/svg" class="atlas-svg">
                <rect width="540" height="320" fill="#090a0f" rx="6"/>
                <line x1="50" y1="270" x2="510" y2="270" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <line x1="60" y1="280" x2="60" y2="30" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <text x="510" y="295" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" text-anchor="end">REAL OUTPUT (Y)</text>
                <text x="25" y="45" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" transform="rotate(-90 25,45)" text-anchor="end">INTEREST RATE (r %)</text>

                <!-- IS Curve (Fixed) -->
                <line x1="120" y1="70" x2="440" y2="250" stroke="#38bdf8" stroke-width="2.5"/>
                <text x="445" y="255" fill="#38bdf8" font-family="var(--font-mono)" font-size="12" font-weight="700">IS₀</text>

                <!-- Baseline LM0 Curve -->
                <line x1="80" y1="230" x2="380" y2="50" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>
                <text x="385" y="50" fill="#f59e0b" font-family="var(--font-mono)" font-size="12">LM₀</text>

                <!-- Shifted LM1 Curve -->
                <line x1="160" y1="230" x2="460" y2="50" stroke="#f59e0b" stroke-width="2.5"/>
                <text x="465" y="50" fill="#f59e0b" font-family="var(--font-mono)" font-size="12" font-weight="700">LM₁ (ΔM > 0)</text>

                <!-- Right Shift Arrow for LM -->
                <line x1="230" y1="140" x2="280" y2="140" stroke="#f59e0b" stroke-width="2"/>
                <polygon points="280,136 288,140 280,144" fill="#f59e0b"/>

                <!-- Crosshair E0 -->
                <line x1="60" y1="130" x2="228" y2="130" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <line x1="228" y1="130" x2="228" y2="270" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <text x="50" y="134" fill="#94a3b8" font-family="var(--font-mono)" font-size="11" text-anchor="end">r₀</text>
                <text x="228" y="286" fill="#94a3b8" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Y₀</text>

                <circle cx="228" cy="130" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="228" cy="130" r="2.5" fill="#d92534"/>
                <line x1="216" y1="130" x2="240" y2="130" stroke="#d92534" stroke-width="1.2"/>
                <line x1="228" y1="118" x2="228" y2="142" stroke="#d92534" stroke-width="1.2"/>
                <text x="238" y="124" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₀</text>

                <!-- Crosshair E1 -->
                <line x1="60" y1="172" x2="302" y2="172" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <line x1="302" y1="172" x2="302" y2="270" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <text x="50" y="176" fill="#f59e0b" font-family="var(--font-mono)" font-size="11" text-anchor="end">r₁</text>
                <text x="302" y="286" fill="#f59e0b" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Y₁</text>

                <circle cx="302" cy="172" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="302" cy="172" r="2.5" fill="#d92534"/>
                <line x1="290" y1="172" x2="314" y2="172" stroke="#d92534" stroke-width="1.2"/>
                <line x1="302" y1="160" x2="302" y2="184" stroke="#d92534" stroke-width="1.2"/>
                <text x="312" y="166" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₁</text>
              </svg>
            </div>

            <div class="atlas-text-panel">
              <div class="intel-block">
                <span class="block-tag">EXAM SITUATION / SCENARIO TRIGGER</span>
                <p>The Reserve Bank of India (RBI) conducts Open Market Operations (OMO) by purchasing ₹40,000 cr of government securities, lowers the Cash Reserve Ratio (CRR), or slashes the Repo Rate by 50 bps.</p>
              </div>

              <div class="intel-block">
                <span class="block-tag">TRANSMISSION SEQUENCE & ECONOMIC MECHANICS</span>
                <ol class="transmission-list">
                  <li><strong>Money Market Shock:</strong> Commercial banks hold excess cash reserves. Real money supply exceeds money demand ($M/P > L$). The <strong>LM curve shifts rightward</strong>.</li>
                  <li><strong>Asset Market Clearing:</strong> Banks and financial investors bid aggressively for debt instruments. Bond prices surge, compressing yields and market interest rates downward ($r_0 \to r_1$).</li>
                  <li><strong>Goods Market Stimulation:</strong> Commercial borrowers and industrial firms respond to cheap interest rates by initiating new capital investment projects ($I \uparrow$).</li>
                  <li><strong>Output Expansion:</strong> Through the investment multiplier, real GDP climbs from $Y_0$ to $Y_1$ at new equilibrium $E_1$.</li>
                </ol>
              </div>

              <div class="scorecard-table-wrap">
                <table class="scorecard-table">
                  <thead><tr><th>Macroeconomic Metric</th><th>Direction</th><th>Intuition</th></tr></thead>
                  <tbody>
                    <tr><td>Interest Rate ($r$)</td><td class="neg-val">FALLS ($\downarrow$)</td><td>Excess monetary liquidity</td></tr>
                    <tr><td>Private Investment ($I$)</td><td class="pos-val">STIMULATED ($\uparrow$)</td><td>Lower opportunity cost of capital</td></tr>
                    <tr><td>Real National Output ($Y$)</td><td class="pos-val">EXPANDS ($\uparrow$)</td><td>Induced investment spending rounds</td></tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>

        <!-- SCENARIO 4: CONTRACTIONARY MONETARY POLICY -->
        <div class="atlas-card" id="atlas-scen-4">
          <div class="atlas-card-header">
            <span class="scen-badge">BLUEPRINT 04 // MONETARY TIGHTENING</span>
            <h4 class="scen-title">Contractionary Monetary Policy ($\downarrow M/P$, Repo Rate Hikes, OMO Bond Sales)</h4>
            <span class="scen-ref">REF: Unit 3, Slides 35-38</span>
          </div>

          <div class="atlas-grid">
            <div class="atlas-svg-panel">
              <svg viewBox="0 0 540 320" xmlns="http://www.w3.org/2000/svg" class="atlas-svg">
                <rect width="540" height="320" fill="#090a0f" rx="6"/>
                <line x1="50" y1="270" x2="510" y2="270" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <line x1="60" y1="280" x2="60" y2="30" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <text x="510" y="295" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" text-anchor="end">REAL OUTPUT (Y)</text>
                <text x="25" y="45" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" transform="rotate(-90 25,45)" text-anchor="end">INTEREST RATE (r %)</text>

                <!-- IS Curve -->
                <line x1="120" y1="70" x2="440" y2="250" stroke="#38bdf8" stroke-width="2.5"/>
                <text x="445" y="255" fill="#38bdf8" font-family="var(--font-mono)" font-size="12" font-weight="700">IS₀</text>

                <!-- Initial LM0 -->
                <line x1="160" y1="230" x2="460" y2="50" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>
                <text x="465" y="50" fill="#f59e0b" font-family="var(--font-mono)" font-size="12">LM₀</text>

                <!-- Shifted LM1 (Left) -->
                <line x1="80" y1="230" x2="380" y2="50" stroke="#f59e0b" stroke-width="2.5"/>
                <text x="385" y="50" fill="#f59e0b" font-family="var(--font-mono)" font-size="12" font-weight="700">LM₁ (ΔM < 0)</text>

                <!-- Left Shift Arrow -->
                <line x1="280" y1="140" x2="230" y2="140" stroke="#f59e0b" stroke-width="2"/>
                <polygon points="230,136 222,140 230,144" fill="#f59e0b"/>

                <!-- Crosshair E0 -->
                <line x1="60" y1="172" x2="302" y2="172" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <line x1="302" y1="172" x2="302" y2="270" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <text x="50" y="176" fill="#94a3b8" font-family="var(--font-mono)" font-size="11" text-anchor="end">r₀</text>
                <text x="302" y="286" fill="#94a3b8" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Y₀</text>

                <circle cx="302" cy="172" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="302" cy="172" r="2.5" fill="#d92534"/>
                <line x1="290" y1="172" x2="314" y2="172" stroke="#d92534" stroke-width="1.2"/>
                <line x1="302" y1="160" x2="302" y2="184" stroke="#d92534" stroke-width="1.2"/>
                <text x="312" y="166" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₀</text>

                <!-- Crosshair E1 -->
                <line x1="60" y1="130" x2="228" y2="130" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <line x1="228" y1="130" x2="228" y2="270" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <text x="50" y="134" fill="#f59e0b" font-family="var(--font-mono)" font-size="11" text-anchor="end">r₁</text>
                <text x="228" y="286" fill="#f59e0b" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Y₁</text>

                <circle cx="228" cy="130" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="228" cy="130" r="2.5" fill="#d92534"/>
                <line x1="216" y1="130" x2="240" y2="130" stroke="#d92534" stroke-width="1.2"/>
                <line x1="228" y1="118" x2="228" y2="142" stroke="#d92534" stroke-width="1.2"/>
                <text x="238" y="124" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₁</text>
              </svg>
            </div>

            <div class="atlas-text-panel">
              <div class="intel-block">
                <span class="block-tag">EXAM SITUATION / SCENARIO TRIGGER</span>
                <p>Central Bank combats runaway inflation by raising the policy Repo Rate, raising reserve requirements, or draining system liquidity via reverse repos.</p>
              </div>

              <div class="intel-block">
                <span class="block-tag">ECONOMIC LOGIC & SCORECARD</span>
                <p>Monetary contraction shifts <strong>LM leftward/upward</strong>. To balance money demand with reduced liquidity, interest rates surge ($r_0 \to r_1$). High cost of capital chokes off corporate capital investment and consumer credit ($I \downarrow, C \downarrow$). Real GDP contracts from $Y_0$ to $Y_1$.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- SCENARIO 5: COORDINATED POLICY MIX (MONETARY ACCOMMODATION) -->
        <div class="atlas-card" id="atlas-scen-5">
          <div class="atlas-card-header">
            <span class="scen-badge">BLUEPRINT 05 // STRATEGIC COORDINATION</span>
            <h4 class="scen-title">Coordinated Policy Mix: Monetary Accommodation with Zero Crowding Out</h4>
            <span class="scen-ref">REF: Unit 3, Slides 39-44 & Midsem Exam Pattern</span>
          </div>

          <div class="atlas-grid">
            <div class="atlas-svg-panel">
              <svg viewBox="0 0 540 320" xmlns="http://www.w3.org/2000/svg" class="atlas-svg">
                <rect width="540" height="320" fill="#090a0f" rx="6"/>
                <line x1="50" y1="270" x2="510" y2="270" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <line x1="60" y1="280" x2="60" y2="30" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <text x="510" y="295" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" text-anchor="end">REAL OUTPUT (Y)</text>
                <text x="25" y="45" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" transform="rotate(-90 25,45)" text-anchor="end">INTEREST RATE (r %)</text>

                <!-- IS0 and IS1 -->
                <line x1="100" y1="70" x2="380" y2="250" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3"/>
                <text x="385" y="255" fill="#38bdf8" font-family="var(--font-mono)" font-size="11">IS₀</text>

                <line x1="190" y1="70" x2="470" y2="250" stroke="#38bdf8" stroke-width="2.5"/>
                <text x="475" y="255" fill="#38bdf8" font-family="var(--font-mono)" font-size="12" font-weight="700">IS₁ (ΔG > 0)</text>

                <!-- LM0 and LM1 -->
                <line x1="80" y1="250" x2="380" y2="70" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>
                <text x="385" y="70" fill="#f59e0b" font-family="var(--font-mono)" font-size="11">LM₀</text>

                <line x1="170" y1="250" x2="470" y2="70" stroke="#f59e0b" stroke-width="2.5"/>
                <text x="475" y="70" fill="#f59e0b" font-family="var(--font-mono)" font-size="12" font-weight="700">LM₁ (Accommodative)</text>

                <!-- Shift arrows -->
                <line x1="240" y1="130" x2="285" y2="130" stroke="#38bdf8" stroke-width="1.8"/>
                <polygon points="285,127 292,130 285,133" fill="#38bdf8"/>
                <line x1="220" y1="180" x2="265" y2="180" stroke="#f59e0b" stroke-width="1.8"/>
                <polygon points="265,177 272,180 265,183" fill="#f59e0b"/>

                <!-- Initial E0 -->
                <line x1="60" y1="160" x2="240" y2="160" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <line x1="240" y1="160" x2="240" y2="270" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <text x="50" y="164" fill="#94a3b8" font-family="var(--font-mono)" font-size="11" text-anchor="end">r₀*</text>
                <text x="240" y="286" fill="#94a3b8" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Y₀</text>

                <circle cx="240" cy="160" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="240" cy="160" r="2.5" fill="#d92534"/>
                <line x1="228" y1="160" x2="252" y2="160" stroke="#d92534" stroke-width="1.2"/>
                <line x1="240" y1="148" x2="240" y2="172" stroke="#d92534" stroke-width="1.2"/>
                <text x="250" y="154" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₀</text>

                <!-- Intermediate Unaccommodated E1 -->
                <circle cx="285" cy="133" r="4" fill="none" stroke="rgba(255,255,255,0.5)" stroke-width="1.5"/>
                <text x="290" y="125" fill="rgba(255,255,255,0.6)" font-family="var(--font-mono)" font-size="10">E_unaccom (r↑)</text>

                <!-- Final Accommodated E2 (Same r0, max Y) -->
                <line x1="240" y1="160" x2="330" y2="160" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3,3"/>
                <line x1="330" y1="160" x2="330" y2="270" stroke="#10b981" stroke-dasharray="3,3"/>
                <text x="330" y="286" fill="#10b981" font-family="var(--font-mono)" font-size="11" text-anchor="middle" font-weight="700">Y₂ (Full Multiplier)</text>

                <circle cx="330" cy="160" r="8" fill="none" stroke="#10b981" stroke-width="2"/>
                <circle cx="330" cy="160" r="3" fill="#10b981"/>
                <line x1="318" y1="160" x2="342" y2="160" stroke="#10b981" stroke-width="1.2"/>
                <line x1="330" y1="148" x2="330" y2="172" stroke="#10b981" stroke-width="1.2"/>
                <text x="340" y="154" fill="#10b981" font-family="var(--font-mono)" font-size="11" font-weight="700">E₂ (TARGET)</text>
              </svg>
            </div>

            <div class="atlas-text-panel">
              <div class="intel-block">
                <span class="block-tag">EXAM SITUATION / SCENARIO TRIGGER</span>
                <p>The Government launches an ambitious capex stimulus program. To ensure private sector borrowing is NOT crowded out, the Central Bank coordinates by injecting exactly enough reserves to stabilize interest rates at baseline $r_0$.</p>
              </div>

              <div class="intel-block">
                <span class="block-tag">OPERATIONAL MECHANICS</span>
                <p>1. Fiscal expansion pushes $IS_0 \to IS_1$. Without accommodation, interest rates would spike to $r_1$, causing crowding out ($E_{unaccom}$).<br>
                2. Central Bank accommodates by shifting $LM_0 \to LM_1$. The increase in money supply perfectly satisfies the surge in transaction money demand ($k \Delta Y$).<br>
                3. <strong>Result:</strong> Equilibrium moves directly horizontally from $E_0$ to $E_2$. Interest rate is maintained at $r_0^*$. <strong>Zero crowding out occurs</strong>, allowing real output to realize the entire Keynesian simple multiplier potential!</p>
              </div>
            </div>
          </div>
        </div>

        <!-- SCENARIO 6: THE LIQUIDITY TRAP & ZERO LOWER BOUND -->
        <div class="atlas-card" id="atlas-scen-6">
          <div class="atlas-card-header">
            <span class="scen-badge">BLUEPRINT 06 // ZERO LOWER BOUND</span>
            <h4 class="scen-title">The Liquidity Trap: Horizontal LM, Impotent Monetary Policy & Max Fiscal Power</h4>
            <span class="scen-ref">REF: Unit 3, Slides 45-48 & Bank of Japan Case Study</span>
          </div>

          <div class="atlas-grid">
            <div class="atlas-svg-panel">
              <svg viewBox="0 0 540 320" xmlns="http://www.w3.org/2000/svg" class="atlas-svg">
                <rect width="540" height="320" fill="#090a0f" rx="6"/>
                <line x1="50" y1="270" x2="510" y2="270" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <line x1="60" y1="280" x2="60" y2="30" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <text x="510" y="295" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" text-anchor="end">REAL OUTPUT (Y)</text>
                <text x="25" y="45" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" transform="rotate(-90 25,45)" text-anchor="end">INTEREST RATE (r %)</text>

                <!-- LM Curve with Flat Horizontal Segment -->
                <path d="M 60 230 L 260 230 L 460 70" fill="none" stroke="#f59e0b" stroke-width="3"/>
                <text x="465" y="70" fill="#f59e0b" font-family="var(--font-mono)" font-size="12" font-weight="700">LM (Flat at ZLB)</text>

                <text x="140" y="222" fill="#f59e0b" font-family="var(--font-mono)" font-size="10" font-weight="700">LIQUIDITY TRAP REGION (h → ∞)</text>

                <!-- IS0 intersecting flat part -->
                <line x1="80" y1="120" x2="220" y2="260" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3"/>
                <text x="225" y="260" fill="#38bdf8" font-family="var(--font-mono)" font-size="11">IS₀</text>

                <!-- IS1 shifted right on flat part -->
                <line x1="160" y1="120" x2="300" y2="260" stroke="#38bdf8" stroke-width="2.5"/>
                <text x="305" y="260" fill="#38bdf8" font-family="var(--font-mono)" font-size="12" font-weight="700">IS₁ (Fiscal Stimulus)</text>

                <line x1="150" y1="190" x2="200" y2="190" stroke="#38bdf8" stroke-width="1.8"/>
                <polygon points="200,187 207,190 200,193" fill="#38bdf8"/>

                <!-- E0 on flat part -->
                <line x1="60" y1="230" x2="190" y2="230" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <line x1="190" y1="230" x2="190" y2="270" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <text x="50" y="234" fill="#94a3b8" font-family="var(--font-mono)" font-size="11" text-anchor="end">r_min ≈ 0</text>
                <text x="190" y="286" fill="#94a3b8" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Y₀</text>

                <circle cx="190" cy="230" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="190" cy="230" r="2.5" fill="#d92534"/>
                <line x1="178" y1="230" x2="202" y2="230" stroke="#d92534" stroke-width="1.2"/>
                <line x1="190" y1="218" x2="190" y2="242" stroke="#d92534" stroke-width="1.2"/>
                <text x="195" y="218" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₀</text>

                <!-- E1 on flat part -->
                <line x1="270" y1="230" x2="270" y2="270" stroke="#38bdf8" stroke-dasharray="3,3"/>
                <text x="270" y="286" fill="#38bdf8" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Y₁</text>

                <circle cx="270" cy="230" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="270" cy="230" r="2.5" fill="#d92534"/>
                <line x1="258" y1="230" x2="282" y2="230" stroke="#d92534" stroke-width="1.2"/>
                <line x1="270" y1="218" x2="270" y2="242" stroke="#d92534" stroke-width="1.2"/>
                <text x="278" y="218" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₁</text>
              </svg>
            </div>

            <div class="atlas-text-panel">
              <div class="intel-block">
                <span class="block-tag">EXAM SITUATION / SCENARIO TRIGGER</span>
                <p>Severe economic depression or prolonged stagnation where nominal policy interest rates fall to the Zero Lower Bound (e.g., Japan's Lost Decades, US 2008 Financial Crisis).</p>
              </div>

              <div class="intel-block">
                <span class="block-tag">THEORETICAL DOCTRINE</span>
                <p>1. <strong>Infinite Interest Elasticity ($h \to \infty$):</strong> Because interest rates cannot drop below zero, agents are indifferent between holding bonds and holding cash. Any money injected by the Central Bank is hoarded as liquidity ("pushed on a string"). Shifting LM rightward has <strong>zero effect on $r$ and zero effect on $Y$</strong>.<br>
                2. <strong>Fiscal Policy is 100% Effective:</strong> When government spends ($\Delta G$), it shifts IS along the horizontal LM line. Because the interest rate cannot rise, <strong>private investment is NOT crowded out at all</strong> ($\Delta r = 0$). Output expands by the exact full Keynesian multiplier: $\Delta Y = \frac{1}{1-MPC} \Delta G$!</p>
              </div>
            </div>
          </div>
        </div>

        <!-- SCENARIO 7: DEMONETISATION MONEY DEMAND SHOCK -->
        <div class="atlas-card" id="atlas-scen-7">
          <div class="atlas-card-header">
            <span class="scen-badge">BLUEPRINT 07 // CURRENCY SHOCK</span>
            <h4 class="scen-title">Demonetisation & Liquidity Preference Shocks in IS-LM</h4>
            <span class="scen-ref">REF: Unit 5 Demonetisation Case Study</span>
          </div>

          <div class="atlas-grid">
            <div class="atlas-svg-panel">
              <svg viewBox="0 0 540 320" xmlns="http://www.w3.org/2000/svg" class="atlas-svg">
                <rect width="540" height="320" fill="#090a0f" rx="6"/>
                <line x1="50" y1="270" x2="510" y2="270" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <line x1="60" y1="280" x2="60" y2="30" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <text x="510" y="295" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" text-anchor="end">REAL OUTPUT (Y)</text>
                <text x="25" y="45" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" transform="rotate(-90 25,45)" text-anchor="end">INTEREST RATE (r %)</text>

                <!-- IS Curve -->
                <line x1="120" y1="70" x2="440" y2="250" stroke="#38bdf8" stroke-width="2.5"/>
                <text x="445" y="255" fill="#38bdf8" font-family="var(--font-mono)" font-size="12" font-weight="700">IS₀</text>

                <!-- Pre-Demonetisation LM0 -->
                <line x1="160" y1="240" x2="460" y2="60" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>
                <text x="465" y="60" fill="#f59e0b" font-family="var(--font-mono)" font-size="11">LM₀ (Pre-Nov 2016)</text>

                <!-- Immediate Cash Crunch LM_shock (Left/Upward) -->
                <line x1="80" y1="240" x2="380" y2="60" stroke="#ef4444" stroke-width="2.5"/>
                <text x="385" y="60" fill="#ef4444" font-family="var(--font-mono)" font-size="12" font-weight="700">LM_shock (Cash Crunch)</text>

                <!-- Left Shift Arrow -->
                <line x1="280" y1="140" x2="230" y2="140" stroke="#ef4444" stroke-width="2"/>
                <polygon points="230,136 222,140 230,144" fill="#ef4444"/>

                <!-- E0 Pre-Shock -->
                <line x1="60" y1="175" x2="305" y2="175" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <line x1="305" y1="175" x2="305" y2="270" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <text x="50" y="179" fill="#94a3b8" font-family="var(--font-mono)" font-size="11" text-anchor="end">r₀</text>
                <text x="305" y="286" fill="#94a3b8" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Y₀</text>

                <circle cx="305" cy="175" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="305" cy="175" r="2.5" fill="#d92534"/>
                <text x="315" y="170" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₀</text>

                <!-- E_shock Cash Crunch -->
                <line x1="60" y1="130" x2="225" y2="130" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <line x1="225" y1="130" x2="225" y2="270" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <text x="50" y="134" fill="#ef4444" font-family="var(--font-mono)" font-size="11" text-anchor="end">r_shadow ↑</text>
                <text x="225" y="286" fill="#ef4444" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Y_slump</text>

                <circle cx="225" cy="130" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="225" cy="130" r="2.5" fill="#d92534"/>
                <text x="235" y="125" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E_shock</text>
              </svg>
            </div>

            <div class="atlas-text-panel">
              <div class="intel-block">
                <span class="block-tag">EXAM SITUATION / SCENARIO TRIGGER</span>
                <p>On 8 November 2016, 86.4% of circulating currency in India (₹500 and ₹1,000 notes) was instantaneously invalidated. Cash velocity ($V$) froze in the informal cash-dependent economy.</p>
              </div>

              <div class="intel-block">
                <span class="block-tag">IS-LM TRANSMISSION MECHANICS</span>
                <p>1. <strong>Sudden Contraction of Effective Money Supply ($M/P \downarrow$):</strong> Despite total bank deposits surging, usable transaction cash vanished. The effective <strong>LM curve shifted severely leftward</strong>.<br>
                2. <strong>Shadow Interest Rate & Credit Friction:</strong> Informal borrowing rates spiked; working capital loans froze.<br>
                3. <strong>Immediate Contraction ($E_{shock}$):</strong> Informal transactions collapsed, agriculture supply chains stalled, and quarterly GDP growth decelerated by ~1.5 percentage points.<br>
                4. <strong>Long-Run Remonetisation:</strong> As new ₹500 and ₹2000 notes circulated and UPI digital payments replaced cash, the LM curve shifted back rightward toward baseline.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ========================================================================= -->
      <!-- SECTION II: THE AD-AS FRAMEWORK & SHOCKS TAXONOMY -->
      <!-- ========================================================================= -->
      <div class="atlas-section-group" id="atlas-sec-adas">
        <div class="atlas-group-header">
          <span class="group-num">REGIME II</span>
          <h3 class="group-title">THE AD-AS FRAMEWORK & SHOCK TRANSMISSION (PRICE LEVEL & OUTPUT)</h3>
          <p class="group-desc">Authoritative Reference: Prof. Sana Tabassum AD-AS Dedicated Decks. Shows the determination of Real Output ($Y$) and Aggregate Price Level ($P$) under short-run wage stickiness and long-run self-correction.</p>
        </div>

        <!-- SCENARIO 8: POSITIVE DEMAND SHOCK & SELF-CORRECTION -->
        <div class="atlas-card" id="atlas-scen-8">
          <div class="atlas-card-header">
            <span class="scen-badge">BLUEPRINT 08 // AD BOOM & SELF-CORRECTION</span>
            <h4 class="scen-title">Positive Aggregate Demand Shock: Demand-Pull Inflation & Wage-Adjustment Return to $Y^*$</h4>
            <span class="scen-ref">REF: Unit 4, Slides 8-16</span>
          </div>

          <div class="atlas-grid">
            <div class="atlas-svg-panel">
              <svg viewBox="0 0 540 320" xmlns="http://www.w3.org/2000/svg" class="atlas-svg">
                <rect width="540" height="320" fill="#090a0f" rx="6"/>
                <line x1="50" y1="270" x2="510" y2="270" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <line x1="60" y1="280" x2="60" y2="30" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <text x="510" y="295" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" text-anchor="end">REAL GDP (Y)</text>
                <text x="25" y="45" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" transform="rotate(-90 25,45)" text-anchor="end">PRICE LEVEL (P)</text>

                <!-- LRAS Vertical -->
                <line x1="250" y1="50" x2="250" y2="270" stroke="#ffffff" stroke-width="2.5"/>
                <text x="250" y="42" fill="#ffffff" font-family="var(--font-mono)" font-size="11" text-anchor="middle" font-weight="700">LRAS (Y*)</text>

                <!-- Initial AD0 -->
                <line x1="100" y1="90" x2="380" y2="250" stroke="#10b981" stroke-width="2" stroke-dasharray="3,3"/>
                <text x="385" y="255" fill="#10b981" font-family="var(--font-mono)" font-size="11">AD₀</text>

                <!-- Shifted AD1 -->
                <line x1="180" y1="90" x2="460" y2="250" stroke="#10b981" stroke-width="2.5"/>
                <text x="465" y="255" fill="#10b981" font-family="var(--font-mono)" font-size="12" font-weight="700">AD₁ (Boom)</text>

                <!-- Initial SRAS0 -->
                <line x1="100" y1="250" x2="380" y2="90" stroke="#f43f5e" stroke-width="2.5"/>
                <text x="385" y="90" fill="#f43f5e" font-family="var(--font-mono)" font-size="11">SRAS₀</text>

                <!-- Self-Corrected SRAS1 (Shifted Left/Upward) -->
                <line x1="60" y1="200" x2="340" y2="40" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4,4"/>
                <text x="345" y="40" fill="#f43f5e" font-family="var(--font-mono)" font-size="12" font-weight="700">SRAS₁ (Wages ↑)</text>

                <!-- E0: Initial Equilibrium at LRAS -->
                <line x1="60" y1="164" x2="250" y2="164" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <text x="50" y="168" fill="#94a3b8" font-family="var(--font-mono)" font-size="11" text-anchor="end">P₀</text>
                <text x="250" y="286" fill="#94a3b8" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Y*</text>

                <circle cx="250" cy="164" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="250" cy="164" r="2.5" fill="#d92534"/>
                <text x="232" y="160" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₀</text>

                <!-- E1: Short Run (AD1 & SRAS0) -->
                <line x1="60" y1="133" x2="305" y2="133" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <line x1="305" y1="133" x2="305" y2="270" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <text x="50" y="137" fill="#10b981" font-family="var(--font-mono)" font-size="11" text-anchor="end">P₁</text>
                <text x="305" y="286" fill="#10b981" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Y₁ (Overheating)</text>

                <circle cx="305" cy="133" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="305" cy="133" r="2.5" fill="#d92534"/>
                <text x="315" y="130" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₁ (Short-Run)</text>

                <!-- E2: Long Run (AD1 & SRAS1 at LRAS) -->
                <line x1="60" y1="91" x2="250" y2="91" stroke="#f43f5e" stroke-dasharray="3,3"/>
                <text x="50" y="95" fill="#f43f5e" font-family="var(--font-mono)" font-size="11" text-anchor="end">P₂ (Final)</text>

                <circle cx="250" cy="91" r="8" fill="none" stroke="#f43f5e" stroke-width="2"/>
                <circle cx="250" cy="91" r="3" fill="#f43f5e"/>
                <text x="258" y="85" fill="#f43f5e" font-family="var(--font-mono)" font-size="11" font-weight="700">E₂ (Long-Run)</text>
              </svg>
            </div>

            <div class="atlas-text-panel">
              <div class="intel-block">
                <span class="block-tag">EXAM SITUATION / SCENARIO TRIGGER</span>
                <p>Surge in export demand ($NX \uparrow$), consumer boom, or major fiscal stimulus moves economy past full employment.</p>
              </div>

              <div class="intel-block">
                <span class="block-tag">TWO-STAGE TRANSMISSION SEQUENCE</span>
                <ol class="transmission-list">
                  <li><strong>Stage 1 (Short-Run Movement to $E_1$):</strong> Aggregate demand shifts right to $AD_1$. In the short run, nominal wages and raw material contracts are <em>sticky</em>. Firms experience higher sales prices while input costs remain fixed, expanding profit margins. Output expands past potential ($Y_1 > Y^*$), unemployment drops below natural rate ($u < u^*$), and price level rises to $P_1$. <strong>An Inflationary Gap opens.</strong></li>
                  <li><strong>Stage 2 (Long-Run Self-Correction to $E_2$):</strong> In an overheated labor market, workers face rising cost of living and labor shortages. When wage contracts expire, workers demand higher nominal wages. Higher wage costs shift the <strong>Short-Run Aggregate Supply curve leftward/upward ($SRAS_0 \to SRAS_1$)</strong>.</li>
                  <li><strong>Final Equilibrium ($E_2$):</strong> The economy self-corrects back to potential output ($Y^*$). Output gains are completely erased, leaving the economy with <strong>permanently higher prices ($P_2 > P_1 > P_0$)</strong>.</li>
                </ol>
              </div>
            </div>
          </div>
        </div>

        <!-- SCENARIO 9: NEGATIVE DEMAND SHOCK & RECESSION -->
        <div class="atlas-card" id="atlas-scen-9">
          <div class="atlas-card-header">
            <span class="scen-badge">BLUEPRINT 09 // RECESSIONARY GAP</span>
            <h4 class="scen-title">Negative Aggregate Demand Shock: Recessionary Slump & Deflationary Adjustment</h4>
            <span class="scen-ref">REF: Unit 4, Slides 17-22</span>
          </div>

          <div class="atlas-grid">
            <div class="atlas-svg-panel">
              <svg viewBox="0 0 540 320" xmlns="http://www.w3.org/2000/svg" class="atlas-svg">
                <rect width="540" height="320" fill="#090a0f" rx="6"/>
                <line x1="50" y1="270" x2="510" y2="270" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <line x1="60" y1="280" x2="60" y2="30" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <text x="510" y="295" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" text-anchor="end">REAL GDP (Y)</text>
                <text x="25" y="45" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" transform="rotate(-90 25,45)" text-anchor="end">PRICE LEVEL (P)</text>

                <line x1="250" y1="50" x2="250" y2="270" stroke="#ffffff" stroke-width="2.5"/>
                <text x="250" y="42" fill="#ffffff" font-family="var(--font-mono)" font-size="11" text-anchor="middle" font-weight="700">LRAS (Y*)</text>

                <!-- Initial AD0 -->
                <line x1="180" y1="90" x2="460" y2="250" stroke="#10b981" stroke-width="2" stroke-dasharray="3,3"/>
                <text x="465" y="255" fill="#10b981" font-family="var(--font-mono)" font-size="11">AD₀</text>

                <!-- Shifted AD1 (Left) -->
                <line x1="100" y1="90" x2="380" y2="250" stroke="#10b981" stroke-width="2.5"/>
                <text x="385" y="255" fill="#10b981" font-family="var(--font-mono)" font-size="12" font-weight="700">AD₁ (Slump)</text>

                <!-- Initial SRAS0 -->
                <line x1="60" y1="200" x2="340" y2="40" stroke="#f43f5e" stroke-width="2.5"/>
                <text x="345" y="40" fill="#f43f5e" font-family="var(--font-mono)" font-size="11">SRAS₀</text>

                <!-- Shifted SRAS1 (Right/Downward in Long Run) -->
                <line x1="100" y1="250" x2="380" y2="90" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4,4"/>
                <text x="385" y="90" fill="#f43f5e" font-family="var(--font-mono)" font-size="11">SRAS₁ (Wages ↓)</text>

                <!-- E0 at LRAS -->
                <circle cx="250" cy="91" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="250" cy="91" r="2.5" fill="#d92534"/>
                <text x="258" y="85" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₀</text>

                <!-- E1 Short Run -->
                <circle cx="195" cy="122" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="195" cy="122" r="2.5" fill="#d92534"/>
                <text x="145" y="118" fill="#10b981" font-family="var(--font-mono)" font-size="11" font-weight="700">E₁ (Recession)</text>

                <!-- E2 Long Run -->
                <circle cx="250" cy="164" r="8" fill="none" stroke="#f43f5e" stroke-width="2"/>
                <circle cx="250" cy="164" r="3" fill="#f43f5e"/>
                <text x="258" y="170" fill="#f43f5e" font-family="var(--font-mono)" font-size="11" font-weight="700">E₂ (Self-Corrected)</text>
              </svg>
            </div>

            <div class="atlas-text-panel">
              <div class="intel-block">
                <span class="block-tag">EXAM SITUATION / SCENARIO TRIGGER</span>
                <p>Global financial crisis, pandemic lockdowns, or banking liquidity crunch causes catastrophic drop in autonomous consumption and investment.</p>
              </div>

              <div class="intel-block">
                <span class="block-tag">ECONOMIC LOGIC & RECESSIONARY GAP</span>
                <p>1. <strong>Short-Run Slump ($E_1$):</strong> $AD$ shifts left. Due to sticky wages, firms cut production and conduct mass layoffs. Real GDP collapses ($Y_1 < Y^*$), unemployment spikes above natural rate ($u > u^*$), and price level softens ($P_1 < P_0$). A <strong>Recessionary Output Gap</strong> emerges.<br>
                2. <strong>Long-Run Self-Correction ($E_2$):</strong> Widespread joblessness eventually forces nominal wages down (or productivity rises relative to stagnant wages). Lower unit labor costs shift $SRAS$ rightward until output returns to $Y^*$ at a permanently reduced price level $P_2$.<br>
                3. <em>Keynesian Caveat:</em> Downward wage rigidity ("sticky-down wages") makes this self-correction excruciatingly slow, justifying countercyclical fiscal/monetary stimulus.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- SCENARIO 10: ADVERSE SUPPLY SHOCK & STAGFLATION (OIL CRISIS) -->
        <div class="atlas-card" id="atlas-scen-10">
          <div class="atlas-card-header">
            <span class="scen-badge">BLUEPRINT 10 // STAGFLATION DILEMMA</span>
            <h4 class="scen-title">Adverse Supply Shock (Stagflation): The 1970s Global Oil Crisis Paradigm</h4>
            <span class="scen-ref">REF: Unit 4 Slides 23-30 & Oil Shock Case Study</span>
          </div>

          <div class="atlas-grid">
            <div class="atlas-svg-panel">
              <svg viewBox="0 0 540 320" xmlns="http://www.w3.org/2000/svg" class="atlas-svg">
                <rect width="540" height="320" fill="#090a0f" rx="6"/>
                <line x1="50" y1="270" x2="510" y2="270" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <line x1="60" y1="280" x2="60" y2="30" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <text x="510" y="295" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" text-anchor="end">REAL GDP (Y)</text>
                <text x="25" y="45" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" transform="rotate(-90 25,45)" text-anchor="end">PRICE LEVEL (P)</text>

                <!-- LRAS -->
                <line x1="260" y1="50" x2="260" y2="270" stroke="#ffffff" stroke-width="2.5"/>
                <text x="260" y="42" fill="#ffffff" font-family="var(--font-mono)" font-size="11" text-anchor="middle" font-weight="700">LRAS (Y*)</text>

                <!-- AD Curve (Fixed) -->
                <line x1="120" y1="70" x2="440" y2="250" stroke="#10b981" stroke-width="2.5"/>
                <text x="445" y="255" fill="#10b981" font-family="var(--font-mono)" font-size="12" font-weight="700">AD₀</text>

                <!-- Baseline SRAS0 -->
                <line x1="100" y1="250" x2="380" y2="90" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,3"/>
                <text x="385" y="90" fill="#f43f5e" font-family="var(--font-mono)" font-size="11">SRAS₀</text>

                <!-- Shifted SRAS1 (Left/Upward) -->
                <line x1="60" y1="200" x2="340" y2="40" stroke="#f43f5e" stroke-width="3"/>
                <text x="345" y="40" fill="#f43f5e" font-family="var(--font-mono)" font-size="12" font-weight="700">SRAS₁ (Oil Spike)</text>

                <!-- Left Shift Arrow -->
                <line x1="280" y1="140" x2="230" y2="140" stroke="#f43f5e" stroke-width="2"/>
                <polygon points="230,136 222,140 230,144" fill="#f43f5e"/>

                <!-- E0 at LRAS -->
                <line x1="60" y1="168" x2="260" y2="168" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <line x1="260" y1="168" x2="260" y2="270" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <text x="50" y="172" fill="#94a3b8" font-family="var(--font-mono)" font-size="11" text-anchor="end">P₀</text>
                <text x="260" y="286" fill="#94a3b8" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Y*</text>

                <circle cx="260" cy="168" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="260" cy="168" r="2.5" fill="#d92534"/>
                <text x="270" y="165" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₀</text>

                <!-- E1 Stagflation -->
                <line x1="60" y1="118" x2="205" y2="118" stroke="#f43f5e" stroke-dasharray="3,3"/>
                <line x1="205" y1="118" x2="205" y2="270" stroke="#f43f5e" stroke-dasharray="3,3"/>
                <text x="50" y="122" fill="#f43f5e" font-family="var(--font-mono)" font-size="11" text-anchor="end">P₁ (Inflation!)</text>
                <text x="205" y="286" fill="#f43f5e" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Y₁ (Stagnation!)</text>

                <circle cx="205" cy="118" r="8" fill="none" stroke="#d92534" stroke-width="2"/>
                <circle cx="205" cy="118" r="3" fill="#d92534"/>
                <text x="145" y="112" fill="#f43f5e" font-family="var(--font-mono)" font-size="11" font-weight="700">E₁ (STAGFLATION)</text>
              </svg>
            </div>

            <div class="atlas-text-panel">
              <div class="intel-block">
                <span class="block-tag">EXAM SITUATION / SCENARIO TRIGGER</span>
                <p>OPEC quadruples crude oil prices, or a geopolitical war disrupts critical energy and fertilizer maritime shipping lines.</p>
              </div>

              <div class="intel-block">
                <span class="block-tag">THE ANATOMY OF STAGFLATION</span>
                <p>1. <strong>Supply Shock:</strong> Raw materials and energy are universal inputs across agriculture, manufacturing, logistics, and power generation. The sharp cost spike forces firms across the entire economy to raise prices and scale back unprofitable production.<br>
                2. <strong>SRAS Shifts Left/Upward:</strong> The economy moves from $E_0$ to $E_1$.<br>
                3. <strong>The Deadly Dual Crisis:</strong> Simultaneous <strong>Stagnation</strong> (output falls below potential, unemployment surges) and <strong>Inflation</strong> (price level shoots up from $P_0 \to P_1$).<br>
                4. <strong>The Policy Dilemma:</strong>
                • If Government stimulates $AD$ to fight unemployment $\to$ Price level explodes even higher (hyperinflation).<br>
                • If Government contracts $AD$ to fight inflation $\to$ Unemployment surges to catastrophic depression levels.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- SCENARIO 11: FAVORABLE SUPPLY SHOCK -->
        <div class="atlas-card" id="atlas-scen-11">
          <div class="atlas-card-header">
            <span class="scen-badge">BLUEPRINT 11 // THE GOLDEN REGIME</span>
            <h4 class="scen-title">Favorable Supply Shock: Disinflationary Growth & Cost Deflation</h4>
            <span class="scen-ref">REF: Unit 4, Slides 31-35</span>
          </div>

          <div class="atlas-grid">
            <div class="atlas-svg-panel">
              <svg viewBox="0 0 540 320" xmlns="http://www.w3.org/2000/svg" class="atlas-svg">
                <rect width="540" height="320" fill="#090a0f" rx="6"/>
                <line x1="50" y1="270" x2="510" y2="270" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <line x1="60" y1="280" x2="60" y2="30" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <text x="510" y="295" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" text-anchor="end">REAL GDP (Y)</text>
                <text x="25" y="45" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" transform="rotate(-90 25,45)" text-anchor="end">PRICE LEVEL (P)</text>

                <line x1="240" y1="50" x2="240" y2="270" stroke="#ffffff" stroke-width="2.5"/>
                <text x="240" y="42" fill="#ffffff" font-family="var(--font-mono)" font-size="11" text-anchor="middle" font-weight="700">LRAS (Y*)</text>

                <line x1="120" y1="70" x2="440" y2="250" stroke="#10b981" stroke-width="2.5"/>
                <text x="445" y="255" fill="#10b981" font-family="var(--font-mono)" font-size="12" font-weight="700">AD₀</text>

                <line x1="60" y1="200" x2="340" y2="40" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,3"/>
                <text x="345" y="40" fill="#f43f5e" font-family="var(--font-mono)" font-size="11">SRAS₀</text>

                <line x1="100" y1="250" x2="380" y2="90" stroke="#10b981" stroke-width="3"/>
                <text x="385" y="90" fill="#10b981" font-family="var(--font-mono)" font-size="12" font-weight="700">SRAS₁ (Cost Relief)</text>

                <circle cx="205" cy="118" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="205" cy="118" r="2.5" fill="#d92534"/>
                <text x="215" y="112" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₀</text>

                <circle cx="260" cy="168" r="8" fill="none" stroke="#10b981" stroke-width="2"/>
                <circle cx="260" cy="168" r="3" fill="#10b981"/>
                <text x="270" y="165" fill="#10b981" font-family="var(--font-mono)" font-size="11" font-weight="700">E₁ (Disinflation Boom)</text>
              </svg>
            </div>

            <div class="atlas-text-panel">
              <div class="intel-block">
                <span class="block-tag">EXAM SITUATION / SCENARIO TRIGGER</span>
                <p>Global crude oil prices crash from $120 to $40 per barrel, or agricultural yields break historical records due to optimal monsoons.</p>
              </div>

              <div class="intel-block">
                <span class="block-tag">ECONOMIC LOGIC</span>
                <p>Widespread reduction in basic production and shipping costs shifts the <strong>SRAS curve downward/rightward</strong>. Firms compete by passing savings to consumers. Result: Real GDP expands ($Y_1 > Y^*$) while consumer inflation falls ($P_1 < P_0$).</p>
              </div>
            </div>
          </div>
        </div>

        <!-- SCENARIO 12: LRAS EXPANSION -->
        <div class="atlas-card" id="atlas-scen-12">
          <div class="atlas-card-header">
            <span class="scen-badge">BLUEPRINT 12 // STRUCTURAL GROWTH</span>
            <h4 class="scen-title">Long-Run Economic Growth: Shifting the Production Frontier (LRAS)</h4>
            <span class="scen-ref">REF: Unit 4, Slides 36-40</span>
          </div>

          <div class="atlas-grid">
            <div class="atlas-svg-panel">
              <svg viewBox="0 0 540 320" xmlns="http://www.w3.org/2000/svg" class="atlas-svg">
                <rect width="540" height="320" fill="#090a0f" rx="6"/>
                <line x1="50" y1="270" x2="510" y2="270" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <line x1="60" y1="280" x2="60" y2="30" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <text x="510" y="295" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" text-anchor="end">REAL GDP (Y)</text>
                <text x="25" y="45" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" transform="rotate(-90 25,45)" text-anchor="end">PRICE LEVEL (P)</text>

                <!-- Initial LRAS0 -->
                <line x1="220" y1="50" x2="220" y2="270" stroke="#ffffff" stroke-width="2" stroke-dasharray="3,3"/>
                <text x="220" y="42" fill="#ffffff" font-family="var(--font-mono)" font-size="11" text-anchor="middle">LRAS₀ (Y₀*)</text>

                <!-- Shifted LRAS1 -->
                <line x1="320" y1="50" x2="320" y2="270" stroke="#ffffff" stroke-width="3"/>
                <text x="320" y="42" fill="#ffffff" font-family="var(--font-mono)" font-size="12" text-anchor="middle" font-weight="700">LRAS₁ (Y₁*)</text>

                <line x1="230" y1="120" x2="310" y2="120" stroke="#ffffff" stroke-width="2"/>
                <polygon points="310,116 318,120 310,124" fill="#ffffff"/>

                <!-- AD Curve -->
                <line x1="120" y1="70" x2="440" y2="250" stroke="#10b981" stroke-width="2.5"/>
                <text x="445" y="255" fill="#10b981" font-family="var(--font-mono)" font-size="12" font-weight="700">AD</text>

                <!-- SRAS0 and SRAS1 -->
                <line x1="80" y1="250" x2="360" y2="90" stroke="#f43f5e" stroke-width="1.8" stroke-dasharray="3,3"/>
                <line x1="180" y1="250" x2="460" y2="90" stroke="#f43f5e" stroke-width="2.5"/>
                <text x="465" y="90" fill="#f43f5e" font-family="var(--font-mono)" font-size="11" font-weight="700">SRAS₁</text>

                <!-- Target crosshairs -->
                <circle cx="220" cy="148" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="220" cy="148" r="2.5" fill="#d92534"/>
                <text x="205" y="142" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₀</text>

                <circle cx="320" cy="190" r="8" fill="none" stroke="#10b981" stroke-width="2"/>
                <circle cx="320" cy="190" r="3" fill="#10b981"/>
                <text x="330" y="185" fill="#10b981" font-family="var(--font-mono)" font-size="11" font-weight="700">E₁</text>
              </svg>
            </div>

            <div class="atlas-text-panel">
              <div class="intel-block">
                <span class="block-tag">EXAM SITUATION / SCENARIO TRIGGER</span>
                <p>Major technological innovation (AI, automation), labor force expansion, or decades of capital accumulation ($K \uparrow$).</p>
              </div>

              <div class="intel-block">
                <span class="block-tag">ECONOMIC LOGIC</span>
                <p>Potential GDP ($Y^*$) is governed strictly by the physical production function: $Y^* = A \cdot F(K, L)$. When technological efficiency ($A$) or physical capital stock ($K$) increases permanently, the vertical <strong>LRAS shifts rightward</strong>. The economy can produce permanently more real output at full employment.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ========================================================================= -->
      <!-- SECTION III: GOODS, MONEY, & LOANABLE FUNDS MARKETS -->
      <!-- ========================================================================= -->
      <div class="atlas-section-group" id="atlas-sec-markets">
        <div class="atlas-group-header">
          <span class="group-num">REGIME III</span>
          <h3 class="group-title">FOUNDATIONAL MARKETS: GOODS, LOANABLE FUNDS, & CENTRAL BANK LIQUIDITY</h3>
          <p class="group-desc">Authoritative Reference: Prof. Sana Tabassum Units 1, 2, and Loanable Funds Deck.</p>
        </div>

        <!-- SCENARIO 13: KEYNESIAN CROSS -->
        <div class="atlas-card" id="atlas-scen-13">
          <div class="atlas-card-header">
            <span class="scen-badge">BLUEPRINT 13 // 45° LINE ENGINE</span>
            <h4 class="scen-title">The Keynesian Cross: Autonomous Injection & The Multiplier Expansion</h4>
            <span class="scen-ref">REF: Unit 2 & Multiplier Derivations</span>
          </div>

          <div class="atlas-grid">
            <div class="atlas-svg-panel">
              <svg viewBox="0 0 540 320" xmlns="http://www.w3.org/2000/svg" class="atlas-svg">
                <rect width="540" height="320" fill="#090a0f" rx="6"/>
                <line x1="50" y1="270" x2="510" y2="270" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <line x1="60" y1="280" x2="60" y2="30" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <text x="510" y="295" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" text-anchor="end">REAL INCOME / OUTPUT (Y)</text>
                <text x="25" y="45" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" transform="rotate(-90 25,45)" text-anchor="end">AGGREGATE EXPENDITURE (AE)</text>

                <!-- 45 Degree Line -->
                <line x1="60" y1="270" x2="310" y2="40" stroke="#ffffff" stroke-width="2"/>
                <text x="315" y="40" fill="#ffffff" font-family="var(--font-mono)" font-size="12" font-weight="700">Y = AE (45° Line)</text>

                <!-- AE0 Line -->
                <line x1="60" y1="180" x2="480" y2="80" stroke="#a855f7" stroke-width="2" stroke-dasharray="3,3"/>
                <text x="485" y="80" fill="#a855f7" font-family="var(--font-mono)" font-size="11">AE₀ = A₀ + cY</text>

                <!-- AE1 Line -->
                <line x1="60" y1="130" x2="480" y2="30" stroke="#a855f7" stroke-width="2.5"/>
                <text x="485" y="30" fill="#a855f7" font-family="var(--font-mono)" font-size="12" font-weight="700">AE₁ = AE₀ + ΔG</text>

                <!-- Vertical Injection Arrow -->
                <line x1="120" y1="165" x2="120" y2="120" stroke="#10b981" stroke-width="2"/>
                <polygon points="116,120 120,112 124,120" fill="#10b981"/>
                <text x="130" y="140" fill="#10b981" font-family="var(--font-mono)" font-size="11">ΔG (Injection)</text>

                <!-- E0 and E1 Crosshairs -->
                <circle cx="178" cy="162" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="178" cy="162" r="2.5" fill="#d92534"/>
                <text x="188" y="158" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₀</text>

                <circle cx="236" cy="108" r="8" fill="none" stroke="#10b981" stroke-width="2"/>
                <circle cx="236" cy="108" r="3" fill="#10b981"/>
                <text x="246" y="104" fill="#10b981" font-family="var(--font-mono)" font-size="11" font-weight="700">E₁</text>

                <!-- Projection drop lines -->
                <line x1="178" y1="162" x2="178" y2="270" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <line x1="236" y1="108" x2="236" y2="270" stroke="#10b981" stroke-dasharray="3,3"/>
                <text x="178" y="286" fill="#94a3b8" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Y₀</text>
                <text x="236" y="286" fill="#10b981" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Y₁</text>

                <!-- Multiplier horizontal bracket -->
                <line x1="178" y1="262" x2="236" y2="262" stroke="#10b981" stroke-width="1.8"/>
                <text x="207" y="254" fill="#10b981" font-family="var(--font-mono)" font-size="9" text-anchor="middle">ΔY = k·ΔG</text>
              </svg>
            </div>

            <div class="atlas-text-panel">
              <div class="intel-block">
                <span class="block-tag">EXAM SITUATION / SCENARIO TRIGGER</span>
                <p>Autonomous investment or government spending rises by $\Delta G$. The Keynesian Cross illustrates the geometric convergence of induced consumption rounds.</p>
              </div>

              <div class="intel-block">
                <span class="block-tag">TRANSMISSION & EQUILIBRIUM FORMULATION</span>
                <p>1. The 45-degree line represents macroeconomic goods market equilibrium where planned expenditure exactly equals actual output ($AE = Y$).<br>
                2. Autonomous spending shifts the entire Aggregate Expenditure line upward by $\Delta G$. At initial output $Y_0$, $AE > Y$, so unintended inventories deplete.<br>
                3. Firms expand output to meet demand. Every additional rupee of income induces $c = MPC$ rupees of consumption spending.<br>
                4. Total output expansion converges to: $\Delta Y = \frac{1}{1 - MPC} \Delta G = k_G \cdot \Delta G$.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- SCENARIO 14: LOANABLE FUNDS & CROWDING OUT -->
        <div class="atlas-card" id="atlas-scen-14">
          <div class="atlas-card-header">
            <span class="scen-badge">BLUEPRINT 14 // FINANCIAL INTERMEDIATION</span>
            <h4 class="scen-title">The Loanable Funds Market: Fiscal Deficit & Direct Private Investment Crowding Out</h4>
            <span class="scen-ref">REF: Unit 2 Loanable Funds Dedicated Deck</span>
          </div>

          <div class="atlas-grid">
            <div class="atlas-svg-panel">
              <svg viewBox="0 0 540 320" xmlns="http://www.w3.org/2000/svg" class="atlas-svg">
                <rect width="540" height="320" fill="#090a0f" rx="6"/>
                <line x1="50" y1="270" x2="510" y2="270" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <line x1="60" y1="280" x2="60" y2="30" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <text x="510" y="295" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" text-anchor="end">QUANTITY OF LOANABLE FUNDS (Q)</text>
                <text x="25" y="45" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" transform="rotate(-90 25,45)" text-anchor="end">REAL INTEREST RATE (r %)</text>

                <!-- Saving Curve S(r) -->
                <line x1="100" y1="250" x2="440" y2="70" stroke="#60a5fa" stroke-width="2.5"/>
                <text x="445" y="70" fill="#60a5fa" font-family="var(--font-mono)" font-size="12" font-weight="700">S(r) (Supply of Funds)</text>

                <!-- Initial Investment Demand I0 -->
                <line x1="100" y1="70" x2="400" y2="250" stroke="#fb923c" stroke-width="2" stroke-dasharray="3,3"/>
                <text x="405" y="255" fill="#fb923c" font-family="var(--font-mono)" font-size="11">I₀(r)</text>

                <!-- Total Demand with Deficit: I + (G - T) -->
                <line x1="180" y1="70" x2="480" y2="250" stroke="#fb923c" stroke-width="2.5"/>
                <text x="485" y="255" fill="#fb923c" font-family="var(--font-mono)" font-size="12" font-weight="700">I + (G - T)</text>

                <line x1="280" y1="120" x2="330" y2="120" stroke="#fb923c" stroke-width="2"/>
                <polygon points="330,116 338,120 330,124" fill="#fb923c"/>

                <!-- E0 crosshair -->
                <circle cx="242" cy="178" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="242" cy="178" r="2.5" fill="#d92534"/>
                <text x="228" y="172" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₀</text>

                <!-- E1 crosshair -->
                <circle cx="312" cy="140" r="8" fill="none" stroke="#10b981" stroke-width="2"/>
                <circle cx="312" cy="140" r="3" fill="#10b981"/>
                <text x="322" y="134" fill="#10b981" font-family="var(--font-mono)" font-size="11" font-weight="700">E₁</text>

                <line x1="60" y1="178" x2="242" y2="178" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <line x1="60" y1="140" x2="312" y2="140" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <text x="50" y="182" fill="#94a3b8" font-family="var(--font-mono)" font-size="11" text-anchor="end">r₀</text>
                <text x="50" y="144" fill="#fb923c" font-family="var(--font-mono)" font-size="11" text-anchor="end">r₁</text>
              </svg>
            </div>

            <div class="atlas-text-panel">
              <div class="intel-block">
                <span class="block-tag">EXAM SITUATION / SCENARIO TRIGGER</span>
                <p>The sovereign treasury runs a large fiscal deficit ($G > T$) and issues sovereign bonds to finance public works.</p>
              </div>

              <div class="intel-block">
                <span class="block-tag">ECONOMIC LOGIC</span>
                <p>1. <strong>Demand for Loanable Funds Surges:</strong> Total borrowing demand shifts right from $I(r)$ to $I(r) + (G - T)$.<br>
                2. <strong>Real Interest Rate Bids Up:</strong> As government competes with private businesses for a finite pool of domestic savings ($S$), real interest rates rise ($r_0 \to r_1$).<br>
                3. <strong>Direct Crowding Out:</strong> At the higher interest rate $r_1$, private corporate projects with marginal return on capital below $r_1$ become unprofitable and are cancelled ($I_1 < I_0$).</p>
              </div>
            </div>
          </div>
        </div>

        <!-- SCENARIO 15: CENTRAL BANK MONEY MARKET -->
        <div class="atlas-card" id="atlas-scen-15">
          <div class="atlas-card-header">
            <span class="scen-badge">BLUEPRINT 15 // MONETARY LIQUIDITY</span>
            <h4 class="scen-title">Central Bank Money Market Equilibrium: OMO & Policy Rate Transmission</h4>
            <span class="scen-ref">REF: Unit 3 Money Market Derivations</span>
          </div>

          <div class="atlas-grid">
            <div class="atlas-svg-panel">
              <svg viewBox="0 0 540 320" xmlns="http://www.w3.org/2000/svg" class="atlas-svg">
                <rect width="540" height="320" fill="#090a0f" rx="6"/>
                <line x1="50" y1="270" x2="510" y2="270" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <line x1="60" y1="280" x2="60" y2="30" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <text x="510" y="295" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" text-anchor="end">REAL MONEY BALANCES (M/P)</text>
                <text x="25" y="45" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" transform="rotate(-90 25,45)" text-anchor="end">INTEREST RATE (r %)</text>

                <!-- Initial Vertical Money Supply MS0 -->
                <line x1="200" y1="50" x2="200" y2="270" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>
                <text x="200" y="42" fill="#f59e0b" font-family="var(--font-mono)" font-size="11" text-anchor="middle">M₀/P</text>

                <!-- Expanded Vertical Money Supply MS1 -->
                <line x1="320" y1="50" x2="320" y2="270" stroke="#f59e0b" stroke-width="3"/>
                <text x="320" y="42" fill="#f59e0b" font-family="var(--font-mono)" font-size="12" text-anchor="middle" font-weight="700">M₁/P (OMO Buy)</text>

                <line x1="210" y1="100" x2="310" y2="100" stroke="#f59e0b" stroke-width="2"/>
                <polygon points="310,96 318,100 310,104" fill="#f59e0b"/>

                <!-- Money Demand Curve L(r, Y) -->
                <line x1="100" y1="70" x2="440" y2="250" stroke="#38bdf8" stroke-width="2.5"/>
                <text x="445" y="255" fill="#38bdf8" font-family="var(--font-mono)" font-size="12" font-weight="700">L(r, Y₀) = kY - hr</text>

                <!-- E0 crosshair -->
                <circle cx="200" cy="123" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="200" cy="123" r="2.5" fill="#d92534"/>
                <text x="185" y="117" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₀</text>

                <!-- E1 crosshair -->
                <circle cx="320" cy="187" r="8" fill="none" stroke="#10b981" stroke-width="2"/>
                <circle cx="320" cy="187" r="3" fill="#10b981"/>
                <text x="330" y="181" fill="#10b981" font-family="var(--font-mono)" font-size="11" font-weight="700">E₁</text>

                <line x1="60" y1="123" x2="200" y2="123" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <line x1="60" y1="187" x2="320" y2="187" stroke="#10b981" stroke-dasharray="3,3"/>
                <text x="50" y="127" fill="#94a3b8" font-family="var(--font-mono)" font-size="11" text-anchor="end">r₀</text>
                <text x="50" y="191" fill="#10b981" font-family="var(--font-mono)" font-size="11" text-anchor="end">r₁</text>
              </svg>
            </div>

            <div class="atlas-text-panel">
              <div class="intel-block">
                <span class="block-tag">EXAM SITUATION / SCENARIO TRIGGER</span>
                <p>RBI conducts an Open Market Operation (OMO purchase) or cuts the policy repo rate.</p>
              </div>

              <div class="intel-block">
                <span class="block-tag">ECONOMIC LOGIC</span>
                <p>Money supply is completely inelastic with respect to the interest rate in the short run because it is controlled exogenously by the monetary authority (vertical line $M_s/P$). Money demand slopes downward because interest rate represents the opportunity cost of holding non-interest-bearing currency. When the central bank expands money supply, excess liquidity forces bond yields and interest rates downward until the public is willing to hold the larger money stock ($r_0 \to r_1$).</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ========================================================================= -->
      <!-- SECTION IV: THE PHILLIPS CURVE & INFLATION EXPECTATIONS -->
      <!-- ========================================================================= -->
      <div class="atlas-section-group" id="atlas-sec-phillips">
        <div class="atlas-group-header">
          <span class="group-num">REGIME IV</span>
          <h3 class="group-title">THE PHILLIPS CURVE: SHORT-RUN TRADE-OFF VS. LONG-RUN NATURAL RATE</h3>
          <p class="group-desc">Authoritative Reference: Prof. Sana Tabassum Phillips Curve Deck. Examines the Friedman-Phelps Accelerationist Hypothesis and Inflation Expectations.</p>
        </div>

        <!-- SCENARIO 16: EXPECTATIONS-AUGMENTED PHILLIPS CURVE -->
        <div class="atlas-card" id="atlas-scen-16">
          <div class="atlas-card-header">
            <span class="scen-badge">BLUEPRINT 16 // FRIEDMAN-PHELPS MODEL</span>
            <h4 class="scen-title">Expectations-Augmented Phillips Curve: SRPC Shifts & Vertical LRPC</h4>
            <span class="scen-ref">REF: Unit 4 Phillips Curve Deck</span>
          </div>

          <div class="atlas-grid">
            <div class="atlas-svg-panel">
              <svg viewBox="0 0 540 320" xmlns="http://www.w3.org/2000/svg" class="atlas-svg">
                <rect width="540" height="320" fill="#090a0f" rx="6"/>
                <line x1="50" y1="270" x2="510" y2="270" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <line x1="60" y1="280" x2="60" y2="30" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
                <text x="510" y="295" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" text-anchor="end">UNEMPLOYMENT RATE (u %)</text>
                <text x="25" y="45" fill="#94a3b8" font-family="var(--font-mono)" font-size="12" transform="rotate(-90 25,45)" text-anchor="end">INFLATION RATE (π %)</text>

                <!-- LRPC Vertical at u* -->
                <line x1="260" y1="40" x2="260" y2="270" stroke="#ffffff" stroke-width="2.5"/>
                <text x="260" y="32" fill="#ffffff" font-family="var(--font-mono)" font-size="11" text-anchor="middle" font-weight="700">LRPC (u = u_n)</text>

                <!-- Initial SRPC0 (Expected Inflation π0^e = 2%) -->
                <line x1="120" y1="110" x2="420" y2="250" stroke="#e11d48" stroke-width="2" stroke-dasharray="3,3"/>
                <text x="425" y="255" fill="#e11d48" font-family="var(--font-mono)" font-size="11">SRPC₀ (π^e = 2%)</text>

                <!-- Shifted SRPC1 (Expected Inflation π1^e = 6%) -->
                <line x1="120" y1="50" x2="420" y2="190" stroke="#e11d48" stroke-width="2.5"/>
                <text x="425" y="195" fill="#e11d48" font-family="var(--font-mono)" font-size="12" font-weight="700">SRPC₁ (π^e = 6%)</text>

                <!-- Shift Arrow Upward -->
                <line x1="330" y1="205" x2="330" y2="155" stroke="#e11d48" stroke-width="2"/>
                <polygon points="326,155 330,147 334,155" fill="#e11d48"/>

                <!-- E0: Initial Equilibrium (u*, 2%) -->
                <line x1="60" y1="175" x2="260" y2="175" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <text x="50" y="179" fill="#94a3b8" font-family="var(--font-mono)" font-size="11" text-anchor="end">π₀ = 2%</text>

                <circle cx="260" cy="175" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="260" cy="175" r="2.5" fill="#d92534"/>
                <text x="270" y="172" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₀</text>

                <!-- E1: Short-Run Demand Stimulus -->
                <line x1="60" y1="138" x2="180" y2="138" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <line x1="180" y1="138" x2="180" y2="270" stroke="rgba(255,255,255,0.25)" stroke-dasharray="3,3"/>
                <text x="50" y="142" fill="#e11d48" font-family="var(--font-mono)" font-size="11" text-anchor="end">π₁ = 6%</text>
                <text x="180" y="286" fill="#e11d48" font-family="var(--font-mono)" font-size="11" text-anchor="middle">u₁ = 3%</text>

                <circle cx="180" cy="138" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                <circle cx="180" cy="138" r="2.5" fill="#d92534"/>
                <text x="135" y="132" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₁ (Short-Run)</text>

                <!-- E2: Long-Run Expectations Adaptation -->
                <line x1="60" y1="115" x2="260" y2="115" stroke="#ffffff" stroke-dasharray="3,3"/>
                <text x="50" y="119" fill="#ffffff" font-family="var(--font-mono)" font-size="11" text-anchor="end">π₂ = 6%</text>
                <text x="260" y="286" fill="#ffffff" font-family="var(--font-mono)" font-size="11" text-anchor="middle">u* (Natural Rate)</text>

                <circle cx="260" cy="115" r="8" fill="none" stroke="#10b981" stroke-width="2"/>
                <circle cx="260" cy="115" r="3" fill="#10b981"/>
                <text x="270" y="110" fill="#10b981" font-family="var(--font-mono)" font-size="11" font-weight="700">E₂ (Long-Run)</text>
              </svg>
            </div>

            <div class="atlas-text-panel">
              <div class="intel-block">
                <span class="block-tag">EXAM SITUATION / SCENARIO TRIGGER</span>
                <p>The Government attempts to artificially drive unemployment below the Natural Rate of Unemployment (NAIRU) via persistent monetary stimulus.</p>
              </div>

              <div class="intel-block">
                <span class="block-tag">THE FRIEDMAN-PHELPS ACCELERATIONIST THEOREM</span>
                <ol class="transmission-list">
                  <li><strong>Short-Run Tradeoff ($E_0 \to E_1$):</strong> Policy stimulus pushes aggregate demand up. With inflation expectations anchored at $\pi_0^e = 2\%$, real wages temporarily fall ($W/P \downarrow$). Firms hire aggressively, driving unemployment down to $u_1 = 3\%$, but actual inflation jumps to $\pi_1 = 6\%$.</li>
                  <li><strong>Expectations Adaptation ($E_1 \to E_2$):</strong> Workers observe that prices rose by 6%. When labor contracts renew, workers demand 6% wage hikes. Expected inflation adjusts upward: $\pi_1^e = 6\%$.</li>
                  <li><strong>SRPC Shifts Upward:</strong> Higher wage demands shift the <strong>Short-Run Phillips Curve up from $SRPC_0$ to $SRPC_1$</strong>. Real wages are restored to baseline, destroying the hiring incentive.</li>
                  <li><strong>Long-Run Vertical Trap:</strong> Unemployment returns to the natural rate ($u^*$), but inflation remains permanently elevated at 6%. <strong>There is no permanent tradeoff between inflation and unemployment in the long run.</strong></li>
                </ol>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    '''
