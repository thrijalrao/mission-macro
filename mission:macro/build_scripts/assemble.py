"""
PROJECT 007: THE MACROECONOMICS INTELLIGENCE FILE
Main Assembly Script: Assembles the entire single-file standalone web application index.html
Re-architected strictly in accordance with user requirements:
- Suits and watches integrated seamlessly for fun into the UI as the luxury cover/face of the notes
- Removed external retail reference text ("RECEIVE YOUR NEW BOND TUX", "NEW 007 WATCHES AVAILABLE")
- Fixed sidebar tracking links for 1, 2, 3, 4 (and all 13 chapters) with dual ID anchors & scrollToChapter
- Direct keyword router in search bar: pressing Enter / Return immediately takes user to the specific chapter
- Gun-barrel red crosshair target/aim symbol on all graph equilibrium points
- 100% intact academic content without deviation
"""

import os
import sys
import base64
import math

# Ensure build_scripts directory is in python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

import theme_css
import engine_js
import ch1_foundations
import ch2_national_income
import ch3_deflator
import ch4_indicators
import ch5_business_cycles
import ch6_savings_investment
import ch7_multiplier
import ch8_policies
import ch9_ad_as
import ch10_is_lm
import ch11_phillips
import ch12_case_studies
import ch13_one_shot_revision
import ch14_midsem_case_studies
import ch15_endsem_simulations
import omega_watch_svg

def generate_gun_barrel_html(gun_barrel_data_uri):
    return f'''<div class="gun-barrel-container" id="gunBarrelBg">
  <img src="{gun_barrel_data_uri}" alt="007 Rifled Gun Barrel Spiral" class="gun-barrel-img">
  <div class="gun-barrel-vignette"></div>
</div>'''

def assemble_website():
    print("Initiating Luxury 007 Project Assembly Sequence...")

    css_content = theme_css.get_theme_css()
    js_content = engine_js.get_engine_js()

    # Load and encode images from assets folder
    assets_dir = os.path.join(current_dir, "..", "assets")
    gun_barrel_path = os.path.join(assets_dir, "gun_barrel_bg.jpg")

    with open(gun_barrel_path, "rb") as f:
        gun_barrel_data_uri = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("utf-8")

    gold_logo_path = os.path.join(assets_dir, "images", "007_gold_logo_web.png")
    with open(gold_logo_path, "rb") as f:
        gold_007_logo_uri = "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

    black_logo_path = os.path.join(assets_dir, "images", "007_black_logo_web.png")
    with open(black_logo_path, "rb") as f:
        black_007_logo_uri = "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

    # Load England Crest for Credentials Gate
    england_crest_path = os.path.join(assets_dir, "images", "london_crest_web.png")
    with open(england_crest_path, "rb") as f:
        england_crest_uri = "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

    gun_barrel_bg_html = generate_gun_barrel_html(gun_barrel_data_uri)
    omega_watch_svg_markup = omega_watch_svg.get_omega_seamaster_svg()

    logo_007_svg = '''<svg width="110" height="36" viewBox="0 0 160 50" fill="none" xmlns="http://www.w3.org/2000/svg" class="header-007-logo-svg">
  <!-- First 0 -->
  <path d="M22 5C10 5 2 14 2 25C2 36 10 45 22 45C34 45 42 36 42 25C42 14 34 5 22 5ZM22 37C15 37 11 31 11 25C11 19 15 13 22 13C29 13 33 19 33 25C33 31 29 37 22 37Z" fill="#ffffff"/>
  <!-- Second 0 -->
  <path d="M58 5C46 5 38 14 38 25C38 36 46 45 58 45C70 45 78 36 78 25C78 14 70 5 58 5ZM58 37C51 37 47 31 47 25C47 19 51 13 58 13C65 13 69 19 69 25C69 31 65 37 58 37Z" fill="#ffffff"/>
  <!-- The 7 with Gun Barrel -->
  <path d="M84 13V5H150V8H155V13H151V10H122V13H112L94 45H82L100 13H84Z" fill="#ffffff"/>
  <!-- Trigger Guard and Grip detail -->
  <path d="M112 13V18H117V13H112Z" fill="#ffffff"/>
  <!-- Barrel flutes detail -->
  <rect x="126" y="7" width="18" height="1.5" fill="#000000"/>
</svg>'''

    chapters_html = [
        ch1_foundations.get_chapter_1(),
        ch2_national_income.get_chapter_2(),
        ch3_deflator.get_chapter_3(),
        ch4_indicators.get_chapter_4(),
        ch5_business_cycles.get_chapter_5(),
        ch6_savings_investment.get_chapter_6(),
        ch7_multiplier.get_chapter_7(),
        ch8_policies.get_chapter_8(),
        ch9_ad_as.get_chapter_9(),
        ch10_is_lm.get_chapter_10(),
        ch11_phillips.get_chapter_11(),
        ch12_case_studies.get_chapter_12(),
        ch13_one_shot_revision.get_chapter_13(),
        ch14_midsem_case_studies.get_chapter_14(),
        ch15_endsem_simulations.get_chapter_15()
    ]

    header_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PROJECT 007: THE MACROECONOMICS INTELLIGENCE FILE</title>
  
  <!-- Favicon / Bond Theme Icon -->
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><circle cx=%2250%22 cy=%2250%22 r=%2245%22 fill=%22%23000000%22 stroke=%22%23ffffff%22 stroke-width=%224%22/><text x=%2250%22 y=%2258%22 font-family=%22serif%22 font-size=%2226%22 font-weight=%22900%22 fill=%22%23ffffff%22 text-anchor=%22middle%22>007</text></svg>">

  <!-- KaTeX for High-Precision Mathematical Typesetting -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css" integrity="sha384-GvrOXuhMATgEsSwCs4smul74iXGOixntILdUW9XmUC6+HX0sLNAK3q71HotJqlAn" crossorigin="anonymous">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js" integrity="sha384-cpW21h6RZv/phavutF+NWtTlCXcAb9ndvq4pzqhIB4X999KZGuIVS283K0MWltG0" crossorigin="anonymous"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script>

  <!-- Google Fonts: Cinzel, Playfair Display, Space Grotesk & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
