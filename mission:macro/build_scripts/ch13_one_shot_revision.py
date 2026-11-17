"""
PROJECT 007: THE MACROECONOMICS INTELLIGENCE FILE
Chapter 13: The One-Shot Revision & Examination Readiness Centre Generator
"""
try:
    import ch13_graph_atlas
except ImportError:
    from . import ch13_graph_atlas

def get_chapter_13():
    atlas_html = ch13_graph_atlas.get_graphical_atlas_html()
    return r'''
<section id="chapter-13" class="mission-chapter">
<a id="ch13" class="chapter-anchor"></a>
    <div class="chapter-header">
        <div class="briefing-tag">TACTICAL INTEL FILE // DOSSIER 13</div>
        <h2 class="chapter-title">CHAPTER 13: THE ONE-SHOT REVISION & EXAMINATION READINESS CENTRE</h2>
        <div class="classified-stamp">TOP SECRET // 007 FINAL CLEARANCE</div>
    </div>

    <div class="tab-container">
        <div class="tab-nav">
            <button class="tab-btn active" onclick="switchSubTab(event, 'ch13-formulas')">MASTER FORMULA SHEET</button>
            <button class="tab-btn" onclick="switchSubTab(event, 'ch13-matrices')">12 CONCEPT MATRICES</button>
            <button class="tab-btn" onclick="switchSubTab(event, 'ch13-gallery')">GRAPHICAL REVISION ATLAS (16 BLUEPRINTS)</button>
            <button class="tab-btn" onclick="switchSubTab(event, 'ch13-toolkit')">7-STEP SOP & TRAPS</button>
            <button class="tab-btn" onclick="switchSubTab(event, 'ch13-mock')">FULL SIMULATION MOCK EXAM</button>
        </div>

        <!-- ==================== SUBTAB 1: MASTER FORMULA SHEET ==================== -->
        <div id="ch13-formulas" class="subtab-content active">
            <div class="intel-card">
                <h3>13.1 Q-Branch Master Formula Inventory (35+ Operational Formulas)</h3>
                <p>Every formula required for the university macroeconomics examination, categorized by functional domain.</p>

                <!-- SECTION A: NATIONAL INCOME -->
                <h4 style="color:var(--accent-silver); margin-top:20px;">A. National Income Accounting (Chapters 1 & 2)</h4>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>Concept / Metric</th>
                            <th>Master Formula</th>
                            <th>Variable Definitions & Key Conditions</th>
                            <th>Examination Pitfall to Avoid</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Production / Value Added Method</strong></td>
                            <td>$$GVA_{mp} = \text{Value of Output} - \text{Intermediate Consumption}$$</td>
                            <td>$\text{Value of Output} = \text{Sales} + \Delta\text{Stock}$. $\Delta\text{Stock} = \text{Closing} - \text{Opening}$.</td>
                            <td>Do NOT subtract purchases of capital machinery (that is gross investment, not intermediate consumption).</td>
                        </tr>
                        <tr>
                            <td><strong>Income Method</strong></td>
                            <td>$$NDP_{fc} = CE + OS + MI$$</td>
                            <td>$CE$ = Compensation of Employees, $OS$ = Operating Surplus (Rent + Interest + Profit), $MI$ = Mixed Income of Self-Employed.</td>
                            <td>Do NOT include transfer payments (pensions, unemployment dole, pocket money).</td>
                        </tr>
                        <tr>
                            <td><strong>Expenditure Method</strong></td>
                            <td>$$GDP_{mp} = C + I + G + (X - M)$$</td>
                            <td>$C$ = Private final consumption, $I$ = Gross capital formation, $G$ = Govt purchases of final goods/services, $(X-M)$ = Net exports.</td>
                            <td>Exclude government transfer outlays and second-hand asset transactions.</td>
                        </tr>
                        <tr>
                            <td><strong>Market Price to Factor Cost</strong></td>
                            <td>$$GDP_{fc} = GDP_{mp} - NIT = GDP_{mp} - (\text{Indirect Taxes} - \text{Subsidies})$$</td>
                            <td>$NIT$ = Net Indirect Taxes = Indirect Taxes minus Subsidies.</td>
                            <td>Watch algebraic sign: Subsidies <em>increase</em> $GDP_{fc}$; Indirect Taxes <em>reduce</em> $GDP_{fc}$.</td>
                        </tr>
                        <tr>
                            <td><strong>Gross to Net Aggregate</strong></td>
                            <td>$$\text{Net Aggregate} = \text{Gross Aggregate} - \text{Depreciation (CFC)}$$</td>
                            <td>$CFC$ = Consumption of Fixed Capital.</td>
                            <td>Do not confuse depreciation of currency with capital depreciation.</td>
                        </tr>
                        <tr>
                            <td><strong>Domestic to National Aggregate</strong></td>
                            <td>$$GNP = GDP + NFIA$$</td>
                            <td>$NFIA$ = Net Factor Income from Abroad = Factor income earned abroad by residents minus factor income earned by non-residents domestically.</td>
                            <td>If domestic factor outflow exceeds resident foreign earnings, $NFIA$ is negative.</td>
                        </tr>
                    </tbody>
                </table>

                <!-- SECTION B: PRICES & INFLATION -->
                <h4 style="color:var(--accent-silver); margin-top:24px;">B. Deflator, Inflation & Labor Market (Chapters 3 & 4)</h4>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>Concept / Metric</th>
                            <th>Master Formula</th>
                            <th>Variable Definitions & Key Conditions</th>
                            <th>Examination Pitfall to Avoid</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Real GDP</strong></td>
                            <td>$$\text{Real GDP}_t = \sum (P_{\text{base}} \times Q_t) = \frac{\text{Nominal GDP}_t}{\text{GDP Deflator}_t} \times 100$$</td>
                            <td>Values current physical output using constant base-year prices. Eliminates price distortions.</td>
                            <td>Always verify the designated base year in the question brief.</td>
                        </tr>
                        <tr>
                            <td><strong>GDP Deflator</strong></td>
                            <td>$$\text{GDP Deflator}_t = \frac{\text{Nominal GDP}_t}{\text{Real GDP}_t} \times 100$$</td>
                            <td>Paasche index measuring price changes of all domestically produced final goods and services. Base year deflator $\equiv 100$.</td>
                            <td>Never forget to multiply by 100. It is an index, not a decimal.</td>
                        </tr>
                        <tr>
                            <td><strong>Annual Inflation Rate</strong></td>
                            <td>$$\pi_t = \frac{P_t - P_{t-1}}{P_{t-1}} \times 100$$</td>
                            <td>Percentage change in price index (Deflator or CPI) over consecutive periods.</td>
                            <td>The denominator MUST be the previous period ($P_{t-1}$), never the current period or base year!</td>
                        </tr>
                        <tr>
                            <td><strong>Double Deflation</strong></td>
                            <td>$$\text{Real GVA} = \frac{\text{Nominal Output}}{P_{\text{output}}} \times 100 - \frac{\text{Nominal IC}}{P_{\text{input}}} \times 100$$</td>
                            <td>Deflates gross output and intermediate consumption by their own specific price indices.</td>
                            <td>Single deflation distorts real value added when raw material and output prices diverge.</td>
                        </tr>
                        <tr>
                            <td><strong>Unemployment Rate ($UR$)</strong></td>
                            <td>$$UR = \frac{\text{Number of Unemployed}}{\text{Labor Force}} \times 100$$</td>
                            <td>$\text{Labor Force} = \text{Employed} + \text{Unemployed (actively seeking work)}$.</td>
                            <td>Do NOT divide by Total Population or Working-Age Population!</td>
                        </tr>
                        <tr>
                            <td><strong>Labor Force Participation Rate ($LFPR$)</strong></td>
                            <td>$$LFPR = \frac{\text{Labor Force}}{\text{Working-Age Population}} \times 100$$</td>
                            <td>Working-Age Population typically defined as ages 15–64.</td>
                            <td>Discouraged workers who drop out of job searching shrink the numerator.</td>
                        </tr>
                    </tbody>
                </table>

                <!-- SECTION C: MULTIPLIERS & POLICIES -->
                <h4 style="color:var(--accent-silver); margin-top:24px;">C. Savings, Multipliers & Policy Mechanics (Chapters 6, 7 & 8)</h4>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>Concept / Metric</th>
                            <th>Master Formula</th>
                            <th>Variable Definitions & Key Conditions</th>
                            <th>Examination Pitfall to Avoid</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Consumption & Saving Functions</strong></td>
                            <td>$$C = C_0 + c(Y - T), \quad S = -C_0 + (1 - c)(Y - T)$$</td>
                            <td>$c = MPC = \frac{\Delta C}{\Delta Y_d}$, $s = MPS = 1 - c = \frac{\Delta S}{\Delta Y_d}$. $MPC + MPS \equiv 1$.</td>
                            <td>Remember saving starts negative at zero income ($-C_0$, dissaving).</td>
                        </tr>
                        <tr>
                            <td><strong>Simple Investment Multiplier</strong></td>
                            <td>$$k_I = \frac{1}{1 - MPC} = \frac{1}{MPS}$$</td>
                            <td>Measures multiple expansion in output from $\Delta I$ in closed private economy without taxes.</td>
                            <td>Valid only when there are no proportional taxes or imports.</td>
                        </tr>
                        <tr>
                            <td><strong>Fiscal Expenditure Multiplier</strong></td>
                            <td>$$k_F = \frac{\Delta Y}{\Delta G} = \frac{1}{1 - c(1 - t)}$$</td>
                            <td>Includes proportional tax rate $t$. $c(1-t)$ is the induced marginal propensity to spend out of gross income.</td>
                            <td>Proportional taxation lowers the multiplier relative to lump-sum taxation.</td>
                        </tr>
                        <tr>
                            <td><strong>Lump-Sum Tax Multiplier</strong></td>
                            <td>$$k_T = \frac{\Delta Y}{\Delta T} = -\frac{c}{1 - c}$$</td>
                            <td>Notice the negative sign! A tax hike reduces disposable income and output.</td>
                            <td>$|k_T| < k_F$ because part of the tax increase is absorbed by reduced saving, not reduced consumption.</td>
                        </tr>
                        <tr>
                            <td><strong>Balanced Budget Multiplier</strong></td>
                            <td>$$k_{BB} = k_F + k_T = \frac{1}{1 - c} + \left(-\frac{c}{1 - c}\right) = \frac{1 - c}{1 - c} = +1$$</td>
                            <td>When $\Delta G = \Delta T$, the expansion in output exactly equals the initial change in spending ($\Delta Y = \Delta G$).</td>
                            <td>Students often falsely assume the net multiplier is zero! It is always $+1$ in a lump-sum world.</td>
                        </tr>
                        <tr>
                            <td><strong>Open Economy Multiplier</strong></td>
                            <td>$$k_{\text{open}} = \frac{1}{1 - c(1 - t) + m}$$</td>
                            <td>$m = MPM = \frac{\Delta M}{\Delta Y}$ is the marginal propensity to import.</td>
                            <td>Imports constitute a leakage, reducing the domestic multiplier.</td>
                        </tr>
                        <tr>
                            <td><strong>Money Multiplier</strong></td>
                            <td>$$m = \frac{1 + cr}{cr + rr}, \quad M = m \times M_0$$</td>
                            <td>$cr = C/D$ (currency-deposit ratio), $rr = R/D$ (reserve-deposit ratio), $M_0$ = High-powered money.</td>
                            <td>A cash drain ($cr \uparrow$) reduces the money multiplier.</td>
                        </tr>
                    </tbody>
                </table>

                <!-- SECTION D: IS-LM & PHILLIPS CURVE -->
                <h4 style="color:var(--accent-silver); margin-top:24px;">D. IS-LM, Central Banking & Phillips Curve (Chapters 9, 10 & 11)</h4>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>Concept / Metric</th>
                            <th>Master Formula</th>
                            <th>Variable Definitions & Key Conditions</th>
                            <th>Examination Pitfall to Avoid</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>IS Curve Equation</strong></td>
                            <td>$$Y = k_F [\bar{A} - br] \iff r = \frac{\bar{A}}{b} - \frac{1}{b \cdot k_F} Y$$</td>
                            <td>$\bar{A} = C_0 - cT + I_0 + G$. $b$ is interest sensitivity of investment. Downward sloping.</td>
                            <td>Points above IS = Excess Supply of Goods; points below = Excess Demand.</td>
                        </tr>
                        <tr>
                            <td><strong>LM Curve Equation</strong></td>
                            <td>$$r = \frac{k}{h} Y - \frac{1}{h}\left(\frac{\bar{M}}{P}\right)$$</td>
                            <td>$k$ = income sensitivity of money demand, $h$ = interest sensitivity. Upward sloping.</td>
                            <td>Points above LM = Excess Supply of Money; points below = Excess Demand.</td>
                        </tr>
                        <tr>
                            <td><strong>Monetary Policy (MP) Reaction Function</strong></td>
                            <td>$$r = \bar{r} + \lambda \pi$$</td>
                            <td>Central bank sets real interest rate $r$ in response to inflation $\pi$. $\lambda > 0$ satisfies Taylor Principle.</td>
                            <td>Ensures real rate rises when inflation accelerates, dampening AD.</td>
                        </tr>
                        <tr>
                            <td><strong>Expectations-Augmented Phillips Curve</strong></td>
                            <td>$$\pi = \pi^e - \beta(u - u_n) + \nu$$</td>
                            <td>$\pi^e$ = expected inflation, $\beta$ = sensitivity parameter, $u_n$ = NAIRU, $\nu$ = supply shock.</td>
                            <td>In the long run, $\pi^e = \pi \implies u = u_n$ (vertical LRPC).</td>
                        </tr>
                        <tr>
                            <td><strong>Sacrifice Ratio</strong></td>
                            <td>$$\text{Sacrifice Ratio} = \frac{\sum \text{Cumulative \% Output Loss}}{\Delta \pi \text{ (Percentage Points Disinflation)}}$$</td>
                            <td>Quantifies the real GDP cost required to lower inflation by 1 percentage point.</td>
                            <td>Credible central banks face lower sacrifice ratios.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- ==================== SUBTAB 2: 12 CONCEPT MATRICES ==================== -->
        <div id="ch13-matrices" class="subtab-content">
            <div class="intel-card">
                <h3>13.2 The 12 Tactical Distinction Matrices (High-Yield Exam Contrasts)</h3>
                <p>Prof. Sana and Prof. Abhishek consistently test boundary definitions. Master these 12 distinction tables.</p>

                <!-- MATRIX 1 -->
                <h4>1. Microeconomics vs. Macroeconomics</h4>
                <table class="data-table">
                    <thead><tr><th>Feature</th><th>Microeconomics</th><th>Macroeconomics</th></tr></thead>
                    <tbody>
                        <tr><td><strong>Unit of Analysis</strong></td><td>Individual agents: single consumer, household, firm, industry.</td><td>Aggregate economy: national income, total output, general price level.</td></tr>
                        <tr><td><strong>Core Objective</strong></td><td>Optimal allocation of scarce resources and price determination.</td><td>Full employment, economic growth, price stability, balance of payments.</td></tr>
                        <tr><td><strong>Central Equilibrium</strong></td><td>Partial equilibrium (holding other industries constant).</td><td>General equilibrium (simultaneous clearing across goods, money, labor).</td></tr>
                    </tbody>
                </table>

                <!-- MATRIX 2 -->
                <h4 style="margin-top:16px;">2. Stock Variables vs. Flow Variables</h4>
                <table class="data-table">
                    <thead><tr><th>Feature</th><th>Stock Variable</th><th>Flow Variable</th></tr></thead>
                    <tbody>
                        <tr><td><strong>Time Dimension</strong></td><td>Measured at a <strong>specific point in time</strong> (snapshot). Has no time duration.</td><td>Measured <strong>per unit of time</strong> (e.g., per month, per year). Has a time dimension.</td></tr>
                        <tr><td><strong>Examples</strong></td><td>National wealth, capital stock ($K$), foreign exchange reserves, public debt, money supply ($M_3$).</td><td>GDP, national income, investment ($\Delta K$), government budget deficit, consumer expenditure.</td></tr>
                    </tbody>
                </table>

                <!-- MATRIX 3 -->
                <h4 style="margin-top:16px;">3. Final Goods vs. Intermediate Goods</h4>
                <table class="data-table">
                    <thead><tr><th>Feature</th><th>Final Goods</th><th>Intermediate Goods</th></tr></thead>
                    <tbody>
                        <tr><td><strong>Ultimate Use</strong></td><td>Purchased for final consumption ($C$) or gross capital formation ($I$).</td><td>Purchased for resale or completely transformed as inputs in production within the accounting year.</td></tr>
                        <tr><td><strong>National Accounting</strong></td><td>Included in GDP to reflect total economic value produced.</td><td><strong>Strictly excluded</strong> to eliminate the error of double counting.</td></tr>
                    </tbody>
                </table>

                <!-- MATRIX 4 -->
                <h4 style="margin-top:16px;">4. Nominal GDP vs. Real GDP</h4>
                <table class="data-table">
                    <thead><tr><th>Feature</th><th>Nominal GDP</th><th>Real GDP</th></tr></thead>
                    <tbody>
                        <tr><td><strong>Pricing Basis</strong></td><td>Valued at <strong>current market prices</strong> prevailing during the production year.</td><td>Valued at <strong>constant base-year prices</strong>.</td></tr>
                        <tr><td><strong>Welfare Significance</strong></td><td>Can rise purely due to inflation without any increase in physical output.</td><td>Rises only when actual physical volume of goods and services increases. True metric of growth.</td></tr>
                    </tbody>
                </table>

                <!-- MATRIX 5 -->
                <h4 style="margin-top:16px;">5. GDP Deflator vs. Consumer Price Index (CPI)</h4>
                <table class="data-table">
                    <thead><tr><th>Feature</th><th>GDP Deflator</th><th>Consumer Price Index (CPI)</th></tr></thead>
                    <tbody>
                        <tr><td><strong>Basket Coverage</strong></td><td>Covers <strong>all domestically produced</strong> goods and services (including capital goods and govt purchases).</td><td>Covers only a <strong>representative basket of consumer goods and services</strong> bought by households.</td></tr>
                        <tr><td><strong>Import Treatment</strong></td><td>Excludes imported goods completely.</td><td>Includes imported consumer goods (e.g., imported electronics, crude oil).</td></tr>
                        <tr><td><strong>Weighting Scheme</strong></td><td>Paasche index (weights change automatically every year with production).</td><td>Laspeyres index (fixed base-year consumption basket weights).</td></tr>
                    </tbody>
                </table>

                <!-- MATRIX 6 -->
                <h4 style="margin-top:16px;">6. Headline Inflation vs. Core Inflation</h4>
                <table class="data-table">
                    <thead><tr><th>Feature</th><th>Headline Inflation</th><th>Core Inflation</th></tr></thead>
                    <tbody>
                        <tr><td><strong>Components</strong></td><td>Covers the <strong>entire consumer basket</strong>, including food and energy items.</td><td><strong>Excludes food and fuel</strong> due to their extreme exogenous price volatility.</td></tr>
                        <tr><td><strong>Monetary Stance</strong></td><td>Captures immediate cost of living felt by common citizens.</td><td>Measures underlying, persistent demand-pull inflationary pressure for central banks.</td></tr>
                    </tbody>
                </table>

                <!-- MATRIX 7 -->
                <h4 style="margin-top:16px;">7. Unemployment Types: Frictional vs. Structural vs. Cyclical</h4>
                <table class="data-table">
                    <thead><tr><th>Type</th><th>Underlying Cause</th><th>Policy Remedy</th></tr></thead>
                    <tbody>
                        <tr><td><strong>Frictional</strong></td><td>Search and transition time between jobs; voluntary job-switching.</td><td>Job search portals, employment exchanges, recruitment information.</td></tr>
                        <tr><td><strong>Structural</strong></td><td>Mismatch between workers' skills/locations and employers' technical needs.</td><td>Vocational retraining, education reform, geographical mobility grants.</td></tr>
                        <tr><td><strong>Cyclical</strong></td><td>Deficient Aggregate Demand during business cycle recessions ($Y < Y^*$).</td><td>Expansionary fiscal policy ($\Delta G > 0$) and monetary easing ($\Delta r < 0$).</td></tr>
                    </tbody>
                </table>

                <!-- MATRIX 8 -->
                <h4 style="margin-top:16px;">8. Autonomous vs. Induced Expenditure</h4>
                <table class="data-table">
                    <thead><tr><th>Feature</th><th>Autonomous Expenditure ($\bar{A}$)</th><th>Induced Expenditure</th></tr></thead>
                    <tbody>
                        <tr><td><strong>Income Dependence</strong></td><td>Independent of current national income ($Y$). Graphically represented as vertical intercept.</td><td>Directly varies with disposable income ($Y_d$). Graphically represented by the slope ($c \cdot Y$).</td></tr>
                        <tr><td><strong>Determinants</strong></td><td>Interest rates, animal spirits, government fiscal policy, basic survival needs.</td><td>Marginal Propensity to Consume ($MPC$) and marginal tax rates ($t$).</td></tr>
                    </tbody>
                </table>

                <!-- MATRIX 9 -->
                <h4 style="margin-top:16px;">9. Classical vs. Keynesian View of Savings & Investment</h4>
                <table class="data-table">
                    <thead><tr><th>Feature</th><th>Classical Loanable Funds Framework</th><th>Keynesian Income-Expenditure Framework</th></tr></thead>
                    <tbody>
                        <tr><td><strong>Equilibrating Mechanism</strong></td><td>The <strong>real interest rate ($r$)</strong> fluctuates to guarantee $S(r) = I(r)$ at full employment.</td><td><strong>National income / output ($Y$)</strong> adjusts via the multiplier to equalize $S(Y) = I$.</td></tr>
                        <tr><td><strong>View of Saving</strong></td><td>Saving is virtuous—it directly finances productive investment and capital accumulation.</td><td><strong>Paradox of Thrift</strong>—collective desire to save more depresses $AD$, contracting $Y$.</td></tr>
                    </tbody>
                </table>

                <!-- MATRIX 10 -->
                <h4 style="margin-top:16px;">10. Crowding Out vs. Crowding In</h4>
                <table class="data-table">
                    <thead><tr><th>Feature</th><th>Crowding Out Effect</th><th>Crowding In Effect</th></tr></thead>
                    <tbody>
                        <tr><td><strong>Mechanism</strong></td><td>Government borrowing raises real interest rates ($r \uparrow$), displacing private investment ($I \downarrow$).</td><td>Public infrastructure capex raises private capital productivity ($MPK \uparrow$), inducing higher private investment ($I \uparrow$).</td></tr>
                        <tr><td><strong>Operating Condition</strong></td><td>Near full employment ($Y \approx Y^*$) or inelastic money supply.</td><td>During deep recessions ($Y \ll Y^*$) with excess capacity and complementary infrastructure needs.</td></tr>
                    </tbody>
                </table>

                <!-- MATRIX 11 -->
                <h4 style="margin-top:16px;">11. Expansionary Fiscal vs. Expansionary Monetary Policy</h4>
                <table class="data-table">
                    <thead><tr><th>Feature</th><th>Fiscal Policy ($\Delta G > 0, \Delta T < 0$)</th><th>Monetary Policy ($\Delta M > 0, \text{Repo} \downarrow$)</th></tr></thead>
                    <tbody>
                        <tr><td><strong>Initiating Authority</strong></td><td>Ministry of Finance / Treasury (Parliamentary approval).</td><td>Central Bank / Monetary Policy Committee (Independent).</td></tr>
                        <tr><td><strong>Interest Rate Effect</strong></td><td>Pushes interest rates <strong>UP</strong> along LM curve ($r \uparrow$).</td><td>Pushes interest rates <strong>DOWN</strong> along IS curve ($r \downarrow$).</td></tr>
                        <tr><td><strong>Implementation Lags</strong></td><td>Long legislative lag, short operational transmission lag.</td><td>Zero legislative lag (overnight decision), long operational transmission lag (6–18 months).</td></tr>
                    </tbody>
                </table>

                <!-- MATRIX 12 -->
                <h4 style="margin-top:16px;">12. Movements Along vs. Shifts of Curves</h4>
                <table class="data-table">
                    <thead><tr><th>Curve</th><th>Movement Along Curve Trigger</th><th>Shift of Curve Trigger</th></tr></thead>
                    <tbody>
                        <tr><td><strong>AD Curve</strong></td><td>Change in Price Level ($P$) via wealth, interest-rate, and exchange-rate effects.</td><td>Changes in $C_0, I_0, G, T, NX$, or Money Supply ($M$).</td></tr>
                        <tr><td><strong>SRAS Curve</strong></td><td>Change in Price Level ($P$) with sticky nominal wages.</td><td>Changes in input costs (oil shock, wages), productivity, or business taxes.</td></tr>
                        <tr><td><strong>IS Curve</strong></td><td>Change in Real Interest Rate ($r$).</td><td>Changes in autonomous spending ($G, T, C_0, I_0$).</td></tr>
                        <tr><td><strong>LM Curve</strong></td><td>Change in Real Income ($Y$) driving transactional money demand.</td><td>Changes in nominal money supply ($M$) or price level ($P$).</td></tr>
                        <tr><td><strong>SRPC</strong></td><td>Change in Aggregate Demand (moving output and unemployment).</td><td>Changes in Expected Inflation ($\pi^e$) or Supply Shocks ($\nu$).</td></tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- ==================== SUBTAB 3: GRAPHICAL REVISION ATLAS ==================== -->
        <div id="ch13-gallery" class="subtab-content">
''' + atlas_html + r'''
        </div>

        <!-- ==================== SUBTAB 4: 7-STEP SOP & TRAPS ==================== -->
        <div id="ch13-toolkit" class="subtab-content">
            <div class="intel-card">
                <h3>13.4 The 7-Step Standard Operating Procedure (SOP)</h3>
                <p>
                    To score maximum marks in numerical and case-study questions, format every solution strictly following the official 7-step blueprint established by the examination evaluators:
                </p>
                <div class="step-list">
                    <div class="step-item">
                        <div class="step-title">STEP 1: MISSION BRIEF</div>
                        <p>Restate the objective of the problem in concise analytical language. Define what exact variables must be calculated or what economic phenomenon is being evaluated.</p>
                    </div>
                    <div class="step-item">
                        <div class="step-title">STEP 2: INTELLIGENCE EXTRACTION</div>
                        <p>Extract all given variables, parameters, and baseline values from the prompt with explicit units (e.g., $MPC = 0.8, t = 0.25, \bar{I} = 400 \text{ Cr}$). Identify all known constraints.</p>
                    </div>
                    <div class="step-item">
                        <div class="step-title">STEP 3: FORMULA SELECTION</div>
                        <p>Write out the unsubstituted algebraic equation. Never skip straight to numbers. Evaluators award distinct formula marks before checking arithmetic.</p>
                    </div>
                    <div class="step-item">
                        <div class="step-title">STEP 4: EXECUTION</div>
                        <p>Substitute numerical values into the formula with clear, intermediate arithmetic steps. Keep fractions and decimals neat and carry standard precision.</p>
                    </div>
                    <div class="step-item">
                        <div class="step-title">STEP 5: GRAPHICAL ANALYSIS</div>
                        <p>Describe or sketch the geometric shift in the relevant economic space (e.g., AD-AS, IS-LM, Phillips Curve). State the initial coordinate, the shift direction, and the final equilibrium point.</p>
                    </div>
                    <div class="step-item">
                        <div class="step-title">STEP 6: ECONOMIC INTERPRETATION</div>
                        <p>Translate the math into economic reasoning. Explain the behavioral transmission mechanism: Why did output change? How did consumer/firm decisions cause this result?</p>
                    </div>
                    <div class="step-item">
                        <div class="step-title">STEP 7: TARGET CONFIRMATION</div>
                        <p>State the final numerical result cleanly inside an explicit summary box with correct economic units.</p>
                    </div>
                </div>

                <div class="warning-box" style="margin-top:24px;">
                    <h4 style="color:var(--accent-crimson);">CRITICAL EXAMINATION RED LINES: DEADLY MISTAKES TO AVOID</h4>
                    <ol style="margin-left:20px; line-height:1.7;">
                        <li><strong>Inverting the Tax Multiplier Sign:</strong> $k_T = -c / (1-c)$ is ALWAYS NEGATIVE. If taxes rise, output MUST contract!</li>
                        <li><strong>Confusing the Base Year for Inflation:</strong> Always divide by the <em>preceding year's price index</em> ($P_{t-1}$), NOT the base-year index ($100$).</li>
                        <li><strong>Forgetting Capital Goods in Intermediate Consumption:</strong> Buying a machine is Gross Capital Formation ($I$), NOT intermediate consumption! Intermediate goods are fully used up within 1 year.</li>
                        <li><strong>Assuming the Balanced Budget Multiplier is Zero:</strong> $\Delta G = \Delta T$ generates an expansion of $\Delta Y = \Delta G$. The multiplier is $+1$, NOT zero!</li>
                        <li><strong>Dividing Unemployment by Total Population:</strong> Unemployment rate denominator is the <strong>Labor Force</strong> ($E + U$), not total population!</li>
                    </ol>
                </div>
            </div>
        </div>

        <!-- ==================== SUBTAB 5: FULL SIMULATION MOCK EXAM ==================== -->
        <div id="ch13-mock" class="subtab-content">
        <a id="ch13-mock-exam"></a>
            <div class="mission-briefing">
                <div class="briefing-tag">FINAL COMBAT EVALUATION // FULL SIMULATION MOCK EXAM</div>
                <h3>Grand End-Semester Examination Simulation</h3>
                <p>Complete multi-section examination covering the entire curriculum. Test your readiness under actual university conditions.</p>
            </div>

            <!-- MOCK QUESTION 1 -->
            <div class="intel-card">
                <div class="mission-status-bar">
                    <span class="difficulty-pill pill-exam">SECTION A: CONCEPTUAL</span>
                    <span class="mission-id">MOCK QUESTION 1 [10 MARKS]</span>
                </div>
                <h4>Macroeconomic Accounting & Economic Welfare</h4>
                <p>
                    "An increase in Nominal GDP is an infallible indicator that the average citizen's economic well-being has improved." Critically evaluate this statement using:
                </p>
                <ol style="margin-left:20px; line-height:1.7;">
                    <li>The distinction between Nominal GDP, Real GDP, and the GDP Deflator.</li>
                    <li>The Kapoor & Debroy welfare critique regarding externalities, unpaid household labor, and income distribution.</li>
                    <li>The Green GDP framework.</li>
                </ol>
                <button class="action-btn" onclick="revealSolution('smock-1')">REVEAL MOCK SOLUTION 1</button>
                <div id="smock-1" class="solution-card" style="margin-top:14px;">
                    <div class="step-title">EXAMINER MODEL SOLUTION: QUESTION 1</div>
                    <p>
                        <strong>1. Distortion of Inflation:</strong> Nominal GDP measures output at current market prices ($Nominal = P_t \times Q_t$). A country can experience a 20% surge in Nominal GDP purely through severe price inflation with zero increase—or even a contraction—in actual physical goods and services produced. Only <strong>Real GDP</strong> ($Real = Nominal / Deflator \times 100$) isolates real physical output expansion.<br><br>
                        <strong>2. The Kapoor & Debroy Welfare Critique:</strong> As articulated in Harvard Business Review analysis, GDP is a measure of market throughput, not living standards:
                        • <em>Negative Externalities:</em> Industrial pollution, environmental degradation, and resource depletion are counted positively if money is spent cleaning them up, ignoring the destruction of natural capital.<br>
                        • <em>Non-Market Transactions:</em> Unpaid care work, household domestic labor, and community volunteer services (overwhelmingly performed by women) are excluded despite creating immense social welfare.<br>
                        • <em>Income Inequality:</em> GDP averages out national income. A surging GDP can coincide with worsening poverty if gains concentrate in the top 1%.<br><br>
                        <strong>3. Green GDP:</strong> $Green\_GDP = GDP - \text{Net Environmental Degradation} - \text{Depletion of Natural Capital}$. True welfare accounting deducts ecological losses from output.
                    </p>
                </div>
            </div>

            <!-- MOCK QUESTION 2 -->
            <div class="intel-card">
                <div class="mission-status-bar">
                    <span class="difficulty-pill pill-exam">SECTION B: NUMERICAL</span>
                    <span class="mission-id">MOCK QUESTION 2 [15 MARKS]</span>
                </div>
                <h4>Integrated Multiplier & Output Gap Mechanics</h4>
                <p>
                    The macroeconomic planners of the sovereign state of Zephyra record the following structural data:
                </p>
                <div class="formula-box">
                    $$C = 500 + 0.80(Y - T)$$
                    $$I = 400$$
                    $$G = 600$$
                    $$T = 500$$
                    $$\text{Potential Full-Employment Output } (Y^*) = 6,500$$
                </div>
                <p><strong>Directives:</strong></p>
                <ol style="margin-left:20px; line-height:1.7;">
                    <li>Calculate the current equilibrium output ($Y_0$).</li>
                    <li>Determine the output gap ($Y_0 - Y^*$) and identify the type of gap.</li>
                    <li>Calculate the required increase in government expenditure ($\Delta G$) to achieve full employment.</li>
                    <li>Calculate the alternative required tax cut ($\Delta T$) to achieve full employment.</li>
                </ol>
                <button class="action-btn" onclick="revealSolution('smock-2')">REVEAL MOCK SOLUTION 2</button>
                <div id="smock-2" class="solution-card" style="margin-top:14px;">
                    <div class="step-title">EXAMINER MODEL SOLUTION: QUESTION 2 (7-STEP SOP)</div>
                    <ol class="step-list">
                        <li class="step-item">
                            <div class="step-title">STEP 1: MISSION BRIEF</div>
                            <p>Calculate equilibrium $Y$, output gap, and required fiscal policy instruments ($\Delta G, \Delta T$) to achieve $Y^* = 6,500$.</p>
                        </li>
                        <li class="step-item">
                            <div class="step-title">STEP 2: INTELLIGENCE EXTRACTION</div>
                            <p>$C_0 = 500, c = 0.80, I = 400, G = 600, T = 500, Y^* = 6,500$.</p>
                        </li>
                        <li class="step-item">
                            <div class="step-title">STEP 3: FORMULA SELECTION</div>
                            <p>$$Y = \frac{C_0 - cT + I + G}{1 - c}, \quad k_F = \frac{1}{1 - c}, \quad k_T = -\frac{c}{1 - c}$$</p>
                        </li>
                        <li class="step-item">
                            <div class="step-title">STEP 4: EXECUTION</div>
                            <p>
                                <strong>1. Baseline Equilibrium:</strong><br>
                                Autonomous spending $\bar{A} = 500 - 0.80(500) + 400 + 600 = 500 - 400 + 1000 = 1100$.<br>
                                $$k_F = \frac{1}{1 - 0.80} = \frac{1}{0.20} = 5.0$$
                                $$Y_0 = 5.0 \times 1100 = \mathbf{5,500}$$
                                <br>
                                <strong>2. Output Gap:</strong><br>
                                $$\text{Gap} = Y_0 - Y^* = 5,500 - 6,500 = \mathbf{-1,000 \quad (\text{Deflationary / Recessionary Gap})}$$
                                <br>
                                <strong>3. Required Expenditure Expansion ($\Delta G$):</strong><br>
                                $$\Delta Y = k_F \times \Delta G \implies +1,000 = 5 \times \Delta G \implies \mathbf{\Delta G = +200}$$
                                <br>
                                <strong>4. Required Tax Cut ($\Delta T$):</strong><br>
                                $$k_T = -\frac{0.80}{1 - 0.80} = -\frac{0.80}{0.20} = -4.0$$
                                $$\Delta Y = k_T \times \Delta T \implies +1,000 = -4 \times \Delta T \implies \mathbf{\Delta T = -250 \quad (\text{Tax Cut of 250})}$$
                            </p>
                        </li>
                        <li class="step-item">
                            <div class="step-title">STEP 5: GRAPHICAL ANALYSIS</div>
                            <p>In the Keynesian Cross diagram, the AD curve shifts upward by 200 (if $\Delta G$) or by $0.8 \times 250 = 200$ (if $\Delta T$), restoring equilibrium at $(Y^* = 6,500)$.</p>
                        </li>
                        <li class="step-item">
                            <div class="step-title">STEP 6: ECONOMIC INTERPRETATION</div>
                            <p>Because households save 20% of disposable income, a tax cut leaks into savings, requiring a larger fiscal intervention ($\$250$) than a direct government expenditure injection ($\$200$).</p>
                        </li>
                        <li class="step-item">
                            <div class="step-title">STEP 7: TARGET CONFIRMATION</div>
                            <div class="formula-box">
                                $$\mathbf{Y_0 = 5,500, \quad \text{Gap} = -1,000, \quad \Delta G = +200, \quad \Delta T = -250}$$
                            </div>
                        </li>
                    </ol>
                </div>
            </div>

            <!-- MOCK QUESTION 3 -->
            <div class="intel-card">
                <div class="mission-status-bar">
                    <span class="difficulty-pill pill-exam">SECTION C: MACROECONOMIC SYNTHESIS</span>
                    <span class="mission-id">MOCK QUESTION 3 [15 MARKS]</span>
                </div>
                <h4>Dual-Market General Equilibrium & Central Bank Policy Mix</h4>
                <p>
                    A national economy is characterized by the following IS-LM equations:
                </p>
                <div class="formula-box">
                    $$IS: Y = 5000 - 150r$$
                    $$LM: Y = 2600 + 150r$$
                    $$I = 1200 - 50r$$
                </div>
                <p><strong>Directives:</strong></p>
                <ol style="margin-left:20px; line-height:1.7;">
                    <li>Find the initial equilibrium values of the real interest rate ($r^*$), national income ($Y^*$), and investment ($I^*$).</li>
                    <li>If the government increases infrastructure spending such that the new IS curve becomes $IS': Y = 5600 - 150r$, find the new equilibrium ($r_1^*, Y_1^*, I_1^*$) and calculate the crowding-out of private investment.</li>
                    <li>What monetary policy shift by the Central Bank would achieve full output expansion while completely preventing any crowding out of private investment? State the required new LM equation.</li>
                </ol>
                <button class="action-btn" onclick="revealSolution('smock-3')">REVEAL MOCK SOLUTION 3</button>
                <div id="smock-3" class="solution-card" style="margin-top:14px;">
                    <div class="step-title">EXAMINER MODEL SOLUTION: QUESTION 3 (7-STEP SOP)</div>
                    <ol class="step-list">
                        <li class="step-item">
                            <div class="step-title">STEP 1: MISSION BRIEF</div>
                            <p>Solve baseline IS-LM equilibrium, quantify crowding out from fiscal stimulus, and design monetary accommodation to eliminate crowding out.</p>
                        </li>
                        <li class="step-item">
                            <div class="step-title">STEP 2: INTELLIGENCE EXTRACTION</div>
                            <p>$IS_0: Y = 5000 - 150r$, $LM_0: Y = 2600 + 150r$, $I = 1200 - 50r$, $IS': Y = 5600 - 150r$.</p>
                        </li>
                        <li class="step-item">
                            <div class="step-title">STEP 3: FORMULA SELECTION</div>
                            <p>Equilibrium condition: $Y_{IS} = Y_{LM}$. Crowding out: $\Delta I = I^* - I_1^*$.</p>
                        </li>
                        <li class="step-item">
                            <div class="step-title">STEP 4: EXECUTION</div>
                            <p>
                                <strong>1. Baseline Equilibrium:</strong><br>
                                $$5000 - 150r = 2600 + 150r \implies 300r = 2400 \implies \mathbf{r^* = 8\%}$$
                                $$Y^* = 5000 - 150(8) = 5000 - 1200 = \mathbf{3800}$$
                                $$I^* = 1200 - 50(8) = 1200 - 400 = \mathbf{800}$$
                                <br>
                                <strong>2. Fiscal Shock ($IS'$ with $LM_0$):</strong><br>
                                $$5600 - 150r = 2600 + 150r \implies 300r = 3000 \implies \mathbf{r_1^* = 10\%}$$
                                $$Y_1^* = 2600 + 150(10) = \mathbf{4100}$$
                                $$I_1^* = 1200 - 50(10) = 1200 - 500 = \mathbf{700}$$
                                $$\text{Private Investment Crowded Out} = 800 - 700 = \mathbf{100 \text{ units}}$$
                                <br>
                                <strong>3. Monetary Accommodation to Eliminate Crowding Out:</strong><br>
                                To maintain $I = 800$, interest rate must stay pinned at $r = 8\%$.<br>
                                Output along $IS'$ at $r = 8\%$:
                                $$Y_2^* = 5600 - 150(8) = 5600 - 1200 = \mathbf{4400}$$
                                The Central Bank must expand the money supply to shift the LM curve rightward such that $(Y=4400, r=8\%)$ satisfies the new equation:<br>
                                $$LM': Y = A_{LM} + 150r \implies 4400 = A_{LM} + 150(8) = A_{LM} + 1200 \implies A_{LM} = 3200$$
                                $$\mathbf{LM': Y = 3200 + 150r}$$
                            </p>
                        </li>
                        <li class="step-item">
                            <div class="step-title">STEP 5: GRAPHICAL ANALYSIS</div>
                            <p>Initial point $(3800, 8\%)$ moves to $(4100, 10\%)$ under fiscal stimulus alone. With monetary accommodation, LM shifts right to intersect $IS'$ at $(4400, 8\%)$, locking interest rates at their low baseline.</p>
                        </li>
                        <li class="step-item">
                            <div class="step-title">STEP 6: ECONOMIC INTERPRETATION</div>
                            <p>Monetary accommodation injects just enough real liquidity to satisfy the increased transactions money demand generated by the fiscal boom, ensuring bond prices do not drop and private corporate borrowing costs remain completely insulated.</p>
                        </li>
                        <li class="step-item">
                            <div class="step-title">STEP 7: TARGET CONFIRMATION</div>
                            <div class="formula-box">
                                $$\mathbf{r^* = 8\%, Y^* = 3800, I^* = 800 \implies r_1^* = 10\%, Y_1^* = 4100, I_1^* = 700 \implies LM': Y = 3200 + 150r}$$
                            </div>
                        </li>
                    </ol>
                </div>
            </div>
        </div>
    </div>
</section>
'''

if __name__ == "__main__":
    print("Testing ch13 module length:", len(get_chapter_13()))
