# build_scripts/ch2_national_income.py
"""
Project 007: Chapter 2 — National Income Accounting
Exhaustive coverage of 3 approaches, cautionary rules, HBR welfare critique,
and all lecture case studies (Breadland, Macrovia, Econia, Media/Entertainment,
Brownie Points, and Mid-Term Exam Question 1).
"""

def get_chapter_2():
    return """
<!-- CHAPTER 2: NATIONAL INCOME ACCOUNTING -->
<div class="chapter-container" id="chapter-2">
  <a id="ch2" class="chapter-anchor"></a>
  <div class="chapter-header">
    <div class="ch-badge-group">
      <span class="ch-code-pill">DOSSIER 02 // INTEL-ACCOUNTING</span>
      <h2 class="ch-title">Chapter 2 — National Income Accounting</h2>
    </div>
    <div class="chapter-actions">
      <button class="ch-mastery-btn" id="ch-mastery-badge-2" onclick="toggleProgressItem(2, 'training', {checked: true})">IN PROGRESS</button>
    </div>
  </div>

  <div class="chapter-nav-tabs">
    <button class="ch-tab-btn active" data-tab="all" onclick="switchChapterTab(2, 'all')">ALL INTEL</button>
    <button class="ch-tab-btn" data-tab="training" onclick="switchChapterTab(2, 'training')">TRAINING (THE BRIEFING)</button>
    <button class="ch-tab-btn" data-tab="missions" onclick="switchChapterTab(2, 'missions')">MISSIONS (ACTIVE OPS)</button>
    <button class="ch-tab-btn" data-tab="targets" onclick="switchChapterTab(2, 'targets')">TARGETS (DEBRIEFING)</button>
  </div>

  <div class="chapter-body">
    <!-- ==================== TRAINING ENVIRONMENT ==================== -->
    <div class="training-section">
      <div class="topic-card">
        <div class="topic-header">
          <h3 class="topic-title">2.1 The Master Identity: Three Approaches to One Reality</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Unit 1, Slides 19-21</span>
        </div>
        <p class="content-lead">
          <strong>Gross Domestic Product (GDP)</strong> or National Income refers to the <em>"Total market value of all final goods and services produced within the economic territory of a country during a given period of time."</em>
        </p>
        <p class="content-text">
          In national income intelligence, there are not three different national incomes—there is only <strong>one single economic reality measured from three distinct vantage points</strong>:
        </p>
        <div class="intel-box key-intuition">
          <div class="intel-box-title">The Three Inquiries of Economic Activity</div>
          <ul style="padding-left:20px; color:var(--silver-200); line-height:1.8;">
            <li><strong>1. What was produced?</strong> $\implies$ <strong>Production Approach / Value-Added Method</strong> (Aggregate Net Output created across all production stages).</li>
            <li><strong>2. Who received income from producing the output?</strong> $\implies$ <strong>Income Approach</strong> (Sum of all factor incomes distributed to households and resource owners).</li>
            <li><strong>3. Who spent money buying the product?</strong> $\implies$ <strong>Expenditure Approach</strong> (Sum of all final expenditures by buyers clearing goods from the market).</li>
          </ul>
        </div>

        <div class="formula-card">
          <div class="formula-card-title">National Income Accounting Master Identity</div>
          <div class="formula-math-display">
            TOTAL PRODUCTION (Value Added) ≡ TOTAL EXPENDITURE (C + I + G) ≡ TOTAL INCOME (W + R + In + P + MI)
          </div>
          <div class="formula-breakdown">
            Because every final purchase is equal to the value of final goods produced, and every rupee paid for a product is completely paid out as factor rewards to workers, landowners, capital lenders, and business owners, all three methods arrive at the identical GDP figure.
          </div>
        </div>
      </div>

      <div class="topic-card">
        <div class="topic-header">
          <a id="ch2-value-added"></a>
          <h3 class="topic-title">2.2 The Production / Value-Added Approach</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Slides 21-22</span>
        </div>
        <p class="content-text">
          The Production Approach calculates GDP by summing the <strong>Gross Value Added (GVA)</strong> created at every stage of the production process across every enterprise in the economy.
        </p>

        <h4 class="section-subtitle">Final Goods vs Intermediate Goods & The Double Counting Hazard</h4>
        <ul style="padding-left:20px; color:var(--silver-300); margin-bottom:16px; line-height:1.8;">
          <li><strong>Intermediate Goods:</strong> Goods and raw materials that are completely used up, transformed, or resold as inputs in the production of other goods during the current accounting period (e.g., wheat sold to a flour mill, sugarcane sold to a sugar factory, denim sold to an apparel maker).</li>
          <li><strong>Final Goods:</strong> Goods purchased by final users (consumers, government, or firms buying capital equipment) that will not undergo any further commercial transformation within the accounting period.</li>
          <li><strong>Double Counting Hazard:</strong> If a statistician simply adds the gross sales revenue of the farmer (₹100), the miller (₹150), and the baker (₹200), total measured output would appear to be ₹450. This is an illusion because the value of the wheat was counted three times and the value of the flour was counted twice!</li>
        </ul>

        <div class="formula-card">
          <div class="formula-card-title">Formula for Gross Value Added</div>
          <div class="formula-math-display">
            Value Added (GVA) = Value of Gross Output − Intermediate Consumption
          </div>
          <div class="formula-breakdown">
            <ul>
              <li><strong>Value of Gross Output:</strong> Total sales revenue plus the value of additions to inventory (unsold output).</li>
              <li><strong>Intermediate Consumption:</strong> The cost of raw materials, energy, and contracted services purchased from other producers and consumed in production.</li>
              <li><strong>GDP via Production Method:</strong> $\text{GDP} = \sum (\text{Value Added by all Domestic Producers})$.</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="topic-card">
        <div class="topic-header">
          <a id="ch2-income-approach"></a>
          <h3 class="topic-title">2.3 The Income Approach</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Slide 21</span>
        </div>
        <p class="content-text">
          The Income Approach measures national income by aggregating all factor payments earned by the owners of factors of production for services rendered in current domestic production.
        </p>
        <div class="formula-card">
          <div class="formula-card-title">Formula for GDP via Income Approach</div>
          <div class="formula-math-display">
            GDP = Wages & Salaries + Rent + Interest + Corporate Profits + Mixed Income
          </div>
          <div class="formula-breakdown">
            <ul>
              <li><strong>Wages & Salaries (Compensation of Employees):</strong> Direct wages, salaries, employer pension contributions, bonuses, and perks.</li>
              <li><strong>Rent:</strong> Income accruing to owners of land, commercial buildings, and natural resources, including imputed rent on owner-occupied housing.</li>
              <li><strong>Interest:</strong> Net interest earned by households on capital lent to businesses and financial intermediaries (consumer loan interest is excluded).</li>
              <li><strong>Profits:</strong> Net corporate earnings, dividends distributed to shareholders, corporate income taxes, and retained/undistributed corporate profits.</li>
              <li><strong>Mixed Income:</strong> Incomes of unincorporated self-employed enterprises (farmers, independent consultants, shop owners) where labor and capital returns cannot be separated.</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="topic-card">
        <div class="topic-header">
          <a id="ch2-expenditure-approach"></a>
          <h3 class="topic-title">2.4 The Expenditure Approach</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Slide 21</span>
        </div>
        <p class="content-text">
          The Expenditure Approach calculates GDP by summing all final expenditures incurred on newly produced domestic goods and services during the accounting year.
        </p>
        <div class="formula-card">
          <div class="formula-card-title">Formula for GDP via Expenditure Approach</div>
          <div class="formula-math-display">
            GDP = C + I + G + NX
          </div>
          <div class="formula-breakdown">
            <ul>
              <li><strong>Consumption ($C$):</strong> Household final consumption expenditure on newly produced durable goods, non-durable goods, and services.</li>
              <li><strong>Investment ($I$):</strong> Gross domestic capital formation:
                <br>1. Business fixed investment (machinery, factory buildings, tech systems).
                <br>2. Residential construction (new housing).
                <br>3. <strong>Change in Inventories ($\Delta \text{Inv}$):</strong> Value of goods produced in the current year but unsold at year-end.
              </li>
              <li><strong>Government Purchases ($G$):</strong> Direct purchases of newly produced goods and services by governments (defense equipment, teacher salaries, public highway construction).</li>
              <li><strong>Net Exports ($NX$):</strong> Exports ($X$) minus Imports ($M$) (in an open economy).</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="topic-card">
        <div class="topic-header">
          <h3 class="topic-title">2.5 Strict National Income Accounting Rules (The Cautionary Code)</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Slide 24</span>
        </div>
        <p class="content-text">
          Examinations rigorously test students on four critical classification rules. Memorizing these rules is mandatory to prevent massive mark deductions:
        </p>
        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th>Economic Transaction</th>
                <th>Accounting Treatment</th>
                <th>Underlying Economic Justification</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Transfer Payments</strong><br>(Pensions, scholarships, unemployment dole)</td>
                <td><strong style="color:var(--bond-crimson);">STRICTLY EXCLUDED</strong></td>
                <td>Transfer payments are unilateral financial grants. No productive economic activity, good, or service is created in return. Counting them would count income without production!</td>
              </tr>
              <tr>
                <td><strong>Purchase & Sale of Second-Hand Goods</strong><br>(Used cars, old apartments, vintage bikes)</td>
                <td><strong style="color:var(--bond-crimson);">STRICTLY EXCLUDED</strong></td>
                <td>Second-hand assets were already counted in GDP during the specific year they were originally produced. Including their resale would cause flagrant double counting across time.</td>
              </tr>
              <tr>
                <td><strong>Services on Second-Hand Goods</strong><br>(Dealer commissions, refurbishment, repairs)</td>
                <td><strong style="color:var(--success-emerald);">INCLUDED IN GDP</strong></td>
                <td>While the underlying used good is excluded, the mechanic's repair, dealer's brokerage, or painter's refurbishment represents <strong>new productive service rendered in the current period</strong>!</td>
              </tr>
              <tr>
                <td><strong>Unsold Inventories</strong><br>(Goods produced this year but unsold)</td>
                <td><strong style="color:var(--success-emerald);">INCLUDED UNDER INVESTMENT (I)</strong></td>
                <td>Production took place this year! To ensure that current production equals expenditure, unsold output is treated as if the producing firm "bought the goods from itself" as inventory investment.</td>
              </tr>
              <tr>
                <td><strong>Prior-Year Inventories Sold This Year</strong></td>
                <td><strong style="color:var(--bond-crimson);">DEDUCTED FROM INVENTORIES</strong></td>
                <td>If a consumer buys a car produced last year, $C$ rises, but inventory investment drops by the identical amount ($\Delta \text{Inv} = -100$), ensuring net impact on current GDP is zero!</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="topic-card">
        <div class="topic-header">
          <a id="ch2-gdp-critique"></a>
          <h3 class="topic-title">2.6 Strategic Critique: GDP Is Not a Measure of Human Well-Being</h3>
          <span class="topic-ref-tag">REF: Harvard Business Review Article (Amit Kapoor & Bibek Debroy, 2019)</span>
        </div>
        <p class="content-lead">
          While GDP is the supreme metric for measuring macroeconomic transaction volume, treating it as an all-encompassing barometer of a nation's welfare is dangerous and anachronistic.
        </p>

        <h4 class="section-subtitle">Historical Genesis: Simon Kuznets (1932) vs John Maynard Keynes (1940)</h4>
        <p class="content-text">
          In 1932, Simon Kuznets formulated the first national income accounts for the US Senate to gauge the devastation of the Great Depression. Kuznets adamantly argued that government spending should NOT be counted as national income unless it served consumer welfare.
        </p>
        <p class="content-text">
          However, in 1940, John Maynard Keynes published an influential essay in the UK Treasury arguing that data paucity crippled Britain's mobilization against Nazi Germany. Keynes realized that if government military procurement was excluded, GDP would show a collapse even while industrial capacity was operating at maximum war mobilization. Keynes therefore established the modern national income formulation ($C + I + G$), enshrining government spending into GDP.
        </p>

        <div class="intel-box exam-tip">
          <div class="intel-box-title">The Robert F. Kennedy Critique (1968)</div>
          <p class="content-text" style="font-style: italic; margin-bottom:0;">
            "GDP counts air pollution and cigarette advertising, and ambulances to clear our highways of carnage... It measures everything, in short, except that which makes life worthwhile."
          </p>
        </div>

        <h4 class="section-subtitle">The Five Structural Blind Spots of GDP</h4>
        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th>Blind Spot</th>
                <th>Economic Reality & Real-World Consequences</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>1. Environmental Degradation</strong></td>
                <td>GDP treats environmental destruction as positive income! Manufacturing toxic chemicals adds to GDP, and spending billions to clean up resulting industrial toxic waste adds to GDP again. Air pollution in Delhi and burning lakes in Bengaluru represent massive welfare erosion, but conventional GDP counts them as industrial success.</td>
              </tr>
              <tr>
                <td><strong>2. Income Inequality</strong></td>
                <td>GDP measures aggregate pie size, not how slices are distributed. An economy where 1 oligarch earns ₹999 crore and 99 citizens earn ₹1 lakh each has the identical GDP of an egalitarian society where 100 citizens earn ₹10 crore each, despite vastly divergent societal stability.</td>
              </tr>
              <tr>
                <td><strong>3. Unpaid Domestic Work & Caregiving</strong></td>
                <td>Essential societal labor—cooking, cleaning, child rearing, elder care—performed within the household is excluded from GDP simply because no commercial transaction takes place.</td>
              </tr>
              <tr>
                <td><strong>4. Value of Leisure & Mental Health</strong></td>
                <td>An economy that forces citizens to work 80 hours a week will generate higher GDP than one working 35 hours a week with balanced leisure, despite lower worker well-being.</td>
              </tr>
              <tr>
                <td><strong>5. The Modern Digital & Service Economy</strong></td>
                <td>Modern welfare is driven by quality of experience (Wikipedia, search engines, open-source code, social media) delivered at near-zero monetary price. GDP fails to capture this immense consumer surplus.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h4 class="section-subtitle">Emerging Alternative Welfare Frameworks</h4>
        <p class="content-text">To overcome these distortions, advanced policy institutions utilize complementary measures:</p>
        <ul style="padding-left:20px; color:var(--silver-300); line-height:1.8;">
          <li><strong>Bhutan's Gross National Happiness (GNH):</strong> Prioritizes spiritual, environmental, and cultural well-being alongside economic vitality.</li>
          <li><strong>UNDP Human Development Index (HDI):</strong> Synthesizes per capita income with life expectancy (health) and mean years of schooling (education).</li>
          <li><strong>India's Ease of Living Index:</strong> Formulated by the Ministry of Housing and Urban Affairs (advisory by Amit Kapoor) to evaluate urban citizens across Quality of Life, Economic Ability, and Sustainability.</li>
        </ul>
      </div>
    </div>

    <!-- ==================== MISSIONS ENVIRONMENT ==================== -->
    <div class="missions-section">
      <div class="mission-card">
        <div class="mission-top-bar">
          <span class="mission-level-badge level-1">LEVEL 1 // FOUNDATION</span>
          <span class="topic-ref-tag">Breadland Case Study</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 2.1: The Breadland Value-Chain Audit</h3>
        <p class="mission-question">
          Breadland is a small closed economy where the only good produced and consumed is bread. The economy consists of three key players:
          <br>• <strong>Farmer:</strong> Grows wheat and sells it to the miller for ₹100.
          <br>• <strong>Miller:</strong> Converts wheat into flour and sells it to the baker for ₹150.
          <br>• <strong>Baker:</strong> Bakes bread and sells it to households for ₹200.
          <br>The total wages paid to workers across all stages is ₹100, rent to landowners is ₹80, and interest paid on capital borrowed is ₹20.
          <br><br>
          <strong>Your Operational Directive:</strong> Calculate the GDP of Breadland using all three approaches to national income accounting and demonstrate their strict equivalence.
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h2_1_1')">Hint 1: Concept</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h2_1_2')">Hint 2: Intermediate Deduction</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h2_1_3')">Hint 3: Income Identity</button>
          </div>
          <div class="hint-content-box" id="h2_1_1">
            <strong>Hint 1:</strong> Value added is gross output minus intermediate input at each stage.
          </div>
          <div class="hint-content-box" id="h2_1_2">
            <strong>Hint 2:</strong> Miller buys wheat (intermediate input = ₹100); Baker buys flour (intermediate input = ₹150).
          </div>
          <div class="hint-content-box" id="h2_1_3">
            <strong>Hint 3:</strong> Expenditure is only household purchase of final bread. Income is wages + rent + interest (profits are zero here).
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_2_1', 2)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_2_1">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Determine Breadland GDP across Production, Income, and Expenditure approaches.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • Farmer output = ₹100 (intermediate input = ₹0).<br>
                • Miller output = ₹150 (intermediate input = ₹100).<br>
                • Baker output = ₹200 (intermediate input = ₹150).<br>
                • Final household bread spending = ₹200.<br>
                • Wages = ₹100, Rent = ₹80, Interest = ₹20, Profits = ₹0.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA SELECTION</span>
              <div class="step-content">
                • Production: $\text{GDP} = \sum (\text{Value of Output} - \text{Intermediate Consumption})$<br>
                • Expenditure: $\text{GDP} = C + I + G$<br>
                • Income: $\text{GDP} = \text{Wages} + \text{Rent} + \text{Interest} + \text{Profits}$
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION</span>
              <div class="step-content">
                <div class="step-math">
                  A. Production Approach:<br>
                  Value Added by Farmer = ₹100 − ₹0 = ₹100<br>
                  Value Added by Miller = ₹150 − ₹100 = ₹50<br>
                  Value Added by Baker = ₹200 − ₹150 = ₹50<br>
                  GDP = ₹100 + ₹50 + ₹50 = ₹200.<br><br>
                  B. Expenditure Approach:<br>
                  Households purchase final bread = ₹200.<br>
                  GDP = C = ₹200.<br><br>
                  C. Income Approach:<br>
                  GDP = Wages (₹100) + Rent (₹80) + Interest (₹20) + Profit (₹0) = ₹200.
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                Stage breakdown shows value compounding: ₹100 (primary) + ₹50 (secondary milling) + ₹50 (tertiary baking) = ₹200 final output.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                Intermediate transactions of ₹250 (₹100 wheat + ₹150 flour) cancel out across the production chain, leaving only the newly created economic value of ₹200.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                <strong>Breadland GDP = ₹200</strong> across all three approaches without discrepancy.
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="mission-card">
        <div class="mission-top-bar">
          <span class="mission-level-badge level-2">LEVEL 2 // STRATEGIC APPLICATION</span>
          <span class="topic-ref-tag">Case Study 1 Macrovia</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 2.2: Macrovia Comprehensive Agricultural & Industrial Audit</h3>
        <p class="mission-question">
          The following information is available for the economy of Macrovia for 2018–19 (all figures in crore Mac):
          <br>• Farmers harvested wheat worth 600, of which half was consumed directly by households, while the remaining half was purchased by a flour mill.
          <br>• The mill converted the wheat into flour and sold the flour to households for 350.
          <br>• Vegetable farmers sold produce worth 200 in local markets directly to households.
          <br>• Dairy cooperatives supplied milk worth 250, consumed by households.
          <br>• Construction companies built highways worth 700 for the government.
          <br>• Manufacturers produced and sold new machinery and equipment worth 100 to firms.
          <br>• Factor incomes: Workers received 700 as wages; business owners earned 300 as profits; landowners received 400 as rent; lenders received 200 as interest; miscellaneous income of self-employed was 300.
          <br><br>
          <strong>Your Operational Directive:</strong> Compute Macrovia's GDP using all three approaches and verify reconciliation.
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h2_2_1')">Hint 1: Concept</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h2_2_2')">Hint 2: Wheat Split</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h2_2_3')">Hint 3: Incomes</button>
          </div>
          <div class="hint-content-box" id="h2_2_1">
            <strong>Hint 1:</strong> Wheat is split into two components: half (300) is final household consumption, and half (300) is intermediate input for the mill!
          </div>
          <div class="hint-content-box" id="h2_2_2">
            <strong>Hint 2:</strong> Flour mill output = 350, intermediate input = 300 $\implies$ Mill Value Added = 50.
          </div>
          <div class="hint-content-box" id="h2_2_3">
            <strong>Hint 3:</strong> Sum all factor incomes: 700 + 300 + 400 + 200 + 300.
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_2_2', 2)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_2_2">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Reconcile Macrovia GDP using Production, Expenditure, and Income approaches.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • Wheat total = 600 (300 direct household consumption, 300 intermediate input to mill).<br>
                • Flour mill output = 350.<br>
                • Vegetables = 200 (final consumption); Milk = 250 (final consumption).<br>
                • Government highway construction = 700 ($G$).<br>
                • New machinery = 100 ($I$).<br>
                • Factor incomes: Wages = 700, Profits = 300, Rent = 400, Interest = 200, Mixed Income = 300.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA SELECTION</span>
              <div class="step-content">
                • Production: $\text{GVA} = \text{Output} - \text{Intermediate Input}$<br>
                • Expenditure: $\text{GDP} = C + I + G$<br>
                • Income: $\text{GDP} = \text{Wages} + \text{Profits} + \text{Rent} + \text{Interest} + \text{Mixed Income}$
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION</span>
              <div class="step-content">
                <div class="step-math">
                  A. Production / Value-Added Approach:<br>
                  • Value added by Wheat Farmers = 600 − 0 = 600<br>
                  • Value added by Flour Mill = 350 − 300 = 50<br>
                  • Value added by Vegetable Farmers = 200 − 0 = 200<br>
                  • Value added by Dairy Cooperatives = 250 − 0 = 250<br>
                  • Value added by Construction Companies (Highways) = 700 − 0 = 700<br>
                  • Value added by Machinery Manufacturers = 100 − 0 = 100<br>
                  GDP = 600 + 50 + 200 + 250 + 700 + 100 = 1,900 crore Mac.<br><br>
                  B. Expenditure Approach:<br>
                  • Household Consumption (C) = 300 (direct wheat) + 350 (flour) + 200 (vegetables) + 250 (milk) = 1,100<br>
                  • Investment (I) = New machinery = 100<br>
                  • Government Spending (G) = Highways = 700<br>
                  GDP = C + I + G = 1,100 + 100 + 700 = 1,900 crore Mac.<br><br>
                  C. Income Approach:<br>
                  GDP = Wages (700) + Profits (300) + Rent (400) + Interest (200) + Mixed Income (300)<br>
                  GDP = 1,900 crore Mac.
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                The flow diagram confirms that total final demand (C: 1100 + I: 100 + G: 700 = 1900) exactly mirrors total factor disbursements (W: 700 + P: 300 + R: 400 + In: 200 + MI: 300 = 1900).
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                The ₹300 crore of wheat delivered to the mill represents an intermediate transaction embedded inside the ₹350 crore flour output. Adding the full ₹600 of wheat plus the ₹350 of flour to consumption would overstate output.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                <strong>Macrovia GDP = ₹1,900 crore Mac</strong> across all three methodologies.
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="mission-card">
        <div class="mission-top-bar">
          <span class="mission-level-badge level-2">LEVEL 2 // STRATEGIC APPLICATION</span>
          <span class="topic-ref-tag">Case Study 2 Econia</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 2.3: Econia Inventory & Second-Hand Good Audit</h3>
        <p class="mission-question">
          Compute National Income for the economy of Econia using the 3 approaches (all figures in million Econs):
          <br>• Sugarcane cooperatives reported output worth 800. Of this, 500 was supplied to sugar mills, while 300 was sold directly for household consumption.
          <br>• Sugar mills processed the sugarcane into sugar worth 900. Of this, 800 was purchased by households, while 100 remained unsold in warehouses.
          <br>• Mango farmers sold produce worth 350; dairy cooperatives supplied milk worth 200 (both consumed by households).
          <br>• Private firms purchased new tractors and transport vehicles worth 400.
          <br>• Government reported spending 250 on a highway expansion project.
          <br>• Household survey data revealed that 200 was spent on second-hand motorcycles.
          <br>• Factor incomes: Wages: 700; Profits: 300; Rent: 120; Interest: 80; Salaries of employed professionals: 1,200.
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h2_3_1')">Hint 1: Concept</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h2_3_2')">Hint 2: Unsold Sugar</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h2_3_3')">Hint 3: Used Motorcycles</button>
          </div>
          <div class="hint-content-box" id="h2_3_1">
            <strong>Hint 1:</strong> Second-hand motorcycles (200 million) must be strictly excluded from GDP!
          </div>
          <div class="hint-content-box" id="h2_3_2">
            <strong>Hint 2:</strong> The 100 million of unsold sugar in warehouses is an addition to inventories, classified under Investment ($I$)!
          </div>
          <div class="hint-content-box" id="h2_3_3">
            <strong>Hint 3:</strong> Total labor income = Wages (700) + Salaries (1,200) = 1,900 million Econs.
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_2_3', 2)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_2_3">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Audit Econia accounts, handle unsold warehouse inventory, filter second-hand asset distortions, and reconcile all 3 approaches.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • Sugarcane = 800 (300 direct consumption, 500 intermediate to mills).<br>
                • Sugar Mill Output = 900 (800 consumed, 100 unsold inventory).<br>
                • Mangoes = 350; Milk = 200.<br>
                • Capital Equipment = 400 (Tractors & transport vehicles).<br>
                • Government Highway = 250.<br>
                • Second-hand motorcycles = 200 (EXCLUDED).<br>
                • Incomes: Wages (700) + Salaries (1,200) + Profits (300) + Rent (120) + Interest (80).
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA SELECTION</span>
              <div class="step-content">
                • Value Added: GVA = Gross Output − Intermediate Inputs.<br>
                • Expenditure: $GDP = C + I + G$, where $I = \text{Fixed Investment} + \Delta \text{Inventories}$.<br>
                • Income: $GDP = \sum \text{Factor Incomes}$.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION</span>
              <div class="step-content">
                <div class="step-math">
                  A. Production Approach:<br>
                  • Sugarcane Cooperatives GVA = 800 − 0 = 800<br>
                  • Sugar Mills GVA = 900 − 500 = 400<br>
                  • Mango Farmers GVA = 350 − 0 = 350<br>
                  • Dairy Cooperatives GVA = 200 − 0 = 200<br>
                  • Tractor & Vehicle Manufacturers GVA = 400 − 0 = 400<br>
                  • Highway Construction GVA = 250 − 0 = 250<br>
                  GDP = 800 + 400 + 350 + 200 + 400 + 250 = 2,400 million Econs.<br><br>
                  B. Expenditure Approach:<br>
                  • Household Consumption (C) = 300 (sugarcane) + 800 (sugar) + 350 (mangoes) + 200 (milk) = 1,650<br>
                  [Note: Second-hand motorcycles (200) are excluded!]<br>
                  • Investment (I) = 400 (tractors/vehicles) + 100 (unsold sugar inventory) = 500<br>
                  • Government Purchases (G) = 250 (highway)<br>
                  GDP = C + I + G = 1,650 + 500 + 250 = 2,400 million Econs.<br><br>
                  C. Income Approach:<br>
                  GDP = Wages (700) + Salaries (1,200) + Profits (300) + Rent (120) + Interest (80)<br>
                  GDP = 2,400 million Econs.
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                Inventory investment of 100 million bridges the gap between production (900 sugar produced) and final sales (800 sugar consumed).
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                Excluding the 200 million spent on second-hand motorcycles prevents counting past output in current GDP. Categorizing unsold sugar as inventory investment ensures that current industrial output is properly valued.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                <strong>Econia National Income = 2,400 million Econs</strong> across all three methodologies.
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="mission-card">
        <div class="mission-top-bar">
          <span class="mission-level-badge level-3">LEVEL 3 // ADVANCED EXAMINATION OPERATION</span>
          <span class="topic-ref-tag">SEPTEMBER 2026 MIDSEM EXAM QUESTION 1</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 2.4: Official Midsem National Income Audit (Gold Standard)</h3>
        <p class="mission-question">
          The National Statistics Office presented the following official information for the year 2024:
          <br>• Farmers produced 400 units of wheat, with each unit valued at ₹5. Of these, 300 units were sold to flour mills, 60 units were sold to households, and the remaining output remained unsold.
          <br>• Flour mills purchased wheat from farmers and produced 300 units of flour at ₹10 per unit, all of which was sold to households.
          <br>• Households also purchased other domestically produced final goods and services worth ₹500.
          <br>• Firms purchased new machinery worth ₹400 during the year.
          <br>• The government spent ₹300 on the construction of public infrastructure and paid ₹100 as pensions to retired citizens.
          <br>• Income records show wages of ₹2,500, rent of ₹400, interest of ₹500, profits of ₹700, and mixed income of ₹600.
          <br><br>
          <strong>Your Operational Directive:</strong> Compute GDP using the three approaches to national income accounting (8 marks).
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h2_4_1')">Hint 1: Unsold Wheat</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h2_4_2')">Hint 2: Intermediate Wheat</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h2_4_3')">Hint 3: Pension Rule</button>
          </div>
          <div class="hint-content-box" id="h2_4_1">
            <strong>Hint 1:</strong> Total wheat produced = 400 units × ₹5 = ₹2,000. Sold to mills: 300 × ₹5 = ₹1,500. Sold to households: 60 × ₹5 = ₹300. Unsold inventory: 40 × ₹5 = ₹200!
          </div>
          <div class="hint-content-box" id="h2_4_2">
            <strong>Hint 2:</strong> Flour mills gross output = 300 × ₹10 = ₹3,000. Intermediate input = ₹1,500. Mill GVA = ₹3,000 − ₹1,500 = ₹1,500.
          </div>
          <div class="hint-content-box" id="h2_4_3">
            <strong>Hint 3:</strong> Pensions (₹100) are transfer payments. Exclude from Government purchases and factor incomes!
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_2_4', 2)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_2_4">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Official Mid-Term Examination Question 1: Derive GDP across Value Added, Expenditure, and Income approaches from primary NSO data.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • Wheat: 400 units @ ₹5 = ₹2,000 gross output.<br>
                &nbsp;&nbsp;- 300 units sold to flour mills = ₹1,500 (intermediate consumption for mills).<br>
                &nbsp;&nbsp;- 60 units sold to households = ₹300 (household consumption).<br>
                &nbsp;&nbsp;- 40 units unsold = ₹200 (inventory investment).<br>
                • Flour Mills: 300 units @ ₹10 = ₹3,000 (all sold to households).<br>
                • Other final goods & services = ₹500 (household consumption).<br>
                • New machinery purchased by firms = ₹400 (business fixed investment).<br>
                • Public infrastructure construction = ₹300 (government expenditure G).<br>
                • Pensions to retired citizens = ₹100 (transfer payment — EXCLUDED).<br>
                • Factor incomes: Wages = ₹2,500, Rent = ₹400, Interest = ₹500, Profits = ₹700, Mixed Income = ₹600.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA SELECTION</span>
              <div class="step-content">
                • Value Added: $\text{GVA} = \text{Value of Output} - \text{Intermediate Consumption}$<br>
                • Expenditure: $\text{GDP} = C + I + G$<br>
                • Income: $\text{GDP} = \text{Wages} + \text{Rent} + \text{Interest} + \text{Profits} + \text{Mixed Income}$
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION (OFFICIAL ANSWER KEY METHODOLOGY)</span>
              <div class="step-content">
                <div class="step-math">
                  A. Value Added Approach:<br>
                  • Farmers: value of wheat output = 400 × ₹5 = ₹2,000.<br>
                  • Flour mills: value added = ₹3,000 − ₹1,500 = ₹1,500.<br>
                  • Other domestically produced final goods and services = ₹500.<br>
                  • New machinery = ₹400.<br>
                  • Public infrastructure = ₹300.<br>
                  GDP = ₹2,000 + ₹1,500 + ₹500 + ₹400 + ₹300 = ₹4,700.<br><br>
                  B. Expenditure Approach:<br>
                  • Consumption (C) = ₹3,000 (flour) + ₹300 (wheat) + ₹500 (other final goods) = ₹3,800.<br>
                  • Investment (I) = ₹400 (new machinery) + ₹200 (unsold wheat inventory) = ₹600.<br>
                  • Government expenditure (G) = ₹300 (public infrastructure).<br>
                  [Note: Pension of ₹100 is a transfer payment and excluded].<br>
                  GDP = C + I + G = ₹3,800 + ₹600 + ₹300 = ₹4,700.<br><br>
                  C. Income Approach:<br>
                  GDP = wages + rent + interest + profits + mixed income<br>
                  GDP = ₹2,500 + ₹400 + ₹500 + ₹700 + ₹600 = ₹4,700.
                </div>
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                The accounting flows reconcile with mathematical perfection: Total value created across producers (₹4,700) equals total final purchases by domestic sectors (₹4,700), which directly disburses as factor incomes to resource suppliers (₹4,700).
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                The official answer key highlights two critical analytical traps:
                1. Unsold wheat (40 units × ₹5 = ₹200) MUST be recorded under Investment ($I$) as inventory addition. If omitted, expenditure totals only ₹4,500, creating an erroneous mismatch!
                2. Pensions (₹100) must be discarded from government spending ($G$) because they do not purchase public goods.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                <strong>OFFICIAL SCORE VERIFICATION:</strong><br>
                • Production Approach GDP = ₹4,700<br>
                • Expenditure Approach GDP = ₹4,700<br>
                • Income Approach GDP = ₹4,700<br>
                <em>Full 8/8 marks confirmed.</em>
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
          <h3 class="topic-title">Chapter 2 Solutions Archive & Reconciliations</h3>
          <span class="topic-ref-tag">TARGET PROTOCOL: 7-STEP VERIFICATION</span>
        </div>
        <p class="content-text">
          Review the detailed breakdowns above. Ensure that in every national income question, you explicitly write out the accounting items before substituting numbers into the master identity.
        </p>
      </div>
    </div>
  </div>
</div>
"""
