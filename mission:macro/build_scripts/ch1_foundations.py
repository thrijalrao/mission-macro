# build_scripts/ch1_foundations.py
"""
Project 007: Chapter 1 — Macroeconomic Foundations
Exhaustive academic content strictly from Prof. Sana Tabassum lecture slides.
"""

def get_chapter_1():
    return """
<!-- CHAPTER 1: MACROECONOMIC FOUNDATIONS -->
<div class="chapter-container" id="chapter-1">
  <a id="ch1" class="chapter-anchor"></a>
  <div class="chapter-header">
    <div class="ch-badge-group">
      <span class="ch-code-pill">DOSSIER 01 // INTEL-FOUNDATIONS</span>
      <h2 class="ch-title">Chapter 1 — Macroeconomic Foundations</h2>
    </div>
    <div class="chapter-actions">
      <button class="ch-mastery-btn" id="ch-mastery-badge-1" onclick="toggleProgressItem(1, 'training', {checked: true})">IN PROGRESS</button>
    </div>
  </div>

  <div class="chapter-nav-tabs">
    <button class="ch-tab-btn active" data-tab="all" onclick="switchChapterTab(1, 'all')">ALL INTEL</button>
    <button class="ch-tab-btn" data-tab="training" onclick="switchChapterTab(1, 'training')">TRAINING (THE BRIEFING)</button>
    <button class="ch-tab-btn" data-tab="missions" onclick="switchChapterTab(1, 'missions')">MISSIONS (ACTIVE OPS)</button>
    <button class="ch-tab-btn" data-tab="targets" onclick="switchChapterTab(1, 'targets')">TARGETS (DEBRIEFING)</button>
  </div>

  <div class="chapter-body">
    <!-- ==================== TRAINING ENVIRONMENT ==================== -->
    <div class="training-section">
      <div class="topic-card">
        <div class="topic-header">
          <h3 class="topic-title">1.1 What is Macroeconomics? Core Definitions & Paradigms</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Unit 1, Slides 2-5</span>
        </div>
        <p class="content-lead">
          In intelligence field operations, viewing a target through a high-magnification sniper scope gives you extreme detail on a single operative—this is <strong>microeconomics</strong>. Viewing the entire satellite reconnaissance theater of an empire reveals the movements of entire armies, trade corridors, and financial flows—this is <strong>macroeconomics</strong>.
        </p>
        <p class="content-text">
          Our primary academic authority provides three canonical definitions that must be memorized with exact precision for the examination:
        </p>
        <div class="intel-box key-intuition">
          <div class="intel-box-title">Authoritative Academic Definitions</div>
          <p class="content-text" style="margin-bottom:8px;">
            <strong>Gardener Ackley:</strong> <em>"Macroeconomics is the study of forces or factors that determine the levels of aggregate production, employment, and prices in the economy."</em>
          </p>
          <p class="content-text" style="margin-bottom:8px;">
            <strong>Kenneth Boulding:</strong> <em>"Macroeconomics deals with not individual quantities but aggregate of these quantities, not with individual incomes but with national income, not with individual prices but total price levels in the economy, not with individual output but with national output."</em>
          </p>
          <p class="content-text" style="margin-bottom:0;">
            <strong>Paul A. Samuelson:</strong> <em>"Macroeconomics is the study of behaviour of the economy as a whole. It examines the overall level of output, employment and prices in the economy."</em>
          </p>
        </div>

        <h4 class="section-subtitle">Core Inquiries of Macroeconomic Intelligence</h4>
        <p class="content-text">Macroeconomic analysis seeks rigorous answers to the following fundamental questions:</p>
        <ul style="padding-left: 20px; color: var(--silver-300); margin-bottom: 16px; line-height: 1.8;">
          <li>What determines the total level of economic activity, national output (GDP), general price level, and employment/unemployment?</li>
          <li>How is the equilibrium level of national income determined?</li>
          <li>What triggers economic fluctuations, business cycles, and crises in national income?</li>
          <li>How do fiscal and monetary policies impact markets and private decision-makers?</li>
          <li>What policies must be executed during recessions versus inflationary booms?</li>
          <li>What factors govern aggregate consumption, saving, and capital investment?</li>
          <li>How do simultaneous shifts in Aggregate Demand (AD) and Aggregate Supply (AS) determine real output and inflation?</li>
        </ul>

        <h4 class="section-subtitle">Strategic Imperative: Why Future Managers Care About Macroeconomics</h4>
        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th>Strategic Dimension</th>
                <th>Managerial & Operational Impact</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Macroeconomic Indicators</strong></td>
                <td>Tracking GDP growth, headline/core inflation, interest rates, and unemployment to assess systemic economic health and market direction.</td>
              </tr>
              <tr>
                <td><strong>Business Cycle Navigation</strong></td>
                <td>Anticipating booms and recessions to dynamically scale production, manage inventory pipelines, and allocate working capital.</td>
              </tr>
              <tr>
                <td><strong>Policy Adaptation</strong></td>
                <td>Anticipating central bank rate hikes (repo rate) and fiscal budget shifts (taxes, subsidies) to adjust borrowing and pricing strategies.</td>
              </tr>
              <tr>
                <td><strong>Enterprise Risk Management</strong></td>
                <td>Insulating firm balance sheets from macroeconomic shocks, exchange rate volatility, supply chain disruptions, and liquidity squeezes.</td>
              </tr>
              <tr>
                <td><strong>Capital Investment Decisions</strong></td>
                <td>Evaluating corporate capex based on real borrowing costs ($r$), expected hurdle rates, consumer confidence, and the marginal propensity to consume.</td>
              </tr>
              <tr>
                <td><strong>Strategic Planning</strong></td>
                <td>Formulating long-term capacity expansion by analyzing structural demographic shifts, productivity growth, and technological diffusion.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="topic-card">
        <div class="topic-header">
          <h3 class="topic-title">1.2 Microeconomics vs Macroeconomics: Master Comparison</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Slide 5</span>
        </div>
        <p class="content-text">
          Examinations regularly demand a rigorous comparative differentiation between microeconomic and macroeconomic paradigms. Memorize the eight dimensions verbatim:
        </p>
        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th>Analytical Aspect</th>
                <th>Microeconomics</th>
                <th>Macroeconomics</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Primary Focus</strong></td>
                <td>Individual economic units (single households, individual business firms, specific industries).</td>
                <td>The entire economy in aggregate as an integrated macroeconomic system.</td>
              </tr>
              <tr>
                <td><strong>Scope of Inquiry</strong></td>
                <td>Specific markets, relative prices of goods, single resource allocation.</td>
                <td>Aggregate indicators, national output, general price level, total employment trends.</td>
              </tr>
              <tr>
                <td><strong>Core Objective</strong></td>
                <td>Resource allocation efficiency and single commodity price determination.</td>
                <td>Sustainable economic growth, price stability, full employment, general equilibrium.</td>
              </tr>
              <tr>
                <td><strong>Key Variables</strong></td>
                <td>Individual demand, market supply, single product price, firm profit, wage rate in a trade.</td>
                <td>Gross Domestic Product (GDP), inflation rate, aggregate unemployment, market interest rates ($r, i$).</td>
              </tr>
              <tr>
                <td><strong>Time Frame</strong></td>
                <td>Short-term marginal adjustments and decisions in specific localized markets.</td>
                <td>Long-term economic growth trends and cyclical fluctuations across business cycles.</td>
              </tr>
              <tr>
                <td><strong>Policy Tools</strong></td>
                <td>Price ceilings, price floors, specific excise taxes, minimum wages in an industry.</td>
                <td>Monetary policy (repo rate, CRR, OMO) and Fiscal policy (government expenditure $G$, taxation $T$).</td>
              </tr>
              <tr>
                <td><strong>Illustrative Question</strong></td>
                <td><em>"Why did the price of Arabica coffee beans increase by 15%?"</em></td>
                <td><em>"What factors caused general consumer price inflation across the economy?"</em></td>
              </tr>
              <tr>
                <td><strong>Methodological Approach</strong></td>
                <td><strong>Bottom-up:</strong> Building from individual consumer utility and firm optimization to market demand.</td>
                <td><strong>Top-down:</strong> Analyzing aggregate demand and supply for the entire economic structure.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="topic-card">
        <div class="topic-header">
          <a id="ch1-stocks-flows"></a>
          <h3 class="topic-title">1.3 Aggregate Economic Variables: Goods Market vs Money Market</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Slides 6-8</span>
        </div>
        <p class="content-text">
          Macroeconomic modeling decomposes the entire economy into two interconnected structural arenas: the <strong>Goods Market</strong> and the <strong>Money Market</strong>. General macroeconomic equilibrium requires simultaneous balance across both.
        </p>

        <h4 class="section-subtitle">A. The Goods Market (Real Sector)</h4>
        <p class="content-text">
          The Goods Market represents the collective aggregate market for all final goods and services produced in the domestic economy. Equilibrium in the goods market determines the total level of production, defined as <strong>Gross Domestic Product (GDP)</strong> or national income ($Y$).
        </p>
        <p class="content-text">The three fundamental behavioral components of goods market demand in a closed economy are:</p>
        <ul style="padding-left: 20px; color: var(--silver-300); margin-bottom: 16px;">
          <li><strong>Consumption Expenditure ($C$):</strong> Total spending by households on final goods and services used to satisfy current consumer needs.</li>
          <li><strong>Planned Investment Expenditure ($I$):</strong> Spending by private business enterprises on capital goods—including machinery, factory equipment, commercial structures, and new residential construction—to expand productive capacity.</li>
          <li><strong>Government Expenditure ($G$):</strong> Spending by national and local governments on newly produced goods, services, and public infrastructure (highways, ports, healthcare facilities, national defense, education). <em>Crucial Note: Transfer payments such as pensions are excluded!</em></li>
        </ul>

        <h4 class="section-subtitle">B. The Money Market (Financial / Monetary Sector)</h4>
        <p class="content-text">
          The Money Market denotes the monetary and financial architecture of the economy where the aggregate demand for money interacts with the supply of money. Equilibrium in the money market determines the market interest rate ($i$ or $r$), which forms the vital transmission conduit linking the money market back to private investment in the goods market.
        </p>
        <ul style="padding-left: 20px; color: var(--silver-300); margin-bottom: 16px;">
          <li><strong>Money Demand ($M_d$ / Liquidity Preference):</strong> The total volume of liquid money balances (currency notes and demand deposits) that households and firms desire to hold rather than illiquid, interest-bearing securities.</li>
          <li><strong>Money Supply ($M_s$):</strong> The total stock of money created and controlled exogenously by the nation's Central Bank (such as the Reserve Bank of India or Federal Reserve).</li>
        </ul>

        <h4 class="section-subtitle">Stock vs Flow Variables in Macroeconomics</h4>
        <div class="intel-box key-intuition">
          <div class="intel-box-title">Examination Rule: Stocks vs Flows</div>
          <p class="content-text">
            <strong>Flow Variable:</strong> Measured per unit of time (e.g., GDP = ₹2,000 cr <em>per year</em>; monthly household income; annual investment $\Delta K$; quarterly government fiscal deficit). A flow continuously feeds into or drains a stock.
          </p>
          <p class="content-text" style="margin-bottom:0;">
            <strong>Stock Variable:</strong> Measured at a specific instant in time (e.g., Total National Capital Stock $K$ on Dec 31; total accumulated public debt; total money supply $M_3$ on Friday; foreign exchange reserves).
          </p>
        </div>
      </div>

      <div class="topic-card">
        <div class="topic-header">
          <a id="ch1-circular-flow"></a>
          <h3 class="topic-title">1.4 The Circular Flow of Income & Output</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Slides 9-15</span>
        </div>
        <p class="content-text">
          The Circular Model of the economy illustrates the continuous reciprocal movement of productive resources, goods, services, and financial funds across different institutional sectors of the economy. It demonstrates the unbreakable economic identity that <strong>every rupee of expenditure becomes a rupee of income for another entity</strong>.
        </p>

        <h4 class="section-subtitle">1. The Two-Sector Economy (Households & Business Firms)</h4>
        <p class="content-text">
          In the foundational two-sector economy, two primary domestic economic agents interact across two counterpart markets:
        </p>
        <ul style="padding-left: 20px; color: var(--silver-300); margin-bottom: 16px;">
          <li><strong>Factor Market (Real Flow vs Factor Payments):</strong> Households own the primary factors of production (Land, Labour, Capital, Enterprise) and supply them to business firms. In exchange, business firms pay households <strong>factor incomes</strong> in the form of <strong>Rent</strong> (for land), <strong>Wages & Salaries</strong> (for labour), <strong>Interest</strong> (for capital), and <strong>Profit</strong> (for enterprise).</li>
          <li><strong>Goods Market (Output Flow vs Consumption Expenditure):</strong> Business firms organize factors to produce final consumer goods and services. Households spend their earned factor income to purchase these goods and services, completing the loop.</li>
        </ul>

        <h4 class="section-subtitle">Inclusion of Financial Institutions (Capital / Loanable Funds Market)</h4>
        <p class="content-text">
          In reality, households do not spend 100% of their disposable income on current consumption. They channel a fraction of unspent income into financial intermediaries (commercial banks, cooperative banks, bond markets) as <strong>Savings ($S$)</strong>. Financial institutions mobilize these savings and extend credit to business firms to finance capital asset accumulation, termed <strong>Investment ($I$)</strong>.
        </p>

        <h4 class="section-subtitle">2. The Three-Sector Economy (Adding the Government Sector)</h4>
        <p class="content-text">
          The government sector alters the circular flow through two fiscal channels:
        </p>
        <ul style="padding-left: 20px; color: var(--silver-300); margin-bottom: 16px;">
          <li><strong>Government & Households:</strong> The government levies direct taxes on household income ($T$). In return, it provides public infrastructure and makes <strong>Transfer Payments ($TR$)</strong> (old-age pensions, unemployment benefits, scholarships) directly to households without demanding any current productive service in return.</li>
          <li><strong>Government & Business Firms:</strong> The government collects corporate taxes ($T$) from firms and purchases goods/infrastructure ($G$). Additionally, it provides financial <strong>Subsidies</strong> (interest subsidies, electricity subsidies, green-energy incentives) to lower production costs and stimulate targeted industry activities.</li>
        </ul>

        <h4 class="section-subtitle">3. The Four-Sector Economy (Open Economy with Foreign Sector)</h4>
        <p class="content-text">
          Incorporate the Rest of the World (External Sector): Domestic firms sell output abroad as <strong>Exports ($X$)</strong>, bringing foreign revenue into the domestic circular flow (Injection). Domestic households, firms, and the government purchase foreign-made goods as <strong>Imports ($M$)</strong>, leaking purchasing power out of the domestic circular flow (Leakage).
        </p>
      </div>

      <div class="topic-card">
        <div class="topic-header">
          <a id="ch1-injections-leakages"></a>
          <h3 class="topic-title">1.5 Injections, Leakages, and Macroeconomic Equilibrium</h3>
          <span class="topic-ref-tag">REF: Prof. Sana Tabassum Slide 15</span>
        </div>
        <p class="content-text">
          A fundamental requirement for examination mastery is the precise identification and balancing of <strong>Leakages (Withdrawals)</strong> and <strong>Injections</strong>.
        </p>

        <div class="formula-card">
          <div class="formula-card-title">Mathematical Definitions of Leakages & Injections</div>
          <div class="formula-math-display">
            Leakages (L) = Savings (S) + Taxes (T) + Imports (M)<br>
            Injections (J) = Investment (I) + Government Purchases (G) + Exports (X)
          </div>
          <div class="formula-breakdown">
            <ul>
              <li><strong>Leakage ($L$):</strong> Any withdrawal of income from the active circular flow of spending and production. It represents money earned that is not immediately recycled into domestic consumption expenditure.</li>
              <li><strong>Injection ($J$):</strong> Any addition of spending into the active circular flow that arises from sources <em>other than</em> household consumption expenditure.</li>
            </ul>
          </div>
        </div>

        <h4 class="section-subtitle">The Equilibrium and Disequilibrium Theorem</h4>
        <div class="data-table-wrap">
          <table class="intel-table">
            <thead>
              <tr>
                <th>Economic Condition</th>
                <th>Relationship</th>
                <th>Dynamic Consequence on National Income ($Y$)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Macroeconomic Equilibrium</strong></td>
                <td><strong>$\text{Leakages} = \text{Injections}$</strong><br>$(S + T + M = I + G + X)$</td>
                <td>National income remains perfectly stable. Total aggregate spending exactly clears total aggregate production. No unplanned inventory changes occur.</td>
              </tr>
              <tr>
                <td><strong>Contractionary Disequilibrium</strong></td>
                <td><strong>$\text{Leakages} > \text{Injections}$</strong><br>$(L > J)$</td>
                <td>More income is being withdrawn than injected. Aggregate planned spending falls below current production. Business inventories accumulate unexpectedly $\implies$ firms cut production and employment $\implies$ <strong>National Income ($Y$) DECREASES</strong>.</td>
              </tr>
              <tr>
                <td><strong>Expansionary Disequilibrium</strong></td>
                <td><strong>$\text{Injections} > \text{Leakages}$</strong><br>$(J > L)$</td>
                <td>New spending entering the system exceeds total withdrawals. Aggregate spending exceeds current production. Unplanned inventory depletion occurs $\implies$ firms hire additional workers and expand production $\implies$ <strong>National Income ($Y$) RISES</strong>.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="intel-box trap">
          <div class="intel-box-title">Examination Trap: Treatment of Transfer Payments</div>
          <p class="content-text" style="margin-bottom:0;">
            A frequent examination trap asks whether a ₹50 crore pension payment or unemployment benefit by the government constitutes an injection. <strong>IT DOES NOT!</strong> Transfer payments are unilateral redistributions of income for which no good or service is provided in return. They enter household disposable income, but do not directly enter the active production flow. Only direct government expenditure on goods and services ($G$) is an injection!
          </p>
        </div>
      </div>
    </div>

    <!-- ==================== MISSIONS ENVIRONMENT ==================== -->
    <div class="missions-section">
      <div class="mission-card">
        <div class="mission-top-bar">
          <span class="mission-level-badge level-1">LEVEL 1 // FOUNDATION BRIEFING</span>
          <span class="topic-ref-tag">Unit 1 Problem 1</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 1.1: Industrial Town Circular Flow Mapping</h3>
        <p class="mission-question">
          In a growing industrial town, households provide their labour and capital to manufacturing companies. In return, they receive wages and interest. Households use a substantial part of this income to purchase food, clothing, transport services, electronic products, and other goods and services produced by businesses. However, not all household income is spent during the year. Families place a portion of their unspent income in financial institutions. Businesses use these funds to purchase equipment capital goods from domestic manufacturers to expand their operations.
          <br><br>
          <strong>Your Operational Directives:</strong><br>
          1. Classify all economic flows into <strong>Real Flows</strong> and <strong>Money Flows</strong>.<br>
          2. Identify the specific <strong>Leakage</strong> and <strong>Injection</strong> in this economy.<br>
          3. Explain what mechanism restores balance if household savings exceed business equipment purchases.
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h1_1_1')">Hint 1: Concept</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h1_1_2')">Hint 2: Flow Rules</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h1_1_3')">Hint 3: Disequilibrium</button>
          </div>
          <div class="hint-content-box" id="h1_1_1">
            <strong>Hint 1:</strong> Differentiate physical factors/products from currency payments. Real flows involve goods/services/labor; money flows involve financial payments.
          </div>
          <div class="hint-content-box" id="h1_1_2">
            <strong>Hint 2:</strong> In a two-sector model with a financial sector, Leakage = Savings deposited into banks. Injection = Loans converted into capital goods purchases (Investment).
          </div>
          <div class="hint-content-box" id="h1_1_3">
            <strong>Hint 3:</strong> If $S > I$, Leakages exceed Injections. Output remains unsold, forcing firms to curtail production until income falls and savings contract to match investment.
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_1_1', 1)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_1_1">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Map the two-sector economy with financial intermediation, identify real and money flows, leakages and injections, and evaluate disequilibrium.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • Agents: Households, Manufacturing Companies, Financial Institutions.<br>
                • Factor Services: Labour, Capital.<br>
                • Factor Payments: Wages, Interest.<br>
                • Consumer Goods: Food, clothing, transport, electronics.<br>
                • Financial Allocation: Unspent income to banks (Savings); Bank funds to firms for equipment (Investment).
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA & CLASSIFICATION MATRIX</span>
              <div class="step-content">
                • Real Flows: Flow of physical factors (labor, capital) and physical goods/services.<br>
                • Money Flows: Counterpart flow of currency (wages, interest, consumption spending, investment borrowing).<br>
                • Leakage ($L$) = Savings ($S$).<br>
                • Injection ($J$) = Investment ($I$).
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION</span>
              <div class="step-content">
                <strong>A. Real Flows:</strong><br>
                (1) Flow of labour and capital services from households to manufacturing companies.<br>
                (2) Flow of finished consumer goods and services (food, clothing, electronics) from manufacturers to households.<br>
                (3) Flow of new capital equipment goods between manufacturers.<br>
                <strong>B. Money Flows:</strong><br>
                (1) Payment of factor returns (wages and interest) from manufacturing companies to households.<br>
                (2) Payment of consumption expenditures from households to businesses.<br>
                (3) Flow of household savings into financial institutions.<br>
                (4) Flow of credit financing from financial institutions to firms to purchase equipment.<br>
                <strong>C. Leakage & Injection:</strong><br>
                • Leakage = Household Savings ($S$) deposited in banks.<br>
                • Injection = Business Investment ($I$) in equipment and capital assets.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                The diagram exhibits an inner loop of factor services and goods (real flows) and an outer loop of wages, interest, and consumer expenditures (money flows). The financial market acts as a reservoir: savings bleed out of the spending loop (downward arrow from households to banks), while investment injects funds back into the production stream (upward arrow from banks to firms).
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                If households increase savings beyond the investment appetite of firms ($S > I$), total spending falls short of output. Retailers experience unsold inventory build-up. Firms slash orders, lay off workers, and decrease national income until savings drop back into equality with investment at a lower equilibrium income.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                <strong>Final Examination Takeaway:</strong> In a two-sector economy with a banking sector, equilibrium requires $S = I$. When $S \neq I$, output and income adjust endogenously to restore macroeconomic balance.
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="mission-card">
        <div class="mission-top-bar">
          <span class="mission-level-badge level-2">LEVEL 2 // STRATEGIC APPLICATION</span>
          <span class="topic-ref-tag">Unit 1 Problem 2</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 1.2: Three-Sector Automobile Region Fiscal Flows</h3>
        <p class="mission-question">
          In an automobile-manufacturing region, households provide labour to automobile manufacturers and receive salaries in return. They spend part of this income on goods and services produced by businesses and save the rest with cooperative banks. The government collects taxes from households and firms. It also provides cash assistance to unemployed workers and financial incentives to start-ups developing clean technologies. Banks provide financing to businesses, which use these funds to purchase new machinery to expand their operations.
          <br><br>
          <strong>Your Operational Directives:</strong><br>
          1. Construct the complete fiscal and financial flow architecture.<br>
          2. Classify: (a) Cash assistance to unemployed workers, (b) Financial incentives to clean-tech start-ups, (c) Taxes collected.<br>
          3. Formulate the comprehensive leakage-injection equilibrium condition for this economy.
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h1_2_1')">Hint 1: Concept</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h1_2_2')">Hint 2: Fiscal Classifications</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h1_2_3')">Hint 3: Equilibrium</button>
          </div>
          <div class="hint-content-box" id="h1_2_1">
            <strong>Hint 1:</strong> Identify the three sectors: Households, Firms, and Government, alongside the Financial Intermediary (Cooperative Banks).
          </div>
          <div class="hint-content-box" id="h1_2_2">
            <strong>Hint 2:</strong> Cash assistance without work = Transfer Payment ($TR$). Financial incentives to clean-tech start-ups = Production Subsidies.
          </div>
          <div class="hint-content-box" id="h1_2_3">
            <strong>Hint 3:</strong> Leakages now include all taxes paid to government plus private savings. Injections include investment plus government direct purchases.
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_1_2', 1)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_1_2">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Analyze three-sector circular flow involving taxes, transfer payments, subsidies, cooperative bank savings, and investment.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • Sectors: Households, Auto Firms, Government, Cooperative Banks.<br>
                • Household Inflows: Salaries (Wages), Cash assistance (Transfer Payment).<br>
                • Household Outflows: Consumption ($C$), Cooperative bank deposits ($S$), Taxes ($T_h$).<br>
                • Firm Inflows: Consumption revenue, Bank investment loans ($I$), Government clean-tech incentives (Subsidies).<br>
                • Firm Outflows: Salaries, Taxes ($T_f$), Machinery purchases ($I$).
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA SELECTION</span>
              <div class="step-content">
                • Total Leakages ($L$) = Private Savings ($S$) + Net Taxes ($T$).<br>
                • Total Injections ($J$) = Investment ($I$) + Government Purchases ($G$).<br>
                • Equilibrium Condition: $S + T = I + G$.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION & CLASSIFICATIONS</span>
              <div class="step-content">
                <strong>(a) Cash Assistance to Unemployed Workers:</strong> Classified strictly as a <strong>Transfer Payment ($TR$)</strong>. It is a unilateral government transfer made without any corresponding current output or service rendered. It supplements disposable income ($Y_d = Y - T + TR$) but is NOT an injection of aggregate demand.<br>
                <strong>(b) Financial Incentives to Clean-Tech Start-ups:</strong> Classified as <strong>Subsidies</strong>. They reduce unit production costs, encouraging private firms to expand capital investment.<br>
                <strong>(c) Taxes Collected:</strong> Classified as a <strong>Leakage ($T$)</strong> from the circular flow of income because they reduce the spendable purchasing power of households and firms.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                The three-sector model features two leakage drains ($S$ into banks, $T$ to government) and two injection conduits ($I$ from banks to firms, $G$ from government to firms). Transfer payments flow from government to households, mitigating net tax withdrawals ($T_{\text{net}} = T - TR$).
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                Government fiscal activity directly alters private sector balance. If the government runs a budget deficit ($G > T$), it injects more spending than it drains, which can offset an excess of private saving over private investment ($S > I$), stabilizing aggregate national output.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                <strong>Three-Sector Equilibrium Law:</strong> $S + T = I + G$. Transfer payments are accounted for within net disposable income, not as primary injections into final goods output.
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="mission-card">
        <div class="mission-top-bar">
          <span class="mission-level-badge level-3">LEVEL 3 // ADVANCED NUMERICAL OPERATION</span>
          <span class="topic-ref-tag">Unit 1 Problem 3</span>
        </div>
        <h3 class="topic-title" style="margin-bottom:12px;">Mission 1.3: Quantitative Injections-Leakages Equilibrium & Pension Audit</h3>
        <p class="mission-question">
          In an industrial region, households earn ₹1,500 crore in the form of wages, rent, interest, and profits from businesses. Households spend 80% of their income on consumption and save the remaining amount with financial institutions. During the year, households and firms pay ₹100 crore and ₹150 crore respectively as taxes.
          <br><br>
          Financial institutions provide funds to businesses, which spend ₹320 crore on new machinery and expansion of production facilities. The government spends ₹280 crore on the construction of roads, hospitals, and other public infrastructure. It also provides ₹50 crore as pension payments.
          <br><br>
          <strong>Your Operational Directives:</strong><br>
          a. Calculate household consumption ($C$) and savings ($S$). Identify and calculate total leakages ($L$) and total injections ($J$) in the economy.<br>
          b. Using the leakage–injection equilibrium condition, determine whether the economy is in equilibrium. If not, state whether national income will tend to increase or decrease.<br>
          c. Should the ₹50 crore pension payment be considered an injection? Explain with rigorous economic justification.
        </p>
        <div class="hints-container">
          <div class="hints-header"><span>HINTS PROTOCOL:</span> Progressive Declassification Available</div>
          <div class="hint-buttons-row">
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h1_3_1')">Hint 1: Concept</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h1_3_2')">Hint 2: Formulas</button>
            <button class="hint-trigger-btn" onclick="toggleHint(this, 'h1_3_3')">Hint 3: Injections vs Transfers</button>
          </div>
          <div class="hint-content-box" id="h1_3_1">
            <strong>Hint 1:</strong> Total factor income earned = ₹1,500 cr. Consumption is 80%, so savings is 20%. Remember that total taxes are paid by both households and firms.
          </div>
          <div class="hint-content-box" id="h1_3_2">
            <strong>Hint 2:</strong> Injections = Investment in machinery + Government direct infrastructure purchases. Leakages = Savings + Total Taxes.
          </div>
          <div class="hint-content-box" id="h1_3_3">
            <strong>Hint 3:</strong> Watch out for pensions! They are transfer payments, NOT direct purchases of final goods ($G$).
          </div>
        </div>
        <div class="solution-reveal-wrap">
          <button class="reveal-solution-btn" onclick="toggleSolution(this, 'sol_1_3', 1)">
            <span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)
          </button>
          <div class="solution-debrief-container" id="sol_1_3">
            <div class="solution-step">
              <span class="step-badge">1. MISSION BRIEF</span>
              <div class="step-content">Perform complete quantitative leakage-injection accounting for the regional economy, test for macroeconomic equilibrium, and deliver a definitive verdict on transfer payments.</div>
            </div>
            <div class="solution-step">
              <span class="step-badge">2. INTELLIGENCE EXTRACTION</span>
              <div class="step-content">
                • Total Factor Income ($Y$) = ₹1,500 crore.<br>
                • Household Consumption propensity = 80% (0.80).<br>
                • Household Taxes ($T_h$) = ₹100 crore; Firm Taxes ($T_f$) = ₹150 crore.<br>
                • Private Investment in capital goods ($I$) = ₹320 crore.<br>
                • Government spending on public infrastructure ($G$) = ₹280 crore.<br>
                • Government pension payments ($TR$) = ₹50 crore.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">3. FORMULA SELECTION</span>
              <div class="step-content">
                • Consumption: $C = 0.80 \times Y$<br>
                • Savings: $S = Y - C = 0.20 \times Y$<br>
                • Total Taxes: $T = T_h + T_f$<br>
                • Total Leakages: $L = S + T$<br>
                • Total Injections: $J = I + G$<br>
                • Equilibrium Condition: $L = J$
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">4. EXECUTION</span>
              <div class="step-content">
                <strong>Part (a): Household Consumption, Savings, Leakages, and Injections</strong><br>
                <div class="step-math">
                  Consumption (C) = 0.80 × ₹1,500 = ₹1,200 crore.<br>
                  Savings (S) = ₹1,500 − ₹1,200 = ₹300 crore (or 0.20 × ₹1,500 = ₹300 crore).<br>
                  Total Taxes (T) = ₹100 + ₹150 = ₹250 crore.<br>
                  Total Leakages (L) = S + T = ₹300 + ₹250 = ₹550 crore.<br><br>
                  Private Investment (I) = ₹320 crore.<br>
                  Government Infrastructure Spending (G) = ₹280 crore.<br>
                  Total Injections (J) = I + G = ₹320 + ₹280 = ₹600 crore.
                </div>
                <strong>Part (b): Equilibrium Determination</strong><br>
                Comparing Total Injections and Total Leakages:
                <div class="step-math">
                  Injections (J) = ₹600 crore<br>
                  Leakages (L) = ₹550 crore<br>
                  J − L = ₹600 − ₹550 = +₹50 crore.
                </div>
                Since $J > L$, the economy is in <strong>DISEQUILIBRIUM</strong>. Because injections exceed leakages by ₹50 crore, aggregate demand exceeds current aggregate supply, causing unplanned inventory depletions. Consequently, <strong>national income will tend to INCREASE</strong>.
                <br><br>
                <strong>Part (c): Pension Payment Economic Verdict</strong><br>
                The ₹50 crore pension payment <strong>SHOULD NOT</strong> be considered an injection. By macroeconomic definition, an injection represents direct spending that enters the active production stream to purchase newly produced final goods and services ($G$). A pension payment is a <strong>transfer payment</strong>—a unilateral transfer from the government to retired citizens without any concurrent economic activity or production in return. While pensions increase household disposable income and may subsequently lead to higher consumption spending ($C$), the pension payment itself is not an injection.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">5. GRAPHICAL ANALYSIS</span>
              <div class="step-content">
                On an injections-leakages coordinate plane (with $Y$ on the horizontal axis): The leakage function $L(Y) = S(Y) + T$ slopes upward with slope equal to the marginal propensity to withdraw ($MPS$). The injection schedule $J = I + G$ is a horizontal line at ₹600 crore. At $Y = 1,500$, the $J$ line sits strictly above the $L$ schedule by ₹50 crore, exerting an expansionary multiplier pressure pushing $Y$ to the right until $L$ expands to ₹600 crore.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge">6. ECONOMIC INTERPRETATION</span>
              <div class="step-content">
                The net surplus of injections ($J - L = +50$ cr) acts as a powerful economic catalyst. Firms receive purchase orders exceeding their production run by ₹50 crore. To meet this excess demand, businesses hire idle labor and ramp up production schedules, unleashing the multiplier sequence across successive rounds.
              </div>
            </div>
            <div class="solution-step">
              <span class="step-badge target-confirm">7. TARGET CONFIRMATION</span>
              <div class="step-content">
                <strong>Final Examination Metrics:</strong><br>
                • Consumption = ₹1,200 crore; Savings = ₹300 crore.<br>
                • Total Leakages ($L$) = ₹550 crore; Total Injections ($J$) = ₹600 crore.<br>
                • Equilibrium State: Disequilibrium ($J > L$).<br>
                • National Income Trajectory: Increasing.<br>
                • Pension Treatment: Excluded from injections (unilateral transfer payment).
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
          <h3 class="topic-title">Chapter 1 Examination Debriefing & Solutions Archive</h3>
          <span class="topic-ref-tag">TARGET PROTOCOL: 7-STEP VERIFICATION</span>
        </div>
        <p class="content-text">
          All Chapter 1 mission solutions have been compiled using the official 7-step evaluation rubric from the September 2026 Examination Answer Key. Review the solutions above by engaging the solution reveal controls, and verify that your own handwritten derivations match the exact structure:
        </p>
        <div class="intel-box exam-tip">
          <div class="intel-box-title">7-Step Answer Key Protocol for Full Marks</div>
          <ol style="padding-left: 20px; color: var(--silver-300); line-height: 1.8;">
            <li><strong>Mission Brief:</strong> Restate the core macroeconomic problem and unknown targets.</li>
            <li><strong>Intelligence Extraction:</strong> Tabulate all given numerical parameters with exact units (crores, percentages).</li>
            <li><strong>Formula Selection:</strong> State the exact formula authorized by lecture slides and explain its economic rationale.</li>
            <li><strong>Execution:</strong> Write out algebraic substitutions step-by-step without skipping intermediate steps.</li>
            <li><strong>Graphical Analysis:</strong> Identify curve axes, shift directions, initial and final equilibria ($E_0 \to E_1$).</li>
            <li><strong>Economic Interpretation:</strong> Explain the real-world economic mechanism (e.g., inventory depletions, price adjustments).</li>
            <li><strong>Target Confirmation:</strong> State the final answer clearly in a boxed summary with definitive conclusion.</li>
          </ol>
        </div>
      </div>
    </div>
  </div>
</div>
"""