"""

    after_css_html = """
  </style>
</head>
<body>
"""

    top_nav_html = f"""
  <!-- MI6 ACCESS CLEARANCE GATE (BOND THEMED PLAIN SIMPLE WHITE PAGE WITH GREY FONT) -->
  <div class="mi6-gate-overlay" id="mi6GateOverlay">
    <!-- Ambient England Crest Watermarks on Both Sides of White Background -->
    <div class="gate-bg-crest gate-bg-crest-left" aria-hidden="true">
      <img src="{england_crest_uri}" alt="England Crest" class="gate-watermark-crest">
      <div class="gate-watermark-label">HER MAJESTY'S SECRET SERVICE // SIS HQ</div>
    </div>
    <div class="gate-bg-crest gate-bg-crest-right" aria-hidden="true">
      <img src="{england_crest_uri}" alt="England Crest" class="gate-watermark-crest">
      <div class="gate-watermark-label">HER MAJESTY'S SECRET SERVICE // SECTION 00</div>
    </div>

    <div class="gate-content-container">
      <!-- Upper Provenance Bar with England Crest Both Sides -->
      <div class="gate-accreditation-header">
        <div class="gate-header-crest-wrap">
          <img src="{england_crest_uri}" alt="England Crest" class="gate-header-crest-img">
        </div>

        <div class="gate-provenance-center">
          <span class="gate-badge-dot"></span>
          <span class="gate-provenance-title">HER MAJESTY'S DIPLOMATIC &amp; SECRET INTELLIGENCE SERVICE</span>
        </div>

        <div class="gate-header-crest-wrap">
          <img src="{england_crest_uri}" alt="England Crest" class="gate-header-crest-img">
        </div>
      </div>

      <!-- Main Credentials Card -->
      <div class="mi6-gate-card">
        <div class="gate-logo-wrapper">
          <img src="{black_007_logo_uri}" alt="007 Logo" class="gate-007-black-logo">
          <div class="barrel-shimmer-sparkle" title="Muzzle Specular Shimmer" aria-hidden="true">
            <div class="barrel-shimmer-core"></div>
            <div class="barrel-shimmer-ray-h"></div>
            <div class="barrel-shimmer-ray-v"></div>
          </div>
        </div>
        <div class="gate-classification">TOP SECRET // MI6 SPECIAL INTELLIGENCE SERVICE</div>
        <h2 class="gate-heading">SECURITY CLEARANCE REQUIRED</h2>
        <div class="gate-clearance-notice">Level 5 Clearance Required to access Mission: Macro</div>

        <form id="mi6AuthForm" onsubmit="handleGateAuthentication(event)" autocomplete="off">
          <div class="gate-field-group">
            <label for="agentCredentialInput" class="gate-label">Input your credentials, Agent:</label>
            <input type="text" id="agentCredentialInput" class="gate-input" placeholder="Enter Agent Code" autocomplete="off" required autofocus>
          </div>

          <div class="gate-field-group">
            <label for="agentPasswordInput" class="gate-label">Input your password, Agent:</label>
            <div class="gate-input-wrapper">
              <input type="password" id="agentPasswordInput" class="gate-input" placeholder="Enter Security Passcode" autocomplete="off" required>
              <button type="button" class="gate-toggle-pw" id="gateTogglePwBtn" onclick="toggleGatePasswordVisibility()" title="Toggle Password Visibility">
                <svg id="eyeIconOpen" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="eye-outline-svg">
                  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                  <circle cx="12" cy="12" r="3"></circle>
                </svg>
                <svg id="eyeIconClosed" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="eye-outline-svg" style="display:none;">
                  <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path>
                  <line x1="1" y1="1" x2="23" y2="23"></line>
                </svg>
              </button>
            </div>
          </div>

          <div class="gate-feedback" id="gateFeedback"></div>

          <button type="submit" class="gate-submit-btn" id="gateSubmitBtn">
            <span class="btn-lock-icon">🔒</span> GRANT ACCESS TO "MISSION: MACRO"
          </button>
        </form>

        <div class="gate-footer-note">
          <span>MINISTRY OF DEFENCE // SECTION 00 // RESTRICTED ACCESS • AGENT 007</span>
        </div>
      </div>
    </div>
  </div>

  {gun_barrel_bg_html}

  <!-- MASTER AGENT HUD NAVIGATION -->
  <header class="master-header">
    <div class="header-left">
      <button class="menu-toggle-btn" onclick="toggleSidebar()" aria-label="Toggle Navigation Dossier">
        <span class="bar-line"></span>
        <span class="bar-line short"></span>
      </button>
      <div class="header-007-logo-wrap" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})" title="Project 007 // Return to Top">
        <img src="{gold_007_logo_uri}" alt="007 Gold Gun Logo" class="header-007-gold-logo-img">
      </div>
      <div class="header-title-text">
        MI6 // Q-BRANCH DIRECTIVE • MACROECONOMICS
      </div>
    </div>

    <!-- Tactical Intelligence Search & Target Router -->
    <div class="header-search-wrap" id="headerSearchWrap">
      <span class="search-icon-hint">⌕</span>
      <input type="text" id="globalSearchInput" class="header-search-input" 
             placeholder="SEARCH ANY CONCEPT (STICKY INPUT PRICES, CROWDING OUT, MULTIPLIER, OKUN)..." 
             autocomplete="off" spellcheck="false"
             oninput="handleSearchInput(this.value)" 
             onkeydown="handleSearchKeyDown(event)" 
             onfocus="handleSearchFocus()">
      <button class="search-action-btn" type="button" onclick="executeSearch()" title="Target Concept [Enter]">TARGET ⌖</button>
      <button class="search-clear-btn" id="searchClearBtn" type="button" onclick="clearSearch()" title="Clear Search" style="display:none;">✕</button>

      <!-- INSTANT JAMES BOND TACTICAL TARGET HUD DROPDOWN -->
      <div class="search-tactical-dropdown" id="searchDropdown" style="display: none;">
        <div class="search-dropdown-header">
          <div class="search-dropdown-title-wrap">
            <span class="search-hud-dot"></span>
            <span class="search-dropdown-tag">007 TACTICAL TARGET ROUTER</span>
          </div>
          <span class="search-count-badge" id="searchResultCount">0 MATCHES</span>
        </div>
        <div class="search-quick-tags" id="searchQuickTags">
          <span class="quick-pill-label">DIRECT TARGETS:</span>
          <button class="quick-pill" type="button" onclick="quickJumpSearch('sticky input prices')">Sticky Input Prices</button>
          <button class="quick-pill" type="button" onclick="quickJumpSearch('crowding out')">Crowding Out</button>
          <button class="quick-pill" type="button" onclick="quickJumpSearch('crowding in')">Crowding In</button>
          <button class="quick-pill" type="button" onclick="quickJumpSearch('multiplier')">Keynes Multiplier</button>
          <button class="quick-pill" type="button" onclick="quickJumpSearch('is-lm')">IS-LM Equilibrium</button>
          <button class="quick-pill" type="button" onclick="quickJumpSearch('okun')">Okun's Law</button>
          <button class="quick-pill" type="button" onclick="quickJumpSearch('liquidity trap')">Liquidity Trap</button>
          <button class="quick-pill" type="button" onclick="quickJumpSearch('phillips curve')">Phillips Curve</button>
          <button class="quick-pill" type="button" onclick="quickJumpSearch('demonetisation')">Demonetisation</button>
          <button class="quick-pill" type="button" onclick="quickJumpSearch('kumbh mela')">Kumbh Mela</button>
          <button class="quick-pill" type="button" onclick="quickJumpSearch('gdp deflator')">GDP Deflator</button>
        </div>
        <div class="search-results-list" id="searchResultsList">
          <!-- Dynamic Live Search Results -->
        </div>
      </div>
    </div>

    <!-- Right Header Controls -->
    <div class="header-right">
      <a href="javascript:void(0)" onclick="scrollToChapter(13)" class="header-icon-link" title="One-Shot Readiness Centre">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 01-8 0"/></svg>
      </a>
      <a href="javascript:void(0)" onclick="scrollToChapter(1)" class="header-icon-link" title="Operative Dossier Clearance">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
      </a>
      
      <!-- Mini Omega Seamaster Dial -->
      <div class="omega-mini-widget" title="Live Examination Readiness Chronometer">
        <div class="omega-dial-mini">
          <svg width="38" height="38" viewBox="0 0 100 100">
            <circle class="omega-track" cx="50" cy="50" r="42"></circle>
            <circle id="miniOmegaRing" class="omega-progress" cx="50" cy="50" r="42" style="stroke-dasharray: 264; stroke-dashoffset: 264;"></circle>
          </svg>
          <span id="miniOmegaPercent" class="omega-percent-mini">0%</span>
        </div>
        <div class="omega-mini-labels">
          <span class="chronometer-title">OMEGA 300M</span>
          <span class="chronometer-sub">EXAM READINESS</span>
        </div>
      </div>

      <!-- Lock Terminal Access Feature -->
      <button class="header-lock-terminal-btn" onclick="lockTerminal()" type="button" title="Lock Terminal (Require 007 Credentials)">
        <span class="lock-icon">🔒</span> LOCK
      </button>
    </div>
  </header>

  <!-- WORKSPACE WRAPPER -->
  <div class="workspace-wrapper">

    <!-- SIDEBAR DOSSIER NAVIGATION RAIL (FULLY FUNCTIONAL 01-15 // COLLAPSIBLE RAIL) -->
    <aside class="sidebar-nav" id="sidebarNav">
      <div class="sidebar-header">
        <div class="sidebar-header-main">
          <div class="sidebar-brand-block">
            <img src="{gold_007_logo_uri}" alt="007" class="sidebar-007-gold-logo">
            <div class="sidebar-text-col">
              <span class="sidebar-tag">INTELLIGENCE DOSSIERS</span>
              <span class="sidebar-sub">TAPMI BBA // ENDSEM CURRICULUM</span>
            </div>
          </div>
          <button class="sidebar-collapse-btn" id="sidebarCollapseBtn" onclick="toggleSidebarCollapse()" type="button" title="Collapse / Expand Sidebar Rail (Keeps instant chapter jumping active)">
            <span class="collapse-icon" id="sidebarCollapseIcon">◀</span>
          </button>
        </div>
      </div>

      <nav class="nav-links">
        <a href="#chapter-1" class="nav-item active" data-tooltip="01 // Macroeconomic Foundations" onclick="navigateToChapter(event, 1)">
          <span class="nav-ch-num">01</span>
          <div class="nav-text-wrap">
            <span class="nav-title">Macroeconomic Foundations</span>
            <span class="nav-sub">Circular Flow & Equilibrium</span>
          </div>
        </a>
        <a href="#chapter-2" class="nav-item" data-tooltip="02 // National Income Accounting" onclick="navigateToChapter(event, 2)">
          <span class="nav-ch-num">02</span>
          <div class="nav-text-wrap">
            <span class="nav-title">National Income Accounting</span>
            <span class="nav-sub">Value Added, Income, Expenditure</span>
          </div>
        </a>
        <a href="#chapter-3" class="nav-item" data-tooltip="03 // Real vs. Nominal GDP & Deflator" onclick="navigateToChapter(event, 3)">
          <span class="nav-ch-num">03</span>
          <div class="nav-text-wrap">
            <span class="nav-title">Real vs. Nominal GDP & Deflator</span>
            <span class="nav-sub">Base Year, Paasche Index & Double Defl.</span>
          </div>
        </a>
        <a href="#chapter-4" class="nav-item" data-tooltip="04 // Key Macro Indicators" onclick="navigateToChapter(event, 4)">
          <span class="nav-ch-num">04</span>
          <div class="nav-text-wrap">
            <span class="nav-title">Key Macro Indicators</span>
            <span class="nav-sub">Inflation, CPI vs Deflator & Labor Mkts</span>
          </div>
        </a>
        <a href="#chapter-5" class="nav-item" data-tooltip="05 // Business Cycles & Output Gaps" onclick="navigateToChapter(event, 5)">
          <span class="nav-ch-num">05</span>
          <div class="nav-text-wrap">
            <span class="nav-title">Business Cycles & Output Gaps</span>
            <span class="nav-sub">Potential Output Y*, Okun & Lab 1</span>
          </div>
        </a>
        <a href="#chapter-6" class="nav-item" data-tooltip="06 // Savings & Investment" onclick="navigateToChapter(event, 6)">
          <span class="nav-ch-num">06</span>
          <div class="nav-text-wrap">
            <span class="nav-title">Savings & Investment</span>
            <span class="nav-sub">Loanable Funds, Crowding Out & Lab 2</span>
          </div>
        </a>
        <a href="#chapter-7" class="nav-item" data-tooltip="07 // The Multiplier Effect" onclick="navigateToChapter(event, 7)">
          <span class="nav-ch-num">07</span>
          <div class="nav-text-wrap">
            <span class="nav-title">The Multiplier Effect</span>
            <span class="nav-sub">Keynesian Multipliers & Lab 3</span>
          </div>
        </a>
        <a href="#chapter-8" class="nav-item" data-tooltip="08 // Fiscal & Monetary Policy" onclick="navigateToChapter(event, 8)">
          <span class="nav-ch-num">08</span>
          <div class="nav-text-wrap">
            <span class="nav-title">Fiscal & Monetary Policy</span>
            <span class="nav-sub">RBI Repo, CRR, OMO, M0-M4 & Mix</span>
          </div>
        </a>
        <a href="#chapter-9" class="nav-item" data-tooltip="09 // AD–AS Framework" onclick="navigateToChapter(event, 9)">
          <span class="nav-ch-num">09</span>
          <div class="nav-text-wrap">
            <span class="nav-title">AD–AS Framework</span>
            <span class="nav-sub">Dedicated Shocks, Self-Correction & Lab 4</span>
          </div>
        </a>
        <a href="#chapter-10" class="nav-item" data-tooltip="10 // The IS–LM Framework" onclick="navigateToChapter(event, 10)">
          <span class="nav-ch-num">10</span>
          <div class="nav-text-wrap">
            <span class="nav-title">The IS–LM Framework</span>
            <span class="nav-sub">General Equil., Liquidity Trap & Lab 5</span>
          </div>
        </a>
        <a href="#chapter-11" class="nav-item" data-tooltip="11 // The Phillips Curve" onclick="navigateToChapter(event, 11)">
          <span class="nav-ch-num">11</span>
          <div class="nav-text-wrap">
            <span class="nav-title">The Phillips Curve</span>
            <span class="nav-sub">SRPC, LRPC, Expectations & Lab 6</span>
          </div>
        </a>
        <a href="#chapter-12" class="nav-item" data-tooltip="12 // Integrated Case Studies" onclick="navigateToChapter(event, 12)">
          <span class="nav-ch-num">12</span>
          <div class="nav-text-wrap">
            <span class="nav-title">Integrated Case Studies</span>
            <span class="nav-sub">Demonetisation, Oil, Kumbh Mela</span>
          </div>
        </a>
        <a href="#chapter-13" class="nav-item" data-tooltip="13 // One-Shot Revision Centre" onclick="navigateToChapter(event, 13)">
          <span class="nav-ch-num">13</span>
          <div class="nav-text-wrap">
            <span class="nav-title">One-Shot Revision Centre</span>
            <span class="nav-sub">35+ Formulas, 12 Matrices & Mock Exam</span>
          </div>
        </a>
        <a href="#chapter-14" class="nav-item" data-tooltip="14 // Midsem 2026 & Case Vault" onclick="navigateToChapter(event, 14)">
          <span class="nav-ch-num">14</span>
          <div class="nav-text-wrap">
            <span class="nav-title">Midsem 2026 & Case Vault</span>
            <span class="nav-sub">Official QP, Answer Key & 10 Case Studies</span>
          </div>
        </a>
        <a href="#chapter-15" class="nav-item" data-tooltip="15 // Endsem Simulation War Room" onclick="navigateToChapter(event, 15)">
          <span class="nav-ch-num">15</span>
          <div class="nav-text-wrap">
            <span class="nav-title">Endsem Simulation War Room</span>
            <span class="nav-sub">3 Full-Length 60M/2Hr Papers with Solutions</span>
          </div>
        </a>
      </nav>
    </aside>

    <!-- MAIN OPERATIONAL CONTENT -->
    <main class="main-content" id="mainContent">

      <!-- ========================================================================= -->
      <!-- LUXURY 007 COVER & FACE OF THE NOTES (SUITS & WATCHES FUN INTEGRATION) -->
      <!-- ========================================================================= -->
      <section class="hero-dribbble-showcase">
        <div class="hero-showcase-grid">

          <!-- Left Column: Vertical Links, Dispatches, Social -->
          <div class="hero-left-column">
            <div class="hero-vert-menu">
              <a href="javascript:void(0)" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})" class="hero-vert-link active">COVER</a>
              <a href="javascript:void(0)" onclick="scrollToChapter(2)" class="hero-vert-link" title="Suits: National Income & Formal Attire">SUITS</a>
              <a href="javascript:void(0)" onclick="scrollToChapter(4)" class="hero-vert-link" title="Watches: Precision Chronometers & Inflation">WATCHES</a>
              <a href="javascript:void(0)" onclick="scrollToChapter(5)" class="hero-vert-link" title="Cycles & Output Gaps">CYCLES</a>
              <a href="javascript:void(0)" onclick="scrollToChapter(7)" class="hero-vert-link" title="The Multiplier Effect">MULTIPLIER</a>
              <a href="javascript:void(0)" onclick="scrollToChapter(10)" class="hero-vert-link" title="IS-LM General Equilibrium">IS-LM</a>
              <a href="javascript:void(0)" onclick="scrollToChapter(13)" class="hero-vert-link" title="One-Shot Readiness Centre">READINESS</a>
              <a href="javascript:void(0)" onclick="scrollToChapter(14)" class="hero-vert-link" title="Midsem 2026 Intelligence & Case Vault">MIDSEM</a>
              <a href="javascript:void(0)" onclick="scrollToChapter(15)" class="hero-vert-link" title="Endsem 60M Simulation War Room">ENDSEM</a>
            </div>

            <!-- Authentic MI6 Field Dispatch Card -->
            <div class="hero-tweets-box">
              <div class="tweets-box-label">MI6 FIELD DISPATCH</div>
              <div class="tweet-user-row">
                <div class="tweet-avatar-circle"><span class="avatar-007-monogram">007</span></div>
                <div class="tweet-user-meta">
                  <span class="tweet-user-name">JAMES BOND <span class="verified-badge">✔</span></span>
                  <span class="tweet-user-handle">@007 • TAPMI BBA DIRECTIVE</span>
                </div>
              </div>
              <p class="tweet-body-text">
                Welcome Agent 007. Master all 15 macroeconomics dossiers. Official authority: Prof. Sana Tabassum & Prof. Abhishek Kumar Rohit. All 7-step solutions verified for exam victory.
              </p>
              <div class="tweet-nav-arrows">
                <button class="tweet-arrow-btn" onclick="scrollToChapter(1)">‹</button>
                <button class="tweet-arrow-btn" onclick="scrollToChapter(13)">›</button>
              </div>
            </div>

            <!-- Minimalist Circular Intelligence Icons -->
            <div class="hero-social-row">
              <a href="javascript:void(0)" onclick="scrollToChapter(1)" class="hero-social-icon" title="Dossier 01: Foundations">◎</a>
              <a href="javascript:void(0)" onclick="scrollToChapter(10)" class="hero-social-icon" title="Dossier 10: IS-LM General Equilibrium">◈</a>
              <a href="javascript:void(0)" onclick="scrollToChapter(13)" class="hero-social-icon" title="Dossier 13: Exam Readiness">❖</a>
            </div>
          </div>

          <!-- Right Column: Cinematic Headline & Picture-in-Picture Cover Frames -->
          <div class="hero-right-column">
            <div class="hero-branding-tag">
              <img src="{gold_007_logo_uri}" alt="007" class="hero-007-gold-tag-logo">
              <span>TOP SECRET // TAPMI BBA-MACROECONOMICS // AGENT 007</span>
            </div>
            <h1 class="hero-cinematic-headline">
              <span class="headline-title-sidebyside">MISSION: MACRO</span>
              <span class="hero-subtle-tagline">Global Economies</span>
            </h1>

            <!-- 007 MISSION TACTICAL COUNTDOWN TIMER (TARGET: NOVEMBER 30TH 10:00 AM) -->
            <div class="hero-countdown-deck" id="missionCountdownDeck">
              <div class="countdown-hud-header">
                <span class="countdown-pulse-dot" id="countdownDot"></span>
                <span class="countdown-target-label" id="countdownStageLabel">MISSION TARGET: NOV 30, 10:00 AM // ENDSEM DEPLOYMENT</span>
              </div>
              <div class="countdown-digits-wrapper" id="countdownDigitsWrap">
                <div class="countdown-segment">
                  <span class="cd-num" id="cdMonths">00</span>
                  <span class="cd-lbl">MM (MONTHS)</span>
                </div>
                <span class="cd-divider">:</span>
                <div class="countdown-segment">
                  <span class="cd-num" id="cdDays">00</span>
                  <span class="cd-lbl">DD (DAYS)</span>
                </div>
                <span class="cd-divider">:</span>
                <div class="countdown-segment">
                  <span class="cd-num" id="cdHours">00</span>
                  <span class="cd-lbl">HH (HOURS)</span>
                </div>
                <span class="cd-divider">:</span>
                <div class="countdown-segment">
                  <span class="cd-num" id="cdMinutes">00</span>
                  <span class="cd-lbl">mm (MINUTES)</span>
                </div>
                <span class="cd-divider">:</span>
                <div class="countdown-segment">
                  <span class="cd-num" id="cdSeconds">00</span>
                  <span class="cd-lbl">ss (SECONDS)</span>
                </div>
              </div>
            </div>

            <!-- THE GRAND OMEGA SEAMASTER 007 MASTER INSTRUMENT STAGE -->
            <div class="hero-omega-master-stage" id="omegaWatchStage">
              <!-- Left Wing: Readiness & Core Chapters -->
              <div class="omega-left-hud-wing">
                <div class="omega-hud-header">
                  <span class="omega-brand-emblem">Ω</span>
                  <div class="omega-brand-text">
                    <span class="omega-hud-title">OMEGA SEAMASTER 300M</span>
                    <span class="omega-hud-sub">CO-AXIAL MASTER CHRONOMETER • 007 EDITION</span>
                  </div>
                </div>
                <div class="omega-readout-card">
                  <span class="readout-label">MINUTE HAND // EXAM READINESS</span>
                  <div class="readout-hero-val-row">
                    <span id="masterOmegaPercent" class="readout-val">0%</span>
                    <span class="readout-unit">TARGET: 100%</span>
                  </div>
                  <div class="readout-bar-track">
                    <div class="readout-bar-fill" id="readoutBarFill" style="width:0%;"></div>
                  </div>
                  <span class="readout-desc">The minute hand traces overall academic readiness across all 13 dossiers. Continuous 360° chronometer sweep.</span>
                </div>
                <div class="omega-readout-card">
                  <span class="readout-label">HOUR HAND // CORE DOSSIERS SECURED</span>
                  <div class="readout-hero-val-row">
                    <span id="masterOmegaChapters" class="readout-val">0 <span style="font-size:0.65em; color:var(--text-muted);">/ 12</span></span>
                  </div>
                  <span class="readout-desc">The hour hand independently indicates the number of core dossiers mastered (Chapters 1–12). Chapter 13 is the one-shot revision centre and is purposefully decoupled.</span>
                </div>
                <div class="omega-spec-pill-row">
                  <span class="spec-pill">GRADE 2 TITANIUM</span>
                  <span class="spec-pill">007 STRIPED NATO</span>
                  <span class="spec-pill">300M WATER RESISTANT</span>
                  <span class="spec-pill">METAS CERTIFIED</span>
                </div>
              </div>

              <!-- Center: Scaled-Up 1-on-1 Omega Seamaster Diver 300M Instrument -->
              <div class="omega-center-instrument-wrap" id="omegaWatchWrap">
                {omega_watch_svg_markup}
              </div>

              <!-- Right Wing: Interactive Seconds Revolver & Precision Telemetry -->
              <div class="omega-right-hud-wing">
                <div class="omega-hud-header">
                  <span class="omega-hud-title">CHRONOGRAPH & SECONDS CONTROL</span>
                  <span class="omega-hud-sub">CALIBRE 8806 • 25,200 VPH (8 Hz SWEEP)</span>
                </div>
                <div class="omega-readout-card">
                  <span class="readout-label">SECONDS HAND DIAL TRACKER</span>
                  <div class="seconds-angle-display" id="omegaSecondsAngle">00s // 000° CHRONO</div>
                  <div class="omega-interactive-note" id="omegaSecondsStatus">
                    <span class="pulse-indicator-red"></span>
                    <span>SECONDS HAND: CO-AXIAL SWEEP (8 Hz)</span>
                  </div>
                  <span class="readout-desc" style="margin-top:8px;">
                    Move or drag cursor <strong>inside the watch dial</strong> to freely revolve the red-tipped seconds hand. Outside the watch, the needle maintains its authentic 8 Hz Co-Axial sweep.
                  </span>
                </div>
                <div class="chrono-action-btns">
                  <button class="watch-ctrl-btn" onclick="zeroChronograph()" type="button">↺ ZERO TO 12:00</button>
                  <button class="watch-ctrl-btn active" id="coaxialSweepToggleBtn" onclick="toggleCoaxialSweep()" type="button">▶ 8 Hz SWEEP: ACTIVE</button>
                </div>
                <div class="omega-spec-card">
                  <span class="spec-card-title">HOROLOGICAL HERITAGE</span>
                  <p class="spec-card-text">
                    Identical to Agent 007's tactical timepiece in <em>No Time To Die</em> on the iconic striped NATO strap (dark brown, grey & beige). Features tropical brown-black aluminum bezel, aged radium Super-LumiNova markers, and the British MoD Broad Arrow (Pheon) at 6 o'clock.
                  </p>
                </div>
              </div>

              <!-- MI6 TACTICAL SATELLITE AUDIO CONSOLE (RIGHT BELOW TITANIUM OMEGA SEAMASTER) -->
              <div class="omega-briefing-console-row" id="omegaBriefingRow">
                <div class="briefing-tactical-deck" id="briefingTacticalDeck">
                  <audio id="briefingAudioPlayer" preload="auto" loop>
                    <source src="assets/audio/briefing.mp3" type="audio/mpeg">
                    <source src="https://p.scdn.co/mp3-preview/c9899af7b5dac27b539e8a43df26bf6958119a85" type="audio/mpeg">
                  </audio>

                  <!-- TACTICAL SATELLITE UPLINK STATUS BAR (DISCRETE BOND CIPHER COMPLICATION) -->
                  <div class="briefing-sat-status-bar">
                    <div class="sat-bar-left">
                      <span class="sat-pulse-led"></span>
                      <span class="player-briefing-silver-title">BRIEFING</span>
                      <span class="sat-hud-tag">// MI6 SAT-COM CIPHER</span>
                      <span class="sat-freq-badge">14.225 GHz KU-BAND</span>
                    </div>
                    <div class="sat-bar-right">
                      <div class="sat-signal-meter" title="Satellite Duplex Signal Strength: 99.8%">
                        <span class="sig-label">SIG LOCK</span>
                        <div class="sig-bars" id="satSignalBars">
                          <span class="s-bar active"></span>
                          <span class="s-bar active"></span>
                          <span class="s-bar active"></span>
                          <span class="s-bar active"></span>
                          <span class="s-bar active"></span>
                        </div>
                      </div>
                      <span class="sat-status-pill" id="satStatusPill">UPLINK ONLINE</span>
                    </div>
                  </div>

                  <!-- ORBITAL & TELEMETRY COMPLICATIONS STRIP -->
                  <div class="briefing-complications-strip">
                    <div class="sat-telemetry-col">
                      <span class="comp-label">SATELLITE NODE</span>
                      <span class="comp-val">SKYNET-07 // MIL-COMSAT</span>
                    </div>
                    <div class="sat-telemetry-col">
                      <span class="comp-label">ORBITAL APOGEE</span>
                      <span class="comp-val">35,786 KM (GEO-SYNC)</span>
                    </div>
                    <div class="sat-telemetry-col">
                      <span class="comp-label">SIS DOWNLINK</span>
                      <span class="comp-val">51°29'14"N 0°07'28"W</span>
                    </div>
                    <div class="sat-telemetry-col">
                      <span class="comp-label">ENCRYPTION PROTOCOL</span>
                      <span class="comp-val">RSA-4096 / DUAL-KEY</span>
                    </div>
                    <div class="sat-telemetry-col hide-mobile">
                      <span class="comp-label">LIVE CARRIER FLUX</span>
                      <span class="comp-val" id="satLockText">CARRIER LOCKED [DUPLEX 99.8%]</span>
                    </div>
                  </div>

                  <!-- MAIN PLAYBACK & FREQUENCY SPECTRUM ROW -->
                  <div class="briefing-deck-main-row">
                    <!-- Master Play / Pause Tactical Cryptographic Trigger -->
                    <button class="briefing-master-play-btn" id="briefingPlayBtn" onclick="toggleBriefingAudio()" type="button" title="Initiate Secure MI6 Audio Transmission">
                      <!-- Corner Rivet / Tactical Hex Screws -->
                      <span class="btn-hex-screw tl"></span>
                      <span class="btn-hex-screw tr"></span>
                      <span class="btn-hex-screw bl"></span>
                      <span class="btn-hex-screw br"></span>

                      <!-- Left: Reticle / Target Radar Glyph with Crosshairs and Play/Pause -->
                      <div class="btn-reticle-cluster">
                        <div class="btn-reticle-ring"></div>
                        <div class="btn-reticle-crosshair"></div>
                        <span class="briefing-btn-icon" id="briefingPlayIcon">▶</span>
                      </div>

                      <!-- Center: Multi-Tier Tactical Text & Telemetry -->
                      <div class="btn-label-stack">
                        <div class="btn-telemetry-micro">
                          <span class="btn-beacon-dot"></span>
                          <span class="btn-tx-state" id="btnTxState">STANDBY // KU-BAND 14.2G</span>
                          <span class="btn-enc-tag">Q-CIPHER</span>
                        </div>
                        <div class="briefing-btn-label" id="briefingPlayLabel">PLAY BRIEFING</div>
                        <div class="btn-sub-directive">TRANSMIT ENCRYPTED AUDIO STREAM</div>
                      </div>

                      <!-- Right: Micro Pulse Equalizer / Waveform Matrix -->
                      <div class="btn-micro-eq" title="Audio Signal Channel">
                        <span class="meq-bar mb-1"></span>
                        <span class="meq-bar mb-2"></span>
                        <span class="meq-bar mb-3"></span>
                        <span class="meq-bar mb-4"></span>
                      </div>

                      <!-- Tactical Arming Border / Laser Sweep Glow -->
                      <div class="btn-scanner-sweep"></div>
                    </button>

                    <!-- Real-Time Frequency Equalizer Spectrum Analyzer -->
                    <div class="briefing-eq-spectrum" id="briefingSpectrum" title="Audio Spectral Telemetry Analyzer">
                      <span class="eq-col col-1"></span>
                      <span class="eq-col col-2"></span>
                      <span class="eq-col col-3"></span>
                      <span class="eq-col col-4"></span>
                      <span class="eq-col col-5"></span>
                      <span class="eq-col col-6"></span>
                      <span class="eq-col col-7"></span>
                      <span class="eq-col col-8"></span>
                      <span class="eq-col col-9"></span>
                      <span class="eq-col col-10"></span>
                      <span class="eq-col col-11"></span>
                      <span class="eq-col col-12"></span>
                      <span class="eq-col col-13"></span>
                      <span class="eq-col col-14"></span>
                      <span class="eq-col col-15"></span>
                      <span class="eq-col col-16"></span>
                    </div>

                    <!-- Calibrated Audio Timeline Scrubber with Millimeter Tick Grids -->
                    <div class="briefing-timeline-wrap">
                      <div class="briefing-scrubber-track" id="briefingScrubberTrack" onclick="seekBriefingAudio(event)" title="Calibrated Reticle Seek">
                        <div class="briefing-scrubber-ticks">
                          <span class="tick"></span><span class="tick"></span><span class="tick"></span><span class="tick"></span><span class="tick"></span>
                          <span class="tick"></span><span class="tick"></span><span class="tick"></span><span class="tick"></span><span class="tick"></span>
                        </div>
                        <div class="briefing-scrubber-fill" id="briefingScrubberFill" style="width: 0%;">
                          <span class="scrubber-head"></span>
                        </div>
                      </div>
                      <div class="briefing-time-readout">
                        <span id="briefingCurrentTime">00:00</span>
                        <span class="briefing-time-sep">/</span>
                        <span id="briefingTotalTime">00:30</span>
                      </div>
                    </div>

                    <!-- Tactical Auxiliary Tools -->
                    <div class="briefing-deck-tools">
                      <button class="briefing-tool-btn active" id="briefingLoopBtn" onclick="toggleBriefingLoop()" type="button" title="Toggle Tactical Loop">
                        <span id="briefingLoopIcon">⟳</span> LOOP
                      </button>
                      <button class="briefing-tool-btn" id="briefingMuteBtn" onclick="toggleBriefingMute()" type="button" title="Audio Mute">
                        <span id="briefingMuteIcon">🔊</span>
                      </button>
                      <input type="range" class="briefing-vol-slider" id="briefingVolSlider" min="0" max="1" step="0.05" value="0.85" oninput="setBriefingVolume(this.value)" title="Volume Level">
                    </div>
                  </div>

                  <!-- FOOTER COMPLICATIONS STATUS CHIP -->
                  <div class="briefing-deck-sub-strip">
                    <span class="sub-chip"><span class="chip-dot"></span>CODEC: 320 KBPS / 44.1 kHz DUAL-MONITOR</span>
                    <span class="sub-chip"><span class="chip-dot"></span>BURST PROTOCOL: MIL-STD-188-181C</span>
                    <span class="sub-chip"><span class="chip-dot"></span>Q-BRANCH SECURE RELAY // NO TIME TO DIE CUE</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- THREE GLOBAL LEARNING ENVIRONMENTS SWITCHER -->
      <div class="environment-switcher">
        <button class="env-btn active" data-env="all" onclick="switchEnvironment('all')">
          <span class="bullet">■</span> <span class="label-text">ALL ENVIRONMENTS</span>
        </button>
        <button class="env-btn" data-env="training" onclick="switchEnvironment('training')">
          <span class="bullet">■</span> <span class="label-text">A. FIELD TRAINING (THEORY)</span>
        </button>
        <button class="env-btn" data-env="missions" onclick="switchEnvironment('missions')">
          <span class="bullet">■</span> <span class="label-text">B. COMBAT MISSIONS (EXAM PROBLEMS)</span>
        </button>
        <button class="env-btn" data-env="targets" onclick="switchEnvironment('targets')">
          <span class="bullet">■</span> <span class="label-text">C. TARGET TARGETS (7-STEP SOLUTIONS)</span>
        </button>
      </div>

      <!-- CHAPTER INJECTION CONTAINER (WRAPPED IN DUAL ANCHORS FOR FLAWLESS JUMPING) -->
      <div class="chapters-stream">
