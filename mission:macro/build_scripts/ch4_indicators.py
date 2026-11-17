# build_scripts/ch4_indicators.py
"""
Project 007: Chapter 4 — Inflation, Unemployment and Macroeconomic Indicators
Exhaustive academic content strictly from Prof. Sana Tabassum lecture slides.
"""

def get_chapter_4():
    return """
<!-- CHAPTER 4: INFLATION, UNEMPLOYMENT AND MACROECONOMIC INDICATORS -->
<div class="chapter-container" id="chapter-4">
  <a id="ch4" class="chapter-anchor"></a>
  <div class="chapter-header">
    <div class="ch-badge-group">
      <span class="ch-code-pill">DOSSIER 04 // INTEL-INDICATORS</span>
      <h2 class="ch-title">Chapter 4 — Inflation, Unemployment & Macro Indicators</h2>
    </div>
    <div class="chapter-actions">
      <button class="ch-mastery-btn" id="ch-mastery-badge-4" onclick="toggleProgressItem(4, 'training', {checked: true})">IN PROGRESS</button>
    </div>
  </div>

  <div class="chapter-nav-tabs">
    <button class="ch-tab-btn active" data-tab="all" onclick="switchChapterTab(4, 'all')">ALL INTEL</button>
    <button class="ch-tab-btn" data-tab="training" onclick="switchChapterTab(4, 'training')">TRAINING (THE BRIEFING)</button>
    <button class="ch-tab-btn" data-tab="missions" onclick="switchChapterTab(4, 'missions')">MISSIONS (ACTIVE OPS)</button>
    <button class="ch-tab-btn" data-tab="targets" onclick="switchChapterTab(4, 'targets')">TARGETS (DEBRIEFING)</button>
  </div>

  <div class="chapter-body">
    <!-- ==================== TRAINING ENVIRONMENT ==================== -->
    <div class="training-section">
      <div class="topic-card">
        <div class="topic-header">
          <h3 class="topic-title">4.1 Inflation: Definition, Dynamics & Price Index Formulations</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Unit 1, Slide 32</span>
        </div>
        <p class="content-lead">
          <strong>Inflation</strong> is defined in macroeconomic intelligence as the <em>"Percentage change of the overall price level in a country over a specified period of time."</em> It quantifies the rate at which general purchasing power decays.
        </p>

        <div class="formula-card">
          <div class="formula-card-title">Canonical Inflation Formulas</div>
          <div class="formula-math-display">
            Inflation Rate (π_t) = [(Price Index_t − Price Index_{t-1}) / Price Index_{t-1}] × 100<br><br>
            Deflator Inflation = [(GDP Deflator_t − GDP Deflator_{t-1}) / GDP Deflator_{t-1}] × 100<br><br>
            CPI Inflation = [(CPI_t − CPI_{t-1}) / CPI_{t-1}] × 100
          </div>
          <div class="formula-breakdown">
            <ul>
              <li><strong>Consumer Price Index (CPI):</strong> Measures changes over time in the retail price of a representative basket of goods and services purchased directly by urban/rural households.</li>
              <li><strong>Critical Inflation Distinction:</strong> A price index level (e.g., $CPI_{2026} = 115$) measures prices relative to the <em>base year</em>. The annual inflation rate in 2026 measures the percentage change relative to <em>the previous year (2025)</em>!</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="topic-card">
        <div class="topic-header">
          <a id="ch4-headline-core"></a>
          <h3 class="topic-title">4.2 Headline Inflation vs Core Inflation: RBI Policy Analysis</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum IS-LM Deck (August 2026 RBI Bulletin)</span>
        </div>
        <p class="content-text">
          Modern central banks, particularly the Reserve Bank of India (RBI), dissect the monthly inflation print into two distinct components:
        </p>
        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th>Analytical Indicator</th>
                <th>August 2026 Actuals (India)</th>
                <th>Components & Scope</th>
                <th>Monetary Policy Interpretation</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Headline Inflation (CPI)</strong></td>
                <td><strong>4.82%</strong><br>(MoSPI Release)</td>
                <td>Includes all consumer goods and services across the entire retail basket, prominently including volatile <strong>Food</strong> and <strong>Fuel</strong> components.</td>
                <td>Reflects the actual out-of-pocket cost-of-living shock felt by ordinary citizens. Serves as India's <strong>formal legal inflation target</strong> under the Monetary Policy Framework (4% ± 2%).</td>
              </tr>
              <tr>
                <td><strong>Core Inflation</strong></td>
                <td><strong>4.20%</strong><br>(RBI Estimate)</td>
                <td>Excludes highly volatile food and energy/fuel items. Focuses on manufactured items, services, housing, education, and transport fares.</td>
                <td>Isolates underlying, persistent demand-side inflationary trends. Strips out transitory monsoon or geopolitical oil supply shocks to reveal long-term momentum.</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="intel-box key-intuition">
          <div class="intel-box-title">Intelligence Debrief: August 2026 Discrepancy</div>
          <p class="content-text" style="margin-bottom:0;">
            Why did Headline Inflation (4.82%) exceed Core Inflation (4.20%)? Food inflation stood at <strong>5.95%</strong> during the period. Volatile vegetable and commodity price surges pushed headline cost-of-living upward. While headline inflation signals immediate household budget strain, a stable core inflation rate of 4.2% indicates that broad underlying demand across non-food sectors remained contained.
          </p>
        </div>
      </div>

      <div class="topic-card">
        <div class="topic-header">
          <a id="ch4-labor-market"></a>
          <h3 class="topic-title">4.3 The Labor Market Architecture & Demographic Classification</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Unit 1, Slides 42-44</span>
        </div>
        <p class="content-text">
          To measure employment accurately, the national population is classified into three concentric demographic tiers according to United Nations (UN) and International Labour Organization (ILO) standards:
        </p>

        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th>Demographic Tier</th>
                <th>Definition & Composition</th>
                <th>Inclusions & Exclusions</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Total Population</strong></td>
                <td>All residents residing in the geographic territory.</td>
                <td>Encompasses infants, children, adults, and the elderly.</td>
              </tr>
              <tr>
                <td><strong>Working-Age Population</strong></td>
                <td>All individuals aged <strong>15 to 64 years</strong> (UN Standard).</td>
                <td>Represents the potential productive human capital. Excludes children (<15) and retirees (>64).</td>
              </tr>
              <tr>
                <td><strong>Labor Force (Economically Active)</strong></td>
                <td>The fraction of the working-age population willing and able to work.</td>
                <td><strong>Labor Force = Employed + Unemployed</strong>.<br>Excludes full-time students, homemakers, and discouraged workers.</td>
              </tr>
              <tr>
                <td><strong>Employed</strong></td>
                <td>Individuals currently engaged in productive economic activity.</td>
                <td>Wage employment, salaried professionals, business owners, self-employed.</td>
              </tr>
              <tr>
                <td><strong>Unemployed</strong></td>
                <td>Individuals in the labor force who: (1) Do not have a job, and (2) <strong>Are actively seeking work</strong>!</td>
                <td>If a jobless person stops looking for work, they exit the labor force and are NOT counted as unemployed!</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="formula-card">
          <div class="formula-card-title">Labor Market Mathematical Metrics</div>
          <div class="formula-math-display">
            Unemployment Rate (UR) = (Number of Unemployed / Total Labor Force) × 100<br><br>
            Employment Rate (ER) = (Number of Employed / Working-Age Population) × 100<br><br>
            Labor Force Participation Rate (LFPR) = (Total Labor Force / Working-Age Population) × 100
          </div>
          <div class="formula-breakdown">
            <ul>
              <li><strong>Common Examination Error:</strong> Dividing Unemployed by Total Population or Working-Age Population. <em>UR MUST ALWAYS be divided by the Total Labor Force!</em></li>
              <li><strong>Mathematical Relationship:</strong> $\text{Employment Rate} = \text{LFPR} \times (1 - \text{UR})$.</li>
            </ul>
          </div>
        </div>

        <h4 class="section-subtitle">Types of Unemployment & The Natural Rate of Unemployment (NRU)</h4>
        <ul style="padding-left:20px; color:var(--silver-300); margin-bottom:16px; line-height:1.8;">
          <li><strong>Frictional Unemployment:</strong> Voluntary, short-term transition unemployment of workers searching for suitable positions, relocating, or graduating.</li>
          <li><strong>Structural Unemployment:</strong> Long-term mismatch between workers' skill sets and employer demands caused by technological obsolescence, automation, or globalization.</li>
          <li><strong>Cyclical Unemployment:</strong> Joblessness directly resulting from deficient aggregate demand during business cycle contractions and recessions.</li>
          <li><strong>Natural Rate of Unemployment (NRU / NAIRU):</strong> The steady-state unemployment rate prevailing when the economy operates at potential output ($Y^*$). At $Y^*$, cyclical unemployment is zero ($u_{\text{cyclical}} = 0$), so:
            <br>$$\text{NRU} = \text{Frictional Unemployment} + \text{Structural Unemployment}$$
            <em>Full employment does NOT mean zero unemployment! It means unemployment equals the NRU.</em>
          </li>
        </ul>
      </div>
    </div>

    <!-- ==================== MISSIONS ENVIRONMENT ==================== -->
    <div class="missions-section">
      <div class="mission-card">
        <div class="mission-top-bar">
          <span class="mission-level-badge level-1">LEVEL 1 // FOUNDATION</span>
          <span class="topic-ref-tag">Unit 1 Problem 3</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 4.1: Representative Household CPI Basket Audit</h3>
        <p class="mission-question">
          A statistical agency uses the following representative household basket. Assume that 2024 is the base year:
          <br>• Food & Beverages: Cost 2024 = ₹6,000; Cost 2025 = ₹6,600
          <br>• Housing: Cost 2024 = ₹5,000; Cost 2025 = ₹5,500
          <br>• Clothing: Cost 2024 = ₹2,000; Cost 2025 = ₹2,100
          <br>• Information & Communication: Cost 2024 = ₹1,000; Cost 2025 = ₹1,050
          <br>• Education: Cost 2024 = ₹2,000; Cost 2025 = ₹2,250
          <br><br>
          <strong>Your Operational Directives:</strong><br>
          1. Calculate the CPI for 2024 and 2025.<br>
          2. Interpret the CPI obtained for 2025.<br>
          3. If the CPI in 2026 is 115, calculate the inflation rate between 2025 and 2026.<br>
          4. Explain why a CPI of 115 in 2026 should NOT be interpreted as an inflation rate of 15% in 2026.
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h4_1_1')">Hint 1: Concept</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h4_1_2')">Hint 2: Basket Sum</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h4_1_3')">Hint 3: 2026 Inflation</button>
          </div>
          <div class="hint-content-box" id="h4_1_1">
            <strong>Hint 1:</strong> CPI = (Cost of Basket in Year t / Cost of Basket in Base Year) × 100.
          </div>
          <div class="hint-content-box" id="h4_1_2">
            <strong>Hint 2:</strong> Total basket cost 2024 = ₹16,000. Total basket cost 2025 = ₹17,500.
          </div>
          <div class="hint-content-box" id="h4_1_3">
            <strong>Hint 3:</strong> Inflation between 2025 and 2026 is [(CPI_2026 - CPI_2025) / CPI_2025] × 100.
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_4_1', 4)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_4_1">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Determine CPI indices across 2024–2026, compute period inflation, and explain base-year index confusion.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • 2024 Basket: 6,000 + 5,000 + 2,000 + 1,000 + 2,000 = ₹16,000.<br>
                • 2025 Basket: 6,600 + 5,500 + 2,100 + 1,050 + 2,250 = ₹17,500.<br>
                • 2026 CPI = 115.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA SELECTION</span>
              <div class="step-content">
                • $\text{CPI}_t = (\text{Cost}_t / \text{Cost}_{\text{base}}) \times 100$<br>
                • $\pi_{2026} = [(\text{CPI}_{2026} - \text{CPI}_{2025}) / \text{CPI}_{2025}] \times 100$
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION</span>
              <div class="step-content">
                <div class="step-math">
                  1. CPI 2024 (Base Year) = (16,000 / 16,000) × 100 = 100.00.<br>
                  CPI 2025 = (17,500 / 16,000) × 100 = 109.375 ≈ 109.38.<br><br>
                  2. Interpretation of CPI 2025 (109.38): The average price of the representative household basket increased by 9.38% between 2024 and 2025.<br><br>
                  3. Inflation rate between 2025 and 2026:<br>
                  π_{2026} = [(115 − 109.375) / 109.375] × 100 = (5.625 / 109.375) × 100 = 5.14%.<br><br>
                  4. Explanation: A CPI of 115 in 2026 indicates that prices have risen by 15% <em>relative to the 2024 base year</em> over a two-year span. It is NOT the inflation rate in 2026 alone. Annual inflation in 2026 measures price growth relative to 2025, which was only 5.14%!
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                CPI index trajectory: 2024 (100) $\to$ 2025 (109.38) $\to$ 2026 (115). Annual price growth decelerated from 9.38% down to 5.14%.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                Differentiating between cumulative price level changes ($CPI - 100$) and periodic inflation rates ($\Delta CPI / CPI_{t-1}$) is crucial for monetary policy calibration.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                • CPI 2024 = 100; CPI 2025 = 109.38.<br>
                • 2025–2026 Inflation Rate = <strong>5.14%</strong>.<br>
                • 15% represents 2-year cumulative change over base year, not annual inflation.
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="mission-card">
        <div class="mission-top-bar">
          <span class="mission-level-badge level-2">LEVEL 2 // STRATEGIC EVALUATION</span>
          <span class="topic-ref-tag">Unit 1 Problem 4</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 4.2: Macroeconomic Deflator vs CPI Matrix</h3>
        <p class="mission-question">
          The following intelligence data is reported for an economy:
          <br>• <strong>2025:</strong> Nominal GDP = ₹15,750 crore; Real GDP = ₹13,125 crore; CPI = 120.
          <br>• <strong>2026:</strong> Nominal GDP = ₹18,900 crore; Real GDP = ₹14,400 crore; CPI = 130.
          <br><br>
          <strong>Your Operational Directives:</strong><br>
          a. Calculate the GDP Deflator for 2025 and 2026.<br>
          b. Calculate the inflation rate between 2025 and 2026 using (1) GDP Deflator, and (2) CPI.<br>
          c. Calculate the percentage growth in Real GDP between 2025 and 2026, and interpret the outcome.<br>
          d. Explain why CPI-based inflation differs from GDP-deflator-based inflation in this economy.
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h4_2_1')">Hint 1: Deflator Math</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h4_2_2')">Hint 2: Inflation Math</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h4_2_3')">Hint 3: Discrepancy Cause</button>
          </div>
          <div class="hint-content-box" id="h4_2_1">
            <strong>Hint 1:</strong> Deflator 2025 = (15,750 / 13,125) × 100 = 120.
          </div>
          <div class="hint-content-box" id="h4_2_2">
            <strong>Hint 2:</strong> Deflator 2026 = (18,900 / 14,400) × 100 = 131.25.
          </div>
          <div class="hint-content-box" id="h4_2_3">
            <strong>Hint 3:</strong> CPI inflation = (130 - 120) / 120 = 8.33%. Deflator inflation = (131.25 - 120) / 120 = 9.38%.
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_4_2', 4)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_4_2">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Audit divergence between producer-wide GDP Deflator inflation and consumer retail CPI inflation.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • 2025: Nominal = ₹15,750 cr; Real = ₹13,125 cr; CPI = 120.<br>
                • 2026: Nominal = ₹18,900 cr; Real = ₹14,400 cr; CPI = 130.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA SELECTION</span>
              <div class="step-content">
                • $\text{GDP Deflator} = (\text{Nominal GDP} / \text{Real GDP}) \times 100$<br>
                • $\pi_{\text{Deflator}} = [(\text{Deflator}_{2026} - \text{Deflator}_{2025}) / \text{Deflator}_{2025}] \times 100$<br>
                • $\pi_{\text{CPI}} = [(\text{CPI}_{2026} - \text{CPI}_{2025}) / \text{CPI}_{2025}] \times 100$<br>
                • $\text{Real GDP Growth} = [(\text{Real}_{2026} - \text{Real}_{2025}) / \text{Real}_{2025}] \times 100$
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION</span>
              <div class="step-content">
                <div class="step-math">
                  a. GDP Deflator 2025 = (15,750 / 13,125) × 100 = 120.00.<br>
                  GDP Deflator 2026 = (18,900 / 14,400) × 100 = 131.25.<br><br>
                  b. Inflation Calculations:<br>
                  • Deflator-based Inflation = [(131.25 − 120.00) / 120.00] × 100 = (11.25 / 120) × 100 = 9.38%.<br>
                  • CPI-based Inflation = [(130.00 − 120.00) / 120.00] × 100 = (10 / 120) × 100 = 8.33%.<br><br>
                  c. Real GDP Growth = [(14,400 − 13,125) / 13,125] × 100 = (1,275 / 13,125) × 100 = 9.71%.<br>
                  <strong>Interpretation:</strong> Physical volume of production expanded robustly by 9.71%.<br><br>
                  d. Why they differ: The GDP Deflator encompasses capital equipment, commercial tech, and government infrastructure purchases, where prices escalated by 9.38%. The CPI tracks only consumer household purchases, where retail prices rose by 8.33%. Furthermore, if import prices rose slower than domestic output prices, CPI would register lower inflation.
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                Comparison plot reveals that capital goods price inflation drove the GDP Deflator above retail CPI inflation.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                Policymakers analyzing only CPI would underestimate systemic economy-wide price pressures occurring across capital goods and infrastructure investment.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                • Deflator 2025 = 120; Deflator 2026 = 131.25.<br>
                • Deflator Inflation = <strong>9.38%</strong>; CPI Inflation = <strong>8.33%</strong>.<br>
                • Real GDP Growth = <strong>9.71%</strong>.
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="mission-card">
        <div class="mission-top-bar">
          <span class="mission-level-badge level-2">LEVEL 2 // STRATEGIC EVALUATION</span>
          <span class="topic-ref-tag">Unit 1 Problem 5</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 4.3: Real Economic Performance Audit: Italy 2011–2012</h3>
        <p class="mission-question">
          The following macroeconomic data is available for Italy:
          <br>1. Nominal GDP increased by roughly 1% between 2011 and 2012.
          <br>2. The rise in the GDP Deflator between 2011 and 2012 was 3%.
          <br>(Assume that 2011 was the base year and Nominal GDP in 2011 was €2,000 billion).
          <br><br>
          <strong>Your Operational Directives:</strong><br>
          a. Is Statement 1 alone sufficient to conclude that the economy grew between 2011 and 2012?<br>
          b. Based on both statements, estimate whether the economy grew or declined, and calculate the exact Real GDP trajectory.
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h4_3_1')">Hint 1: Concept</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h4_3_2')">Hint 2: Growth Rule</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h4_3_3')">Hint 3: Math Approximation</button>
          </div>
          <div class="hint-content-box" id="h4_3_1">
            <strong>Hint 1:</strong> Nominal growth alone is never sufficient because it confounds price increases with physical output growth.
          </div>
          <div class="hint-content-box" id="h4_3_2">
            <strong>Hint 2:</strong> 2011 Nominal = 2000. 2012 Nominal = 2020. 2012 Deflator = 103.
          </div>
          <div class="hint-content-box" id="h4_3_3">
            <strong>Hint 3:</strong> Real GDP Growth ≈ %ΔNominal GDP − %ΔGDP Deflator = 1% − 3% = −2%.
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_4_3', 4)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_4_3">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Audit Italy's macroeconomic performance using Nominal GDP and GDP Deflator adjustments.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • 2011 Base Year: Nominal GDP = €2,000 billion; Deflator = 100.<br>
                • 2012: Nominal GDP increased by 1% = €2,020 billion.<br>
                • Deflator increased by 3% = 103.00.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA SELECTION</span>
              <div class="step-content">
                • $\text{Real GDP}_{2012} = (\text{Nominal GDP}_{2012} / \text{Deflator}_{2012}) \times 100$<br>
                • %ΔReal GDP ≈ %ΔNominal GDP − %ΔDeflator
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION</span>
              <div class="step-content">
                <div class="step-math">
                  a. Statement 1 is <strong>NOT SUFFICIENT</strong>. A 1% increase in nominal GDP could be caused entirely by higher price levels while real physical production stagnates or shrinks.<br><br>
                  b. Quantitative Verification:<br>
                  • Real GDP 2011 = €2,000 billion.<br>
                  • Nominal GDP 2012 = €2,000 × 1.01 = €2,020 billion.<br>
                  • Real GDP 2012 = (€2,020 / 103) × 100 = €1,961.17 billion.<br>
                  • Percentage change in Real GDP = [(1,961.17 − 2,000) / 2,000] × 100 = −1.94% (≈ −2.00%).<br><br>
                  <strong>Definitive Conclusion:</strong> The economy <strong>DECLINED</strong> by approximately 1.94%. The nominal gain was a statistical illusion masking an active recession.
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                The price index line climbed faster than total expenditure, causing physical output to contract from €2,000B to €1,961.17B.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                During the European debt crisis of 2011–2012, stagflationary pressures squeezed real consumer demand, causing Italy's real output to contract despite positive nominal receipts.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                <strong>Verdict:</strong> Economy contracted. Real GDP = €1,961.17 billion (<strong>−1.94% contraction</strong>).
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
          <h3 class="topic-title">Chapter 4 Solutions & Verification Dossier</h3>
          <span class="topic-ref-tag">TARGET PROTOCOL: 7-STEP VERIFICATION</span>
        </div>
        <p class="content-text">
          Remember the core exam takeaway: The unemployment rate must ALWAYS be calculated as a percentage of the <strong>Labor Force</strong>, while the employment rate is calculated as a percentage of the <strong>Working-Age Population</strong>!
        </p>
      </div>
    </div>
  </div>
</div>
"""
