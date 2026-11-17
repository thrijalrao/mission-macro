# ch14_midsem_case_studies.py
"""
PROJECT 007: THE MACROECONOMICS INTELLIGENCE FILE
Chapter 14: Midsem 2026 Intelligence Dossier & Comprehensive Case Study Vault
Verbatim Examination Paper, Official Marking Scheme & Step-by-Step Mathematical Solutions
Plus 10 Multi-Chapter Integrated Real-World Case Studies with 7-Step SOP Solutions
"""

def get_chapter_14():
    return r'''
<section id="chapter-14" class="mission-chapter">
<a id="ch14" class="chapter-anchor"></a>
    <div class="chapter-header">
        <div class="briefing-tag">TACTICAL INTEL FILE // DOSSIER 14</div>
        <h2 class="chapter-title">CHAPTER 14: MIDSEM 2026 INTELLIGENCE DOSSIER & COMPREHENSIVE CASE STUDY VAULT</h2>
        <div class="classified-stamp">OFFICIAL TAPMI MIDTERM ARCHIVE & CASE VAULT</div>
    </div>

    <div class="tab-container">
        <div class="tab-nav">
            <button class="tab-btn active" onclick="switchSubTab(event, 'ch14-qp')">MIDSEM 2026 QUESTION PAPER (20 MARKS)</button>
            <button class="tab-btn" onclick="switchSubTab(event, 'ch14-solutions')">OFFICIAL ANSWER KEY & STEP-BY-STEP DEBRIEF</button>
            <button class="tab-btn" onclick="switchSubTab(event, 'ch14-cases')">COMPREHENSIVE CASE STUDY VAULT (10 CASES)</button>
        </div>

        <!-- ==================== SUBTAB 1: MIDSEM QUESTION PAPER ==================== -->
        <div id="ch14-qp" class="subtab-content active">
            <div class="intel-card">
                <div class="card-eyebrow">OFFICIAL UNIVERSITY EXAMINATION // SEPTEMBER 2026</div>
                <h3 style="color:var(--accent-silver); margin-top:8px;">MACROECONOMICS MID TERM EXAMINATION — SEPTEMBER 2026</h3>
                <p><strong>Course:</strong> BBA Macroeconomics | <strong>Faculty:</strong> Prof. Sana Tabassum & Prof. Abhishek Kumar Rohit | <strong>Time:</strong> 60 Minutes | <strong>Total Marks:</strong> 20 Marks</p>
                <div style="background:rgba(217,37,52,0.08); border-left:3px solid var(--bond-crimson); padding:10px 14px; margin:14px 0; font-size:0.85rem;">
                    <strong>OPERATIONAL INSTRUCTIONS:</strong> Answer all questions. Clearly state all assumptions, formulas, and balance identities before substituting values. Calculators permitted.
                </div>

                <!-- QUESTION 1 -->
                <div class="mission-card" style="margin-top:20px;">
                    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:8px;">
                        <h4 style="color:#ffffff; margin:0;">QUESTION 1: THREE APPROACHES TO NATIONAL INCOME ACCOUNTING</h4>
                        <span class="badge" style="background:rgba(217,37,52,0.25); color:#ff6b78; border:1px solid #d92534; padding:3px 8px; font-weight:700;">8 MARKS</span>
                    </div>
                    <p style="margin-top:12px;">The National Statistics Office presented the following economic data for the year 2024:</p>
                    <ul style="color:var(--silver-200); line-height:1.7; font-size:0.92rem;">
                        <li><strong>Farmers:</strong> Produced 400 units of wheat, valued at ₹5 per unit. Of these, 300 units were sold to flour mills, 60 units were sold to households, and the remaining output remained unsold in inventory.</li>
                        <li><strong>Flour Mills:</strong> Purchased wheat from farmers and produced 300 units of flour at ₹10 per unit, all of which was sold to households.</li>
                        <li><strong>Households:</strong> Also purchased other domestically produced final goods and services worth ₹500.</li>
                        <li><strong>Firms:</strong> Purchased new capital machinery worth ₹400 during the year.</li>
                        <li><strong>Government:</strong> Spent ₹300 on the construction of public infrastructure and paid ₹100 as retirement pensions to retired citizens.</li>
                        <li><strong>Income Records:</strong> Show aggregate wages of ₹2,500, rent of ₹400, interest of ₹500, corporate profits of ₹700, and mixed income of the self-employed of ₹600.</li>
                    </ul>
                    <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); padding:12px; margin-top:12px;">
                        <strong style="color:var(--accent-silver);">MANDATORY DIRECTIVE:</strong> Compute Gross Domestic Product (GDP) using the <strong>three approaches</strong> to national income accounting: (A) Value Added / Production Approach, (B) Expenditure Approach, and (C) Income Approach. Demonstrate accounting balance across all three.
                    </div>
                </div>

                <!-- QUESTION 2 -->
                <div class="mission-card" style="margin-top:24px;">
                    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:8px;">
                        <h4 style="color:#ffffff; margin:0;">QUESTION 2: MANUFACTURING GVA & DOUBLE DEFLATION IN ZEPHYRA</h4>
                        <span class="badge" style="background:rgba(217,37,52,0.25); color:#ff6b78; border:1px solid #d92534; padding:3px 8px; font-weight:700;">4 MARKS</span>
                    </div>
                    <p style="margin-top:12px;">The government of Zephyra has announced that manufacturing activity recovered strongly in 2025. An opposition economist disputes this claim, arguing that real manufacturing Gross Value Added (GVA) did not grow at all.</p>
                    <p>The following statistical information is available. The base year is 2020.</p>
                    <table class="data-table" style="margin:12px 0;">
                        <thead>
                            <tr>
                                <th>Item</th>
                                <th>2020 (Base Year)</th>
                                <th>2025 (Current Year)</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Nominal value of manufacturing output</td>
                                <td>₹1,000 crore</td>
                                <td>₹1,440 crore</td>
                            </tr>
                            <tr>
                                <td>Nominal value of intermediate inputs</td>
                                <td>₹400 crore</td>
                                <td>₹720 crore</td>
                            </tr>
                            <tr>
                                <td>Output-price index ($P_{\text{out}}$)</td>
                                <td>100</td>
                                <td>120</td>
                            </tr>
                            <tr>
                                <td>Input-price index ($P_{\text{in}}$)</td>
                                <td>100</td>
                                <td>150</td>
                            </tr>
                        </tbody>
                    </table>

                    <p><strong>Additional Information on Product Taxes & Subsidies:</strong></p>
                    <table class="data-table" style="margin:12px 0;">
                        <thead>
                            <tr>
                                <th>Item</th>
                                <th>2020 (Base Year)</th>
                                <th>2025 (Current Year)</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Nominal product taxes</td>
                                <td>₹70 crore</td>
                                <td>₹120 crore</td>
                            </tr>
                            <tr>
                                <td>Nominal product subsidies</td>
                                <td>₹10 crore</td>
                                <td>₹20 crore</td>
                            </tr>
                            <tr>
                                <td>Net product taxes at constant 2020 prices</td>
                                <td>₹60 crore</td>
                                <td>₹80 crore</td>
                            </tr>
                        </tbody>
                    </table>
                    <p style="font-size:0.9rem; color:var(--silver-300);">
                        <em>Note:</em> The opposition economist calculates real GVA by dividing the 2025 nominal GVA by the output-price index (Single Deflation). The government argues that output and intermediate inputs must be deflated separately (Double Deflation).
                    </p>
                    <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); padding:12px; margin-top:12px;">
                        <strong style="color:var(--accent-silver);">TASKS FOR ECONOMIC ADVISER:</strong>
                        <ol style="margin-top:6px; line-height:1.7; padding-left:20px;">
                            <li>Calculate nominal manufacturing GVA and nominal GDP for 2025. <em>(1 Mark)</em></li>
                            <li>Estimate 2025 real GVA under the opposition’s method (single deflation) and the government’s method (double deflation). <em>(1 Mark)</em></li>
                            <li>Advise on which method better reflects the available price information, and calculate double-deflated real GVA growth. <em>(1 Mark)</em></li>
                            <li>Calculate real GDP growth between 2020 and 2025 and evaluate the government’s claim that the increase in real GDP was driven entirely by increased production. <em>(1 Mark)</em></li>
                        </ol>
                    </div>
                </div>

                <!-- QUESTION 3 -->
                <div class="mission-card" style="margin-top:24px;">
                    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:8px;">
                        <h4 style="color:#ffffff; margin:0;">QUESTION 3: LOANABLE FUNDS, MULTIPLIER & OUTPUT GAP IN OSTARA</h4>
                        <span class="badge" style="background:rgba(217,37,52,0.25); color:#ff6b78; border:1px solid #d92534; padding:3px 8px; font-weight:700;">8 MARKS</span>
                    </div>
                    <p style="margin-top:12px;">The economy of Ostara is experiencing rising unemployment and uncertainty about future employment. Households respond by increasing precautionary saving. As a result, planned household savings increases by 12%, while improved business expectations simultaneously increase planned investment by 8%.</p>
                    <p>The initial loanable-funds schedules are given by:</p>
                    <div style="background:#090a0d; border:1px solid rgba(255,255,255,0.1); padding:10px; text-align:center; font-family:var(--font-mono); margin:10px 0;">
                        $$S_L = 1000 + 100r$$
                        $$I_L = 1600 - 100r$$
                    </div>
                    <p style="font-size:0.9rem; color:var(--silver-300);">
                        where $S_L$ and $I_L$ are measured in billion ostars and $r$ is the real interest rate expressed in percentage points. Assume that the changes in planned saving and investment shift the respective schedules horizontally by the desired amounts.
                    </p>
                    <p>Ostara’s current real GDP is <strong>8,640 billion ostars</strong>, which is equal to <strong>60% of potential GDP</strong>. The marginal propensity to consume ($MPC$) is <strong>0.75</strong>. Assume no taxes, imports, or crowding out.</p>
                    <p>The government proposes increasing expenditure by <strong>1,600 billion ostars</strong>, claiming that this will exactly eliminate the output gap.</p>
                    <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); padding:12px; margin-top:12px;">
                        <strong style="color:var(--accent-silver);">TASKS FOR ECONOMIC ADVISER:</strong>
                        <ol type="a" style="margin-top:6px; line-height:1.7; padding-left:20px;">
                            <li>Calculate the initial and new equilibrium real interest rate and quantity of loanable funds. Illustrate the changes in an appropriately labelled diagram and explain why the interest rate changes in the observed direction. <em>(4 Marks)</em></li>
                            <li>Taking account of both the increase in precautionary saving and the increase in planned investment:
                                <ol style="padding-left:20px; margin-top:4px;">
                                    <li>Calculate the expenditure multiplier. <em>(1 Mark)</em></li>
                                    <li>Estimate the resulting change in equilibrium output following the private-sector adjustments described above. <em>(1 Mark)</em></li>
                                    <li>Assess whether the proposed increase in government expenditure is sufficient to eliminate the output gap. Based on your calculations, determine the exact increase in government expenditure required to close the output gap completely. <em>(2 Marks)</em></li>
                                </ol>
                            </li>
                        </ol>
                    </div>
                </div>
            </div>
        </div>

        <!-- ==================== SUBTAB 2: OFFICIAL ANSWER KEY & DEBRIEF ==================== -->
        <div id="ch14-solutions" class="subtab-content">
            <div class="intel-card">
                <div class="card-eyebrow">OFFICIAL MARKING SCHEME // FACULTY DEBRIEFING</div>
                <h3 style="color:var(--accent-gold);">SEPTEMBER 2026 MIDSEM: STEP-BY-STEP MATHEMATICAL SOLUTIONS</h3>
                <p>Complete step-by-step scoring breakdown, underlying economic principles, common pitfalls, and visual blueprints.</p>

                <!-- DEBRIEF Q1 -->
                <div class="solution-box revealed" style="margin-top:20px; border-left:3px solid #10b981;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <h4 style="color:#ffffff; margin:0;">OFFICIAL SOLUTION: QUESTION 1 (NATIONAL INCOME ACCOUNTING — 8 MARKS)</h4>
                        <span class="badge" style="background:rgba(16,185,129,0.2); color:#10b981; border:1px solid #10b981; padding:2px 8px; font-weight:700;">8 / 8 MARKS</span>
                    </div>

                    <!-- Part A: Value Added -->
                    <div style="margin-top:16px;">
                        <h5 style="color:var(--accent-silver); text-transform:uppercase; letter-spacing:0.08em;">A. Value Added / Output Approach (3 Marks)</h5>
                        <p style="font-size:0.92rem;">$$\text{GDP} = \sum \text{Gross Value Added at Market Prices} (GVA_{mp}) = \text{Value of Output} - \text{Intermediate Consumption}$$</p>
                        <table class="data-table" style="font-size:0.88rem; margin:10px 0;">
                            <thead>
                                <tr>
                                    <th>Sector / Producer</th>
                                    <th>Gross Value of Output (₹)</th>
                                    <th>Intermediate Consumption (₹)</th>
                                    <th>Gross Value Added (GVA) (₹)</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>Wheat Farmers</strong></td>
                                    <td>$400 \times ₹5 = ₹2,000$</td>
                                    <td>₹0 (No intermediate inputs specified)</td>
                                    <td><strong>₹2,000</strong></td>
                                </tr>
                                <tr>
                                    <td><strong>Flour Mills</strong></td>
                                    <td>$300 \times ₹10 = ₹3,000$</td>
                                    <td>$300 \text{ units wheat} \times ₹5 = ₹1,500$</td>
                                    <td>$₹3,000 - ₹1,500 = \mathbf{₹1,500}$</td>
                                </tr>
                                <tr>
                                    <td><strong>Other Domestically Produced Final Goods</strong></td>
                                    <td>₹500</td>
                                    <td>₹0</td>
                                    <td><strong>₹500</strong></td>
                                </tr>
                                <tr>
                                    <td><strong>Firms (Capital Machinery Formation)</strong></td>
                                    <td>₹400</td>
                                    <td>₹0</td>
                                    <td><strong>₹400</strong></td>
                                </tr>
                                <tr>
                                    <td><strong>Government Public Infrastructure Construction</strong></td>
                                    <td>₹300</td>
                                    <td>₹0</td>
                                    <td><strong>₹300</strong></td>
                                </tr>
                            </tbody>
                        </table>
                        <div style="background:rgba(16,185,129,0.1); border:1px solid #10b981; padding:10px 14px; margin-top:8px;">
                            <strong>TOTAL GDP (Value Added Approach):</strong>
                            $$\text{GDP} = ₹2,000 + ₹1,500 + ₹500 + ₹400 + ₹300 = \mathbf{₹4,700}$$
                        </div>
                    </div>

                    <!-- Part B: Expenditure -->
                    <div style="margin-top:20px;">
                        <h5 style="color:var(--accent-silver); text-transform:uppercase; letter-spacing:0.08em;">B. Expenditure Approach (3 Marks)</h5>
                        <p style="font-size:0.92rem;">$$\text{GDP} = C + I + G + (X - M)$$</p>
                        <ol style="line-height:1.7; font-size:0.9rem; padding-left:20px;">
                            <li><strong>Private Final Consumption Expenditure ($C$):</strong>
                                <ul>
                                    <li>Flour purchased by households: $300 \times ₹10 = ₹3,000$</li>
                                    <li>Wheat purchased directly by households: $60 \times ₹5 = ₹300$</li>
                                    <li>Other final goods & services: ₹500</li>
                                    <li><em>Total $C$:</em> $₹3,000 + ₹300 + ₹500 = \mathbf{₹3,800}$</li>
                                </ul>
                            </li>
                            <li><strong>Gross Domestic Capital Formation / Investment ($I$):</strong>
                                <ul>
                                    <li>New machinery purchased by firms: ₹400</li>
                                    <li>Inventory Investment ($\Delta \text{Stock}$ of unsold wheat):
                                        $$\text{Unsold Wheat} = 400 - (300 + 60) = 40 \text{ units}$$
                                        $$\text{Value of Inventory Change} = 40 \times ₹5 = ₹200$$
                                    </li>
                                    <li><em>Total $I$:</em> $₹400 + ₹200 = \mathbf{₹600}$</li>
                                </ul>
                            </li>
                            <li><strong>Government Final Expenditure ($G$):</strong>
                                <ul>
                                    <li>Public infrastructure construction: <strong>₹300</strong></li>
                                    <li><em style="color:#f87171;">EXCLUSION:</em> Retirement pensions of ₹100 are unilateral transfer payments (not for current production of goods/services) and are strictly <strong>EXCLUDED</strong> from $G$!</li>
                                </ul>
                            </li>
                            <li><strong>Net Exports ($NX = X - M$):</strong> ₹0 (Closed economy context).</li>
                        </ol>
                        <div style="background:rgba(16,185,129,0.1); border:1px solid #10b981; padding:10px 14px; margin-top:8px;">
                            <strong>TOTAL GDP (Expenditure Approach):</strong>
                            $$\text{GDP} = C + I + G = ₹3,800 + ₹600 + ₹300 = \mathbf{₹4,700}$$
                        </div>
                    </div>

                    <!-- Part C: Income -->
                    <div style="margin-top:20px;">
                        <h5 style="color:var(--accent-silver); text-transform:uppercase; letter-spacing:0.08em;">C. Income Approach (2 Marks)</h5>
                        <p style="font-size:0.92rem;">$$\text{GDP} = \text{Compensation of Employees (Wages)} + \text{Rent} + \text{Interest} + \text{Profits} + \text{Mixed Income}$$</p>
                        <ul style="line-height:1.7; font-size:0.9rem;">
                            <li>Wages = ₹2,500</li>
                            <li>Rent = ₹400</li>
                            <li>Interest = ₹500</li>
                            <li>Profits = ₹700</li>
                            <li>Mixed Income = ₹600</li>
                        </ul>
                        <div style="background:rgba(16,185,129,0.1); border:1px solid #10b981; padding:10px 14px; margin-top:8px;">
                            <strong>TOTAL GDP (Income Approach):</strong>
                            $$\text{GDP} = ₹2,500 + ₹400 + ₹500 + ₹700 + ₹600 = \mathbf{₹4,700}$$
                        </div>
                    </div>

                    <!-- Verification Box -->
                    <div style="margin-top:16px; background:#050608; border:1px solid rgba(255,255,255,0.15); padding:12px; font-family:var(--font-mono); font-size:0.85rem;">
                        <span style="color:#10b981;">✔ MASTER ACCOUNTING IDENTITY VERIFIED:</span><br>
                        $$\text{Value Added } (₹4,700) \equiv \text{Expenditure } (₹4,700) \equiv \text{Income } (₹4,700)$$
                    </div>
                </div>

                <!-- DEBRIEF Q2 -->
                <div class="solution-box revealed" style="margin-top:24px; border-left:3px solid #38bdf8;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <h4 style="color:#ffffff; margin:0;">OFFICIAL SOLUTION: QUESTION 2 (DOUBLE DEFLATION & GVA — 4 MARKS)</h4>
                        <span class="badge" style="background:rgba(56,189,248,0.2); color:#38bdf8; border:1px solid #38bdf8; padding:2px 8px; font-weight:700;">4 / 4 MARKS</span>
                    </div>

                    <!-- Subquestion 1 -->
                    <div style="margin-top:14px;">
                        <h5 style="color:var(--accent-silver);">1. Nominal Manufacturing GVA and Nominal GDP (2025) [1 Mark]</h5>
                        $$\text{Nominal GVA}_{2025} = \text{Nominal Output} - \text{Nominal Intermediate Inputs} = 1,440 - 720 = \mathbf{₹720 \text{ crore}}$$
                        $$\text{Net Product Taxes}_{2025} = \text{Product Taxes} - \text{Subsidies} = 120 - 20 = \mathbf{₹100 \text{ crore}}$$
                        $$\text{Nominal GDP}_{2025} = \text{Nominal GVA} + \text{Net Product Taxes} = 720 + 100 = \mathbf{₹820 \text{ crore}}$$
                    </div>

                    <!-- Subquestion 2 -->
                    <div style="margin-top:18px;">
                        <h5 style="color:var(--accent-silver);">2. Real GVA Under Both Methods [1 Mark]</h5>
                        <p><strong>A. Opposition Method (Single Deflation):</strong><br>
                        Divides total nominal GVA by the output price index ($P_{\text{out}} = 120$, deflator = $1.20$):
                        $$\text{Real GVA}_{\text{Single}} = \frac{\text{Nominal GVA}}{P_{\text{out}} / 100} = \frac{720}{1.20} = \mathbf{₹600 \text{ crore}}$$
                        </p>
                        <p><strong>B. Government Method (Double Deflation):</strong><br>
                        Deflates gross output and intermediate consumption separately using their respective specific deflators:
                        $$\text{Real Output} = \frac{\text{Nominal Output}}{P_{\text{out}} / 100} = \frac{1,440}{1.20} = ₹1,200 \text{ crore}$$
                        $$\text{Real Intermediate Consumption} = \frac{\text{Nominal Inputs}}{P_{\text{in}} / 100} = \frac{720}{1.50} = ₹480 \text{ crore}$$
                        $$\text{Real GVA}_{\text{Double}} = \text{Real Output} - \text{Real Intermediate Inputs} = 1,200 - 480 = \mathbf{₹720 \text{ crore}}$$
                        </p>
                    </div>

                    <!-- Subquestion 3 -->
                    <div style="margin-top:18px;">
                        <h5 style="color:var(--accent-silver);">3. Advisory on Method Fidelity & Real GVA Growth [1 Mark]</h5>
                        <p style="font-size:0.9rem; line-height:1.7;">
                            <strong>Adviser's Ruling:</strong> The <strong>Double Deflation method</strong> is theoretically superior and accurately reflects available price information. 
                            Output prices rose by $20\%$ ($P_{\text{out}}=120$) while intermediate input prices surged by $50\%$ ($P_{\text{in}}=150$). 
                            Single deflation mistakenly applies the lower output price index to intermediate inputs, understating real intermediate input reduction and falsely concluding real GVA stagnated at ₹600 crore.
                        </p>
                        <div style="background:#090a0d; padding:10px; font-family:var(--font-mono); font-size:0.86rem; border:1px solid rgba(255,255,255,0.08);">
                            $$\text{Base Year Real GVA } (2020) = 1,000 - 400 = ₹600 \text{ crore}$$
                            $$\text{Double Deflated Real GVA Growth} = \left(\frac{720 - 600}{600}\right) \times 100 = \mathbf{20.0\%}$$
                            <em>(The opposition's claim of 0% growth is completely debunked by the double deflation calculation!)</em>
                        </div>
                    </div>

                    <!-- Subquestion 4 -->
                    <div style="margin-top:18px;">
                        <h5 style="color:var(--accent-silver);">4. Real GDP Growth and Evaluation of Production Claim [1 Mark]</h5>
                        <p style="font-size:0.9rem;">Calculate real GDP at constant 2020 prices:</p>
                        $$\text{Real GDP}_{2020} = \text{GVA}_{2020} + \text{Net Product Taxes}_{2020} = 600 + (70 - 10) = \mathbf{₹660 \text{ crore}}$$
                        $$\text{Real GDP}_{2025} = \text{Real GVA}_{2025} + \text{Net Product Taxes at 2020 Prices} = 720 + 80 = \mathbf{₹800 \text{ crore}}$$
                        $$\text{Real GDP Growth Rate} = \left(\frac{800 - 660}{660}\right) \times 100 = \mathbf{21.21\%}$$
                        <p style="margin-top:10px; font-size:0.9rem; line-height:1.7;">
                            <strong>Evaluation of Production Claim:</strong><br>
                            The total increase in real GDP is $800 - 660 = ₹140\text{ crore}$.
                            $$\text{Contribution of Real Production (GVA)} = 720 - 600 = ₹120 \text{ crore } \left(\frac{120}{140} = \mathbf{85.7\%}\right)$$
                            $$\text{Contribution of Real Net Product Taxes} = 80 - 60 = ₹20 \text{ crore } \left(\frac{20}{140} = \mathbf{14.3\%}\right)$$
                            <strong>Conclusion:</strong> The government's claim that the increase in real GDP was driven <em>entirely</em> by increased production is <strong>INCORRECT</strong>. While $85.7\%$ was driven by real production, $14.3\%$ was driven by higher real net product tax collections.
                        </p>
                    </div>
                
                        <!-- Conceptual Graph: Double Deflation vs Single Deflation -->
                        <div style="margin-top:14px; background:#07080b; border:1px solid rgba(255,255,255,0.1); padding:16px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); display:block; margin-bottom:8px;">ZEPHYRA GVA: DOUBLE DEFLATION VS SINGLE DEFLATION TRAJECTORY</span>
                            <svg viewBox="0 0 540 260" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="60" y1="220" x2="500" y2="220" stroke="#444" stroke-width="1.5"/>
                                <line x1="60" y1="20" x2="60" y2="220" stroke="#444" stroke-width="1.5"/>
                                <text x="505" y="225" fill="#aaa" font-family="var(--font-mono)" font-size="11">Year</text>
                                <text x="25" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="11">Real GVA (₹ Cr)</text>

                                <!-- Base Year 2020: 600 Cr -->
                                <circle cx="160" cy="140" r="6" fill="#38bdf8"/>
                                <text x="160" y="240" fill="#aaa" font-family="var(--font-mono)" font-size="11" text-anchor="middle">2020 (Base)</text>
                                <text x="145" y="135" fill="#38bdf8" font-family="var(--font-mono)" font-size="11" font-weight="700">₹600 Cr</text>

                                <!-- Single Deflation Flat Line to 2025: 600 Cr (0% growth) -->
                                <line x1="160" y1="140" x2="400" y2="140" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>
                                <circle cx="400" cy="140" r="7" fill="none" stroke="#f59e0b" stroke-width="2"/>
                                <circle cx="400" cy="140" r="2.5" fill="#f59e0b"/>
                                <text x="410" y="145" fill="#f59e0b" font-family="var(--font-mono)" font-size="10">Single Deflation: ₹600 Cr (0.0% Growth)</text>

                                <!-- Double Deflation Upward Line to 2025: 720 Cr (+20% growth) -->
                                <line x1="160" y1="140" x2="400" y2="60" stroke="#10b981" stroke-width="2.5"/>
                                <!-- Red Target Crosshair on True Equilibrium E_true -->
                                <line x1="60" y1="60" x2="400" y2="60" stroke="rgba(255,255,255,0.2)" stroke-dasharray="2,2"/>
                                <line x1="400" y1="60" x2="400" y2="220" stroke="rgba(255,255,255,0.2)" stroke-dasharray="2,2"/>
                                <circle cx="400" cy="60" r="9" fill="none" stroke="#d92534" stroke-width="2"/>
                                <circle cx="400" cy="60" r="3" fill="#d92534"/>
                                <line x1="388" y1="60" x2="412" y2="60" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="400" y1="48" x2="400" y2="72" stroke="#d92534" stroke-width="1.2"/>
                                <text x="412" y="55" fill="#10b981" font-family="var(--font-mono)" font-size="11" font-weight="700">Double Deflation: ₹720 Cr (+20.0%)</text>
                                <text x="400" y="240" fill="#aaa" font-family="var(--font-mono)" font-size="11" text-anchor="middle">2025</text>
                                <text x="25" y="65" fill="#10b981" font-family="var(--font-mono)" font-size="10">₹720</text>
                                <text x="25" y="145" fill="#38bdf8" font-family="var(--font-mono)" font-size="10">₹600</text>

                                <!-- Divergence bracket / label -->
                                <path d="M 405 70 L 415 100 L 405 130" stroke="#d92534" stroke-width="1.5" fill="none"/>
                                <text x="425" y="103" fill="#d92534" font-family="var(--font-mono)" font-size="9">Input Inflation Wedge (P_in=1.50 vs P_out=1.20)</text>
                            </svg>
                        </div>
</div>

                <!-- DEBRIEF Q3 -->
                <div class="solution-box revealed" style="margin-top:24px; border-left:3px solid #fb923c;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <h4 style="color:#ffffff; margin:0;">OFFICIAL SOLUTION: QUESTION 3 (LOANABLE FUNDS, MULTIPLIER & STIMULUS — 8 MARKS)</h4>
                        <span class="badge" style="background:rgba(251,146,60,0.2); color:#fb923c; border:1px solid #fb923c; padding:2px 8px; font-weight:700;">8 / 8 MARKS</span>
                    </div>

                    <!-- Part A: Equilibrium shifts -->
                    <div style="margin-top:14px;">
                        <h5 style="color:var(--accent-silver);">Part a: Initial & New Loanable Funds Equilibrium [4 Marks]</h5>
                        <p><strong>1. Initial Equilibrium:</strong></p>
                        $$S_L = I_L \implies 1000 + 100r = 1600 - 100r \implies 200r = 600 \implies \mathbf{r^* = 3.0\%}$$
                        $$Q^* = 1000 + 100(3.0) = \mathbf{1,300 \text{ billion ostars}}$$

                        <p style="margin-top:12px;"><strong>2. Horizontal Curve Shifts:</strong></p>
                        <ul>
                            <li>Precautionary savings increase by $12\%$ of autonomous saving ($1,000$):
                                $$\Delta S = 0.12 \times 1,000 = +120 \text{ billion ostars}$$
                                $$\mathbf{S'_L = 1120 + 100r}$$
                            </li>
                            <li>Planned investment increases by $8\%$ of autonomous investment ($1,600$):
                                $$\Delta I = 0.08 \times 1,600 = +128 \text{ billion ostars}$$
                                $$\mathbf{I'_L = 1728 - 100r}$$
                            </li>
                        </ul>

                        <p style="margin-top:12px;"><strong>3. New Equilibrium:</strong></p>
                        $$S'_L = I'_L \implies 1120 + 100r = 1728 - 100r \implies 200r = 608 \implies \mathbf{r' = 3.04\%}$$
                        $$Q' = 1120 + 100(3.04) = 1120 + 304 = \mathbf{1,424 \text{ billion ostars}}$$

                        <!-- Graph Blueprint -->
                        <div style="margin-top:14px; background:#07080b; border:1px solid rgba(255,255,255,0.1); padding:16px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); display:block; margin-bottom:8px;">LOANABLE FUNDS EQUILIBRIUM SHIFT DIAGRAM (OSTARA)</span>
                            <svg viewBox="0 0 540 280" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <!-- Grid & Axes -->
                                <line x1="60" y1="240" x2="500" y2="240" stroke="#444" stroke-width="1.5"/>
                                <line x1="60" y1="20" x2="60" y2="240" stroke="#444" stroke-width="1.5"/>
                                <text x="505" y="245" fill="#aaa" font-family="var(--font-mono)" font-size="11">Q (Loanable Funds)</text>
                                <text x="45" y="15" fill="#aaa" font-family="var(--font-mono)" font-size="11">r (%)</text>

                                <!-- Initial Saving S0 and Investment I0 -->
                                <line x1="80" y1="210" x2="420" y2="50" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <text x="425" y="55" fill="#38bdf8" font-family="var(--font-mono)" font-size="11">S₀ (1000 + 100r)</text>

                                <line x1="80" y1="50" x2="420" y2="210" stroke="#fb923c" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <text x="425" y="215" fill="#fb923c" font-family="var(--font-mono)" font-size="11">I₀ (1600 - 100r)</text>

                                <!-- Shifted Saving S1 and Investment I1 -->
                                <line x1="130" y1="210" x2="470" y2="50" stroke="#38bdf8" stroke-width="2.5"/>
                                <text x="475" y="45" fill="#38bdf8" font-family="var(--font-mono)" font-size="11" font-weight="700">S₁ (1120 + 100r)</text>

                                <line x1="140" y1="50" x2="480" y2="210" stroke="#fb923c" stroke-width="2.5"/>
                                <text x="485" y="225" fill="#fb923c" font-family="var(--font-mono)" font-size="11" font-weight="700">I₁ (1728 - 100r)</text>

                                <!-- E0 Equilibrium (r=3%, Q=1300) with Red Crosshair Target -->
                                <line x1="60" y1="130" x2="250" y2="130" stroke="rgba(255,255,255,0.2)" stroke-dasharray="2,2"/>
                                <line x1="250" y1="130" x2="250" y2="240" stroke="rgba(255,255,255,0.2)" stroke-dasharray="2,2"/>
                                <circle cx="250" cy="130" r="8" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="250" cy="130" r="2.5" fill="#d92534"/>
                                <line x1="238" y1="130" x2="262" y2="130" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="250" y1="118" x2="250" y2="142" stroke="#d92534" stroke-width="1.2"/>
                                <text x="236" y="122" fill="#ffffff" font-family="var(--font-mono)" font-size="11" font-weight="700">E₀</text>
                                <text x="238" y="255" fill="#aaa" font-family="var(--font-mono)" font-size="10">1,300</text>
                                <text x="35" y="133" fill="#aaa" font-family="var(--font-mono)" font-size="10">3.0%</text>

                                <!-- E1 Equilibrium (r=3.04%, Q=1424) with Green/Gold Target -->
                                <line x1="60" y1="126" x2="310" y2="126" stroke="rgba(255,255,255,0.2)" stroke-dasharray="2,2"/>
                                <line x1="310" y1="126" x2="310" y2="240" stroke="rgba(255,255,255,0.2)" stroke-dasharray="2,2"/>
                                <circle cx="310" cy="126" r="8" fill="none" stroke="#10b981" stroke-width="2"/>
                                <circle cx="310" cy="126" r="3" fill="#10b981"/>
                                <line x1="298" y1="126" x2="322" y2="126" stroke="#10b981" stroke-width="1.2"/>
                                <line x1="310" y1="114" x2="310" y2="138" stroke="#10b981" stroke-width="1.2"/>
                                <text x="318" y="120" fill="#10b981" font-family="var(--font-mono)" font-size="11" font-weight="700">E₁</text>
                                <text x="298" y="255" fill="#10b981" font-family="var(--font-mono)" font-size="10">1,424</text>
                                <text x="22" y="122" fill="#10b981" font-family="var(--font-mono)" font-size="10">3.04%</text>

                                <!-- Directional arrows -->
                                <path d="M 230 180 L 270 180 M 265 176 L 270 180 L 265 184" stroke="#38bdf8" stroke-width="2" fill="none"/>
                                <path d="M 290 180 L 340 180 M 335 176 L 340 180 L 335 184" stroke="#fb923c" stroke-width="2" fill="none"/>
                            </svg>
                        </div>

                        <p style="margin-top:10px; font-size:0.9rem; line-height:1.7;">
                            <strong>Economic Explanation for Interest Rate Movement:</strong><br>
                            Both curves shifted horizontally to the right. However, the rightward shift in investment demand ($\Delta I = +128\text{ billion}$) exceeded the rightward shift in saving supply ($\Delta S = +120\text{ billion}$). Because the additional demand for funds exceeded the additional supply of loanable funds by $8\text{ billion ostars}$, a mild excess demand emerged at the original $3\%$ rate, bidding the real interest rate upward from $3.00\%$ to $3.04\%$.
                        </p>
                    </div>

                    <!-- Part B: Multiplier and Stimulus -->
                    <div style="margin-top:20px;">
                        <h5 style="color:var(--accent-silver);">Part b: Expenditure Multiplier, Output Adjustment & Government Policy [4 Marks]</h5>
                        <p><strong>1. Expenditure Multiplier (1 Mark):</strong></p>
                        $$k = \frac{1}{1 - MPC} = \frac{1}{1 - 0.75} = \frac{1}{0.25} = \mathbf{4.0}$$

                        <p style="margin-top:12px;"><strong>2. Change in Output Following Private Sector Adjustments (1 Mark):</strong><br>
                        With planned investment expanding by $\Delta I = 128\text{ billion ostars}$:
                        $$\Delta Y_{\text{private}} = k \times \Delta I = 4 \times 128 = \mathbf{+512 \text{ billion ostars}}$$
                        $$\text{New Real GDP} = Y_{\text{initial}} + \Delta Y_{\text{private}} = 8,640 + 512 = \mathbf{9,152 \text{ billion ostars}}$$
                        </p>

                        <p style="margin-top:12px;"><strong>3. Assessment of Government Proposal & Required $\Delta G$ (2 Marks):</strong><br>
                        First determine Potential GDP ($Y_p$):
                        $$Y_{\text{current}} = 0.60 \times Y_p \implies Y_p = \frac{8,640}{0.60} = \mathbf{14,400 \text{ billion ostars}}$$
                        $$\text{Initial Recessionary Output Gap} = Y_p - Y_{\text{current}} = 14,400 - 8,640 = \mathbf{5,760 \text{ billion ostars}}$$
                        After the private-sector expansion of $+512\text{ billion}$, the remaining output gap is:
                        $$\text{Remaining Output Gap} = 14,400 - 9,152 = \mathbf{5,248 \text{ billion ostars}}$$
                        Evaluating the Government's proposal ($\Delta G = 1,600\text{ billion}$):
                        $$\Delta Y_{\text{gov}} = k \times \Delta G = 4 \times 1,600 = \mathbf{6,400 \text{ billion ostars}}$$
                        $$\text{Stimulus Overshoot} = 6,400 - 5,248 = \mathbf{1,152 \text{ billion ostars}}$$
                        The government's proposal is <strong>excessive</strong>; it would overshoot potential GDP, creating severe demand-pull inflation!
                        <div style="background:rgba(251,146,60,0.1); border:1px solid #fb923c; padding:10px 14px; margin-top:8px;">
                            <strong>EXACT REQUIRED INCREASE IN GOVERNMENT EXPENDITURE:</strong>
                            $$\Delta G^* = \frac{\text{Remaining Output Gap}}{k} = \frac{5,248}{4} = \mathbf{1,312 \text{ billion ostars}}$$
                        </div>
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <!-- ==================== SUBTAB 3: COMPREHENSIVE CASE STUDY VAULT ==================== -->
        <div id="ch14-cases" class="subtab-content">
            <div class="intel-card">
                <div class="card-eyebrow">INTEGRATED CASE VAULT // 10 FULL SCENARIOS</div>
                <h3 style="color:var(--accent-silver);">COMPREHENSIVE MACROECONOMIC CASE REPOSITORY</h3>
                <p>Real-world policy dilemmas spanning Chapters 1 through 12. Each case incorporates full economic context, multi-tier questions, 7-step analytical solutions, and policy debriefings.</p>

                <!-- CASE 1 -->
                <div class="mission-card" style="margin-top:20px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <h4 style="color:#ffffff; margin:0;">CASE 1: THE GREAT RE-BASING & DOUBLE DEFLATION CONTROVERSY (INDIA MCA-21)</h4>
                        <span class="badge" style="background:rgba(217,37,52,0.2); color:#ff6b78; border:1px solid #d92534; padding:2px 8px;">CH 2 & 3</span>
                    </div>
                    <p style="margin-top:10px; font-size:0.9rem; line-height:1.7;">
                        <strong>Context:</strong> In 2015, the Central Statistics Office (CSO) of India updated its GDP base year from 2004-05 to 2011-12 and adopted the Ministry of Corporate Affairs (MCA-21) database. Critics observed that between 2014 and 2016, manufacturing GVA showed robust growth exceeding 8% while volume indicators (Index of Industrial Production - IIP, bank credit growth, and freight transport) were stagnant. 
                        Global crude oil and commodity prices had collapsed by over 50%, while wholesale manufacturing output prices declined far less.
                    </p>
                    <div style="background:rgba(255,255,255,0.03); padding:10px; border:1px solid rgba(255,255,255,0.08); font-size:0.88rem;">
                        <strong>Analytical Question:</strong> Explain why single deflation using WPI manufacturing output index artificially inflates real GVA during a commodity price collapse, and demonstrate mathematically how double deflation corrects this distortion.
                    </div>
                    <button class="action-btn" onclick="toggleSolution(this, 'case1-sol', 14)" style="margin-top:12px;">CONFIRM TARGET IDENTIFICATION // REVEAL SOLUTION</button>
                    <div id="case1-sol" class="solution-box" style="display:none; margin-top:14px; border-left:3px solid #38bdf8;">
                        <h5 style="color:#38bdf8;">7-STEP INTEL DEBRIEF // CASE 1</h5>
                        <p style="font-size:0.88rem; line-height:1.7;">
                            <strong>1. Mechanism:</strong> Nominal GVA is Output minus Inputs. When crude oil and raw material prices drop by 50% ($P_{\text{in}} = 50$) while output prices only fall by 5% ($P_{\text{out}} = 95$), operating profit margins expand dramatically in nominal terms.<br>
                            <strong>2. Single Deflation Distortion:</strong> Single deflation divides nominal GVA by $P_{\text{out}}$. Because the nominal profit surge is deflated only by the modest output price drop, it misinterprets a terms-of-trade windfall as massive real physical volume growth!<br>
                            <strong>3. Double Deflation Correction:</strong> Double deflation deflates outputs by $P_{\text{out}}$ and inputs by $P_{\text{in}}$. Since real input consumption did not fall, real physical GVA is accurately measured, aligning with stagnant industrial volume indicators (IIP).
                        </p>
                    
                        <!-- Case 1 Graph -->
                        <div style="margin-top:12px; background:#07080b; border:1px solid rgba(255,255,255,0.08); padding:12px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); display:block; margin-bottom:6px;">MCA-21 COMMODITY PRICE COLLAPSE & GVA DISTORTION</span>
                            <svg viewBox="0 0 500 200" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="50" y1="170" x2="460" y2="170" stroke="#444" stroke-width="1.2"/>
                                <line x1="50" y1="20" x2="50" y2="170" stroke="#444" stroke-width="1.2"/>
                                <text x="465" y="174" fill="#aaa" font-family="var(--font-mono)" font-size="10">Period</text>
                                <text x="20" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">Growth Rate (%)</text>
                                <!-- Single Deflation Artificially High -->
                                <path d="M 60 140 Q 250 30 440 40" stroke="#f59e0b" stroke-width="2" fill="none"/>
                                <text x="445" y="45" fill="#f59e0b" font-family="var(--font-mono)" font-size="9">Single Deflated GVA (+8.5%)</text>
                                <!-- Double Deflation True Physical Volume -->
                                <path d="M 60 140 Q 250 110 440 120" stroke="#10b981" stroke-width="2.2" fill="none"/>
                                <text x="445" y="125" fill="#10b981" font-family="var(--font-mono)" font-size="9">Double Deflated GVA (+3.2%)</text>
                                <!-- Real Volume IIP -->
                                <path d="M 60 140 Q 250 120 440 130" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3" fill="none"/>
                                <text x="445" y="145" fill="#38bdf8" font-family="var(--font-mono)" font-size="9">IIP Industrial Volume (+2.8%)</text>
                                <!-- Target crosshair on True Growth -->
                                <circle cx="340" cy="115" r="7" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="340" cy="115" r="2.5" fill="#d92534"/>
                                <line x1="330" y1="115" x2="350" y2="115" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="340" y1="105" x2="340" y2="125" stroke="#d92534" stroke-width="1.2"/>
                                <text x="330" y="98" fill="#d92534" font-family="var(--font-mono)" font-size="9">True Physical Volume</text>
                            </svg>
                        </div>
                    </div>
                </div>

                <!-- CASE 2 -->
                <div class="mission-card" style="margin-top:20px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <h4 style="color:#ffffff; margin:0;">CASE 2: COVID-19 PRECAUTIONARY SAVING SURGE & THE PARADOX OF THRIFT</h4>
                        <span class="badge" style="background:rgba(217,37,52,0.2); color:#ff6b78; border:1px solid #d92534; padding:2px 8px;">CH 5, 6 & 7</span>
                    </div>
                    <p style="margin-top:10px; font-size:0.9rem; line-height:1.7;">
                        <strong>Context:</strong> During Q1-Q2 2020, lockdowns and acute employment uncertainty caused household personal saving rates in advanced economies to leap from 7% to historic highs of over 30%. While individuals attempted to protect their future solvency, aggregate consumer spending plummeted by 11%, leading to the fastest quarterly GDP contraction on record.
                    </p>
                    <div style="background:rgba(255,255,255,0.03); padding:10px; border:1px solid rgba(255,255,255,0.08); font-size:0.88rem;">
                        <strong>Analytical Question:</strong> Using the Keynesian Cross and loanable funds models, prove why an exogenous increase in the marginal propensity to save ($MPS$) reduces aggregate income without increasing aggregate savings (The Paradox of Thrift).
                    </div>
                    <button class="action-btn" onclick="toggleSolution(this, 'case2-sol', 14)" style="margin-top:12px;">CONFIRM TARGET IDENTIFICATION // REVEAL SOLUTION</button>
                    <div id="case2-sol" class="solution-box" style="display:none; margin-top:14px; border-left:3px solid #38bdf8;">
                        <h5 style="color:#38bdf8;">7-STEP INTEL DEBRIEF // CASE 2</h5>
                        <p style="font-size:0.88rem; line-height:1.7;">
                            <strong>1. Mathematical Proof:</strong> In equilibrium without government: $S(Y) = -c_0 + (1-c_1)Y = I_0$. If autonomous saving increases by $+\Delta S_0$, planned consumption falls by $\Delta C_0 = -\Delta S_0$.<br>
                            <strong>2. Multiplier Cascade:</strong> Equilibrium output falls by $\Delta Y = \frac{-\Delta S_0}{1 - c_1}$.<br>
                            <strong>3. Final Aggregate Savings:</strong> The new aggregate savings is:
                            $$S' = (S_0 + \Delta S_0) + (1-c_1)(Y_0 + \Delta Y) = S_0 + \Delta S_0 + (1-c_1)\left[\frac{-\Delta S_0}{1-c_1}\right] = S_0 + \Delta S_0 - \Delta S_0 = S_0$$
                            Aggregate savings remains completely unchanged, but aggregate national income has collapsed! If investment is induced by output ($I = I_0 + d_1 Y$), aggregate savings actually declines.
                        </p>
                    
                        <!-- Case 2 Graph -->
                        <div style="margin-top:12px; background:#07080b; border:1px solid rgba(255,255,255,0.08); padding:12px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); display:block; margin-bottom:6px;">PARADOX OF THRIFT: PRECAUTIONARY SAVING SURGE & OUTPUT COLLAPSE</span>
                            <svg viewBox="0 0 500 200" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="50" y1="170" x2="460" y2="170" stroke="#444" stroke-width="1.2"/>
                                <line x1="50" y1="20" x2="50" y2="170" stroke="#444" stroke-width="1.2"/>
                                <text x="465" y="174" fill="#aaa" font-family="var(--font-mono)" font-size="10">Y (Output)</text>
                                <text x="25" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">S, I</text>
                                <!-- Investment Line Horizontal -->
                                <line x1="60" y1="110" x2="440" y2="110" stroke="#fb923c" stroke-width="2"/>
                                <text x="445" y="113" fill="#fb923c" font-family="var(--font-mono)" font-size="10">I = I₀</text>
                                <!-- Initial Saving S0 -->
                                <line x1="100" y1="170" x2="380" y2="50" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <text x="385" y="55" fill="#38bdf8" font-family="var(--font-mono)" font-size="9">S₀</text>
                                <!-- Shifted Saving S1 -->
                                <line x1="60" y1="150" x2="340" y2="30" stroke="#38bdf8" stroke-width="2.2"/>
                                <text x="345" y="35" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700">S₁ (Precautionary)</text>
                                <!-- E0 -->
                                <circle cx="240" cy="110" r="6" fill="#38bdf8"/>
                                <text x="235" y="130" fill="#aaa" font-family="var(--font-mono)" font-size="9">E₀ (Y₀)</text>
                                <!-- E1 with Red Crosshair Target -->
                                <circle cx="160" cy="110" r="8" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="160" cy="110" r="2.5" fill="#d92534"/>
                                <line x1="150" y1="110" x2="170" y2="110" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="160" y1="100" x2="160" y2="120" stroke="#d92534" stroke-width="1.2"/>
                                <text x="145" y="130" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">E₁ (Y₁ &lt; Y₀)</text>
                                <!-- Collapse arrow -->
                                <path d="M 230 110 L 175 110" stroke="#d92534" stroke-width="2" marker-end="url(#arrow)" fill="none"/>
                            </svg>
                        </div>
                    </div>
                </div>

                <!-- CASE 3 -->
                <div class="mission-card" style="margin-top:20px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <h4 style="color:#ffffff; margin:0;">CASE 3: THE FISCAL STIMULUS OVERSHOOT & CROWDING OUT (ARRA VS ARP)</h4>
                        <span class="badge" style="background:rgba(217,37,52,0.2); color:#ff6b78; border:1px solid #d92534; padding:2px 8px;">CH 6, 7 & 8</span>
                    </div>
                    <p style="margin-top:10px; font-size:0.9rem; line-height:1.7;">
                        <strong>Context:</strong> Contrast the 2009 American Recovery and Reinvestment Act ($831 billion stimulus during an estimated $2.1 trillion output gap) with the 2021 American Rescue Plan ($1.9 trillion stimulus passed when the remaining output gap was estimated at only $420 billion by the Congressional Budget Office). Larry Summers cautioned that an excessive stimulus relative to the output gap would trigger severe demand-pull inflation and interest rate spikes.
                    </p>
                    <div style="background:rgba(255,255,255,0.03); padding:10px; border:1px solid rgba(255,255,255,0.08); font-size:0.88rem;">
                        <strong>Analytical Question:</strong> Calculate the inflationary gap generated when $\Delta G \times k$ exceeds the potential GDP gap, and trace the resulting crowding out through the loanable funds mechanism.
                    </div>
                    <button class="action-btn" onclick="toggleSolution(this, 'case3-sol', 14)" style="margin-top:12px;">CONFIRM TARGET IDENTIFICATION // REVEAL SOLUTION</button>
                    <div id="case3-sol" class="solution-box" style="display:none; margin-top:14px; border-left:3px solid #38bdf8;">
                        <h5 style="color:#38bdf8;">7-STEP INTEL DEBRIEF // CASE 3</h5>
                        <p style="font-size:0.88rem; line-height:1.7;">
                            <strong>1. Stimulus vs Gap:</strong> With multiplier $k \approx 1.5$, a $\$1.9\text{T}$ stimulus creates $\Delta Y = 1.9 \times 1.5 = \$2.85\text{T}$ of aggregate demand against a gap of only $\$420\text{B}$.<br>
                            <strong>2. Inflationary Gap:</strong> Generates an inflationary gap of $\$2.85\text{T} - \$0.42\text{T} = \$2.43\text{T}$. In AD-AS, AD shifts far past LRAS, bidding up wages and input costs until SRAS shifts leftward.<br>
                            <strong>3. Loanable Funds Deficit:</strong> Treasury bond issuance of $\$1.9\text{T}$ absorbs national savings, shifting the demand for loanable funds rightward and driving real borrowing costs up, reducing private capital formation (Financial Crowding Out).
                        </p>
                    
                        <!-- Case 3 Graph -->
                        <div style="margin-top:12px; background:#07080b; border:1px solid rgba(255,255,255,0.08); padding:12px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); display:block; margin-bottom:6px;">STIMULUS OVERSHOOT & INFLATIONARY GAP</span>
                            <svg viewBox="0 0 500 200" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="50" y1="170" x2="460" y2="170" stroke="#444" stroke-width="1.2"/>
                                <line x1="50" y1="20" x2="50" y2="170" stroke="#444" stroke-width="1.2"/>
                                <text x="465" y="174" fill="#aaa" font-family="var(--font-mono)" font-size="10">Y (Real Output)</text>
                                <text x="30" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">Price P</text>
                                <!-- LRAS -->
                                <line x1="250" y1="20" x2="250" y2="170" stroke="#eab308" stroke-width="2"/>
                                <text x="255" y="35" fill="#eab308" font-family="var(--font-mono)" font-size="9">LRAS (Y*)</text>
                                <!-- SRAS -->
                                <line x1="100" y1="160" x2="400" y2="50" stroke="#fb923c" stroke-width="2"/>
                                <text x="405" y="55" fill="#fb923c" font-family="var(--font-mono)" font-size="9">SRAS</text>
                                <!-- AD 0 -->
                                <line x1="100" y1="60" x2="360" y2="160" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <!-- AD 1 Overshoot -->
                                <line x1="180" y1="40" x2="440" y2="150" stroke="#d92534" stroke-width="2.2"/>
                                <text x="445" y="150" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">AD₁ (Stimulus)</text>
                                <!-- Target Crosshair on Inflationary Equilibrium -->
                                <circle cx="310" cy="85" r="8" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="310" cy="85" r="2.5" fill="#d92534"/>
                                <line x1="300" y1="85" x2="320" y2="85" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="310" y1="75" x2="310" y2="95" stroke="#d92534" stroke-width="1.2"/>
                                <text x="315" y="75" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">E₁ (Y &gt; Y* Gap)</text>
                            </svg>
                        </div>
                    </div>
                </div>

                <!-- CASE 4 -->
                <div class="mission-card" style="margin-top:20px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <h4 style="color:#ffffff; margin:0;">CASE 4: THE 1970S OPEC OIL EMBARGO & THE STAGFLATION TRAP</h4>
                        <span class="badge" style="background:rgba(217,37,52,0.2); color:#ff6b78; border:1px solid #d92534; padding:2px 8px;">CH 9 & 11</span>
                    </div>
                    <p style="margin-top:10px; font-size:0.9rem; line-height:1.7;">
                        <strong>Context:</strong> In October 1973, OPEC imposed an oil embargo following the Yom Kippur War, quadrupling world crude oil prices from $3 to $12 per barrel. A second shock in 1979 pushed prices to $36. The industrialized world suffered simultaneous economic stagnation ($Y \downarrow, u \uparrow$) and runaway inflation ($P \uparrow$), shattering traditional Keynesian Phillips Curve assumptions.
                    </p>
                    <div style="background:rgba(255,255,255,0.03); padding:10px; border:1px solid rgba(255,255,255,0.08); font-size:0.88rem;">
                        <strong>Analytical Question:</strong> Illustrate in the AD-AS framework why an adverse supply shock creates a policy dilemma where monetary accommodation cures unemployment only by worsening inflation, while monetary tightening cures inflation only by deepening recession.
                    </div>
                    <button class="action-btn" onclick="toggleSolution(this, 'case4-sol', 14)" style="margin-top:12px;">CONFIRM TARGET IDENTIFICATION // REVEAL SOLUTION</button>
                    <div id="case4-sol" class="solution-box" style="display:none; margin-top:14px; border-left:3px solid #38bdf8;">
                        <h5 style="color:#38bdf8;">7-STEP INTEL DEBRIEF // CASE 4</h5>
                        <p style="font-size:0.88rem; line-height:1.7;">
                            <strong>1. AD-AS Dynamics:</strong> The quadrupling of energy costs shifts SRAS sharply upward/leftward ($\text{SRAS}_0 \to \text{SRAS}_1$). Output contracts below potential ($Y_1 < Y_p$) while price level spikes ($P_1 > P_0$).<br>
                            <strong>2. Policy Dilemma:</strong><br>
                            - <em>Accommodating Policy ($\Delta M > 0$):</em> Shifts AD rightward to restore full employment ($Y \to Y_p$), but drives prices up permanently to $P_2 \gg P_1$, validating inflation expectations.<br>
                            - <em>Anti-Inflation Policy ($\Delta M < 0$):</em> Shifts AD leftward to suppress price pressure ($P \to P_0$), but plunges the economy into a deep recession ($Y \downarrow\downarrow$).
                        </p>
                    
                        <!-- Case 4 Graph -->
                        <div style="margin-top:12px; background:#07080b; border:1px solid rgba(255,255,255,0.08); padding:12px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); display:block; margin-bottom:6px;">1973 OPEC OIL EMBARGO: COST-PUSH STAGFLATION</span>
                            <svg viewBox="0 0 500 200" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="50" y1="170" x2="460" y2="170" stroke="#444" stroke-width="1.2"/>
                                <line x1="50" y1="20" x2="50" y2="170" stroke="#444" stroke-width="1.2"/>
                                <text x="465" y="174" fill="#aaa" font-family="var(--font-mono)" font-size="10">Y (Output)</text>
                                <text x="30" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">Price P</text>
                                <!-- AD -->
                                <line x1="100" y1="50" x2="400" y2="160" stroke="#38bdf8" stroke-width="2"/>
                                <text x="405" y="160" fill="#38bdf8" font-family="var(--font-mono)" font-size="9">AD</text>
                                <!-- SRAS 0 -->
                                <line x1="120" y1="160" x2="420" y2="60" stroke="#fb923c" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <!-- SRAS 1 Shock -->
                                <line x1="70" y1="130" x2="370" y2="30" stroke="#d92534" stroke-width="2.5"/>
                                <text x="375" y="35" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">SRAS₁ (Oil Shock)</text>
                                <!-- E0 Equilibrium -->
                                <circle cx="260" cy="110" r="5" fill="#38bdf8"/>
                                <text x="268" y="120" fill="#aaa" font-family="var(--font-mono)" font-size="9">E₀ (P₀, Y*)</text>
                                <!-- E1 Stagflation with Target Crosshair -->
                                <circle cx="200" cy="85" r="8" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="200" cy="85" r="2.5" fill="#d92534"/>
                                <line x1="190" y1="85" x2="210" y2="85" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="200" y1="75" x2="200" y2="95" stroke="#d92534" stroke-width="1.2"/>
                                <text x="140" y="80" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">E₁ (P↑, Y↓)</text>
                            </svg>
                        </div>
                    </div>
                </div>

                <!-- CASE 5 -->
                <div class="mission-card" style="margin-top:20px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <h4 style="color:#ffffff; margin:0;">CASE 5: JAPAN'S LOST DECADES & THE LIQUIDITY TRAP</h4>
                        <span class="badge" style="background:rgba(217,37,52,0.2); color:#ff6b78; border:1px solid #d92534; padding:2px 8px;">CH 8 & 10</span>
                    </div>
                    <p style="margin-top:10px; font-size:0.9rem; line-height:1.7;">
                        <strong>Context:</strong> Following the collapse of Japan's asset price bubble in 1991, the Bank of Japan cut its uncollateralized call rate to 0.5% in 1995 and 0.0% in 1999 (Zero Lower Bound). Despite injecting massive base money, commercial bank lending did not expand, corporate investment stagnated, and the economy remained trapped in deflationary pressure for over two decades.
                    </p>
                    <div style="background:rgba(255,255,255,0.03); padding:10px; border:1px solid rgba(255,255,255,0.08); font-size:0.88rem;">
                        <strong>Analytical Question:</strong> Model Japan's liquidity trap in the IS-LM framework. Explain why the LM curve becomes horizontal at zero nominal interest rates, rendering standard monetary policy completely powerless, while fiscal policy operates at maximum multiplier potency.
                    </div>
                    <button class="action-btn" onclick="toggleSolution(this, 'case5-sol', 14)" style="margin-top:12px;">CONFIRM TARGET IDENTIFICATION // REVEAL SOLUTION</button>
                    <div id="case5-sol" class="solution-box" style="display:none; margin-top:14px; border-left:3px solid #38bdf8;">
                        <h5 style="color:#38bdf8;">7-STEP INTEL DEBRIEF // CASE 5</h5>
                        <p style="font-size:0.88rem; line-height:1.7;">
                            <strong>1. Zero Lower Bound:</strong> When $i \to 0$, cash and short-term government bonds become perfect substitutes. The demand for money becomes infinitely interest-elastic ($h \to \infty$).<br>
                            <strong>2. Flat LM Curve:</strong> In IS-LM, the LM curve becomes completely horizontal at $i = 0$. Further injections of base money ($\Delta M > 0$) simply shift the flat section of LM without changing the intersection with IS.<br>
                            <strong>3. Maximum Fiscal Multiplier:</strong> In a liquidity trap, fiscal expansion ($\Delta G > 0$) shifts the IS curve rightward along the flat LM curve. Because interest rates do not rise ($\Delta r = 0$), there is <strong>zero crowding out</strong> of private investment! The fiscal multiplier operates at its pure Keynesian maximum: $\Delta Y = \frac{\Delta G}{1 - MPC}$.
                        </p>
                    
                        <!-- Case 5 Graph -->
                        <div style="margin-top:12px; background:#07080b; border:1px solid rgba(255,255,255,0.08); padding:12px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); display:block; margin-bottom:6px;">BANK OF JAPAN: LIQUIDITY TRAP & ZERO LOWER BOUND</span>
                            <svg viewBox="0 0 500 200" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="50" y1="170" x2="460" y2="170" stroke="#444" stroke-width="1.2"/>
                                <line x1="50" y1="20" x2="50" y2="170" stroke="#444" stroke-width="1.2"/>
                                <text x="465" y="174" fill="#aaa" font-family="var(--font-mono)" font-size="10">Y (Income)</text>
                                <text x="30" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">r (%)</text>
                                <!-- Horizontal LM at ZLB -->
                                <line x1="50" y1="165" x2="350" y2="165" stroke="#10b981" stroke-width="3"/>
                                <line x1="350" y1="165" x2="440" y2="50" stroke="#10b981" stroke-width="2.5"/>
                                <text x="360" y="155" fill="#10b981" font-family="var(--font-mono)" font-size="9" font-weight="700">LM (Horizontal at ZLB)</text>
                                <!-- IS 0 -->
                                <line x1="80" y1="50" x2="240" y2="170" stroke="#fb923c" stroke-width="2"/>
                                <text x="245" y="165" fill="#fb923c" font-family="var(--font-mono)" font-size="9">IS₀</text>
                                <!-- IS 1 Fiscal Stimulus -->
                                <line x1="160" y1="50" x2="320" y2="170" stroke="#38bdf8" stroke-width="2.2"/>
                                <text x="325" y="165" fill="#38bdf8" font-family="var(--font-mono)" font-size="9" font-weight="700">IS₁ (Fiscal)</text>
                                <!-- Target Crosshair on Stimulus Point -->
                                <circle cx="310" cy="165" r="8" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="310" cy="165" r="2.5" fill="#d92534"/>
                                <line x1="300" y1="165" x2="320" y2="165" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="310" y1="155" x2="310" y2="175" stroke="#d92534" stroke-width="1.2"/>
                                <text x="315" y="145" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">Full Multiplier (Zero Crowding Out)</text>
                            </svg>
                        </div>
                    </div>
                </div>

                <!-- CASE 6 -->
                <div class="mission-card" style="margin-top:20px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <h4 style="color:#ffffff; margin:0;">CASE 6: THE VOLCKER DISINFLATION & SACRIFICE RATIO (1979-1982)</h4>
                        <span class="badge" style="background:rgba(217,37,52,0.2); color:#ff6b78; border:1px solid #d92534; padding:2px 8px;">CH 11</span>
                    </div>
                    <p style="margin-top:10px; font-size:0.9rem; line-height:1.7;">
                        <strong>Context:</strong> Federal Reserve Chairman Paul Volcker took office in August 1979 with US inflation running at 13.3%. Volcker targeted bank reserves, driving the federal funds rate above 20%. Inflation plummeted to 3.2% by 1983, but at the cost of the deepest recession since the 1930s, with unemployment peaking at 10.8%.
                    </p>
                    <div style="background:rgba(255,255,255,0.03); padding:10px; border:1px solid rgba(255,255,255,0.08); font-size:0.88rem;">
                        <strong>Analytical Question:</strong> Define the Sacrifice Ratio. Calculate the cumulative percentage of one year's GDP sacrificed to reduce inflation by 10 percentage points under Okun's Law, and compare the adaptive expectations versus rational expectations predictions.
                    </div>
                    <button class="action-btn" onclick="toggleSolution(this, 'case6-sol', 14)" style="margin-top:12px;">CONFIRM TARGET IDENTIFICATION // REVEAL SOLUTION</button>
                    <div id="case6-sol" class="solution-box" style="display:none; margin-top:14px; border-left:3px solid #38bdf8;">
                        <h5 style="color:#38bdf8;">7-STEP INTEL DEBRIEF // CASE 6</h5>
                        <p style="font-size:0.88rem; line-height:1.7;">
                            <strong>1. Sacrifice Ratio Definition:</strong> The cumulative percentage of one year's real GDP that must be forgone to reduce the inflation rate by 1 percentage point.<br>
                            <strong>2. Historical Calculation:</strong> Under Volcker, inflation dropped by $10\%$. Cumulative excess cyclical unemployment over 1980–1983 was approximately $10$ percentage-point years. By Okun's Law (each $1\%$ excess unemployment $= 2\%$ lost GDP), total output loss was $20\%$ of GDP. The sacrifice ratio was:
                            $$\text{Sacrifice Ratio} = \frac{20\% \text{ Lost GDP}}{10\% \text{ Inflation Reduction}} = \mathbf{2.0}$$
                            <strong>3. Lucas Critique:</strong> Thomas Sargent argued that if the central bank commitment is fully credible and announced in advance, rational economic agents immediately adjust $\pi^e \to \pi_{\text{new}}$, allowing disinflation with a near-zero sacrifice ratio. Because Volcker had to establish credibility through painful policy, expectations adjusted adaptively with high output loss.
                        </p>
                    
                        <!-- Case 6 Graph -->
                        <div style="margin-top:12px; background:#07080b; border:1px solid rgba(255,255,255,0.08); padding:12px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); display:block; margin-bottom:6px;">VOLCKER DISINFLATION: PHILLIPS CURVE SACRIFICE TRAJECTORY</span>
                            <svg viewBox="0 0 500 200" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="50" y1="170" x2="460" y2="170" stroke="#444" stroke-width="1.2"/>
                                <line x1="50" y1="20" x2="50" y2="170" stroke="#444" stroke-width="1.2"/>
                                <text x="465" y="174" fill="#aaa" font-family="var(--font-mono)" font-size="10">u (%)</text>
                                <text x="30" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">π (%)</text>
                                <!-- LRPC -->
                                <line x1="200" y1="20" x2="200" y2="170" stroke="#eab308" stroke-width="2"/>
                                <text x="205" y="35" fill="#eab308" font-family="var(--font-mono)" font-size="9">LRPC (u_n=6%)</text>
                                <!-- SRPC High -->
                                <line x1="100" y1="40" x2="400" y2="140" stroke="#d92534" stroke-width="2"/>
                                <text x="405" y="140" fill="#d92534" font-family="var(--font-mono)" font-size="9">SRPC (10% Exp)</text>
                                <!-- SRPC Low -->
                                <line x1="100" y1="90" x2="400" y2="170" stroke="#10b981" stroke-width="2"/>
                                <text x="405" y="170" fill="#10b981" font-family="var(--font-mono)" font-size="9">SRPC (3% Exp)</text>
                                <!-- Crosshair on Volcker Recession Point -->
                                <circle cx="320" cy="115" r="8" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="320" cy="115" r="2.5" fill="#d92534"/>
                                <line x1="310" y1="115" x2="330" y2="115" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="320" y1="105" x2="320" y2="125" stroke="#d92534" stroke-width="1.2"/>
                                <text x="325" y="105" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">1982 Sacrifice (u=10.8%)</text>
                            </svg>
                        </div>
                    </div>
                </div>

                <!-- CASE 7 -->
                <div class="mission-card" style="margin-top:20px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <h4 style="color:#ffffff; margin:0;">CASE 7: THE CLINTON-GREENSPAN POLICY MIX (1990S BOOM)</h4>
                        <span class="badge" style="background:rgba(217,37,52,0.2); color:#ff6b78; border:1px solid #d92534; padding:2px 8px;">CH 8 & 10</span>
                    </div>
                    <p style="margin-top:10px; font-size:0.9rem; line-height:1.7;">
                        <strong>Context:</strong> In 1993, President Clinton passed the Omnibus Budget Reconciliation Act, cutting government deficits through spending caps and tax increases ($\Delta G < 0, \Delta T > 0$). Federal Reserve Chairman Alan Greenspan accommodated this fiscal consolidation by easing monetary policy ($\Delta M > 0$). Instead of plunging into recession, the US experienced its longest peacetime economic expansion in history with surging private investment and federal budget surpluses.
                    </p>
                    <div style="background:rgba(255,255,255,0.03); padding:10px; border:1px solid rgba(255,255,255,0.08); font-size:0.88rem;">
                        <strong>Analytical Question:</strong> Trace in the IS-LM diagram how fiscal contraction paired with monetary expansion can maintain full employment output while drastically lowering real interest rates and altering the composition of GDP from government consumption to private capital formation.
                    </div>
                    <button class="action-btn" onclick="toggleSolution(this, 'case7-sol', 14)" style="margin-top:12px;">CONFIRM TARGET IDENTIFICATION // REVEAL SOLUTION</button>
                    <div id="case7-sol" class="solution-box" style="display:none; margin-top:14px; border-left:3px solid #38bdf8;">
                        <h5 style="color:#38bdf8;">7-STEP INTEL DEBRIEF // CASE 7</h5>
                        <p style="font-size:0.88rem; line-height:1.7;">
                            <strong>1. IS Shift:</strong> Deficit reduction ($\Delta G < 0, \Delta T > 0$) shifts IS leftward from $\text{IS}_0$ to $\text{IS}_1$. Alone, this would reduce output and lower interest rates.<br>
                            <strong>2. LM Shift:</strong> Greenspan's Fed accommodates by expanding real money balances ($\Delta M > 0$), shifting the LM curve rightward from $\text{LM}_0$ to $\text{LM}_1$.<br>
                            <strong>3. Final Composition Effect:</strong> The joint policy restores equilibrium output back to full potential ($Y_1 = Y_p$), but real interest rates drop dramatically ($r_1 \ll r_0$). Lower borrowing costs unleash a massive boom in corporate private investment ($I \uparrow\uparrow$), transforming GDP composition from public consumption to productive private technology capital.
                        </p>
                    
                        <!-- Case 7 Graph -->
                        <div style="margin-top:12px; background:#07080b; border:1px solid rgba(255,255,255,0.08); padding:12px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); display:block; margin-bottom:6px;">CLINTON-GREENSPAN MIX (1993): FISCAL CONTRACTION + MONETARY EASING</span>
                            <svg viewBox="0 0 500 200" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="50" y1="170" x2="460" y2="170" stroke="#444" stroke-width="1.2"/>
                                <line x1="50" y1="20" x2="50" y2="170" stroke="#444" stroke-width="1.2"/>
                                <text x="465" y="174" fill="#aaa" font-family="var(--font-mono)" font-size="10">Y (GDP)</text>
                                <text x="30" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">r (%)</text>
                                <!-- IS 0 to IS 1 (Inward) -->
                                <line x1="140" y1="40" x2="400" y2="160" stroke="#fb923c" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <line x1="80" y1="40" x2="340" y2="160" stroke="#fb923c" stroke-width="2.2"/>
                                <text x="345" y="160" fill="#fb923c" font-family="var(--font-mono)" font-size="9">IS₁ (Deficit Cut)</text>
                                <!-- LM 0 to LM 1 (Outward) -->
                                <line x1="80" y1="150" x2="340" y2="50" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <line x1="140" y1="160" x2="400" y2="60" stroke="#38bdf8" stroke-width="2.2"/>
                                <text x="405" y="65" fill="#38bdf8" font-family="var(--font-mono)" font-size="9">LM₁ (Fed Easing)</text>
                                <!-- Target Crosshair on Final E1 -->
                                <circle cx="260" cy="120" r="8" fill="none" stroke="#10b981" stroke-width="2"/>
                                <circle cx="260" cy="120" r="2.5" fill="#10b981"/>
                                <line x1="250" y1="120" x2="270" y2="120" stroke="#10b981" stroke-width="1.2"/>
                                <line x1="260" y1="110" x2="260" y2="130" stroke="#10b981" stroke-width="1.2"/>
                                <text x="268" y="115" fill="#10b981" font-family="var(--font-mono)" font-size="9" font-weight="700">E₁: Low r, Stable Y</text>
                            </svg>
                        </div>
                    </div>
                </div>

                <!-- CASE 8 -->
                <div class="mission-card" style="margin-top:20px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <h4 style="color:#ffffff; margin:0;">CASE 8: DEMONETISATION & THE MONEY MULTIPLIER CRUNCH (INDIA 2016)</h4>
                        <span class="badge" style="background:rgba(217,37,52,0.2); color:#ff6b78; border:1px solid #d92534; padding:2px 8px;">CH 4 & 8</span>
                    </div>
                    <p style="margin-top:10px; font-size:0.9rem; line-height:1.7;">
                        <strong>Context:</strong> On 8 November 2016, India invalidated all ₹500 and ₹1,000 currency notes, which constituted 86.4% of total currency in circulation. Because citizens deposited cash into bank accounts under withdrawal limits, currency with the public ($C$) contracted precipitously while bank deposits ($D$) surged by over ₹15 lakh crore, temporarily lowering the currency-deposit ratio ($cr$) while informal sector transactions collapsed.
                    </p>
                    <div style="background:rgba(255,255,255,0.03); padding:10px; border:1px solid rgba(255,255,255,0.08); font-size:0.88rem;">
                        <strong>Analytical Question:</strong> Using the money multiplier model $M = \frac{1 + cr}{cr + rr} \times H$, explain the immediate mechanical paradox where broad money ($M_3$) multiplier technically rose, while transaction velocity ($V$) in the equation of exchange $M V = P Y$ plummeted, resulting in a temporary real GDP growth drag.
                    </div>
                    <button class="action-btn" onclick="toggleSolution(this, 'case8-sol', 14)" style="margin-top:12px;">CONFIRM TARGET IDENTIFICATION // REVEAL SOLUTION</button>
                    <div id="case8-sol" class="solution-box" style="display:none; margin-top:14px; border-left:3px solid #38bdf8;">
                        <h5 style="color:#38bdf8;">7-STEP INTEL DEBRIEF // CASE 8</h5>
                        <p style="font-size:0.88rem; line-height:1.7;">
                            <strong>1. Money Multiplier Formula:</strong> With $cr = C/D$ falling dramatically as cash entered bank accounts, the theoretical broad money multiplier $m = \frac{1+cr}{cr+rr}$ mathematically increased because $rr < 1$.<br>
                            <strong>2. Commercial Bank Excess Reserves:</strong> However, banks were unable to lend these funds due to high borrower uncertainty and RBI's temporary 100% Incremental CRR on new deposits, neutralizing the credit expansion.<br>
                            <strong>3. Velocity Collapse:</strong> In the cash-dependent informal sector (agriculture, small retail, construction), transaction velocity $V$ collapsed. From $PY = MV$, even though $M_3$ remained stable, the plunge in $V$ forced nominal and real economic activity $Y$ downward for two quarters.
                        </p>
                    
                        <!-- Case 8 Graph -->
                        <div style="margin-top:12px; background:#07080b; border:1px solid rgba(255,255,255,0.08); padding:12px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); display:block; margin-bottom:6px;">DEMONETISATION SHOCK: TRANSACTION VELOCITY & CASH FREEZE</span>
                            <svg viewBox="0 0 500 200" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="50" y1="170" x2="460" y2="170" stroke="#444" stroke-width="1.2"/>
                                <line x1="50" y1="20" x2="50" y2="170" stroke="#444" stroke-width="1.2"/>
                                <text x="465" y="174" fill="#aaa" font-family="var(--font-mono)" font-size="10">Y (Output)</text>
                                <text x="30" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">r (%)</text>
                                <!-- LM Shock Inward -->
                                <line x1="160" y1="160" x2="400" y2="40" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <line x1="90" y1="160" x2="330" y2="40" stroke="#d92534" stroke-width="2.5"/>
                                <text x="220" y="45" fill="#d92534" font-family="var(--font-mono)" font-size="9">LM_crunch (Cash Frozen)</text>
                                <!-- IS Curve -->
                                <line x1="100" y1="40" x2="380" y2="160" stroke="#fb923c" stroke-width="2"/>
                                <!-- Red Target Crosshair on Shock -->
                                <circle cx="210" cy="85" r="8" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="210" cy="85" r="2.5" fill="#d92534"/>
                                <line x1="200" y1="85" x2="220" y2="85" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="210" y1="75" x2="210" y2="95" stroke="#d92534" stroke-width="1.2"/>
                                <text x="145" y="80" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">Informal Contraction</text>
                            </svg>
                        </div>
                    </div>
                </div>

                <!-- CASE 9 -->
                <div class="mission-card" style="margin-top:20px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <h4 style="color:#ffffff; margin:0;">CASE 9: THE KUMBH MELA TEMPORARY ECONOMIC MULTIPLIER</h4>
                        <span class="badge" style="background:rgba(217,37,52,0.2); color:#ff6b78; border:1px solid #d92534; padding:2px 8px;">CH 2 & 7</span>
                    </div>
                    <p style="margin-top:10px; font-size:0.9rem; line-height:1.7;">
                        <strong>Context:</strong> The 2019 Prayagraj Ardh Kumbh Mela attracted an estimated 240 million pilgrim visits over 50 days. The state and central governments invested ₹4,300 crore in infrastructure (temporary roads, pontoon bridges, sanitation, railway expansion). Industry bodies estimated that total business generated across hospitality, transport, religious artifacts, and local trade exceeded ₹1.2 lakh crore.
                    </p>
                    <div style="background:rgba(255,255,255,0.03); padding:10px; border:1px solid rgba(255,255,255,0.08); font-size:0.88rem;">
                        <strong>Analytical Question:</strong> Deconstruct the Kumbh Mela multiplier into autonomous infrastructure expenditure, pilgrim consumption injection, and secondary velocity rounds. How does national income accounting distinguish between permanent capacity enhancement versus temporary transitory income velocity?
                    </div>
                    <button class="action-btn" onclick="toggleSolution(this, 'case9-sol', 14)" style="margin-top:12px;">CONFIRM TARGET IDENTIFICATION // REVEAL SOLUTION</button>
                    <div id="case9-sol" class="solution-box" style="display:none; margin-top:14px; border-left:3px solid #38bdf8;">
                        <h5 style="color:#38bdf8;">7-STEP INTEL DEBRIEF // CASE 9</h5>
                        <p style="font-size:0.88rem; line-height:1.7;">
                            <strong>1. Public Infrastructure ($\Delta G$):</strong> Permanent assets (bridge widening, airport terminal, railway electrification) enter Gross Fixed Capital Formation ($I$), expanding the economy's long-run productive capacity ($LRAS$).<br>
                            <strong>2. Autonomous Consumption Injection ($\Delta C_0$):</strong> Pilgrim travel and lodging represents an exogenous consumption injection funded by past savings, with high local marginal propensity to consume ($MPC_{\text{local}} \approx 0.8$).<br>
                            <strong>3. Regional vs National Multiplier:</strong> In national accounting, temporary events create a localized velocity spike ($V \uparrow$) and temporary regional GVA bump. However, because much of pilgrim expenditure represents domestic expenditure diversion (postponed consumption elsewhere in India), the net national GDP gain is smaller than the gross regional transaction turnover.
                        </p>
                    
                        <!-- Case 9 Graph -->
                        <div style="margin-top:12px; background:#07080b; border:1px solid rgba(255,255,255,0.08); padding:12px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); display:block; margin-bottom:6px;">KUMBH MELA: AUTONOMOUS CONSUMPTION JUMP IN KEYNESIAN CROSS</span>
                            <svg viewBox="0 0 500 200" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="50" y1="170" x2="460" y2="170" stroke="#444" stroke-width="1.2"/>
                                <line x1="50" y1="20" x2="50" y2="170" stroke="#444" stroke-width="1.2"/>
                                <text x="465" y="174" fill="#aaa" font-family="var(--font-mono)" font-size="10">Y (Regional Output)</text>
                                <text x="25" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">AE</text>
                                <!-- 45 Degree Line -->
                                <line x1="50" y1="170" x2="430" y2="30" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3"/>
                                <text x="435" y="35" fill="#64748b" font-family="var(--font-mono)" font-size="9">Y = AE (45°)</text>
                                <!-- AE 0 -->
                                <line x1="50" y1="120" x2="420" y2="60" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="3,3"/>
                                <!-- AE 1 Kumbh Surge -->
                                <line x1="50" y1="90" x2="420" y2="30" stroke="#10b981" stroke-width="2.5"/>
                                <text x="425" y="30" fill="#10b981" font-family="var(--font-mono)" font-size="9" font-weight="700">AE₁ (ΔC₀ Surge)</text>
                                <!-- Target Crosshair on Expanded Regional Equilibrium -->
                                <circle cx="310" cy="72" r="8" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="310" cy="72" r="2.5" fill="#d92534"/>
                                <line x1="300" y1="72" x2="320" y2="72" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="310" y1="62" x2="310" y2="82" stroke="#d92534" stroke-width="1.2"/>
                                <text x="315" y="65" fill="#10b981" font-family="var(--font-mono)" font-size="9" font-weight="700">ΔY = k·ΔC₀</text>
                            </svg>
                        </div>
                    </div>
                </div>

                <!-- CASE 10 -->
                <div class="mission-card" style="margin-top:20px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <h4 style="color:#ffffff; margin:0;">CASE 10: WEIMAR HYPERINFLATION (1923) & THE FISHER EFFECT</h4>
                        <span class="badge" style="background:rgba(217,37,52,0.2); color:#ff6b78; border:1px solid #d92534; padding:2px 8px;">CH 3 & 4</span>
                    </div>
                    <p style="margin-top:10px; font-size:0.9rem; line-height:1.7;">
                        <strong>Context:</strong> In 1922–1923, the German Reichsbank monetized massive war reparations and government deficits by operating money printing presses 24 hours a day. Monthly inflation peaked at 29,500% in October 1923. Workers were paid twice daily in wheelbarrows of cash that had to be spent immediately before prices doubled again. The real value of the currency collapsed to zero.
                    </p>
                    <div style="background:rgba(255,255,255,0.03); padding:10px; border:1px solid rgba(255,255,255,0.08); font-size:0.88rem;">
                        <strong>Analytical Question:</strong> Using the Fisher Equation $i = r + \pi^e$ and the real money demand equation $(M/P)^d = L(Y, i)$, explain why hyperinflation leads to a collapse in real money balances and shoe-leather costs reaching catastrophic extremes.
                    </div>
                    <button class="action-btn" onclick="toggleSolution(this, 'case10-sol', 14)" style="margin-top:12px;">CONFIRM TARGET IDENTIFICATION // REVEAL SOLUTION</button>
                    <div id="case10-sol" class="solution-box" style="display:none; margin-top:14px; border-left:3px solid #38bdf8;">
                        <h5 style="color:#38bdf8;">7-STEP INTEL DEBRIEF // CASE 10</h5>
                        <p style="font-size:0.88rem; line-height:1.7;">
                            <strong>1. Fisher Equation:</strong> Nominal interest rate $i = r + \pi^e$. When inflation expectations $\pi^e$ surge to thousands of percent per month, the opportunity cost of holding non-interest-bearing cash becomes astronomical.<br>
                            <strong>2. Real Money Demand Collapse:</strong> As $i \to \infty$, demand for real balances $(M/P)^d = L(Y, i) \to 0$. Everyone attempts to rid themselves of cash immediately.<br>
                            <strong>3. Velocity Explosion:</strong> The rate at which money changes hands ($V$) explodes toward infinity. Prices ($P$) rise much faster than the money supply ($M$) itself because:
                            $$P = \frac{M \times V}{Y}$$
                            Even though printing presses operated continuously, the real purchasing power of the money stock ($M/P$) was lower in late 1923 than before the war!
                        </p>
                    
                        <!-- Case 10 Graph -->
                        <div style="margin-top:12px; background:#07080b; border:1px solid rgba(255,255,255,0.08); padding:12px; text-align:center;">
                            <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); display:block; margin-bottom:6px;">WEIMAR HYPERINFLATION & THE FISHER EFFECT SPIRAL</span>
                            <svg viewBox="0 0 500 200" style="max-width:100%; height:auto;" xmlns="http://www.w3.org/2000/svg">
                                <line x1="50" y1="170" x2="460" y2="170" stroke="#444" stroke-width="1.2"/>
                                <line x1="50" y1="20" x2="50" y2="170" stroke="#444" stroke-width="1.2"/>
                                <text x="465" y="174" fill="#aaa" font-family="var(--font-mono)" font-size="10">Time (Months 1923)</text>
                                <text x="20" y="18" fill="#aaa" font-family="var(--font-mono)" font-size="10">i, π (%)</text>
                                <!-- Exponential nominal rate curve -->
                                <path d="M 60 160 Q 280 150 420 30" stroke="#d92534" stroke-width="2.8" fill="none"/>
                                <text x="425" y="30" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">Nominal Rate i = r + πᵉ</text>
                                <!-- Real Money Demand Collapsing -->
                                <path d="M 60 40 Q 280 140 420 165" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3" fill="none"/>
                                <text x="425" y="165" fill="#38bdf8" font-family="var(--font-mono)" font-size="9">Real Balances (M/P)</text>
                                <!-- Target crosshair on hyperinflation explosion -->
                                <circle cx="380" cy="55" r="8" fill="none" stroke="#d92534" stroke-width="1.8"/>
                                <circle cx="380" cy="55" r="2.5" fill="#d92534"/>
                                <line x1="370" y1="55" x2="390" y2="55" stroke="#d92534" stroke-width="1.2"/>
                                <line x1="380" y1="45" x2="380" y2="65" stroke="#d92534" stroke-width="1.2"/>
                                <text x="310" y="45" fill="#d92534" font-family="var(--font-mono)" font-size="9" font-weight="700">Velocity V → ∞</text>
                            </svg>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>
</section>
'''