"""

    footer_html = f"""
      </div>

      <!-- GLOBAL OPERATIONAL FOOTER -->
      <footer class="master-footer">
        <div class="footer-top">
          <div class="footer-brand">
            <div class="footer-logo">
              <img src="{gold_007_logo_uri}" alt="007 Gold Gun Logo" class="footer-007-gold-logo-img">
            </div>
            <div class="footer-info">
              <h4>PROJECT 007: THE MACROECONOMICS INTELLIGENCE FILE</h4>
              <p>Top-Secret Interactive Examination Preparation Terminal for Agent 007.</p>
            </div>
          </div>
          <div class="footer-badges">
            <span class="f-badge">STRICT SOURCE AUDIT CONFIRMED</span>
            <span class="f-badge">14 OFFICIAL PPTs MAPPED</span>
            <span class="f-badge">OFFICIAL ANSWER KEY COMPLIANT</span>
            <span class="f-badge">6 DUAL-MODE CANVAS LABS</span>
          </div>
        </div>
        <div class="footer-bottom">
          <p class="copyright-notice">
            ACADEMIC CITATIONS: Prof. Sana Tabassum, Prof. Abhishek Kumar Rohit, Prof. Chandrakanti (TAPMI BBA-Macroeconomics). Developed under MI6 Q-Branch Advanced Instructional Design Protocol. Visual aesthetics inspired by Daniel Craig-era 007 cinematography, luxury black-tie design, and Omega Seamaster chronometry. No official affiliation or commercial endorsement implied.
          </p>
        </div>
      </footer>

    </main>
  </div>

  <!-- JAVASCRIPT EXECUTION ENGINE -->
  <script>
