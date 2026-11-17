# build_scripts/ch3_deflator.py
"""
Project 007: Chapter 3 — GDP Measurement, National Income Conversions and Deflators
Exhaustive academic content on Real vs Nominal, Base Year, Conversions,
GDP Deflator, Double Deflation Method, and Mid-Term Exam Question 2.
"""

def get_chapter_3():
    return """
<!-- CHAPTER 3: GDP MEASUREMENT, CONVERSIONS AND DEFLATORS -->
<div class="chapter-container" id="chapter-3">
  <a id="ch3" class="chapter-anchor"></a>
  <div class="chapter-header">
    <div class="ch-badge-group">
      <span class="ch-code-pill">DOSSIER 03 // INTEL-CONVERSIONS</span>
      <h2 class="ch-title">Chapter 3 — GDP Measurement, Conversions & Deflators</h2>
    </div>
    <div class="chapter-actions">
      <button class="ch-mastery-btn" id="ch-mastery-badge-3" onclick="toggleProgressItem(3, 'training', {checked: true})">IN PROGRESS</button>
    </div>
  </div>

  <div class="chapter-nav-tabs">
    <button class="ch-tab-btn active" data-tab="all" onclick="switchChapterTab(3, 'all')">ALL INTEL</button>
    <button class="ch-tab-btn" data-tab="training" onclick="switchChapterTab(3, 'training')">TRAINING (THE BRIEFING)</button>
    <button class="ch-tab-btn" data-tab="missions" onclick="switchChapterTab(3, 'missions')">MISSIONS (ACTIVE OPS)</button>
    <button class="ch-tab-btn" data-tab="targets" onclick="switchChapterTab(3, 'targets')">TARGETS (DEBRIEFING)</button>
  </div>

  <div class="chapter-body">
    <!-- ==================== TRAINING ENVIRONMENT ==================== -->
    <div class="training-section">
      <div class="topic-card">
        <div class="topic-header">
          <h3 class="topic-title">3.1 Real GDP vs Nominal GDP & The Base Year Mechanism</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Unit 1, Slides 29-31</span>
        </div>
        <p class="content-lead">
          When examining national economic expansion, a critical operational distinction must be drawn between an economy producing <em>more actual goods and services</em> versus an economy merely selling the <em>same volume at higher inflated price tags</em>.
        </p>

        <div class="formula-card">
          <div class="formula-card-title">Mathematical Formulation: Nominal vs Real GDP</div>
          <div class="formula-math-display">
            Nominal GDP = ∑ (Current Year Quantity Q_t × Current Year Price P_t)<br>
            Real GDP = ∑ (Current Year Quantity Q_t × Base Year Price P_base)
          </div>
          <div class="formula-breakdown">
            <ul>
              <li><strong>Nominal GDP:</strong> The market value of final goods and services measured at current prevailing prices. It is heavily distorted by inflation.</li>
              <li><strong>Real GDP:</strong> The market value of final goods and services measured at constant base-year prices. It strips out all price-level changes, serving as the authentic indicator of an economy's physical production capacity.</li>
              <li><strong>Base Year:</strong> The benchmark reference year chosen by national statistical agencies to compare physical output over time (assigned an index of 100). <em>Note: In India, the official GDP base year was updated from 2011–12 to 2022–23 by MoSPI!</em></li>
            </ul>
          </div>
        </div>
      </div>

      <div class="topic-card">
        <div class="topic-header">
          <h3 class="topic-title">3.2 National Income Aggregates & Conversion Matrix</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Unit 1, Slide 41</span>
        </div>
        <p class="content-text">
          To transition seamlessly between macroeconomic indicators, memorize the three core transition bridges:
        </p>
        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th>Conversion Dimension</th>
                <th>Mathematical Operation</th>
                <th>Underlying Economic Meaning</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Gross to Net (Depreciation)</strong></td>
                <td><strong>Net = Gross − Depreciation</strong><br>$(NDP = GDP - \text{Depreciation})$</td>
                <td>Depreciation (Consumption of Fixed Capital) represents the physical wear, tear, and obsolescence of machinery during production. Net product reflects sustainable additions to capital.</td>
              </tr>
              <tr>
                <td><strong>Domestic to National (NFIA)</strong></td>
                <td><strong>National = Domestic + NFIA</strong><br>$(GNP = GDP + NFIA)$</td>
                <td><strong>Net Factor Income from Abroad (NFIA)</strong> = Factor income earned by domestic residents abroad minus factor income earned by foreign residents inside the domestic territory.</td>
              </tr>
              <tr>
                <td><strong>Market Price to Factor Cost (NIT)</strong></td>
                <td><strong>$GDP_{FC} = GDP_{MP} − \text{Net Indirect Taxes}$</strong><br>$\text{NIT} = \text{Indirect Taxes} − \text{Subsidies}$</td>
                <td>Market prices include indirect product taxes (which artificially inflate prices) and subtract subsidies (which artificially lower prices). Factor cost measures pure factor payments.</td>
              </tr>
              <tr>
                <td><strong>National Income (NNP at FC)</strong></td>
                <td><strong>$\text{National Income} = \text{NNP}_{FC}$</strong></td>
                <td>Net National Product at Factor Cost is recognized internationally as the purest measure of national income earned by a country's citizens.</td>
              </tr>
              <tr>
                <td><strong>Personal Disposable Income ($Y_d$)</strong></td>
                <td><strong>$Y_d = GDP + NFIA + TR − T$</strong></td>
                <td>The net purchasing power actually available to households for current consumption ($C$) and private saving ($S_p$).</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="topic-card">
        <div class="topic-header">
          <a id="ch3-deflator-mechanics"></a>
          <h3 class="topic-title">3.3 The GDP Deflator: Mechanics, Computation & Interpretation</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Unit 1, Slides 31-32</span>
        </div>
        <p class="content-text">
          The <strong>GDP Deflator</strong> is a comprehensive price index that measures the overall change in prices of all final domestically produced goods and services in an economy relative to the base year.
        </p>

        <div class="formula-card">
          <div class="formula-card-title">Formula for GDP Deflator & Inflation</div>
          <div class="formula-math-display">
            GDP Deflator = (Nominal GDP / Real GDP) × 100<br><br>
            Inflation Rate (π_t) = [(GDP Deflator_t − GDP Deflator_{t-1}) / GDP Deflator_{t-1}] × 100
          </div>
          <div class="formula-breakdown">
            <ul>
              <li><strong>Interpretation when Deflator = 100:</strong> The overall price level in the current year is identical to the base year.</li>
              <li><strong>Interpretation when Deflator > 100:</strong> The price level has increased. For example, a deflator of 125 means overall prices have risen by $125 - 100 = 25\%$ compared to the base year.</li>
              <li><strong>Interpretation when Deflator < 100:</strong> The price level has declined (deflation). A deflator of 95 indicates prices are 5% lower than in the base year.</li>
            </ul>
          </div>
        </div>

        <h4 class="section-subtitle">GDP Deflator vs Consumer Price Index (CPI): Master Comparison</h4>
        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th>Feature</th>
                <th>GDP Deflator</th>
                <th>Consumer Price Index (CPI)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Basket of Goods</strong></td>
                <td>Includes <strong>all final goods and services produced domestically</strong> (consumption goods, capital goods, infrastructure, defense goods).</td>
                <td>Includes a fixed, representative basket of goods and services <strong>typically purchased and consumed by households</strong>.</td>
              </tr>
              <tr>
                <td><strong>Treatment of Imports</strong></td>
                <td><strong>STRICTLY EXCLUDED:</strong> Imported goods (e.g., imported crude oil, foreign electronics) are not produced domestically and never enter GDP.</td>
                <td><strong>INCLUDED:</strong> Imported consumer items purchased by domestic households directly impact the household cost-of-living basket.</td>
              </tr>
              <tr>
                <td><strong>Capital Goods</strong></td>
                <td><strong>INCLUDED:</strong> New factory machinery, commercial transport, and industrial robots enter GDP as investment.</td>
                <td><strong>EXCLUDED:</strong> Households do not buy commercial data servers or construction cranes!</td>
              </tr>
              <tr>
                <td><strong>Weighting Structure</strong></td>
                <td><strong>Paasche Index (Changing Weights):</strong> Weights adjust automatically each year to reflect current production quantities.</td>
                <td><strong>Laspeyres Index (Fixed Weights):</strong> Evaluates a fixed market basket determined in a historical survey period.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="topic-card">
        <div class="topic-header">
          <a id="ch3-double-deflation"></a>
          <h3 class="topic-title">3.4 Double Deflation Method: Advanced Industrial Intelligence</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Dedicated Deck & Midsem Question 2</span>
        </div>
        <p class="content-lead">
          The <strong>Double Deflation Method</strong> is the gold-standard statistical technique used to calculate real Gross Value Added (GVA) by separately adjusting the nominal value of gross output and its intermediate inputs using distinct, specific price indices.
        </p>

        <div class="formula-card">
          <div class="formula-card-title">Formulas for Double Deflation</div>
          <div class="formula-math-display">
            Real GVA = Real Gross Output − Real Intermediate Inputs<br><br>
            Real Gross Output = (Nominal Gross Output / Output Price Index) × 100<br>
            Real Intermediate Inputs = (Nominal Intermediate Value / Input Price Index) × 100
          </div>
          <div class="formula-breakdown">
            <ul>
              <li><strong>Single Deflation (Opposition / Flawed Method):</strong> Deflates nominal GVA by a single output price index: $\text{Real GVA} = \frac{\text{Nominal GVA}}{\text{Output Price Index}} \times 100$. This naively assumes that input prices and output prices move at identical rates!</li>
              <li><strong>Why Double Deflation is Superior:</strong> Input prices (raw materials, energy, imported petroleum) frequently experience violent price swings that diverge completely from the selling prices of finished goods. Double deflation eliminates distortions and accurately captures genuine physical value addition.</li>
              <li><strong>Institutional Mandate:</strong> Strongly recommended by the United Nations System of National Accounts (SNA) and officially implemented by India's Ministry of Statistics and Programme Implementation (MoSPI) under the 2022–23 base series.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- ==================== MISSIONS ENVIRONMENT ==================== -->
    <div class="missions-section">
      <div class="mission-card">
        <div class="mission-top-bar">
          <span class="mission-level-badge level-1">LEVEL 1 // FOUNDATION</span>
          <span class="topic-ref-tag">Unit 1 Problem 1</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 3.1: Two-Good Economy Deflator & Growth Tracking</h3>
        <p class="mission-question">
          A stylized economy produces only two final goods: Books and Bags. The economic data is as follows:
          <br>• <strong>2022 (Base Year):</strong> Books: Price = ₹200, Quantity = 100; Bags: Price = ₹500, Quantity = 50.
          <br>• <strong>2025 (Current Year):</strong> Books: Price = ₹250, Quantity = 120; Bags: Price = ₹600, Quantity = 60.
          <br><br>
          <strong>Your Operational Directives:</strong><br>
          a. Calculate Nominal GDP in 2022.<br>
          b. Calculate Nominal GDP in 2025.<br>
          c. Calculate Real GDP in 2025 using 2022 as base year.<br>
          d. Compute the GDP Deflator for 2025 and interpret the result.<br>
          e. Calculate the percentage growth in Real GDP between 2022 and 2025.
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h3_1_1')">Hint 1: Concept</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h3_1_2')">Hint 2: Formulas</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h3_1_3')">Hint 3: Execution</button>
          </div>
          <div class="hint-content-box" id="h3_1_1">
            <strong>Hint 1:</strong> In the base year (2022), Nominal GDP and Real GDP are identical.
          </div>
          <div class="hint-content-box" id="h3_1_2">
            <strong>Hint 2:</strong> Real GDP in 2025 evaluates 2025 quantities using 2022 base prices.
          </div>
          <div class="hint-content-box" id="h3_1_3">
            <strong>Hint 3:</strong> Deflator = (Nominal / Real) × 100. Growth = [(Real 2025 - Real 2022) / Real 2022] × 100.
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_3_1', 3)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_3_1">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Determine Nominal GDP, Real GDP, GDP Deflator, and Real Economic Growth for a two-good economy.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • 2022: $P_b = 200, Q_b = 100; P_g = 500, Q_g = 50$.<br>
                • 2025: $P_b = 250, Q_b = 120; P_g = 600, Q_g = 60$.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA SELECTION</span>
              <div class="step-content">
                • $\text{Nominal GDP}_t = \sum (P_t \times Q_t)$<br>
                • $\text{Real GDP}_t = \sum (P_{2022} \times Q_t)$<br>
                • $\text{Deflator}_{2025} = (\text{Nominal}_{2025} / \text{Real}_{2025}) \times 100$<br>
                • $\text{Real Growth} = [(\text{Real}_{2025} - \text{Real}_{2022}) / \text{Real}_{2022}] \times 100$
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION</span>
              <div class="step-content">
                <div class="step-math">
                  a. Nominal GDP 2022 = (200 × 100) + (500 × 50) = 20,000 + 25,000 = ₹45,000.<br><br>
                  b. Nominal GDP 2025 = (250 × 120) + (600 × 60) = 30,000 + 36,000 = ₹66,000.<br><br>
                  c. Real GDP 2025 (at 2022 prices) = (200 × 120) + (500 × 60) = 24,000 + 30,000 = ₹54,000.<br><br>
                  d. GDP Deflator 2025 = (₹66,000 / ₹54,000) × 100 = 122.22.<br>
                  <strong>Interpretation:</strong> The overall price level of final goods has increased by 22.22% between 2022 and 2025.<br><br>
                  e. Real GDP Growth = [(₹54,000 − ₹45,000) / ₹45,000] × 100 = (9,000 / 45,000) × 100 = 20.00%.
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                Nominal GDP expanded by 46.67% (from ₹45,000 to ₹66,000). The deflator proves that 26.67% of that increase was pure price inflation, while genuine physical output expanded by 20%.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                Evaluating the economy purely on Nominal GDP would severely overstate performance. Real GDP isolates physical volume, confirming that production expanded by 20%.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                • Nominal GDP 2022 = ₹45,000; Nominal GDP 2025 = ₹66,000.<br>
                • Real GDP 2025 = ₹54,000.<br>
                • GDP Deflator = 122.22 (+22.22% price increase).<br>
                • Real GDP Growth = 20.00%.
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="mission-card">
        <div class="mission-top-bar">
          <span class="mission-level-badge level-2">LEVEL 2 // STRATEGIC EVALUATION</span>
          <span class="topic-ref-tag">Unit 1 Problem 2</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 3.2: Media Claim Interception (Growth Illusion)</h3>
        <p class="mission-question">
          In 2025, a newspaper reported that the economy had performed strongly because GDP increased from ₹6,000 crore in 2024 to ₹6,600 crore in 2025. The report concluded that the country's production of goods and services had increased by 10% during the year.
          <br>However, the National Statistical Office reported that the GDP Deflator increased from 100 in 2024 to 120 in 2025.
          <br><br>
          <strong>Your Operational Directives:</strong><br>
          a. Calculate Real GDP for 2024 and 2025.<br>
          b. Calculate the true percentage change in Real GDP between 2024 and 2025.<br>
          c. Evaluate whether the newspaper's conclusion that production increased by 10% is correct.
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h3_2_1')">Hint 1: Concept</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h3_2_2')">Hint 2: Deflating GDP</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h3_2_3')">Hint 3: Evaluation</button>
          </div>
          <div class="hint-content-box" id="h3_2_1">
            <strong>Hint 1:</strong> The newspaper looked only at Nominal GDP (which rose 10% from 6,000 to 6,600).
          </div>
          <div class="hint-content-box" id="h3_2_2">
            <strong>Hint 2:</strong> Real GDP = (Nominal GDP / Deflator) × 100.
          </div>
          <div class="hint-content-box" id="h3_2_3">
            <strong>Hint 3:</strong> If price levels rose by 20% (deflator 120) while nominal spending rose only 10%, physical production must have fallen!
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_3_2', 3)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_3_2">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Audit newspaper claim of 10% output growth using official deflator statistics.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • 2024: Nominal GDP = ₹6,000 crore; GDP Deflator = 100.<br>
                • 2025: Nominal GDP = ₹6,600 crore; GDP Deflator = 120.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA SELECTION</span>
              <div class="step-content">
                • $\text{Real GDP} = (\text{Nominal GDP} / \text{GDP Deflator}) \times 100$<br>
                • $\text{Real GDP Growth} = [(\text{Real GDP}_{2025} - \text{Real GDP}_{2024}) / \text{Real GDP}_{2024}] \times 100$
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION</span>
              <div class="step-content">
                <div class="step-math">
                  a. Real GDP 2024 = (₹6,000 / 100) × 100 = ₹6,000 crore.<br>
                  Real GDP 2025 = (₹6,600 / 120) × 100 = ₹5,500 crore.<br><br>
                  b. True Real GDP Change = [(₹5,500 − ₹6,000) / ₹6,000] × 100 = (−₹500 / ₹6,000) × 100 = −8.33%.<br><br>
                  c. Evaluation: The newspaper's conclusion that production increased by 10% is <strong>COMPLETELY INCORRECT</strong>. The 10% increase was purely nominal price inflation. In physical reality, production contracted by 8.33%! The economy was in recession.
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                The deflator index line (100 to 120) outpaces the nominal GDP expansion line (6000 to 6600), driving the real GDP vector downward from 6000 to 5500.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                A classic illustration of "money illusion": Citizens and journalists mistake higher price totals for higher physical wealth, blinding policymakers to an active industrial contraction.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                <strong>Verdict:</strong> Newspaper claim rejected. Real GDP fell by <strong>-8.33%</strong> (from ₹6,000 cr to ₹5,500 cr).
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="mission-card">
        <div class="mission-top-bar">
          <span class="mission-level-badge level-3">LEVEL 3 // ADVANCED EXAMINATION OPERATION</span>
          <span class="topic-ref-tag">SEPTEMBER 2026 MIDSEM EXAM QUESTION 2</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 3.3: Zephyra Manufacturing & Double Deflation Audit</h3>
        <p class="mission-question">
          The government of Zephyra has announced that manufacturing activity recovered strongly in 2025. An opposition economist disputes this claim, arguing that real manufacturing GVA did not grow at all. The base year is 2020.
          <br><br>
          <strong>Primary Intelligence Data:</strong>
          <br>• Nominal value of manufacturing output: 2020 = ₹1,000 crore; 2025 = ₹1,440 crore.
          <br>• Nominal value of intermediate inputs: 2020 = ₹400 crore; 2025 = ₹720 crore.
          <br>• Output-price index: 2020 = 100; 2025 = 120.
          <br>• Input-price index: 2020 = 100; 2025 = 150.
          <br><br>
          <strong>Additional Fiscal Data:</strong>
          <br>• Nominal product taxes: 2020 = ₹70 crore; 2025 = ₹120 crore.
          <br>• Nominal product subsidies: 2020 = ₹10 crore; 2025 = ₹20 crore.
          <br>• Net product taxes at 2020 prices: 2020 = ₹60 crore; 2025 = ₹80 crore.
          <br><br>
          The opposition economist calculates real GVA by dividing 2025 nominal GVA by the output-price index. The government argues that output and intermediate inputs must be deflated separately.
          <br><br>
          <strong>Your Operational Directives (Official 4-Part Mandate):</strong><br>
          1. Calculate nominal manufacturing GVA and nominal GDP for 2025 (1 mark).<br>
          2. Estimate 2025 real GVA under the opposition's method and the government's method (1 mark).<br>
          3. Advise on which method better reflects the available price information (1 mark).<br>
          4. Calculate real GDP growth between 2020 and 2025 and evaluate the government's additional claim that the increase in real GDP was driven entirely by increased production (1 mark).
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h3_3_1')">Hint 1: Nominal Accounting</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h3_3_2')">Hint 2: Deflation Discrepancy</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h3_3_3')">Hint 3: Production Claim</button>
          </div>
          <div class="hint-content-box" id="h3_3_1">
            <strong>Hint 1:</strong> Nominal GVA = Gross Output − Intermediate Inputs. Nominal GDP = Nominal GVA + Net Product Taxes.
          </div>
          <div class="hint-content-box" id="h3_3_2">
            <strong>Hint 2:</strong> Opposition single deflation: 720 / 1.20. Double deflation: (1,440 / 1.20) − (720 / 1.50).
          </div>
          <div class="hint-content-box" id="h3_3_3">
            <strong>Hint 3:</strong> Decompose the ₹140 cr real GDP rise: How much came from real GVA vs real net taxes?
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_3_3', 3)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_3_3">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Official Mid-Term Examination Question 2: Audit Zephyra manufacturing accounts, execute Single vs Double Deflation, calculate growth, and evaluate political claims.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • 2020 (Base Year): Output = ₹1,000 cr; Inputs = ₹400 cr; Output Index = 100; Input Index = 100.<br>
                • 2020 Taxes: Product taxes = ₹70 cr; Subsidies = ₹10 cr; Net taxes = ₹60 cr.<br>
                • 2025: Output = ₹1,440 cr; Inputs = ₹720 cr; Output Index = 120 (1.20); Input Index = 150 (1.50).<br>
                • 2025 Taxes: Product taxes = ₹120 cr; Subsidies = ₹20 cr; Real net taxes at 2020 prices = ₹80 cr.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA SELECTION</span>
              <div class="step-content">
                • $\text{Nominal GVA} = \text{Output} - \text{Inputs}$<br>
                • $\text{Nominal GDP} = \text{Nominal GVA} + \text{Net Product Taxes}$<br>
                • $\text{Single Deflated Real GVA} = \text{Nominal GVA} / (\text{Output Index} / 100)$<br>
                • $\text{Double Deflated Real GVA} = [\text{Output} / (\text{Output Index} / 100)] - [\text{Inputs} / (\text{Input Index} / 100)]$<br>
                • $\text{Real GDP} = \text{Real GVA} + \text{Real Net Product Taxes}$
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION (OFFICIAL ANSWER KEY METHODOLOGY)</span>
              <div class="step-content">
                <div class="step-math">
                  1. Nominal manufacturing GVA and nominal GDP, 2025:<br>
                  Nominal GVA = ₹1,440 − ₹720 = ₹720 crore.<br>
                  Net product taxes (nominal) = ₹120 − ₹20 = ₹100 crore.<br>
                  Nominal GDP = ₹720 + ₹100 = ₹820 crore.<br><br>
                  2. Real GVA under the two methods:<br>
                  Opposition method: Real GVA = ₹720 / 1.20 = ₹600 crore.<br>
                  Government Method (Double deflation method):<br>
                  Real output = ₹1,440 / 1.20 = ₹1,200 crore;<br>
                  Real intermediate consumption = ₹720 / 1.50 = ₹480 crore.<br>
                  Government method: Real GVA = Real output − real intermediate consumption<br>
                  = ₹1,200 − ₹480 = ₹720 crore.<br><br>
                  3. Method Assessment & Advice:<br>
                  Double deflation method better reflects the given price data because the output and the intermediate inputs have different indices (120 and 150). Single deflation applies the output price index to both components and understates the real GVA of 2025.<br>
                  Base year real GVA (2020) = ₹1,000 − ₹400 = ₹600 crore.<br>
                  Double deflated real GVA growth = [(720 − 600) / 600] × 100 = 20%.<br><br>
                  4. Real GDP growth and production claim:<br>
                  Real GDP (2020) = 600 + (70 − 10) = ₹660 crore.<br>
                  Real GDP 2025 at 2020 prices = Real GVA + Real net product taxes = 720 + 80 = ₹800 crore.<br>
                  Real GDP growth between 2020 and 2025 = [(800 − 660) / 660] × 100 = 21.21%.<br><br>
                  Evaluation of Claim: Out of the ₹140 crore increase in real GDP (800 − 660):<br>
                  • ₹120 crore (85.7%) arose from higher real GVA (production).<br>
                  • ₹20 crore (14.3%) arose from higher real net product taxes (80 − 60).<br>
                  Therefore, the increase was NOT entirely accounted for by increased production!
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                A decomposition graph shows: Real GDP 2020 = ₹660 cr $\to$ Real GDP 2025 = ₹800 cr. Physical production contributed ₹120 cr, while tax policy shifts contributed ₹20 cr.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                Intermediate inputs experienced severe inflation (index 150) compared to finished goods (index 120). By deflating intermediate consumption by the appropriate input index (150), double deflation recognizes that firms achieved physical intermediate savings, revealing authentic production growth of 20% rather than 0%.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                <strong>OFFICIAL SCORE METRICS:</strong><br>
                1. 2025 Nominal GVA = ₹720 crore; Nominal GDP = ₹820 crore.<br>
                2. Opposition Real GVA = ₹600 crore; Double Deflated Real GVA = ₹720 crore.<br>
                3. Double deflation endorsed: eliminates input-output price divergence bias.<br>
                4. Real GDP Growth = 21.21%; Government claim refuted (14.3% of growth driven by net taxes).<br>
                <em>Full 4/4 marks verified.</em>
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
          <h3 class="topic-title">Chapter 3 Target Solutions & Deflator Toolkit</h3>
          <span class="topic-ref-tag">TARGET PROTOCOL: 7-STEP VERIFICATION</span>
        </div>
        <p class="content-text">
          Master the double deflation procedure: Always compute Real Output and Real Intermediate Consumption separately before finding Real GVA. Never apply a single deflator across disparate input-output price regimes.
        </p>
      </div>
    </div>
  </div>
</div>
"""
