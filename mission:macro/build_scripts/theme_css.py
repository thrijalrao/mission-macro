"""
Project 007: The Macroeconomics Intelligence File
Daniel Craig 007 Cinematic Visual Identity & Design System CSS
Re-architected strictly in accordance with the luxury Dribbble 007 Web Design Reference:
- Deep obsidian and jet black background (#000000)
- Iconic 007 Gun Barrel Rifling Spiral background motif
- Crisp 2px solid white picture-in-picture frames with thin technical leader lines
- High-fashion luxury serif display typography ("INSIDE THE WORLD OF JAMES BOND")
- Minimalist tracked-out vertical navigation with crisp white underline active states
- Sleek tweets / MI6 dispatch card with verified badge and circular avatar
- Architectural 90-degree geometry (zero rounded corners, pure tuxedo sophistication)
"""

def get_theme_css():
    return """
:root {
  /* PURE TUXEDO LUXURY 007 PALETTE */
  --bg-primary: #000000;
  --bg-secondary: #050507;
  --bg-tertiary: #0a0a0d;
  --bg-card: #08080a;
  --bg-card-hover: #101014;
  --bg-card-active: #14141a;

  --text-primary: #ffffff;
  --text-secondary: #e0e0e6;
  --text-muted: #8e8e98;
  --text-dim: #555560;

  --silver-100: #ffffff;
  --silver-200: #ededf0;
  --silver-300: #d0d2d8;
  --silver-400: #9a9ca6;
  --silver-500: #666872;

  --border-subtle: rgba(255, 255, 255, 0.14);
  --border-medium: rgba(255, 255, 255, 0.28);
  --border-strong: rgba(255, 255, 255, 0.55);
  --border-white: #ffffff;

  --bond-crimson: #d92534;
  --bond-crimson-glow: rgba(217, 37, 52, 0.35);

  --font-serif: 'Cinzel', 'Playfair Display', Georgia, serif;
  --font-sans: 'Space Grotesk', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-mono: 'JetBrains Mono', "SF Mono", Menlo, Courier, monospace;

  --radius-none: 0px;
  --radius-sm: 0px;
  --radius-md: 0px;
  --radius-lg: 0px;

  --transition-fast: 0.15s ease;
  --transition-med: 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

/* --- RESET & FOUNDATION --- */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
  font-size: 16px;
  background-color: #000000;
  color: var(--silver-300);
}

body {
  font-family: var(--font-sans);
  background-color: #000000;
  min-height: 100vh;
  line-height: 1.6;
  overflow-x: hidden;
  position: relative;
  -webkit-font-smoothing: antialiased;
}

/* --- ICONIC 007 RIFLED GUN BARREL SPIRAL BACKGROUND (iStock Reference Fidelity) --- */
.gun-barrel-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 0;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #000000;
}

.gun-barrel-img {
  position: absolute;
  width: 125vmax;
  height: 125vmax;
  min-width: 100vw;
  min-height: 100vh;
  object-fit: cover;
  opacity: 0.35;
  filter: contrast(1.22) brightness(0.95);
  animation: subtleBarrelBreathe 28s ease-in-out infinite alternate;
  transform-origin: center center;
  pointer-events: none;
}

@keyframes subtleBarrelBreathe {
  0% { transform: scale(1) rotate(0deg); opacity: 0.32; }
  50% { transform: scale(1.03) rotate(2deg); opacity: 0.40; }
  100% { transform: scale(1) rotate(0deg); opacity: 0.32; }
}

.gun-barrel-vignette {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at 50% 50%, rgba(0, 0, 0, 0.05) 0%, rgba(0, 0, 0, 0.35) 60%, rgba(0, 0, 0, 0.65) 100%);
  pointer-events: none;
}

/* --- TOP NAVIGATION / MASTER AGENT HUD --- */
.master-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(0, 0, 0, 0.92);
  backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--border-subtle);
  padding: 12px 32px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 20px;
}

.menu-toggle-btn {
  background: transparent;
  border: none;
  color: var(--silver-300);
  cursor: pointer;
  padding: 4px;
  display: flex;
  flex-direction: column;
  gap: 5px;
  transition: color var(--transition-fast);
}

.menu-toggle-btn .bar-line {
  display: block;
  width: 24px;
  height: 2px;
  background: #ffffff;
  transition: transform var(--transition-fast);
}

.menu-toggle-btn .bar-line.short {
  width: 16px;
}

.menu-toggle-btn:hover .bar-line {
  background: var(--bond-crimson);
}

/* 007 Gun Logo in Header */
.header-007-logo-wrap {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.header-007-logo-svg {
  height: 28px;
  width: auto;
  fill: #ffffff;
  transition: filter var(--transition-fast);
}

.header-007-logo-svg:hover {
  filter: drop-shadow(0 0 8px rgba(255, 255, 255, 0.6));
}

.header-title-text {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.15em;
  color: var(--text-muted);
  border-left: 1px solid var(--border-subtle);
  padding-left: 16px;
  text-transform: uppercase;
}

/* Live Search Box */
/* --- LUXURY 007 TACTICAL SEARCH HUD & ROUTER --- */
.header-search-wrap {
  flex: 1;
  max-width: 580px;
  position: relative;
  display: flex;
  align-items: center;
}

.header-search-input {
  width: 100%;
  background: rgba(15, 17, 21, 0.95);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-none);
  padding: 8px 105px 8px 36px;
  color: #ffffff;
  font-family: var(--font-mono);
  font-size: 0.74rem;
  letter-spacing: 0.05em;
  transition: all var(--transition-fast);
}

.header-search-input:focus {
  outline: none;
  background: #000000;
  border-color: #d92534;
  box-shadow: 0 0 16px rgba(217, 37, 52, 0.45);
}

.search-action-btn {
  position: absolute;
  right: 6px;
  top: 50%;
  transform: translateY(-50%);
  background: #d92534;
  border: 1px solid #ff4d5a;
  color: #ffffff;
  font-family: var(--font-mono);
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  padding: 4px 9px;
  border-radius: 2px;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 4px;
}

.search-action-btn:hover {
  background: #ff2d3d;
  box-shadow: 0 0 12px rgba(217, 37, 52, 0.7);
}

.search-clear-btn {
  position: absolute;
  right: 88px;
  top: 50%;
  transform: translateY(-50%);
  background: transparent;
  border: none;
  color: var(--text-muted);
  font-size: 0.75rem;
  cursor: pointer;
  padding: 4px 6px;
  line-height: 1;
}

.search-clear-btn:hover {
  color: #ffffff;
}

/* Tactical HUD Dropdown */
.search-tactical-dropdown {
  position: absolute;
  top: calc(100% + 8px);
  left: 0;
  right: 0;
  background: rgba(10, 12, 16, 0.98);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(217, 37, 52, 0.5);
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.95), 0 0 25px rgba(217, 37, 52, 0.2);
  z-index: 1000;
  max-height: 480px;
  overflow-y: auto;
  border-radius: 0;
}

.search-dropdown-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 14px;
  background: rgba(20, 24, 30, 0.9);
  border-bottom: 1px solid var(--border-subtle);
}

.search-dropdown-title-wrap {
  display: flex;
  align-items: center;
  gap: 8px;
}

.search-hud-dot {
  width: 6px;
  height: 6px;
  background: #d92534;
  border-radius: 50%;
  box-shadow: 0 0 6px #d92534;
  animation: pulseDot 1.5s infinite;
}

@keyframes pulseDot {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.4; transform: scale(0.85); }
}

.search-dropdown-tag {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  letter-spacing: 0.12em;
  color: var(--silver-200);
  font-weight: 700;
}

.search-count-badge {
  font-family: var(--font-mono);
  font-size: 0.6rem;
  color: #d92534;
  background: rgba(217, 37, 52, 0.15);
  padding: 2px 6px;
  border: 1px solid rgba(217, 37, 52, 0.3);
}

/* Quick pills */
.search-quick-tags {
  padding: 8px 12px;
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  align-items: center;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  background: rgba(0, 0, 0, 0.4);
}

.quick-pill-label {
  font-family: var(--font-mono);
  font-size: 0.58rem;
  color: var(--text-dim);
  letter-spacing: 0.08em;
  margin-right: 4px;
}

.quick-pill {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: var(--silver-200);
  font-family: var(--font-mono);
  font-size: 0.62rem;
  padding: 3px 8px;
  cursor: pointer;
  border-radius: 2px;
  transition: all 0.15s ease;
  white-space: nowrap;
}

.quick-pill:hover {
  background: rgba(217, 37, 52, 0.2);
  border-color: #d92534;
  color: #ffffff;
}

/* Results list */
.search-results-list {
  padding: 6px 0;
}

.search-result-item {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  padding: 10px 14px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
  cursor: pointer;
  transition: background 0.15s ease;
  text-decoration: none;
}

.search-result-item:hover, .search-result-item.selected {
  background: rgba(217, 37, 52, 0.12);
  border-left: 3px solid #d92534;
}

.search-item-info {
  flex: 1;
  padding-right: 12px;
}

.search-item-badge {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.58rem;
  letter-spacing: 0.1em;
  color: #d92534;
  margin-bottom: 2px;
  font-weight: 700;
}

.search-item-title {
  display: block;
  font-family: var(--font-sans);
  font-size: 0.82rem;
  color: #ffffff;
  font-weight: 600;
  margin-bottom: 3px;
}

.search-item-snippet {
  display: block;
  font-family: var(--font-sans);
  font-size: 0.72rem;
  color: var(--text-muted);
  line-height: 1.35;
}

.search-item-action {
  align-self: center;
  font-family: var(--font-mono);
  font-size: 0.62rem;
  letter-spacing: 0.08em;
  color: var(--silver-300);
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.15);
  padding: 4px 8px;
  border-radius: 2px;
  white-space: nowrap;
}

.search-result-item:hover .search-item-action {
  background: #d92534;
  border-color: #ff4d5a;
  color: #ffffff;
}

/* Red Sniper Reticle Pulse Highlight on Targeted Card */
@keyframes reticlePulse {
  0% {
    box-shadow: 0 0 0 rgba(217, 37, 52, 0);
    border-color: rgba(217, 37, 52, 0.4);
  }
  25% {
    box-shadow: 0 0 45px rgba(217, 37, 52, 0.85), inset 0 0 25px rgba(217, 37, 52, 0.35);
    border-color: #d92534;
  }
  60% {
    box-shadow: 0 0 30px rgba(217, 37, 52, 0.65), inset 0 0 15px rgba(217, 37, 52, 0.2);
    border-color: #d92534;
  }
  100% {
    box-shadow: 0 0 0 rgba(217, 37, 52, 0);
    border-color: var(--border-subtle);
  }
}

.target-reticle-pulse {
  border: 2px solid #d92534 !important;
  animation: reticlePulse 3s cubic-bezier(0.16, 1, 0.3, 1) forwards !important;
  position: relative;
  z-index: 5;
}

/* Native scroll margin to prevent header obscuring content */
.chapter-container, .mission-chapter, .topic-card, .mission-card, .intel-box, .chapter-header {
  scroll-margin-top: 85px;
}

.search-icon-hint {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-muted);
  font-size: 0.75rem;
  pointer-events: none;
}

/* Header Right: Minimalist Icons */
.header-right {
  display: flex;
  align-items: center;
  gap: 20px;
}

.header-icon-link {
  color: var(--silver-300);
  text-decoration: none;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color var(--transition-fast);
}

.header-icon-link:hover {
  color: #ffffff;
}

/* Mini Omega Chronometer Widget */
.omega-mini-widget {
  display: flex;
  align-items: center;
  gap: 12px;
  padding-left: 14px;
  border-left: 1px solid var(--border-subtle);
}

.omega-dial-mini {
  position: relative;
  width: 38px;
  height: 38px;
}

.omega-track {
  fill: none;
  stroke: rgba(255, 255, 255, 0.12);
  stroke-width: 5;
}

.omega-progress {
  fill: none;
  stroke: #ffffff;
  stroke-width: 5;
  stroke-linecap: square;
  transform: rotate(-90deg);
  transform-origin: 50% 50%;
  transition: stroke-dashoffset 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

.omega-percent-mini {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-family: var(--font-mono);
  font-size: 0.62rem;
  font-weight: 700;
  color: #ffffff;
}

.omega-mini-labels {
  display: flex;
  flex-direction: column;
}

.chronometer-title {
  font-family: var(--font-serif);
  font-size: 0.72rem;
  letter-spacing: 0.08em;
  color: #ffffff;
  font-weight: 600;
}

.chronometer-sub {
  font-family: var(--font-mono);
  font-size: 0.6rem;
  letter-spacing: 0.12em;
  color: var(--text-muted);
}

/* --- MAIN WORKSPACE LAYOUT --- */
.workspace-wrapper {
  position: relative;
  z-index: 2;
  display: flex;
  max-width: 1720px;
  margin: 0 auto;
}

/* --- SIDEBAR DOSSIER NAVIGATION RAIL --- */
.sidebar-nav {
  width: 280px;
  min-width: 280px;
  border-right: 1px solid var(--border-subtle);
  background: rgba(0, 0, 0, 0.88);
  backdrop-filter: blur(12px);
  padding: 20px 0;
  position: sticky;
  top: 60px;
  height: calc(100vh - 60px);
  overflow-y: auto;
  transition: width 0.28s cubic-bezier(0.16, 1, 0.3, 1), min-width 0.28s cubic-bezier(0.16, 1, 0.3, 1), transform var(--transition-med);
  z-index: 100;
}

.sidebar-header {
  padding: 0 18px 16px 18px;
  border-bottom: 1px solid var(--border-subtle);
  margin-bottom: 10px;
}

.sidebar-header-main {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}

.sidebar-brand-block {
  display: flex;
  align-items: center;
  gap: 10px;
  min-width: 0;
}

.sidebar-text-col {
  min-width: 0;
}

.sidebar-collapse-btn {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.16);
  color: var(--accent-silver);
  width: 28px;
  height: 28px;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 0.72rem;
  flex-shrink: 0;
}

.sidebar-collapse-btn:hover {
  background: rgba(212, 175, 55, 0.2);
  border-color: var(--accent-gold);
  color: #ffffff;
}

/* Collapsed state */
.sidebar-nav.collapsed {
  width: 72px;
  min-width: 72px;
}

.sidebar-nav.collapsed .sidebar-text-col,
.sidebar-nav.collapsed .sidebar-007-gold-logo,
.sidebar-nav.collapsed .nav-text-wrap,
.sidebar-nav.collapsed .nav-badge {
  display: none !important;
}

.sidebar-nav.collapsed .sidebar-header {
  padding: 0 0 14px 0;
  display: flex;
  justify-content: center;
}

.sidebar-nav.collapsed .sidebar-header-main {
  justify-content: center;
}

.sidebar-nav.collapsed .nav-item {
  justify-content: center;
  padding: 8px 0;
  position: relative;
}

.sidebar-nav.collapsed .nav-ch-num {
  margin: 0;
  width: 38px;
  height: 38px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  font-size: 0.85rem;
  font-weight: 800;
}

.sidebar-nav.collapsed .nav-item.active .nav-ch-num {
  background: rgba(212, 175, 55, 0.25);
  border: 1.5px solid #d4af37;
  color: #d4af37;
  box-shadow: 0 0 12px rgba(212, 175, 55, 0.5);
}

/* Floating HUD tooltip for collapsed state */
.sidebar-nav.collapsed .nav-item:hover::after {
  content: attr(data-tooltip);
  position: absolute;
  left: 74px;
  top: 50%;
  transform: translateY(-50%);
  background: #0a0b0f;
  border: 1px solid var(--accent-gold);
  color: #ffffff;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.08em;
  padding: 7px 14px;
  border-radius: 4px;
  white-space: nowrap;
  box-shadow: 0 6px 25px rgba(0, 0, 0, 0.95), 0 0 12px rgba(212, 175, 55, 0.35);
  z-index: 1000;
  pointer-events: none;
}

.sidebar-tag {
  display: block;
  font-family: var(--font-mono);
  font-size: 0.68rem;
  letter-spacing: 0.16em;
  color: #ffffff;
  font-weight: 700;
}

.sidebar-sub {
  display: block;
  font-family: var(--font-mono);
  font-size: 0.62rem;
  color: var(--text-muted);
  letter-spacing: 0.08em;
  margin-top: 2px;
}

.nav-links {
  display: flex;
  flex-direction: column;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 10px 24px;
  text-decoration: none;
  color: var(--text-muted);
  font-size: 0.8rem;
  border-left: 2px solid transparent;
  transition: all var(--transition-fast);
}

.nav-item:hover {
  color: #ffffff;
  background: rgba(255, 255, 255, 0.03);
  border-left-color: rgba(255, 255, 255, 0.4);
}

.nav-item.active {
  color: #ffffff;
  background: rgba(255, 255, 255, 0.06);
  border-left-color: #ffffff;
  font-weight: 600;
}

.nav-ch-num {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--text-muted);
  min-width: 20px;
}

.nav-item.active .nav-ch-num {
  color: #ffffff;
}

.nav-text-wrap {
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.nav-title {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  letter-spacing: 0.02em;
}

.nav-sub {
  font-family: var(--font-mono);
  font-size: 0.62rem;
  color: var(--text-dim);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* --- MAIN CONTENT AREA --- */
.main-content {
  flex: 1;
  min-width: 0;
  padding: 32px 48px;
}

/* ========================================================================= */
/* --- THE LUXURY 007 HERO SHOWCASE (DRIBBLE REFERENCE FIDELITY) --- */
/* ========================================================================= */
.hero-dribbble-showcase {
  position: relative;
  background: #000000;
  border: 1px solid var(--border-subtle);
  padding: 44px 44px 48px 44px;
  margin-bottom: 40px;
  box-shadow: 0 24px 60px rgba(0, 0, 0, 0.95);
  overflow: visible;
}

.hero-showcase-grid {
  display: grid;
  grid-template-columns: 240px 1fr;
  gap: 48px;
  align-items: start;
}

/* Left Hero Column: Minimalist Menu + Tweets + Social */
.hero-left-column {
  display: flex;
  flex-direction: column;
  gap: 28px;
}

.hero-vert-menu {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.hero-vert-link {
  font-family: var(--font-sans);
  font-size: 0.76rem;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--text-muted);
  text-decoration: none;
  transition: color var(--transition-fast);
  display: inline-block;
  width: fit-content;
}

.hero-vert-link:hover {
  color: #ffffff;
}

.hero-vert-link.active {
  color: #ffffff;
  border-bottom: 2px solid #ffffff;
  padding-bottom: 4px;
}

/* Sleek Tweets / Intelligence Dispatches Card */
.hero-tweets-box {
  background: #08080a;
  border: 1px solid var(--border-subtle);
  padding: 16px;
  margin-top: 10px;
}

.tweets-box-label {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  letter-spacing: 0.18em;
  color: var(--text-dim);
  text-transform: uppercase;
  margin-bottom: 12px;
}

.tweet-user-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 8px;
}

.tweet-avatar-circle {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 1px solid var(--border-subtle);
  background-size: cover;
  background-position: center;
  flex-shrink: 0;
}

.tweet-user-meta {
  display: flex;
  flex-direction: column;
  line-height: 1.2;
}

.tweet-user-name {
  font-size: 0.78rem;
  font-weight: 700;
  color: #ffffff;
  letter-spacing: 0.05em;
  display: flex;
  align-items: center;
  gap: 4px;
}

.verified-badge {
  color: #38bdf8;
  font-size: 0.75rem;
}

.tweet-user-handle {
  font-family: var(--font-mono);
  font-size: 0.62rem;
  color: var(--text-dim);
}

.tweet-body-text {
  font-size: 0.74rem;
  color: var(--silver-300);
  line-height: 1.5;
  margin-top: 6px;
}

.tweet-nav-arrows {
  display: flex;
  gap: 8px;
  margin-top: 12px;
  justify-content: flex-end;
}

.tweet-arrow-btn {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-subtle);
  color: var(--silver-300);
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.7rem;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.tweet-arrow-btn:hover {
  background: #ffffff;
  color: #000000;
}

/* Minimalist Circular Social Icons */
.hero-social-row {
  display: flex;
  gap: 12px;
}

.hero-social-icon {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  border: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-muted);
  text-decoration: none;
  font-size: 0.75rem;
  transition: all var(--transition-fast);
}

.hero-social-icon:hover {
  border-color: #ffffff;
  color: #ffffff;
}

/* Right Hero Column: Headline & Overlapping White Frames */
.hero-right-column {
  display: flex;
  flex-direction: column;
}

.hero-branding-tag {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  letter-spacing: 0.22em;
  color: var(--text-muted);
  text-transform: uppercase;
  margin-bottom: 8px;
}

.hero-cinematic-headline {
  margin-bottom: 22px;
  line-height: 1.1;
}

.headline-title-sidebyside {
  display: block;
  font-family: 'Cinzel', var(--font-serif);
  font-size: clamp(2.4rem, 4.8vw, 4.2rem);
  font-weight: 900;
  color: #ffffff;
  letter-spacing: 0.12em;
  white-space: nowrap;
  text-shadow: 0 0 35px rgba(212, 175, 55, 0.4), 0 2px 4px rgba(0, 0, 0, 0.95);
}

.hero-subtle-tagline {
  display: block;
  font-family: var(--font-sans);
  font-size: 1.05rem;
  font-weight: 600;
  letter-spacing: 0.28em;
  color: var(--accent-gold);
  margin-top: 8px;
  text-transform: uppercase;
  opacity: 0.95;
}

/* THE GRAND OMEGA SEAMASTER 007 MASTER INSTRUMENT STAGE */
.hero-omega-master-stage {
  position: relative;
  width: 100%;
  margin-top: 15px;
  background: radial-gradient(circle at 50% 50%, rgba(22, 24, 30, 0.85) 0%, rgba(10, 11, 15, 0.98) 70%, #050608 100%);
  border: 1.5px solid rgba(255, 255, 255, 0.15);
  box-shadow: 0 25px 70px rgba(0, 0, 0, 0.98), inset 0 0 50px rgba(0, 0, 0, 0.9);
  padding: 24px 28px;
  display: grid;
  grid-template-columns: 280px minmax(320px, 460px) 280px;
  gap: 24px;
  align-items: center;
  justify-content: center;
}

.avatar-007-monogram {
  font-family: var(--font-mono);
  font-size: 0.85rem;
  font-weight: 900;
  letter-spacing: 0.1em;
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #1f2228 0%, #0d0f12 100%);
  border-radius: 50%;
  border: 1px solid rgba(217, 37, 52, 0.5);
  box-shadow: 0 0 8px rgba(217, 37, 52, 0.3);
}

.omega-left-hud-wing, .omega-right-hud-wing {
  display: flex;
  flex-direction: column;
  gap: 14px;
  min-width: 0;
}

.omega-hud-header {
  display: flex;
  align-items: center;
  gap: 10px;
  padding-bottom: 8px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
}

.omega-brand-emblem {
  font-family: 'Cinzel', serif;
  font-size: 1.6rem;
  color: #ffffff;
  font-weight: 700;
  line-height: 1;
}

.omega-hud-title {
  display: block;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  color: #ffffff;
}

.omega-hud-sub {
  display: block;
  font-family: var(--font-mono);
  font-size: 0.56rem;
  letter-spacing: 0.08em;
  color: #dfa868;
}

.omega-readout-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-left: 3px solid #dfa868;
  padding: 10px 14px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.readout-hero-val-row {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
}

.readout-bar-track {
  width: 100%;
  height: 5px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 3px;
  overflow: hidden;
  margin: 4px 0 2px;
}

.readout-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #dfa868 0%, #d92534 100%);
  border-radius: 3px;
  transition: width 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

.readout-unit {
  font-family: var(--font-mono);
  font-size: 0.60rem;
  color: var(--silver-400);
}

.omega-spec-pill-row {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.spec-pill {
  font-family: var(--font-mono);
  font-size: 0.55rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  padding: 3px 7px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: var(--silver-200);
  border-radius: 2px;
}

.omega-center-instrument-wrap {
  width: 100%;
  max-width: 440px;
  aspect-ratio: 460 / 560;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  margin: 0 auto;
}

.omega-seamaster-svg-instrument {
  width: 100%;
  height: 100%;
  filter: drop-shadow(0 20px 45px rgba(0, 0, 0, 0.95)) drop-shadow(0 0 30px rgba(223, 168, 104, 0.15));
}

.seconds-angle-display {
  font-family: var(--font-mono);
  font-size: 1.05rem;
  font-weight: 700;
  color: #ffffff;
  letter-spacing: 0.08em;
  padding: 4px 0;
}

.chrono-action-btns {
  display: flex;
  gap: 8px;
}

.watch-ctrl-btn {
  flex: 1;
  font-family: var(--font-mono);
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  padding: 7px 10px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.18);
  color: var(--silver-200);
  cursor: pointer;
  transition: all 0.2s ease;
  border-radius: 2px;
  text-align: center;
}

.watch-ctrl-btn:hover {
  background: rgba(255, 255, 255, 0.12);
  color: #ffffff;
  border-color: rgba(255, 255, 255, 0.35);
}

.watch-ctrl-btn.active {
  background: rgba(217, 37, 52, 0.18);
  border-color: #d92534;
  color: #ffffff;
}

.omega-spec-card {
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.06);
  padding: 8px 12px;
}

.spec-card-title {
  display: block;
  font-family: var(--font-mono);
  font-size: 0.58rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: #dfa868;
  margin-bottom: 4px;
}

.spec-card-text {
  font-size: 0.68rem;
  line-height: 1.45;
  color: var(--silver-400);
  margin: 0;
}

/* --- SUBTLE HERO TAGLINE --- */
.hero-subtle-tagline {
  display: block;
  font-family: var(--font-mono);
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.38em;
  color: var(--silver-400);
  text-transform: uppercase;
  margin-top: 10px;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.8);
}

/* --- MISSION COUNTDOWN DECK --- */
.hero-countdown-deck {
  background: rgba(12, 14, 18, 0.92);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 8px;
  padding: 12px 20px;
  margin-top: 16px;
  margin-bottom: 22px;
  display: inline-flex;
  flex-direction: column;
  gap: 8px;
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.85), inset 0 0 25px rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  transition: all 0.4s ease;
}

.countdown-hud-header {
  display: flex;
  align-items: center;
  gap: 8px;
}

.countdown-pulse-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: currentColor;
  box-shadow: 0 0 8px currentColor;
  animation: countdownDotBlink 1.4s infinite ease-in-out;
  flex-shrink: 0;
}

@keyframes countdownDotBlink {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.35; transform: scale(0.85); }
}

.countdown-target-label {
  font-family: var(--font-mono);
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  color: var(--silver-200);
  text-transform: uppercase;
}

.countdown-digits-wrapper {
  display: flex;
  align-items: baseline;
  gap: 8px;
  font-family: var(--font-mono);
  font-feature-settings: "tnum";
  font-variant-numeric: tabular-nums;
  transition: color 0.4s ease, text-shadow 0.4s ease;
}

.countdown-segment {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-width: 48px;
}

.cd-num {
  font-family: var(--font-mono);
  font-size: 2.1rem;
  font-weight: 900;
  line-height: 1;
  letter-spacing: 0.05em;
  color: inherit;
}

.cd-lbl {
  font-family: var(--font-mono);
  font-size: 0.54rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: var(--silver-400);
  margin-top: 5px;
}

.cd-divider {
  font-family: var(--font-mono);
  font-size: 1.8rem;
  font-weight: 800;
  line-height: 1;
  opacity: 0.5;
  color: inherit;
  margin-bottom: 14px;
}

/* --- MI6 TACTICAL SATELLITE AUDIO CONSOLE (RIGHT BELOW TITANIUM OMEGA SEAMASTER) --- */
.omega-briefing-console-row {
  grid-column: 1 / -1;
  width: 100%;
  margin-top: 24px;
  position: relative;
  z-index: 5;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.briefing-tactical-deck {
  width: 100%;
  max-width: 920px;
  background: linear-gradient(180deg, rgba(18, 20, 26, 0.98) 0%, rgba(10, 11, 15, 0.99) 100%);
  border: 1.5px solid rgba(217, 37, 52, 0.35);
  border-radius: 8px;
  padding: 14px 20px;
  box-shadow: 0 14px 40px rgba(0, 0, 0, 0.95), 0 0 25px rgba(217, 37, 52, 0.15), inset 0 1px 0 rgba(255, 255, 255, 0.08);
}

/* SATELLITE UPLINK STATUS BAR */
.briefing-sat-status-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-bottom: 10px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  margin-bottom: 10px;
  flex-wrap: wrap;
  gap: 10px;
}
.sat-bar-left {
  display: flex;
  align-items: center;
  gap: 10px;
}
.sat-pulse-led {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #10b981;
  box-shadow: 0 0 8px #10b981;
  animation: pulseGreen 1.4s infinite;
}
.player-briefing-silver-title, .player-briefing-red-title {
  font-family: 'Cinzel', var(--font-serif);
  font-size: 1.45rem;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 0.28em;
  line-height: 1;
  background: linear-gradient(135deg, #ffffff 0%, #e2e8f0 30%, #94a3b8 70%, #f8fafc 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  color: #e2e8f0;
  filter: drop-shadow(0 0 12px rgba(226, 232, 240, 0.75)) drop-shadow(0 1px 3px rgba(0, 0, 0, 0.9));
}
.sat-hud-tag {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  letter-spacing: 0.1em;
  color: var(--accent-silver);
  opacity: 0.85;
}
.sat-freq-badge {
  font-family: var(--font-mono);
  font-size: 0.62rem;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 3px;
  background: rgba(212, 175, 55, 0.12);
  border: 1px solid rgba(212, 175, 55, 0.35);
  color: var(--accent-gold);
  letter-spacing: 0.08em;
}

.sat-bar-right {
  display: flex;
  align-items: center;
  gap: 14px;
}
.sat-signal-meter {
  display: flex;
  align-items: center;
  gap: 6px;
  background: rgba(0, 0, 0, 0.4);
  padding: 3px 8px;
  border-radius: 4px;
  border: 1px solid rgba(255, 255, 255, 0.08);
}
.sig-label {
  font-family: var(--font-mono);
  font-size: 0.58rem;
  color: var(--text-dim);
  letter-spacing: 0.06em;
}
.sig-bars {
  display: flex;
  align-items: flex-end;
  gap: 2px;
  height: 12px;
}
.sig-bars .s-bar {
  width: 3px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 1px;
}
.sig-bars .s-bar:nth-child(1) { height: 4px; }
.sig-bars .s-bar:nth-child(2) { height: 6px; }
.sig-bars .s-bar:nth-child(3) { height: 8px; }
.sig-bars .s-bar:nth-child(4) { height: 10px; }
.sig-bars .s-bar:nth-child(5) { height: 12px; }
.sig-bars .s-bar.active {
  background: #10b981;
  box-shadow: 0 0 4px #10b981;
}
.sig-bars.active .s-bar.active {
  background: #ef4444;
  box-shadow: 0 0 6px #ef4444;
  animation: signalPulse 0.8s ease-in-out infinite alternate;
}
@keyframes signalPulse {
  0% { opacity: 0.6; }
  100% { opacity: 1; }
}

.sat-status-pill {
  font-family: var(--font-mono);
  font-size: 0.64rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  padding: 3px 9px;
  border-radius: 3px;
  background: rgba(16, 185, 129, 0.15);
  border: 1px solid rgba(16, 185, 129, 0.4);
  color: #10b981;
  text-transform: uppercase;
}
.sat-status-pill.live {
  background: rgba(217, 37, 52, 0.2);
  border-color: rgba(217, 37, 52, 0.6);
  color: #ef4444;
  box-shadow: 0 0 10px rgba(217, 37, 52, 0.4);
}

/* ORBITAL & TELEMETRY COMPLICATIONS STRIP */
.briefing-complications-strip {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 10px;
  padding: 8px 12px;
  background: rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 4px;
  margin-bottom: 12px;
}
.sat-telemetry-col {
  display: flex;
  flex-direction: column;
  gap: 2px;
}
.comp-label {
  font-family: var(--font-mono);
  font-size: 0.54rem;
  color: var(--text-dim);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}
.comp-val {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  color: #ffffff;
  font-weight: 700;
  letter-spacing: 0.06em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* MAIN DECK ROW */
.briefing-deck-main-row {
  display: flex;
  align-items: center;
  gap: 16px;
  width: 100%;
}

/* --- COMPLICATED MI6 Q-BRANCH TACTICAL ENGAGEMENT TRIGGER ("PLAY BRIEFING" BUTTON) --- */
.briefing-master-play-btn {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 14px;
  background: linear-gradient(145deg, #181b22 0%, #0c0e12 60%, #14171e 100%);
  border: 1.5px solid rgba(212, 175, 55, 0.4);
  border-radius: 6px;
  padding: 10px 18px 10px 14px;
  cursor: pointer;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.9), inset 0 1px 0 rgba(255, 255, 255, 0.2), inset 0 0 14px rgba(0, 0, 0, 0.8);
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  overflow: hidden;
  user-select: none;
  text-align: left;
}

.briefing-master-play-btn:hover {
  border-color: rgba(212, 175, 55, 0.85);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.95), 0 0 20px rgba(212, 175, 55, 0.25), inset 0 1px 0 rgba(255, 255, 255, 0.35);
  transform: translateY(-1px);
}

.briefing-master-play-btn:active {
  transform: translateY(1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.9);
}

/* Playing state */
.briefing-master-play-btn.is-playing {
  border-color: rgba(16, 185, 129, 0.65);
  background: linear-gradient(145deg, #0e1a17 0%, #06110e 60%, #0a1713 100%);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.9), 0 0 22px rgba(16, 185, 129, 0.25), inset 0 1px 0 rgba(16, 185, 129, 0.3);
}

/* 4 Corner Hex Screws / Rivets */
.btn-hex-screw {
  position: absolute;
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #374151;
  border: 1px solid #111827;
  box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.35);
}
.btn-hex-screw.tl { top: 3px; left: 3px; }
.btn-hex-screw.tr { top: 3px; right: 3px; }
.btn-hex-screw.bl { bottom: 3px; left: 3px; }
.btn-hex-screw.br { bottom: 3px; right: 3px; }

/* Left: Reticle / Radar Target Cluster */
.btn-reticle-cluster {
  position: relative;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(217, 37, 52, 0.15) 0%, rgba(0, 0, 0, 0.6) 80%);
  border: 1.5px solid rgba(212, 175, 55, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.8), inset 0 0 8px rgba(217, 37, 52, 0.2);
}

.briefing-master-play-btn.is-playing .btn-reticle-cluster {
  border-color: rgba(16, 185, 129, 0.7);
  background: radial-gradient(circle, rgba(16, 185, 129, 0.2) 0%, rgba(0, 0, 0, 0.6) 80%);
  box-shadow: 0 0 12px rgba(16, 185, 129, 0.35);
}

.btn-reticle-ring {
  position: absolute;
  inset: 2px;
  border-radius: 50%;
  border: 1px dashed rgba(255, 255, 255, 0.25);
  animation: reticleSpin 12s linear infinite;
}

.briefing-master-play-btn.is-playing .btn-reticle-ring {
  border-color: rgba(16, 185, 129, 0.5);
  animation: reticleSpin 4s linear infinite;
}

@keyframes reticleSpin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.btn-reticle-crosshair {
  position: absolute;
  inset: 0;
  pointer-events: none;
}
.btn-reticle-crosshair::before,
.btn-reticle-crosshair::after {
  content: '';
  position: absolute;
  background: rgba(255, 255, 255, 0.2);
}
.btn-reticle-crosshair::before {
  top: 50%; left: 2px; right: 2px; height: 1px;
}
.btn-reticle-crosshair::after {
  left: 50%; top: 2px; bottom: 2px; width: 1px;
}

.briefing-btn-icon {
  font-size: 0.95rem;
  color: #ffffff;
  position: relative;
  z-index: 2;
  text-shadow: 0 0 8px rgba(255, 255, 255, 0.6);
  margin-left: 2px;
}

.briefing-master-play-btn.is-playing .briefing-btn-icon {
  color: #10b981;
  text-shadow: 0 0 8px rgba(16, 185, 129, 0.8);
  margin-left: 0;
}

/* Center: Multi-Tier Typography */
.btn-label-stack {
  display: flex;
  flex-direction: column;
  gap: 2px;
  min-width: 140px;
}

.btn-telemetry-micro {
  display: flex;
  align-items: center;
  gap: 6px;
  font-family: var(--font-mono);
  font-size: 0.55rem;
  letter-spacing: 0.08em;
  color: var(--text-dim);
}

.btn-beacon-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #eab308;
  box-shadow: 0 0 5px #eab308;
  animation: pulseAmber 1.2s infinite;
}

.briefing-master-play-btn.is-playing .btn-beacon-dot {
  background: #10b981;
  box-shadow: 0 0 6px #10b981;
  animation: pulseGreen 0.9s infinite;
}

.btn-enc-tag {
  background: rgba(212, 175, 55, 0.15);
  border: 1px solid rgba(212, 175, 55, 0.35);
  color: var(--accent-gold);
  padding: 1px 4px;
  border-radius: 2px;
  font-size: 0.5rem;
  font-weight: 700;
  letter-spacing: 0.06em;
}

.briefing-btn-label {
  font-family: 'Cinzel', var(--font-serif);
  font-size: 0.88rem;
  font-weight: 900;
  letter-spacing: 0.14em;
  color: #ffffff;
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
  line-height: 1.1;
}

.briefing-master-play-btn.is-playing .briefing-btn-label {
  color: #a7f3d0;
  text-shadow: 0 0 10px rgba(16, 185, 129, 0.5);
}

.btn-sub-directive {
  font-family: var(--font-mono);
  font-size: 0.54rem;
  color: #94a3b8;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

/* Right: Micro Waveform Matrix */
.btn-micro-eq {
  display: flex;
  align-items: flex-end;
  gap: 2px;
  height: 18px;
  padding: 2px 4px;
  background: rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 3px;
  flex-shrink: 0;
}

.btn-micro-eq .meq-bar {
  width: 2.5px;
  height: 4px;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 1px;
  transition: height 0.15s ease;
}

.briefing-master-play-btn.is-playing .btn-micro-eq .meq-bar {
  background: linear-gradient(to top, #10b981, #d4af37);
  animation: microEqBounce 0.6s ease-in-out infinite alternate;
}
.briefing-master-play-btn.is-playing .btn-micro-eq .mb-1 { animation-delay: 0.05s; }
.briefing-master-play-btn.is-playing .btn-micro-eq .mb-2 { animation-delay: 0.25s; }
.briefing-master-play-btn.is-playing .btn-micro-eq .mb-3 { animation-delay: 0.15s; }
.briefing-master-play-btn.is-playing .btn-micro-eq .mb-4 { animation-delay: 0.35s; }

@keyframes microEqBounce {
  0% { height: 3px; }
  100% { height: 16px; }
}

/* Laser sweep reflection */
.btn-scanner-sweep {
  position: absolute;
  top: 0;
  left: -100%;
  width: 50%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.12), transparent);
  transform: skewX(-20deg);
  pointer-events: none;
}

.briefing-master-play-btn:hover .btn-scanner-sweep {
  animation: laserSweep 1.2s cubic-bezier(0.16, 1, 0.3, 1) infinite;
}

@keyframes laserSweep {
  0% { left: -100%; }
  100% { left: 200%; }
}

/* EQUALIZER SPECTRUM */
.briefing-eq-spectrum {
  display: flex;
  align-items: flex-end;
  gap: 3px;
  height: 28px;
  padding: 0 6px;
  background: rgba(0, 0, 0, 0.55);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 4px;
}
.briefing-eq-spectrum .eq-col {
  width: 4px;
  height: 4px;
  background: linear-gradient(to top, #d92534, #d4af37);
  border-radius: 1px;
  transition: height 0.15s ease;
}
.briefing-eq-spectrum.active .eq-col {
  animation: eqBounce 0.75s ease-in-out infinite alternate;
}
.briefing-eq-spectrum.active .col-1  { animation-delay: 0.05s; }
.briefing-eq-spectrum.active .col-2  { animation-delay: 0.22s; }
.briefing-eq-spectrum.active .col-3  { animation-delay: 0.12s; }
.briefing-eq-spectrum.active .col-4  { animation-delay: 0.38s; }
.briefing-eq-spectrum.active .col-5  { animation-delay: 0.18s; }
.briefing-eq-spectrum.active .col-6  { animation-delay: 0.42s; }
.briefing-eq-spectrum.active .col-7  { animation-delay: 0.28s; }
.briefing-eq-spectrum.active .col-8  { animation-delay: 0.50s; }
.briefing-eq-spectrum.active .col-9  { animation-delay: 0.15s; }
.briefing-eq-spectrum.active .col-10 { animation-delay: 0.32s; }
.briefing-eq-spectrum.active .col-11 { animation-delay: 0.25s; }
.briefing-eq-spectrum.active .col-12 { animation-delay: 0.45s; }
.briefing-eq-spectrum.active .col-13 { animation-delay: 0.08s; }
.briefing-eq-spectrum.active .col-14 { animation-delay: 0.35s; }
.briefing-eq-spectrum.active .col-15 { animation-delay: 0.20s; }
.briefing-eq-spectrum.active .col-16 { animation-delay: 0.48s; }

@keyframes eqBounce {
  0% { height: 4px; }
  35% { height: 18px; }
  65% { height: 10px; }
  100% { height: 26px; }
}

/* SCRUBBER TRACK WITH TICKS */
.briefing-timeline-wrap {
  flex: 1;
  min-width: 180px;
  display: flex;
  align-items: center;
  gap: 12px;
}
.briefing-scrubber-track {
  flex: 1;
  height: 8px;
  background: rgba(255, 255, 255, 0.12);
  border-radius: 4px;
  cursor: pointer;
  position: relative;
  transition: height 0.15s ease;
}
.briefing-scrubber-ticks {
  position: absolute;
  inset: 0;
  display: flex;
  justify-content: space-between;
  pointer-events: none;
  padding: 0 4px;
  align-items: center;
}
.briefing-scrubber-ticks .tick {
  width: 1px;
  height: 4px;
  background: rgba(255, 255, 255, 0.2);
}
.briefing-scrubber-fill {
  height: 100%;
  background: linear-gradient(90deg, #d92534, #ef4444);
  box-shadow: 0 0 10px rgba(217, 37, 52, 0.8);
  border-radius: 4px;
  width: 0%;
  position: relative;
}
.scrubber-head {
  position: absolute;
  right: -3px;
  top: 50%;
  transform: translateY(-50%);
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #ffffff;
  box-shadow: 0 0 6px #ef4444;
}

.briefing-time-readout {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--accent-silver);
  letter-spacing: 0.08em;
  white-space: nowrap;
}
.briefing-time-sep {
  opacity: 0.4;
  margin: 0 2px;
}

.briefing-deck-tools {
  display: flex;
  align-items: center;
  gap: 10px;
}
.briefing-tool-btn {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: var(--text-dim);
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  padding: 6px 10px;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s ease;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}
.briefing-tool-btn:hover {
  background: rgba(255, 255, 255, 0.14);
  color: #ffffff;
  border-color: rgba(255, 255, 255, 0.3);
}
.briefing-tool-btn.active {
  background: rgba(217, 37, 52, 0.25);
  border-color: rgba(217, 37, 52, 0.7);
  color: #ffffff;
  box-shadow: 0 0 8px rgba(217, 37, 52, 0.4);
}
.briefing-vol-slider {
  width: 70px;
  accent-color: #d92534;
  cursor: pointer;
}

/* FOOTER PROTOCOL CHIP */
.briefing-deck-sub-strip {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 8px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  margin-top: 10px;
  flex-wrap: wrap;
  gap: 8px;
}
.sub-chip {
  font-family: var(--font-mono);
  font-size: 0.58rem;
  color: var(--text-dim);
  letter-spacing: 0.06em;
  display: inline-flex;
  align-items: center;
  gap: 5px;
}
.chip-dot {
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: var(--accent-gold);
}

.readout-label {
  display: block;
  font-family: var(--font-mono);
  font-size: 0.52rem;
  letter-spacing: 0.08em;
  color: var(--text-dim);
}

.readout-val {
  display: block;
  font-family: var(--font-sans);
  font-size: 1.15rem;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.2;
}

.readout-desc {
  display: block;
  font-family: var(--font-mono);
  font-size: 0.50rem;
  color: var(--text-muted);
}

.omega-interactive-note {
  display: flex;
  align-items: center;
  gap: 6px;
  font-family: var(--font-mono);
  font-size: 0.52rem;
  color: var(--silver-300);
  letter-spacing: 0.05em;
  padding: 4px 6px;
  background: rgba(217, 37, 52, 0.08);
  border: 1px solid rgba(217, 37, 52, 0.25);
}

.pulse-indicator-red {
  width: 5px;
  height: 5px;
  background: #d92534;
  border-radius: 50%;
  box-shadow: 0 0 6px #d92534;
  animation: pulseDot 1.2s infinite;
  flex-shrink: 0;
}

.omega-frame-status {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  font-weight: 700;
  color: #38bdf8;
  margin-top: 6px;
  letter-spacing: 0.08em;
}

/* Technical Leader Line for Watch Frame */
.callout-watch-lead {
  position: absolute;
  top: -34px;
  right: 40px;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.callout-watch-label {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  letter-spacing: 0.16em;
  color: #ffffff;
  text-transform: uppercase;
  margin-bottom: 4px;
}

.callout-watch-line {
  width: 1px;
  height: 16px;
  background: #ffffff;
}

/* Bottom Right Carousel Pagination Dots */
.hero-carousel-dots {
  position: absolute;
  bottom: -40px;
  right: 0;
  display: flex;
  align-items: center;
  gap: 8px;
}

.dot-pill-active {
  width: 28px;
  height: 4px;
  background: #ffffff;
}

.dot-circle-inactive {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.25);
}

/* --- THREE GLOBAL LEARNING ENVIRONMENTS SWITCHER --- */
.environment-switcher {
  display: flex;
  flex-wrap: wrap;
  gap: 0;
  border: 1px solid var(--border-subtle);
  background: #000000;
  margin-top: 36px;
  margin-bottom: 36px;
}

.env-btn {
  flex: 1;
  min-width: 200px;
  background: transparent;
  border: none;
  border-right: 1px solid var(--border-subtle);
  color: var(--text-muted);
  font-family: var(--font-sans);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  padding: 16px 20px;
  cursor: pointer;
  transition: all var(--transition-fast);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  position: relative;
}

.env-btn:last-child {
  border-right: none;
}

.env-btn:hover {
  color: #ffffff;
  background: rgba(255, 255, 255, 0.03);
}

.env-btn.active {
  color: #000000;
  background: #ffffff;
}

.env-btn.active .bullet {
  color: #000000;
}

.bullet {
  font-size: 0.65rem;
  color: var(--text-dim);
}

/* ========================================================================= */
/* --- CHAPTER DOSSIERS & CARDS (SHARP TUXEDO ARCHITECTURE) --- */
/* ========================================================================= */
.mission-chapter, .chapter-container {
  background: #050507;
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-none);
  margin-bottom: 40px;
  padding: 32px 36px;
  position: relative;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.9);
  transition: border-color var(--transition-med);
}

.mission-chapter:hover, .chapter-container:hover {
  border-color: var(--border-medium);
}

.chapter-header {
  border-bottom: 1px solid var(--border-subtle);
  padding-bottom: 18px;
  margin-bottom: 24px;
}

.briefing-tag, .ch-code-pill {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  letter-spacing: 0.18em;
  color: var(--text-muted);
  text-transform: uppercase;
  margin-bottom: 6px;
  display: inline-block;
}

.chapter-title, .ch-title {
  font-family: var(--font-serif);
  font-size: 1.65rem;
  color: #ffffff;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.classified-stamp {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  color: #ffffff;
  letter-spacing: 0.16em;
  border: 1px solid #ffffff;
  padding: 3px 8px;
  display: inline-block;
  margin-top: 8px;
  text-transform: uppercase;
}

/* Tabs: Underlined Minimalist Luxury */
.tab-nav, .chapter-nav-tabs {
  display: flex;
  gap: 24px;
  border-bottom: 1px solid var(--border-subtle);
  margin-bottom: 28px;
  flex-wrap: wrap;
}

.tab-btn, .ch-tab-btn {
  background: transparent;
  border: none;
  border-bottom: 2px solid transparent;
  color: var(--text-muted);
  font-family: var(--font-sans);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  padding: 8px 4px 12px 4px;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.tab-btn:hover, .ch-tab-btn:hover {
  color: #ffffff;
}

.tab-btn.active, .ch-tab-btn.active {
  color: #ffffff;
  border-bottom-color: #ffffff;
}

.subtab-content {
  display: none;
}

.subtab-content.active {
  display: block;
}

/* Intelligence Cards */
.intel-card, .ch-card {
  background: #08080a;
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-none);
  padding: 24px 28px;
  margin-bottom: 24px;
}

.intel-card:hover, .ch-card:hover {
  border-color: var(--border-medium);
}

.intel-card h3, .topic-title {
  font-family: var(--font-serif);
  font-size: 1.25rem;
  color: #ffffff;
  font-weight: 700;
  letter-spacing: 0.05em;
  margin-bottom: 14px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.intel-card h4 {
  font-family: var(--font-sans);
  font-size: 0.95rem;
  font-weight: 700;
  color: #ffffff;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  margin-top: 18px;
  margin-bottom: 10px;
}

/* Solution Reveal Cards (Unified for All 13 Chapters) */
.solution-card, .gold-solution-block, .solution-debrief-container {
  display: none;
  background: #08090d;
  border: 1px solid rgba(255, 255, 255, 0.16);
  border-left: 3px solid #e2b475;
  border-radius: var(--radius-none);
  padding: 24px 28px;
  margin-top: 18px;
  margin-bottom: 24px;
  box-shadow: 0 14px 35px rgba(0, 0, 0, 0.95);
  transition: all 0.25s ease;
}

.solution-card.revealed, .gold-solution-block.revealed, .solution-debrief-container.revealed {
  display: block !important;
  animation: fadeIn 0.28s cubic-bezier(0.16, 1, 0.3, 1);
}

.action-btn.revealed-active, .reveal-solution-btn.revealed-active {
  background: #d92534 !important;
  color: #ffffff !important;
  border-color: #d92534 !important;
  box-shadow: 0 0 12px rgba(217, 37, 52, 0.4);
}

/* Practice Section Solution Diagrams */
.solution-svg-diagram {
  margin: 16px 0;
  background: #050608;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 4px;
  padding: 12px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.solution-svg-diagram svg {
  max-width: 520px;
  width: 100%;
  height: auto;
  display: block;
}

.solution-svg-caption {
  margin-top: 8px;
  font-family: var(--font-mono);
  font-size: 0.65rem;
  letter-spacing: 0.08em;
  color: #e2b475;
  text-transform: uppercase;
}

/* Interactive Graph Lab Reset Button */
.graph-reset-btn {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: var(--silver-200);
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 6px 14px;
  border-radius: 2px;
  cursor: pointer;
  transition: all var(--transition-fast);
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.graph-reset-btn:hover {
  background: rgba(217, 37, 52, 0.15);
  border-color: #d92534;
  color: #ffffff;
  box-shadow: 0 0 10px rgba(217, 37, 52, 0.3);
}

/* Master Graphical Intelligence Atlas (Chapter 13) */
.graphical-atlas-container {
  display: flex;
  flex-direction: column;
  gap: 32px;
  margin-top: 10px;
}

.atlas-header-banner {
  background: linear-gradient(135deg, rgba(20, 22, 28, 0.95) 0%, rgba(8, 9, 12, 0.98) 100%);
  border: 1.5px solid rgba(255, 255, 255, 0.18);
  border-left: 4px solid #e2b475;
  padding: 24px 30px;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.9);
}

.atlas-badge {
  font-family: var(--font-mono);
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  color: #d92534;
  margin-bottom: 6px;
}

.atlas-title {
  font-family: var(--font-serif);
  font-size: 1.5rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  color: #ffffff;
  margin-bottom: 6px;
}

.atlas-subtitle {
  font-family: var(--font-sans);
  font-size: 0.88rem;
  color: var(--silver-400);
  line-height: 1.5;
  margin: 0;
}

.atlas-quick-nav {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
  padding: 14px 18px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.quick-nav-label {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  font-weight: 700;
  color: var(--silver-400);
  margin-right: 4px;
}

.quick-nav-pill {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  font-weight: 700;
  color: var(--silver-300);
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.15);
  padding: 5px 12px;
  text-decoration: none;
  transition: all var(--transition-fast);
}

.quick-nav-pill:hover {
  background: rgba(226, 180, 117, 0.15);
  border-color: #e2b475;
  color: #ffffff;
}

.atlas-section-group {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.atlas-group-header {
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
  padding-bottom: 12px;
}

.group-num {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  font-weight: 700;
  color: #e2b475;
  letter-spacing: 0.14em;
}

.group-title {
  font-family: var(--font-serif);
  font-size: 1.22rem;
  font-weight: 700;
  color: #ffffff;
  margin: 4px 0 6px 0;
}

.group-desc {
  font-family: var(--font-sans);
  font-size: 0.82rem;
  color: var(--silver-400);
  margin: 0;
}

.atlas-card {
  background: #08090d;
  border: 1.5px solid rgba(255, 255, 255, 0.12);
  border-left: 3px solid #e2b475;
  padding: 22px 24px;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.9);
}

.atlas-card-header {
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  padding-bottom: 10px;
  margin-bottom: 16px;
}

.scen-badge {
  font-family: var(--font-mono);
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  color: #38bdf8;
}

.scen-title {
  font-family: var(--font-sans);
  font-size: 1.05rem;
  font-weight: 700;
  color: #ffffff;
  margin: 4px 0;
}

.scen-ref {
  font-family: var(--font-mono);
  font-size: 0.58rem;
  color: var(--silver-400);
}

.atlas-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 22px;
  align-items: start;
}

@media (max-width: 980px) {
  .atlas-grid {
    grid-template-columns: 1fr;
  }
}

.atlas-svg-panel {
  display: flex;
  align-items: center;
  justify-content: center;
}

.atlas-svg {
  width: 100%;
  height: auto;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 4px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.8);
}

.atlas-text-panel {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.scorecard-table-wrap {
  overflow-x: auto;
  margin-top: 6px;
}

.scorecard-table {
  width: 100%;
  border-collapse: collapse;
  font-family: var(--font-mono);
  font-size: 0.68rem;
}

.scorecard-table th, .scorecard-table td {
  padding: 6px 10px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  text-align: left;
}

.scorecard-table th {
  background: rgba(255, 255, 255, 0.05);
  color: #e2b475;
}

.scorecard-table td.pos-val {
  color: #10b981;
  font-weight: 700;
}

.scorecard-table td.neg-val {
  color: #ef4444;
  font-weight: 700;
}

.trap-warning-box {
  background: rgba(217, 37, 52, 0.08);
  border: 1px solid rgba(217, 37, 52, 0.3);
  padding: 10px 14px;
  font-family: var(--font-sans);
  font-size: 0.78rem;
  color: var(--silver-300);
  line-height: 1.5;
}

.trap-tag {
  color: #d92534;
  font-weight: 700;
  font-family: var(--font-mono);
  font-size: 0.65rem;
  margin-right: 6px;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

.step-list {
  list-style: none;
  padding-left: 0;
  margin-top: 14px;
}

.step-item, .sop-step {
  position: relative;
  padding-left: 20px;
  margin-bottom: 18px;
  border-left: 1px solid rgba(255, 255, 255, 0.3);
}

.step-title, .sop-step-title {
  font-family: var(--font-mono);
  font-size: 0.76rem;
  font-weight: 700;
  color: #ffffff;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 6px;
}

/* Progressive Hints */
.hint-container, .hints-container {
  margin-top: 16px;
  margin-bottom: 18px;
}

.hint-btn, .hint-trigger-btn {
  background: transparent;
  border: 1px solid var(--border-subtle);
  color: var(--text-muted);
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 7px 14px;
  cursor: pointer;
  margin-right: 8px;
  margin-bottom: 8px;
  transition: all var(--transition-fast);
}

.hint-btn:hover, .hint-trigger-btn:hover,
.hint-btn.active, .hint-trigger-btn.active {
  border-color: #ffffff;
  color: #ffffff;
  background: rgba(255, 255, 255, 0.04);
}

.hint-text, .hint-content-box {
  display: none;
  background: #0c0c10;
  border: 1px solid var(--border-subtle);
  border-left: 2px solid var(--silver-400);
  padding: 12px 18px;
  font-size: 0.85rem;
  color: #ffffff;
  margin-top: 8px;
  margin-bottom: 12px;
}

.hint-text.visible, .hint-content-box.visible {
  display: block !important;
}

/* Action Trigger Buttons */
.action-btn, .reveal-solution-btn {
  background: #ffffff;
  border: 1px solid #ffffff;
  color: #000000;
  font-family: var(--font-sans);
  font-size: 0.76rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 11px 22px;
  border-radius: var(--radius-none);
  cursor: pointer;
  transition: all var(--transition-fast);
  display: inline-flex;
  align-items: center;
  gap: 10px;
}

.action-btn:hover, .reveal-solution-btn:hover {
  background: #000000;
  color: #ffffff;
  border-color: #ffffff;
}

/* Difficulty & Classification Badges */
.difficulty-pill, .ch-code-pill {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  padding: 4px 10px;
  border-radius: var(--radius-none);
  letter-spacing: 0.1em;
  display: inline-block;
  text-transform: uppercase;
}

.pill-hard {
  border: 1px solid #ef4444;
  color: #ef4444;
  background: transparent;
}

.pill-med {
  border: 1px solid #f59e0b;
  color: #f59e0b;
  background: transparent;
}

.pill-exam {
  border: 1px solid #ffffff;
  color: #ffffff;
  background: transparent;
}

.mission-id {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--text-muted);
  letter-spacing: 0.1em;
}

.mission-status-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  padding-bottom: 10px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

/* Data Tables */
.data-table {
  width: 100%;
  border-collapse: collapse;
  margin: 18px 0;
  font-size: 0.85rem;
}

.data-table th, .data-table td {
  padding: 12px 16px;
  border: 1px solid var(--border-subtle);
  text-align: left;
}

.data-table th {
  background: rgba(255, 255, 255, 0.05);
  color: #ffffff;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.data-table tr:hover {
  background: rgba(255, 255, 255, 0.02);
}

/* Formula Callouts */
.formula-box, .concept-box {
  background: #000000;
  border: 1px solid var(--border-medium);
  border-radius: var(--radius-none);
  padding: 16px 22px;
  margin: 16px 0;
  font-family: var(--font-mono);
  overflow-x: auto;
}

.warning-box {
  background: #0a0505;
  border: 1px solid rgba(217, 37, 52, 0.4);
  border-left: 3px solid var(--bond-crimson);
  border-radius: var(--radius-none);
  padding: 14px 20px;
  margin: 16px 0;
  font-size: 0.88rem;
  color: #ffffff;
}

/* Metric Grids */
.grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
  margin-top: 16px;
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
  margin-top: 16px;
}

.metric-box {
  background: #000000;
  border: 1px solid var(--border-subtle);
  padding: 16px;
}

.metric-label {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  color: var(--text-muted);
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.metric-val {
  font-family: var(--font-mono);
  font-size: 1.25rem;
  font-weight: 700;
  color: #ffffff;
  margin-top: 6px;
}

/* Interactive Canvas Lab Screens */
.canvas-lab-container, .graph-display-panel {
  background: #000000;
  border: 1px solid var(--border-medium);
  padding: 20px;
  margin: 20px 0;
  position: relative;
}

.canvas-screen, .canvas-viewport-wrap canvas {
  width: 100%;
  max-width: 100%;
  display: block;
  background: #000000;
}

.canvas-controls, .graph-controls-toolbar {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid var(--border-subtle);
}

.control-group, .slider-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
  flex: 1;
  min-width: 180px;
}

.control-group label, .slider-group label {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  color: var(--text-muted);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.control-group input[type="range"], .slider-group input[type="range"] {
  accent-color: #ffffff;
}

/* Telemetry Readouts */
.graph-telemetry-readout {
  display: flex;
  flex-wrap: wrap;
  gap: 18px;
  margin-top: 14px;
  padding-top: 12px;
  border-top: 1px dashed var(--border-subtle);
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.06em;
}

.telemetry-item {
  color: var(--text-muted);
}

.telemetry-item span {
  color: #ffffff;
  font-weight: 700;
}

/* Master Footer */
.master-footer {
  border-top: 1px solid var(--border-subtle);
  padding: 44px 0 28px 0;
  margin-top: 60px;
  background: #000000;
}

.footer-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 24px;
  padding-bottom: 24px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.footer-brand {
  display: flex;
  align-items: center;
  gap: 16px;
}

.footer-logo {
  display: flex;
  align-items: center;
}

/* --- GOLD 007 METALLIC LOGO STYLING --- */
.header-007-gold-logo-img {
  height: 38px;
  width: auto;
  display: block;
  filter: drop-shadow(0 0 10px rgba(212, 175, 55, 0.45));
  transition: transform 0.2s ease, filter 0.2s ease;
}
.header-007-gold-logo-img:hover {
  transform: scale(1.04);
  filter: drop-shadow(0 0 18px rgba(212, 175, 55, 0.8));
}
.footer-007-gold-logo-img {
  height: 52px;
  width: auto;
  display: block;
  filter: drop-shadow(0 0 12px rgba(212, 175, 55, 0.5));
}
.sidebar-007-gold-logo {
  height: 24px;
  width: auto;
  display: block;
  filter: drop-shadow(0 0 8px rgba(212, 175, 55, 0.4));
}
.hero-007-gold-tag-logo {
  height: 18px;
  width: auto;
  display: inline-block;
  vertical-align: middle;
  margin-right: 8px;
  filter: drop-shadow(0 0 6px rgba(212, 175, 55, 0.5));
}

.footer-info h4 {
  font-family: var(--font-serif);
  font-size: 0.95rem;
  color: #ffffff;
  letter-spacing: 0.06em;
}

.footer-info p {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  color: var(--text-muted);
}

.footer-badges {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.f-badge {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  color: var(--text-muted);
  border: 1px solid var(--border-subtle);
  padding: 4px 10px;
  letter-spacing: 0.08em;
}

.copyright-notice {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  color: var(--text-dim);
  line-height: 1.6;
  margin-top: 20px;
}

/* ========================================================================= */
/* --- MI6 ACCESS CLEARANCE GATE (BOND THEMED PLAIN SIMPLE WHITE PAGE) --- */
/* ========================================================================= */
.mi6-gate-overlay {
  position: fixed;
  inset: 0;
  z-index: 999999;
  background: #ffffff;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding: 36px 20px;
  overflow-y: auto;
  transition: opacity 0.5s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.5s cubic-bezier(0.16, 1, 0.3, 1);
  box-sizing: border-box;
}

.mi6-gate-overlay.unlocked {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}

body.gate-locked {
  overflow: hidden !important;
}

/* Ambient Crest Watermarks on White Background Canvas */
.gate-bg-crest {
  position: fixed;
  top: 50%;
  transform: translateY(-50%);
  pointer-events: none;
  user-select: none;
  display: flex;
  flex-direction: column;
  align-items: center;
  opacity: 0.12;
  transition: opacity 0.3s ease;
  z-index: 1;
}

.gate-bg-crest-left {
  left: 3.5vw;
}

.gate-bg-crest-right {
  right: 3.5vw;
}

.gate-watermark-crest {
  width: 190px;
  height: 190px;
  object-fit: contain;
  filter: contrast(1.05);
}

.gate-watermark-label {
  font-family: var(--font-mono);
  font-size: 0.58rem;
  font-weight: 700;
  letter-spacing: 0.16em;
  color: #4b5563;
  margin-top: 10px;
  text-transform: uppercase;
}

@media (max-width: 1250px) {
  .gate-bg-crest {
    display: none;
  }
}

.gate-content-container {
  width: 100%;
  max-width: 520px;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  z-index: 2;
  margin: auto 0;
}

/* Provenance & Heraldic Header */
.gate-accreditation-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  margin-bottom: 18px;
  padding: 10px 18px;
  background: #fbfbfb;
  border: 1px solid #eef0f2;
  border-radius: 10px;
  box-sizing: border-box;
  gap: 12px;
}

.gate-header-crest-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.gate-header-crest-img {
  width: 36px;
  height: 36px;
  object-fit: contain;
  filter: drop-shadow(0 1px 2px rgba(0, 0, 0, 0.08));
}

.gate-provenance-center {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  flex: 1;
  text-align: center;
}

.gate-provenance-title {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: #374151;
  text-transform: uppercase;
  white-space: nowrap;
}

.gate-badge-dot {
  width: 6px;
  height: 6px;
  background: #059669;
  border-radius: 50%;
  display: inline-block;
  flex-shrink: 0;
  box-shadow: 0 0 6px rgba(5, 150, 105, 0.6);
}

@media (max-width: 560px) {
  .gate-provenance-title {
    font-size: 0.52rem;
    letter-spacing: 0.04em;
    white-space: normal;
  }
}

.mi6-gate-card {
  background: #ffffff;
  width: 100%;
  padding: 38px 36px;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.06), 0 4px 16px rgba(0, 0, 0, 0.03);
  text-align: center;
  position: relative;
  transition: transform 0.2s ease;
  box-sizing: border-box;
}

@keyframes gateShake {
  0%, 100% { transform: translateX(0); }
  20%, 60% { transform: translateX(-8px); }
  40%, 80% { transform: translateX(8px); }
}

.mi6-gate-card.shake {
  animation: gateShake 0.4s ease-in-out;
}

.gate-logo-wrapper {
  position: relative;
  display: inline-block;
  margin: 0 auto 16px auto;
}

.gate-007-black-logo {
  height: 48px;
  width: auto;
  margin: 0 auto;
  display: block;
  filter: drop-shadow(0 2px 6px rgba(0, 0, 0, 0.14));
}

.barrel-shimmer-sparkle {
  position: absolute;
  top: 3.5%;
  right: 0%;
  transform: translate(50%, -50%);
  width: 16px;
  height: 16px;
  pointer-events: none;
  display: flex;
  align-items: center;
  justify-content: center;
  animation: barrelShimmerPulse 3.5s ease-in-out infinite;
}

.barrel-shimmer-core {
  position: absolute;
  width: 3.5px;
  height: 3.5px;
  background: #ffffff;
  border-radius: 50%;
  box-shadow: 0 0 6px 1.5px rgba(255, 255, 255, 0.95), 0 0 10px 3px rgba(180, 210, 255, 0.7);
}

.barrel-shimmer-ray-h {
  position: absolute;
  width: 16px;
  height: 1.5px;
  background: linear-gradient(90deg, transparent 0%, rgba(255, 255, 255, 0.92) 50%, transparent 100%);
  border-radius: 1px;
}

.barrel-shimmer-ray-v {
  position: absolute;
  width: 1.5px;
  height: 16px;
  background: linear-gradient(180deg, transparent 0%, rgba(255, 255, 255, 0.92) 50%, transparent 100%);
  border-radius: 1px;
}

@keyframes barrelShimmerPulse {
  0%, 100% {
    opacity: 0.15;
    transform: translate(50%, -50%) scale(0.6) rotate(0deg);
  }
  30% {
    opacity: 0.25;
    transform: translate(50%, -50%) scale(0.7) rotate(15deg);
  }
  45% {
    opacity: 1;
    transform: translate(50%, -50%) scale(1.3) rotate(45deg);
    filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.95));
  }
  60% {
    opacity: 0.35;
    transform: translate(50%, -50%) scale(0.8) rotate(75deg);
  }
  75% {
    opacity: 0.15;
    transform: translate(50%, -50%) scale(0.6) rotate(90deg);
  }
}

.gate-classification {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.22em;
  color: #6b7280;
  text-transform: uppercase;
  margin-bottom: 8px;
}

.gate-heading {
  font-family: 'Cinzel', var(--font-serif);
  font-size: 1.65rem;
  font-weight: 800;
  color: #1f2937;
  letter-spacing: 0.12em;
  margin: 0 0 10px 0;
  line-height: 1.2;
}

.gate-clearance-notice {
  font-family: var(--font-mono);
  font-size: 0.74rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: #4b5563;
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 4px;
  padding: 6px 14px;
  margin: 0 auto 24px auto;
  display: inline-block;
  line-height: 1.4;
}

.gate-field-group {
  margin-bottom: 18px;
  text-align: left;
}

.gate-label {
  display: block;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 700;
  color: #374151;
  letter-spacing: 0.06em;
  margin-bottom: 8px;
}

.gate-input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.gate-input {
  width: 100%;
  background: #ffffff;
  border: 1.5px solid #d1d5db;
  border-radius: 6px;
  padding: 12px 14px;
  font-family: var(--font-mono);
  font-size: 0.95rem;
  color: #111827;
  letter-spacing: 0.08em;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
  box-sizing: border-box;
}

.gate-input:focus {
  border-color: #4b5563;
  box-shadow: 0 0 0 3px rgba(107, 114, 128, 0.15);
  outline: none;
}

.gate-input::placeholder {
  color: #9ca3af;
  font-size: 0.85rem;
}

.gate-toggle-pw {
  position: absolute;
  right: 12px;
  background: none;
  border: none;
  cursor: pointer;
  color: #6b7280;
  padding: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.2s ease, transform 0.15s ease;
}

.gate-toggle-pw:hover {
  color: #111827;
}

.eye-outline-svg {
  width: 18px;
  height: 18px;
  display: block;
  stroke: currentColor;
}

.gate-feedback {
  min-height: 20px;
  margin-bottom: 14px;
  font-family: var(--font-mono);
  font-size: 0.76rem;
  font-weight: 700;
  text-align: center;
}

.gate-feedback.error {
  color: #b91c1c;
  background: #fef2f2;
  border: 1px solid #fecaca;
  padding: 9px 12px;
  border-radius: 6px;
  animation: gateShake 0.35s ease-in-out;
}

.gate-feedback.success {
  color: #047857;
  background: #ecfdf5;
  border: 1px solid #a7f3d0;
  padding: 9px 12px;
  border-radius: 6px;
}

.gate-submit-btn {
  width: 100%;
  background: #1f2937;
  color: #ffffff;
  font-family: var(--font-mono);
  font-size: 0.82rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 14px 20px;
  border: 1px solid #111827;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.12);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.gate-submit-btn:hover {
  background: #111827;
  transform: translateY(-1px);
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.2);
}

.gate-submit-btn:active {
  transform: translateY(0);
}

.gate-footer-note {
  margin-top: 24px;
  padding-top: 14px;
  border-top: 1px solid #f3f4f6;
  font-family: var(--font-mono);
  font-size: 0.62rem;
  color: #9ca3af;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

/* Header Lock Terminal Button */
.header-lock-terminal-btn {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.18);
  color: var(--accent-silver);
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  padding: 6px 12px;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s ease;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.header-lock-terminal-btn:hover {
  background: rgba(217, 37, 52, 0.2);
  border-color: rgba(217, 37, 52, 0.6);
  color: #ffffff;
  box-shadow: 0 0 10px rgba(217, 37, 52, 0.4);
}

/* Responsive Breakpoints */
@media (max-width: 1200px) {
  .hero-showcase-grid {
    grid-template-columns: 1fr;
    gap: 36px;
  }
  .frame-tuxedo-primary {
    width: 100%;
    max-width: 480px;
  }
  .frame-omega-secondary {
    left: 180px;
  }
}

@media (max-width: 1100px) {
  .hero-omega-master-stage {
    grid-template-columns: 1fr;
    gap: 20px;
    padding: 20px 16px;
  }
  .omega-left-hud-wing, .omega-right-hud-wing {
    max-width: 480px;
    margin: 0 auto;
    width: 100%;
  }
}

@media (max-width: 900px) {
  .sidebar-nav {
    position: fixed;
    left: -280px;
    z-index: 150;
  }
  .sidebar-nav.open {
    transform: translateX(280px);
  }
  .main-content {
    padding: 24px 18px;
  }
  .frame-omega-secondary {
    position: static;
    margin-top: 20px;
    width: 100%;
  }
  .hero-overlapping-stage {
    min-height: auto;
  }
  .callout-tuxedo-lead, .callout-watch-lead {
    display: none;
  }
}

@media (max-width: 768px) {
  .briefing-red-bold-title {
    font-size: 2.1rem;
    letter-spacing: 0.22em;
  }
  .briefing-deck-main-row {
    flex-direction: column;
    align-items: stretch;
    gap: 12px;
  }
  .briefing-timeline-wrap {
    width: 100%;
  }
  .briefing-deck-tools {
    justify-content: flex-end;
  }
}
"""

if __name__ == "__main__":
    print("Testing theme_css module length:", len(get_theme_css()))