"""

    closing_script_html = """
    // Auto-render KaTeX on DOM ready with graceful fallback
    document.addEventListener("DOMContentLoaded", function() {
      if (typeof renderMathInElement === "function") {
        renderMathInElement(document.body, {
          delimiters: [
            {left: "$$", right: "$$", display: true},
            {left: "$", right: "$", display: false},
            {left: "\\\\(", right: "\\\\)", display: false},
            {left: "\\\\[", right: "\\\\]", display: true}
          ],
          throwOnError: false
        });
      }
    });

    // Mobile sidebar toggle
    window.toggleSidebar = function() {
      const sidebar = document.getElementById('sidebarNav') || document.getElementById('sidebar');
      if (sidebar) sidebar.classList.toggle('open');
    };

    // Sidebar active item handler with smooth scrolling
    window.navigateToChapter = function(event, chNum) {
      if (event) event.preventDefault();
      if (typeof window.scrollToChapter === 'function') {
        window.scrollToChapter(chNum);
      }
    };

    window.activateNavLink = function(el, chNum) {
      document.querySelectorAll('.sidebar-nav .nav-item').forEach(item => item.classList.remove('active'));
      if (el) el.classList.add('active');
      const sidebar = document.getElementById('sidebarNav') || document.getElementById('sidebar');
      if (sidebar && sidebar.classList.contains('open')) sidebar.classList.remove('open');
      if (chNum && typeof window.scrollToChapter === 'function') {
        window.scrollToChapter(chNum);
      }
    };
  </script>
</body>
</html>
"""

    parts = [
        header_html,
        css_content,
        after_css_html,
        top_nav_html
    ]

    for i, ch_html in enumerate(chapters_html, 1):
        parts.append(f"\n<!-- ==================== CHAPTER {i} BOUNDARY ==================== -->\n")
        parts.append(ch_html)

    parts.append(footer_html)
    parts.append(js_content)
    parts.append(closing_script_html)

    final_html = "".join(parts)

    output_path = os.path.join(current_dir, "..", "index.html")
    output_path = os.path.abspath(output_path)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    print("Assembly completed successfully!")
    print(f"Generated luxury 007 standalone index.html at: {output_path}")
    print(f"Total file size: {len(final_html):,} bytes ({len(final_html)/(1024*1024):.2f} MB)")

if __name__ == "__main__":
    assemble_website()
