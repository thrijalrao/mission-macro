# build_scripts/engine_js.py
"""
Project 007: The Macroeconomics Intelligence File
Core JavaScript Engine: Omega Seamaster Chronometer, 6 Canvas Graph Labs,
Progress Tracker, Search & Filtering, 3-Tier Progressive Hints, and Solution Reveals.
"""

def get_engine_js():
    return r"""
// PROJECT 007 CORE JAVASCRIPT ENGINE
(function() {
  'use strict';

  // --- STATE MANAGEMENT & LOCAL STORAGE ---
  const STORAGE_KEY = 'project007_macro_progress_v1';
  let appState = {
    currentEnv: 'all', // 'all', 'training', 'missions', 'targets'
    currentChapter: 1,
    chapterProgress: {} // chId: { training: bool, formulas: bool, graphs: bool, missions: bool, targets: bool }
  };

  // Initialize chapter state for 15 chapters
  for (let i = 1; i <= 15; i++) {
    appState.chapterProgress[i] = {
      training: false,
      formulas: false,
      graphs: false,
      missions: false,
      targets: false
    };
  }

  function loadState() {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        const parsed = JSON.parse(saved);
        if (parsed.chapterProgress) {
          appState.chapterProgress = Object.assign(appState.chapterProgress, parsed.chapterProgress);
        }
      }
    } catch (e) {
      console.warn('LocalStorage error or unavailable:', e);
    }
  }

  function saveState() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({
        chapterProgress: appState.chapterProgress
      }));
    } catch (e) {
      console.warn('Could not save to LocalStorage:', e);
    }
  }

  // --- OMEGA SEAMASTER CHRONOMETER CALCULATOR & RENDERER ---
  function calculateTotalProgress() {
    let totalItems = 15 * 5; // 75 items total across 15 chapters
    let completed = 0;
    for (let i = 1; i <= 15; i++) {
      const ch = appState.chapterProgress[i];
      if (ch) {
        if (ch.training) completed++;
        if (ch.formulas) completed++;
        if (ch.graphs) completed++;
        if (ch.missions) completed++;
        if (ch.targets) completed++;
      }
    }
    return Math.round((completed / totalItems) * 100);
  }

  // --- OMEGA SEAMASTER 300M 007 EDITION (TITANIUM) INTERACTIVE CONTROLLER ---
  let isMouseInsideDial = false;
  let targetSecondsAngle = 0;
  let currentSecondsAngle = 0;
  let lastDialInteractionTime = 0;
  let secondsAnimStarted = false;
  let isCoaxialSweepActive = true;

  window.toggleCoaxialSweep = function() {
    isCoaxialSweepActive = !isCoaxialSweepActive;
    const btn = document.getElementById('coaxialSweepToggleBtn');
    if (btn) {
      if (isCoaxialSweepActive) {
        btn.classList.add('active');
        btn.innerHTML = '▶ 8 Hz SWEEP: ACTIVE';
      } else {
        btn.classList.remove('active');
        btn.innerHTML = '❚❚ 8 Hz SWEEP: PAUSED';
      }
    }
    const statusNote = document.getElementById('omegaSecondsStatus');
    if (statusNote) {
      statusNote.innerHTML = isCoaxialSweepActive 
        ? '<span class="pulse-indicator-red"></span><span>SECONDS HAND: CO-AXIAL SWEEP (8 Hz)</span>'
        : '<span class="pulse-indicator-muted"></span><span>SECONDS HAND: PARKED</span>';
    }
  };

  window.zeroChronograph = function() {
    targetSecondsAngle = 0;
    currentSecondsAngle = 0;
    isMouseInsideDial = false;
    isCoaxialSweepActive = false;
    const btn = document.getElementById('coaxialSweepToggleBtn');
    if (btn) {
      btn.classList.remove('active');
      btn.innerHTML = '❚❚ 8 Hz SWEEP: PAUSED';
    }
    const secHand = document.getElementById('omegaSecondsHand');
    if (secHand) {
      secHand.setAttribute('transform', 'rotate(0)');
    }
    const angleDisplay = document.getElementById('omegaSecondsAngle');
    if (angleDisplay) {
      angleDisplay.textContent = '00s // 000° ZEROED';
    }
    const statusNote = document.getElementById('omegaSecondsStatus');
    if (statusNote) {
      statusNote.innerHTML = '<span class="pulse-indicator-muted"></span><span>CHRONO ZEROED AT 12:00</span>';
    }
  };

  // =========================================================================
  // --- 007 MISSION TACTICAL COUNTDOWN TIMER TO NOVEMBER 30TH 10:00 AM ---
  // =========================================================================
  // Format: MM (Months) : DD (Days) : HH (Hours 24-hr system) : mm (Minutes) : ss (Seconds)
  // Stage 1 (Green): Till Nov 22, 2026 12:00 AM IST
  // Stage 2 (Yellow): Nov 22, 2026 12:00 AM to Nov 25, 2026 12:00 AM IST
  // Stage 3 (Red): Nov 25, 2026 12:00 AM to Nov 30, 2026 10:00 AM IST
  // Stage 4 (Grey): From Nov 30, 2026 10:00 AM IST onwards (turns grey, locks at 00:00:00:00:00)

  const CD_TARGET_TIME = new Date('2026-11-30T10:00:00+05:30').getTime();
  const CD_STAGE1_TIME = new Date('2026-11-22T00:00:00+05:30').getTime();
  const CD_STAGE2_TIME = new Date('2026-11-25T00:00:00+05:30').getTime();

  function updateMissionCountdown() {
    const now = Date.now();
    const diff = CD_TARGET_TIME - now;

    let color = '';
    let glow = '';
    let stageText = '';
    let monthsStr = '00';
    let daysStr = '00';
    let hoursStr = '00';
    let minsStr = '00';
    let secsStr = '00';

    if (diff <= 0) {
      // Stage 4: Grey when countdown hits all 0s (Nov 30th 10:00 AM onwards)
      color = '#888888';
      glow = 'none';
      stageText = 'Terminated - Mission Accomplished, Agent';
      monthsStr = '00';
      daysStr = '00';
      hoursStr = '00';
      minsStr = '00';
      secsStr = '00';
    } else {
      // Active Stages
      if (now < CD_STAGE1_TIME) {
        // Stage 1: Green till Nov 22 12:00 AM
        color = '#10b981';
        glow = '0 0 16px rgba(16, 185, 129, 0.45)';
        stageText = 'PHASE 1 // ACTIVE READINESS (TARGET: NOV 30, 10:00 AM)';
      } else if (now < CD_STAGE2_TIME) {
        // Stage 2: Yellow from Nov 22 12:00 AM to Nov 25 12:00 AM
        color = '#eab308';
        glow = '0 0 16px rgba(234, 179, 8, 0.45)';
        stageText = 'PHASE 2 // REVISION ESCALATION (TARGET: NOV 30, 10:00 AM)';
      } else {
        // Stage 3: Red from Nov 25 12:00 AM to Nov 30 10:00 AM
        color = '#d92534';
        glow = '0 0 18px rgba(217, 37, 52, 0.55)';
        stageText = 'PHASE 3 // IMMINENT EXAM EXECUTION (TARGET: NOV 30, 10:00 AM)';
      }

      const totalSeconds = Math.floor(diff / 1000);
      const nowDate = new Date(now);
      const targetDate = new Date(CD_TARGET_TIME);

      // Months calculation
      let months = (targetDate.getFullYear() - nowDate.getFullYear()) * 12 + (targetDate.getMonth() - nowDate.getMonth());
      if (nowDate.getDate() > targetDate.getDate() || (nowDate.getDate() === targetDate.getDate() && nowDate.getHours() > targetDate.getHours())) {
        months = Math.max(0, months - 1);
      }

      const days = Math.floor(totalSeconds / 86400);
      const hours = Math.floor((totalSeconds % 86400) / 3600); // 24-hour system
      const minutes = Math.floor((totalSeconds % 3600) / 60);
      const seconds = totalSeconds % 60;

      monthsStr = String(months).padStart(2, '0');
      daysStr = String(days).padStart(2, '0');
      hoursStr = String(hours).padStart(2, '0');
      minsStr = String(minutes).padStart(2, '0');
      secsStr = String(seconds).padStart(2, '0');
    }

    // Apply values to DOM
    const elMonths = document.getElementById('cdMonths');
    const elDays = document.getElementById('cdDays');
    const elHours = document.getElementById('cdHours');
    const elMins = document.getElementById('cdMinutes');
    const elSecs = document.getElementById('cdSeconds');
    const elStageLabel = document.getElementById('countdownStageLabel');
    const elDeck = document.getElementById('missionCountdownDeck');
    const elDot = document.getElementById('countdownDot');
    const digitsWrap = document.getElementById('countdownDigitsWrap');

    if (elMonths) elMonths.textContent = monthsStr;
    if (elDays) elDays.textContent = daysStr;
    if (elHours) elHours.textContent = hoursStr;
    if (elMins) elMins.textContent = minsStr;
    if (elSecs) elSecs.textContent = secsStr;

    if (digitsWrap) {
      digitsWrap.style.color = color;
      digitsWrap.style.textShadow = glow;
    }
    if (elDot) {
      elDot.style.color = color;
    }
    if (elDeck) {
      elDeck.style.borderColor = color + '44';
      elDeck.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.8), 0 0 15px ' + color + '22';
    }
    if (elStageLabel) {
      elStageLabel.textContent = stageText;
    }
  }

  // Initialize countdown on script load
  if (typeof window !== 'undefined') {
    window.updateMissionCountdown = updateMissionCountdown;
    setInterval(updateMissionCountdown, 1000);
  }

  function setupOmegaSecondsTracking() {
    if (secondsAnimStarted) return;
    const watchSvg = document.getElementById('omegaSeamasterSvg');
    if (!watchSvg) return;
    secondsAnimStarted = true;

    const hitArea = document.getElementById('omegaDialHitArea') || watchSvg;
    const statusNote = document.getElementById('omegaSecondsStatus');
    const angleDisplay = document.getElementById('omegaSecondsAngle');

    function calculateDialAngle(clientX, clientY) {
      const rect = watchSvg.getBoundingClientRect();
      if (rect.width === 0) return null;
      // Center of viewBox 0 0 460 560 is at (230, 280)
      const centerX = rect.left + rect.width * (230 / 460);
      const centerY = rect.top + rect.height * (280 / 560);
      const dx = clientX - centerX;
      const dy = clientY - centerY;
      const dist = Math.hypot(dx, dy);
      // Dial radius in px (radius of dial face is 120 in SVG units)
      const maxDialRadius = rect.width * (120 / 460);
      if (dist > maxDialRadius) return null; // Outside the watch dial!

      let deg = Math.atan2(dy, dx) * (180 / Math.PI) + 90;
      if (deg < 0) deg += 360;
      return deg;
    }

    // ONLY listen inside the watch dial!
    function handleDialPointer(clientX, clientY) {
      const deg = calculateDialAngle(clientX, clientY);
      if (deg !== null) {
        targetSecondsAngle = deg;
        isMouseInsideDial = true;
        lastDialInteractionTime = performance.now();
        const secVal = Math.floor(deg / 6) % 60;
        const secStr = (secVal < 10 ? '0' : '') + secVal;
        const degStr = Math.round(deg) + '°';
        if (statusNote) {
          statusNote.innerHTML = '<span class="pulse-indicator-red"></span><span>SECONDS: REVOLVING IN WATCH (' + secStr + 's / ' + degStr + ')</span>';
        }
        if (angleDisplay) {
          angleDisplay.textContent = secStr + 's // ' + degStr + ' DIAL AZIMUTH';
        }
        return true;
      } else {
        isMouseInsideDial = false;
        return false;
      }
    }

    hitArea.addEventListener('mousedown', function(e) {
      handleDialPointer(e.clientX, e.clientY);
    });

    hitArea.addEventListener('mousemove', function(e) {
      handleDialPointer(e.clientX, e.clientY);
    });

    hitArea.addEventListener('mouseleave', function() {
      isMouseInsideDial = false;
      if (statusNote && isCoaxialSweepActive) {
        statusNote.innerHTML = '<span class="pulse-indicator-red"></span><span>SECONDS HAND: CO-AXIAL SWEEP (8 Hz)</span>';
      }
    });

    // Touch events for mobile/tablet directly on the watch dial
    hitArea.addEventListener('touchstart', function(e) {
      if (e.touches.length > 0) {
        const touch = e.touches[0];
        handleDialPointer(touch.clientX, touch.clientY);
      }
    }, { passive: true });

    hitArea.addEventListener('touchmove', function(e) {
      if (e.touches.length > 0) {
        const touch = e.touches[0];
        const deg = calculateDialAngle(touch.clientX, touch.clientY);
        if (deg !== null) {
          e.preventDefault();
          targetSecondsAngle = deg;
          isMouseInsideDial = true;
          lastDialInteractionTime = performance.now();
        }
      }
    }, { passive: false });

    hitArea.addEventListener('touchend', function() {
      isMouseInsideDial = false;
    });

    function animateSeconds(time) {
      const secHand = document.getElementById('omegaSecondsHand');
      if (secHand) {
        if (isMouseInsideDial && (time - lastDialInteractionTime < 3000)) {
          // Revolve to cursor position inside the watch with smooth damping
          let diff = (targetSecondsAngle - currentSecondsAngle);
          diff = (diff + 180) % 360 - 180;
          currentSecondsAngle += diff * 0.28;
        } else if (isCoaxialSweepActive) {
          isMouseInsideDial = false;
          // Smooth 8 Hz Co-Axial Sweep
          const now = new Date();
          const sec = now.getSeconds();
          const ms = now.getMilliseconds();
          // Step in 8 discrete increments per second (authentic Omega Co-Axial Calibre 8806: 25,200 vph = 7-8 ticks/sec)
          const discreteFraction = Math.floor((ms / 1000) * 8) / 8;
          const sweepDeg = (sec + discreteFraction) * 6;
          let diff = (sweepDeg - currentSecondsAngle);
          diff = (diff + 180) % 360 - 180;
          currentSecondsAngle += diff * 0.35;

          const currentSec = Math.floor(currentSecondsAngle / 6) % 60;
          const secFormatted = (currentSec < 10 ? '0' : '') + currentSec;
          if (angleDisplay && Math.abs(diff) > 0.05) {
            angleDisplay.textContent = secFormatted + 's // ' + Math.round((currentSecondsAngle % 360 + 360) % 360) + '° CHRONO';
          }
        }
        secHand.setAttribute('transform', 'rotate(' + currentSecondsAngle.toFixed(2) + ')');
      }
      requestAnimationFrame(animateSeconds);
    }
    requestAnimationFrame(animateSeconds);
  }

  function renderOmegaDials() {
    const percent = calculateTotalProgress();
    const circumference = 2 * Math.PI * 42; // r=42 for header widget
    const strokeDashoffset = circumference - (percent / 100) * circumference;

    // Calculate core chapters finished out of 12 (Excluding Dossier 13 for revision)
    let coreDone = 0;
    for (let i = 1; i <= 12; i++) {
      const ch = appState.chapterProgress[i];
      if (ch) {
        const items = (ch.training?1:0) + (ch.formulas?1:0) + (ch.graphs?1:0) + (ch.missions?1:0) + (ch.targets?1:0);
        if (items >= 3 || (ch.training && ch.missions)) {
          coreDone++;
        }
      }
    }

    // 1. MINUTE HAND: Shows Exam Readiness Percentage (0% -> 100% = 0° -> 360°)
    const minuteDeg = (percent / 100) * 360;
    const minHand = document.getElementById('omegaMinuteHand');
    if (minHand) {
      minHand.setAttribute('transform', 'rotate(' + minuteDeg.toFixed(1) + ')');
    }

    // 2. HOUR HAND: Shows Number of Core Chapters Finished (0 -> 12 = 0° -> 360°, Excl. 13)
    const hourDeg = (coreDone / 12) * 360;
    const hrHand = document.getElementById('omegaHourHand');
    if (hrHand) {
      hrHand.setAttribute('transform', 'rotate(' + hourDeg.toFixed(1) + ')');
    }

    // Start mouse-tracking on seconds hand
    setupOmegaSecondsTracking();

    // Mini dial in master header
    const miniVal = document.getElementById('miniOmegaPercent');
    const miniRing = document.getElementById('miniOmegaRing');
    if (miniVal) miniVal.textContent = percent + '%';
    if (miniRing) miniRing.style.strokeDashoffset = strokeDashoffset;

    // Master Hero Digital Telemetry Readouts
    const masterVal = document.getElementById('masterOmegaPercent');
    const masterChapters = document.getElementById('masterOmegaChapters');
    const barFill = document.getElementById('readoutBarFill');
    if (masterVal) masterVal.textContent = percent + '%';
    if (masterChapters) masterChapters.innerHTML = coreDone + ' <span style="font-size:0.65em; color:var(--text-muted);">/ 12</span>';
    if (barFill) barFill.style.width = percent + '%';

    // Update chapter checkboxes if on revision page
    for (let i = 1; i <= 13; i++) {
      const p = appState.chapterProgress[i];
      const allDone = p.training && p.formulas && p.graphs && p.missions && p.targets;
      const chBadge = document.getElementById('ch-mastery-badge-' + i);
      if (chBadge) {
        if (allDone) {
          chBadge.classList.add('mastered');
          chBadge.innerHTML = '★ MASTERED';
        } else {
          chBadge.classList.remove('mastered');
          chBadge.innerHTML = 'IN PROGRESS';
        }
      }
    }
  }

  // --- ENVIRONMENT SWITCHING (ALL / TRAINING / MISSIONS / TARGETS) ---
  window.switchEnvironment = function(env) {
    appState.currentEnv = env;
    document.querySelectorAll('.env-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.env === env);
    });

    const trainingSections = document.querySelectorAll('.training-section, [id$="-training"], [id$="-formulas"], [id$="-matrices"], [id$="-gallery"]');
    const missionSections = document.querySelectorAll('.missions-section, [id$="-missions"], [id$="-mock"]');
    const targetSections = document.querySelectorAll('.targets-section, [id$="-targets"], [id$="-toolkit"]');

    if (env === 'all') {
      document.querySelectorAll('.subtab-content').forEach(s => {
        if (s.classList.contains('active')) s.style.display = 'block';
      });
      trainingSections.forEach(s => s.style.display = 'block');
      missionSections.forEach(s => s.style.display = 'block');
      targetSections.forEach(s => s.style.display = 'block');
    } else if (env === 'training') {
      document.querySelectorAll('.tab-btn').forEach(b => {
        if (b.innerText.includes('TRAINING') || b.innerText.includes('FORMULA') || b.innerText.includes('MATRICES')) b.click();
      });
      trainingSections.forEach(s => s.style.display = 'block');
      missionSections.forEach(s => s.style.display = 'none');
      targetSections.forEach(s => s.style.display = 'none');
    } else if (env === 'missions') {
      document.querySelectorAll('.tab-btn').forEach(b => {
        if (b.innerText.includes('MISSIONS') || b.innerText.includes('MOCK')) b.click();
      });
      trainingSections.forEach(s => s.style.display = 'none');
      missionSections.forEach(s => s.style.display = 'block');
      targetSections.forEach(s => s.style.display = 'none');
    } else if (env === 'targets') {
      document.querySelectorAll('.tab-btn').forEach(b => {
        if (b.innerText.includes('TARGETS') || b.innerText.includes('SOP')) b.click();
      });
      trainingSections.forEach(s => s.style.display = 'none');
      missionSections.forEach(s => s.style.display = 'none');
      targetSections.forEach(s => s.style.display = 'block');
    }
  };

  // --- CHAPTER SUB-TAB SWITCHING ---
  window.switchChapterTab = function(chId, tab) {
    const ch = document.getElementById('chapter-' + chId) || document.getElementById('ch' + chId);
    if (!ch) return;

    ch.querySelectorAll('.ch-tab-btn, .tab-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.tab === tab || (btn.getAttribute('onclick') && btn.getAttribute('onclick').includes(tab)));
    });

    const trainingSec = ch.querySelector('.training-section, [id$="-training"]');
    const missionsSec = ch.querySelector('.missions-section, [id$="-missions"]');
    const targetsSec = ch.querySelector('.targets-section, [id$="-targets"]');

    if (tab === 'all') {
      if (trainingSec) trainingSec.style.display = 'block';
      if (missionsSec) missionsSec.style.display = 'block';
      if (targetsSec) targetsSec.style.display = 'block';
    } else if (tab === 'training') {
      if (trainingSec) trainingSec.style.display = 'block';
      if (missionsSec) missionsSec.style.display = 'none';
      if (targetsSec) targetsSec.style.display = 'none';
    } else if (tab === 'missions') {
      if (trainingSec) trainingSec.style.display = 'none';
      if (missionsSec) missionsSec.style.display = 'block';
      if (targetsSec) targetsSec.style.display = 'none';
    } else if (tab === 'targets') {
      if (trainingSec) trainingSec.style.display = 'none';
      if (missionsSec) missionsSec.style.display = 'none';
      if (targetsSec) targetsSec.style.display = 'block';
    }
  };

  // --- UNIFIED SUBTAB SWITCHER (FOR CH1-4 & CH10-13) ---
  window.switchSubTab = function(event, subtabId) {
    const targetSubtab = document.getElementById(subtabId);
    if (!targetSubtab) return;
    const parentContainer = targetSubtab.closest('.tab-container');
    if (!parentContainer) return;

    parentContainer.querySelectorAll('.subtab-content').forEach(s => {
      s.classList.remove('active');
      s.style.display = 'none';
    });

    parentContainer.querySelectorAll('.tab-btn').forEach(b => {
      b.classList.remove('active');
    });

    targetSubtab.classList.add('active');
    targetSubtab.style.display = 'block';

    if (event && event.currentTarget) {
      event.currentTarget.classList.add('active');
    }
  };

  // --- PROGRESSIVE HINTS SYSTEM (UNIFIED) ---
  window.toggleHint = function(arg1, arg2) {
    let btn = null;
    let hintId = null;

    if (arg2) {
      btn = arg1;
      hintId = arg2;
    } else {
      hintId = arg1;
      if (window.event && window.event.currentTarget) {
        btn = window.event.currentTarget;
      }
    }

    const hintBox = document.getElementById(hintId);
    if (!hintBox) return;

    const isVisible = hintBox.classList.contains('visible') || hintBox.style.display === 'block';
    const parentContainer = btn ? btn.closest('.hints-container, .hint-container') : null;

    if (parentContainer && arg2) {
      parentContainer.querySelectorAll('.hint-trigger-btn, .hint-btn').forEach(b => b.classList.remove('active'));
      parentContainer.querySelectorAll('.hint-content-box, .hint-text').forEach(b => {
        b.classList.remove('visible');
        b.style.display = 'none';
      });
    }

    if (!isVisible) {
      hintBox.classList.add('visible');
      hintBox.style.display = 'block';
      if (btn) btn.classList.add('active');
    } else {
      hintBox.classList.remove('visible');
      hintBox.style.display = 'none';
      if (btn) btn.classList.remove('active');
    }
  };

  // --- ROBUST UNIFIED SOLUTION REVEAL ENGINE ---
  window.toggleSolution = function(btn, solutionId, chId) {
    if (typeof btn === 'string') {
      chId = solutionId;
      solutionId = btn;
      btn = document.querySelector('button[onclick*="' + solutionId + '"]');
    }

    const solBox = document.getElementById(solutionId);
    if (!solBox) return;

    const isRevealed = solBox.classList.contains('revealed') || solBox.style.display === 'block';

    if (isRevealed) {
      solBox.classList.remove('revealed');
      solBox.style.display = 'none';
      if (btn) {
        btn.classList.remove('revealed-active');
        if (btn.dataset.originalText) {
          btn.innerHTML = btn.dataset.originalText;
        } else if (btn.classList.contains('action-btn')) {
          btn.innerHTML = 'CONFIRM TARGET IDENTIFICATION // REVEAL SOLUTION';
        } else {
          btn.innerHTML = '<span style="color:var(--bond-crimson);">▶</span> ACCESS TARGET DEBRIEFING (7-STEP SOLUTION)';
        }
      }
    } else {
      solBox.classList.add('revealed');
      solBox.style.display = 'block';
      if (btn) {
        if (!btn.dataset.originalText) {
          btn.dataset.originalText = btn.innerHTML;
        }
        btn.classList.add('revealed-active');
        btn.innerHTML = '▲ CONCEAL TARGET DEBRIEFING';
      }

      // If solution is inside a hidden tab container, ensure it is displayed
      const parentSubtab = solBox.closest('.subtab-content');
      if (parentSubtab && parentSubtab.style.display === 'none') {
        parentSubtab.style.display = 'block';
        parentSubtab.classList.add('active');
      }

      // Smooth scroll if element was off screen
      const rect = solBox.getBoundingClientRect();
      if (rect.top < 60 || rect.bottom > window.innerHeight) {
        solBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      // Re-render KaTeX math if needed
      if (window.renderMathInElement) {
        try {
          window.renderMathInElement(solBox, {
            delimiters: [
              { left: '$$', right: '$$', display: true },
              { left: '$', right: '$', display: false }
            ],
            throwOnError: false
          });
        } catch (e) {}
      }

      // Update chapter mastery
      let cNum = chId;
      if (!cNum && solutionId) {
        const m = solutionId.match(/(?:s|sol_?)(\d+)/);
        if (m) cNum = parseInt(m[1], 10);
      }
      if (cNum && appState && appState.chapterProgress && appState.chapterProgress[cNum]) {
        appState.chapterProgress[cNum].targets = true;
        saveState();
        renderOmegaDials();
      }
    }
  };

  window.revealSolution = function(arg1, arg2, arg3) {
    if (typeof arg1 === 'string') {
      const btn = document.querySelector('button[onclick*="' + arg1 + '"]');
      window.toggleSolution(btn, arg1, arg2);
    } else {
      window.toggleSolution(arg1, arg2, arg3);
    }
  };

  // --- CHECKBOX TOGGLE FOR REVISION CHECKLIST ---
  window.toggleProgressItem = function(chId, key, checkbox) {
    if (appState.chapterProgress[chId]) {
      appState.chapterProgress[chId][key] = checkbox.checked;
      saveState();
      renderOmegaDials();
    }
  };

  // --- INTERACTIVE SIMULATION AUDITOR (CHAPTER 15) ---
  window.auditSimulationScore = function() {
    const paper = document.getElementById('rubricPaperSelect')?.value || 'p1';
    const sA = Math.max(0, Math.min(20, parseFloat(document.getElementById('secAScore')?.value) || 0));
    const sB = Math.max(0, Math.min(20, parseFloat(document.getElementById('secBScore')?.value) || 0));
    const sC = Math.max(0, Math.min(20, parseFloat(document.getElementById('secCScore')?.value) || 0));
    const total = sA + sB + sC;
    const pct = ((total / 60) * 100).toFixed(1);
    
    let grade = '';
    let color = '';
    let assessment = '';
    if (total >= 50) {
      grade = 'A+ // OUTSTANDING DISTINCTION';
      color = '#10b981';
      assessment = 'Flawless mastery of macroeconomic identities, multi-step algebraic derivations, and equilibrium graphic precision. Recommended for Top Honours.';
    } else if (total >= 42) {
      grade = 'A // FIRST CLASS WITH DISTINCTION';
      color = '#38bdf8';
      assessment = 'Strong command of theoretical and quantitative frameworks. Minor point deductions typically arise from omitting intermediate steps or diagram labels.';
    } else if (total >= 30) {
      grade = 'B+ // CLEAR PASS';
      color = '#eab308';
      assessment = 'Good conceptual understanding, but requires deeper practice on 10-mark quantitative derivations and multi-market policy mixes.';
    } else {
      grade = 'NEEDS REVIEW // CONDITIONAL PASS';
      color = '#d92534';
      assessment = 'Review Chapter 13 One-Shot Revision and Chapter 14 Official Answer Key. Focus on core formulas (IS-LM, Multiplier, Phillips curve) and step-by-step arithmetic.';
    }

    const resBox = document.getElementById('rubricAuditResult');
    if (resBox) {
      resBox.style.display = 'block';
      resBox.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:8px;">
          <span style="font-family:var(--font-mono); color:${color}; font-weight:700; font-size:1.05rem;">TOTAL SCORE: ${total} / 60 (${pct}%) — ${grade}</span>
          <span class="badge" style="background:${color}22; color:${color}; border:1px solid ${color}; padding:2px 8px;">AUDITED</span>
        </div>
        <p style="margin-top:10px; font-size:0.88rem; color:var(--silver-200); line-height:1.6;">${assessment}</p>
        <div style="display:flex; gap:16px; margin-top:8px; font-family:var(--font-mono); font-size:0.8rem; color:var(--text-muted);">
          <span>Sec A: ${sA}/20</span>
          <span>Sec B: ${sB}/20</span>
          <span>Sec C: ${sC}/20</span>
        </div>
      `;
    }
  };

  // =========================================================================
  // --- 007 MASTER INTELLIGENCE SEARCH INDEX & TACTICAL ROUTER ---
  // =========================================================================
  const SEARCH_INDEX = [
    // CHAPTER 1: MACROECONOMIC FOUNDATIONS
    {
      ch: 1,
      targetId: 'chapter-1',
      badge: 'DOSSIER 01 // OVERVIEW',
      title: 'Macroeconomic Foundations & Scope',
      subtitle: 'Micro vs Macro, goods market, money market, aggregate variables',
      keywords: ['macroeconomics', 'foundations', 'scope', 'aggregates', 'ackley', 'samuelson', 'goods market', 'money market']
    },
    {
      ch: 1,
      targetId: 'ch1-circular-flow',
      badge: 'DOSSIER 01 // SECTION 1.4',
      title: 'Circular Flow of Income & Output (2, 3 & 4 Sector)',
      subtitle: 'Real flow vs money flow, financial intermediaries, government & foreign sector',
      keywords: ['circular flow', 'two sector', 'three sector', 'four sector', 'real flow', 'money flow', 'closed economy', 'open economy']
    },
    {
      ch: 1,
      targetId: 'ch1-injections-leakages',
      badge: 'DOSSIER 01 // SECTION 1.5',
      title: 'Injections, Leakages & Macroeconomic Equilibrium',
      subtitle: 'S + T + M = I + G + X identity, transfer payments trap, disequilibrium',
      keywords: ['injections', 'leakages', 'equilibrium condition', 'savings', 'taxes', 'imports', 'investment', 'government spending', 'exports', 'transfer payments']
    },
    {
      ch: 1,
      targetId: 'ch1-stocks-flows',
      badge: 'DOSSIER 01 // SECTION 1.3',
      title: 'Stock vs Flow Variables in Macroeconomics',
      subtitle: 'Point in time (wealth, debt, capital) vs interval of time (GDP, income, investment)',
      keywords: ['stock', 'flow', 'stock vs flow', 'wealth', 'capital stock', 'inventory', 'debt']
    },

    // CHAPTER 2: NATIONAL INCOME ACCOUNTING
    {
      ch: 2,
      targetId: 'chapter-2',
      badge: 'DOSSIER 02 // OVERVIEW',
      title: 'National Income Accounting & The Master Identity',
      subtitle: 'Production = Income = Expenditure equivalence, national accounting rules',
      keywords: ['national income', 'gdp', 'master identity', 'accounting rules']
    },
    {
      ch: 2,
      targetId: 'ch2-value-added',
      badge: 'DOSSIER 02 // SECTION 2.2',
      title: 'Production / Value-Added Approach & Double Counting',
      subtitle: 'GVA = Value of Output - Intermediate Consumption, Breadland & Macrovia audit',
      keywords: ['value added', 'gva', 'intermediate consumption', 'double counting', 'production approach', 'breadland', 'macrovia']
    },
    {
      ch: 2,
      targetId: 'ch2-income-approach',
      badge: 'DOSSIER 02 // SECTION 2.3',
      title: 'Income Approach: Factor Payments & Operating Surplus',
      subtitle: 'Compensation of Employees (COE) + Operating Surplus (OS) + Mixed Income (MI)',
      keywords: ['income approach', 'factor payments', 'compensation of employees', 'operating surplus', 'rent', 'wages', 'interest', 'profit', 'mixed income']
    },
    {
      ch: 2,
      targetId: 'ch2-expenditure-approach',
      badge: 'DOSSIER 02 // SECTION 2.4',
      title: 'Expenditure Approach: C + I + G + (X - M)',
      subtitle: 'Household consumption, gross capital formation, government consumption, net exports',
      keywords: ['expenditure approach', 'consumption', 'gross investment', 'government expenditure', 'net exports', 'c + i + g + nx']
    },
    {
      ch: 2,
      targetId: 'ch2-gdp-critique',
      badge: 'DOSSIER 02 // SECTION 2.6',
      title: 'Strategic Critique: GDP Is Not Human Well-Being',
      subtitle: 'Structural blind spots: Simon Kuznets, RFK critique, non-market labor, environment',
      keywords: ['gdp critique', 'well-being', 'kuznets', 'rfk critique', 'green gdp', 'hdi']
    },

    // CHAPTER 3: REAL VS NOMINAL GDP & DEFLATOR
    {
      ch: 3,
      targetId: 'chapter-3',
      badge: 'DOSSIER 03 // SECTION 3.1',
      title: 'Real vs Nominal GDP & Base Year Mechanism',
      subtitle: 'Eliminating the inflation illusion: Constant prices vs Current market prices',
      keywords: ['real gdp', 'nominal gdp', 'base year', 'constant prices', 'growth illusion']
    },
    {
      ch: 3,
      targetId: 'ch3-deflator-mechanics',
      badge: 'DOSSIER 03 // SECTION 3.3',
      title: 'The GDP Deflator: Mechanics & Paasche Index',
      subtitle: 'GDP Deflator = (Nominal GDP / Real GDP) * 100, implicitly weighted Paasche formula',
      keywords: ['gdp deflator', 'deflator', 'paasche index', 'implicit deflator', 'cpi vs deflator']
    },
    {
      ch: 3,
      targetId: 'ch3-double-deflation',
      badge: 'DOSSIER 03 // SECTION 3.4',
      title: 'Double Deflation Method: Advanced Industrial Intelligence',
      subtitle: 'Deflating gross output by output PPI and intermediate inputs by input PPI (Zephyra)',
      keywords: ['double deflation', 'single deflation', 'industrial gva', 'zephyra']
    },

    // CHAPTER 4: KEY MACRO INDICATORS
    {
      ch: 4,
      targetId: 'chapter-4',
      badge: 'DOSSIER 04 // SECTION 4.1',
      title: 'Inflation Measurement & Consumer Price Index (CPI)',
      subtitle: 'Laspeyres fixed basket methodology, annual inflation rate formulation',
      keywords: ['cpi', 'inflation', 'laspeyres', 'price index', 'fixed basket']
    },
    {
      ch: 4,
      targetId: 'ch4-headline-core',
      badge: 'DOSSIER 04 // SECTION 4.2',
      title: 'Headline Inflation vs Core Inflation (RBI Policy)',
      subtitle: 'All-inclusive index vs Non-food non-fuel core inflation, supply shocks filter',
      keywords: ['headline inflation', 'core inflation', 'rbi policy', 'food and fuel', 'monetary policy committee']
    },
    {
      ch: 4,
      targetId: 'ch4-labor-market',
      badge: 'DOSSIER 04 // SECTION 4.3',
      title: 'Labor Market Architecture, LFPR & Unemployment Types',
      subtitle: 'LFPR, WPR, Frictional, Structural, Cyclical unemployment, Natural Rate (NRU)',
      keywords: ['unemployment', 'lfpr', 'labor force participation', 'natural rate of unemployment', 'nru', 'frictional unemployment', 'structural unemployment', 'cyclical unemployment']
    },

    // CHAPTER 5: BUSINESS CYCLES & OUTPUT GAPS
    {
      ch: 5,
      targetId: 'chapter-5',
      badge: 'DOSSIER 05 // SECTION 5.1',
      title: 'Business Cycles: Peak, Recession, Trough, Recovery',
      subtitle: 'Fluctuation phases around long-run potential trend, turning points',
      keywords: ['business cycle', 'recession', 'expansion', 'trough', 'peak', 'turning points']
    },
    {
      ch: 5,
      targetId: 'ch5-output-gap',
      badge: 'DOSSIER 05 // SECTION 5.2',
      title: 'Potential Output (Y*) & Output Gap Formulation',
      subtitle: 'Output Gap = (Y - Y*) / Y* * 100%, Recessionary gap vs Inflationary gap',
      keywords: ['output gap', 'potential output', 'sustainable capacity', 'recessionary gap', 'inflationary gap', 'y*']
    },
    {
      ch: 5,
      targetId: 'ch5-price-stickiness',
      badge: 'DOSSIER 05 // SECTION 5.3',
      title: 'Price Stickiness & Okun\'s Law Transmission',
      subtitle: 'Menu costs, staggered wage contracts, coordination failures, Okun\'s rule',
      keywords: ['okun', 'okun\'s law', 'price stickiness', 'menu costs', 'staggered wage setting', 'sticky prices']
    },

    // CHAPTER 6: SAVINGS & INVESTMENT
    {
      ch: 6,
      targetId: 'chapter-6',
      badge: 'DOSSIER 06 // SECTION 6.1',
      title: 'Consumption & Saving Functions (Keynesian Architecture)',
      subtitle: 'C = C₀ + c(Y - T), S = -C₀ + (1 - c)(Y - T), MPC + MPS = 1 identity',
      keywords: ['consumption function', 'saving function', 'mpc', 'mps', 'autonomous consumption', 'marginal propensity to consume']
    },
    {
      ch: 6,
      targetId: 'ch6-loanable-funds',
      badge: 'DOSSIER 06 // SECTION 6.2',
      title: 'Loanable Funds Market & S = I Closed Economy Equilibrium',
      subtitle: 'Downward sloping investment curve, upward sloping saving curve, real interest rate',
      keywords: ['loanable funds', 's = i', 'investment curve', 'saving curve', 'real interest rate']
    },
    {
      ch: 6,
      targetId: 'ch6-ready-reckoner',
      badge: 'DOSSIER 06 // SECTION 6.3',
      title: 'Simultaneous Shifts in S & I (The Ready Reckoner)',
      subtitle: '4 Master scenarios: When quantity is determinate vs when interest rate is determinate',
      keywords: ['ready reckoner', 'simultaneous shifts', 'loanable funds shifts', 'ostara']
    },
    {
      ch: 6,
      targetId: 'crowding-out-in',
      badge: 'DOSSIER 06 // SECTION 6.4',
      title: 'The Crowding-Out & Crowding-In Mechanisms',
      subtitle: 'Crowding Out (near full capacity, r↑, I↓) vs Crowding In (slump, public capex, MPK↑, I↑)',
      keywords: ['crowding out', 'crowding in', 'crowding out effect', 'crowding in effect', 'public capex', 'deficit financing', 'infrastructure investment', 'private investment']
    },

    // CHAPTER 7: THE MULTIPLIER EFFECT
    {
      ch: 7,
      targetId: 'chapter-7',
      badge: 'DOSSIER 07 // SECTION 7.1',
      title: 'The Multiplier Effect & Spending Ripple',
      subtitle: 'Autonomous expenditure ripple: 1 / (1 - MPC) or 1 / MPS, round-by-round math',
      keywords: ['multiplier', 'multiplier effect', 'keynesian multiplier', 'spending ripple', 'mpc']
    },
    {
      ch: 7,
      targetId: 'ch7-multiplier-taxonomy',
      badge: 'DOSSIER 07 // SECTION 7.2',
      title: 'Tax Multiplier, Balanced Budget Multiplier & Accelerator',
      subtitle: 'Tax multiplier = -c / (1 - c), Balanced Budget Multiplier = 1, Capital accelerator',
      keywords: ['tax multiplier', 'balanced budget multiplier', 'accelerator principle', 'leakages in multiplier']
    },

    // CHAPTER 8: FISCAL & MONETARY POLICY
    {
      ch: 8,
      targetId: 'chapter-8',
      badge: 'DOSSIER 08 // SECTION 8.1',
      title: 'Fiscal Policy: Government Spending, Taxes & Stabilizers',
      subtitle: 'Expansionary vs Contractionary fiscal levers, automatic vs discretionary stabilizers',
      keywords: ['fiscal policy', 'government expenditure', 'tax cuts', 'automatic stabilizers', 'discretionary fiscal']
    },
    {
      ch: 8,
      targetId: 'ch8-monetary-policy',
      badge: 'DOSSIER 08 // SECTION 8.2',
      title: 'Monetary Policy & Central Banking Instruments (RBI)',
      subtitle: 'Repo Rate, Reverse Repo, CRR, SLR, Open Market Operations (OMO), M0 to M4 money aggregates',
      keywords: ['monetary policy', 'rbi', 'repo rate', 'crr', 'cash reserve ratio', 'omo', 'open market operations', 'money supply', 'm0', 'm1', 'm2', 'm3', 'm4']
    },

    // CHAPTER 9: AD-AS FRAMEWORK
    {
      ch: 9,
      targetId: 'ad-framework',
      badge: 'DOSSIER 09 // SECTION 9.1',
      title: 'The Aggregate Demand (AD) Framework & Downward Slope',
      subtitle: 'Why AD slopes downward: Wealth Effect (Pigou), Interest Rate Effect (Keynes), Exchange Rate Effect',
      keywords: ['aggregate demand', 'ad curve', 'wealth effect', 'pigou effect', 'interest rate effect', 'keynes effect', 'exchange rate effect', 'ad downward slope']
    },
    {
      ch: 9,
      targetId: 'sticky-input-prices',
      badge: 'DOSSIER 09 // SECTION 9.2',
      title: 'The Sticky Input Prices Theory & Upward Sloping SRAS',
      subtitle: 'Four pillars of sticky costs: nominal wages, commodity contracts, leases, contracted services. Why LRAS is vertical at Y*',
      keywords: ['sticky input prices', 'sticky wages', 'wage rigidity', 'sticky prices', 'sras', 'short run aggregate supply', 'lras', 'long run aggregate supply', 'why sras slopes upward', 'vertical lras', 'potential output']
    },
    {
      ch: 9,
      targetId: 'ad-as-shocks',
      badge: 'DOSSIER 09 // SECTION 9.3',
      title: 'Dedicated AD-AS Shocks Taxonomy & Self-Correction',
      subtitle: 'Demand-pull inflation, Recessionary slump, Cost-push stagflation, Supply relief, Permanent shocks',
      keywords: ['stagflation', 'ad-as shocks', 'supply shock', 'demand shock', 'self-correction', 'cost-push inflation', 'demand-pull inflation', 'ardonia', 'caledonia']
    },

    // CHAPTER 10: IS-LM FRAMEWORK
    {
      ch: 10,
      targetId: 'ch10-is-curve',
      badge: 'DOSSIER 10 // SECTION 10.2',
      title: 'The IS Curve: Goods Market Equilibrium',
      subtitle: 'Derivation of IS: Y = C + I(r) + G, negative slope, goods market disequilibrium (excess supply/demand)',
      keywords: ['is curve', 'is-lm', 'goods market equilibrium', 'is slope', 'goods market disequilibrium']
    },
    {
      ch: 10,
      targetId: 'ch10-lm-curve',
      badge: 'DOSSIER 10 // SECTION 10.3',
      title: 'The LM Curve: Money Market Equilibrium',
      subtitle: 'M/P = L(Y, r), transaction and speculative demand for money, positive slope, money market disequilibrium',
      keywords: ['lm curve', 'money market equilibrium', 'liquidity preference', 'speculative demand', 'transaction demand', 'lm slope']
    },
    {
      ch: 10,
      targetId: 'ch10-liquidity-trap',
      badge: 'DOSSIER 10 // SECTION 10.5',
      title: 'Liquidity Trap & Zero Lower Bound (ZLB)',
      subtitle: 'Horizontal LM curve at near-zero rates, monetary policy impotence, fiscal policy supremacy (Japan case)',
      keywords: ['liquidity trap', 'zero lower bound', 'zlb', 'horizontal lm', 'japan liquidity trap', 'monetary impotence', 'fiscal multiplier in liquidity trap']
    },

    // CHAPTER 11: THE PHILLIPS CURVE
    {
      ch: 11,
      targetId: 'chapter-11',
      badge: 'DOSSIER 11 // OVERVIEW',
      title: 'The Phillips Curve: Inflation vs Unemployment Tradeoff',
      subtitle: 'Historical genesis, original Phillips empirical curve, A.W. Phillips (1958)',
      keywords: ['phillips curve', 'inflation unemployment tradeoff', 'a.w. phillips', 'empirical phillips']
    },
    {
      ch: 11,
      targetId: 'ch11-friedman-phelps',
      badge: 'DOSSIER 11 // SECTION 11.3 & 11.4',
      title: 'Friedman-Phelps Critique & Expectations-Augmented Curve',
      subtitle: 'π = πᵉ - β(u - u_n) + v, demise of stable trade-off, adaptive vs rational expectations',
      keywords: ['friedman-phelps', 'expectations-augmented', 'natural rate of unemployment', 'nairu', 'adaptive expectations', 'sacrifice ratio']
    },
    {
      ch: 11,
      targetId: 'ch11-srpc-lrpc',
      badge: 'DOSSIER 11 // SECTION 11.5',
      title: 'SRPC vs LRPC: Shifts vs Movements Along',
      subtitle: 'Vertical Long-Run Phillips Curve (LRPC) at Natural Rate of Unemployment (u = u_n)',
      keywords: ['srpc', 'lrpc', 'vertical phillips curve', 'movements along phillips', 'shifts in phillips curve']
    },

    // CHAPTER 12: INTEGRATED CASE STUDIES
    {
      ch: 12,
      targetId: 'ch12-demonetisation',
      badge: 'DOSSIER 12 // CASE STUDY 12.1',
      title: 'Demonetisation & Liquidity Shock Analysis (India 2016)',
      subtitle: 'Extraction of 86% high-powered currency, M0 shock, cash-velocity collapse, short-run GVA dip',
      keywords: ['demonetisation', 'demonetization', 'liquidity shock', 'india 2016', 'cash velocity', 'm0 extraction', 'informal sector shock']
    },
    {
      ch: 12,
      targetId: 'ch12-oil-shock',
      badge: 'DOSSIER 12 // CASE STUDY 12.2',
      title: 'Geopolitical Oil Supply Shock & The Policy Dilemma',
      subtitle: 'Crude oil surge, leftward SRAS shift, cost-push stagflation, central bank monetary dilemma',
      keywords: ['oil shock', 'geopolitical shock', 'stagflation case study', 'policy dilemma', 'cost-push shock']
    },
    {
      ch: 12,
      targetId: 'ch12-kumbh-mela',
      badge: 'DOSSIER 12 // CASE STUDY 12.3',
      title: 'Prayagraj Maha Kumbh Mela: Public Capex & Crowding In',
      subtitle: '₹30,000 Cr public infrastructure investment catalyzing ₹1.5+ Lakh Cr private investment',
      keywords: ['kumbh mela', 'prayagraj', 'public capex', 'crowding in case study', 'infrastructure multiplier', 'mega events']
    },

    // CHAPTER 13: ONE-SHOT REVISION CENTRE
    {
      ch: 13,
      targetId: 'ch13-formulas',
      badge: 'DOSSIER 13 // REVISION CENTRE',
      title: 'Q-Branch Master Formula Inventory (35+ Formulas)',
      subtitle: 'Step-by-step substitution guides, high-yield examination formula sheet',
      keywords: ['revision', 'formula sheet', 'formulas', 'one shot', 'cheat sheet', 'exam formulas']
    },
    {
      ch: 13,
      targetId: 'ch13-matrices',
      badge: 'DOSSIER 13 // SECTION 13.2',
      title: 'The 12 Tactical Distinction Matrices (High-Yield Contrasts)',
      subtitle: 'GDP Deflator vs CPI, Crowding Out vs In, SRAS vs LRAS, Fiscal vs Monetary, SRPC vs LRPC',
      keywords: ['distinction matrices', 'comparison tables', 'matrices', 'contrast', 'high-yield traps', 'crowding out vs in table']
    },
    {
      ch: 13,
      targetId: 'ch13-mock',
      badge: 'DOSSIER 13 // SECTION 13.3',
      title: 'Rapid-Fire Mock Exam & Examination Traps',
      subtitle: '20 High-yield exam traps with 7-step solution protocol and marking schemes',
      keywords: ['mock exam', 'exam traps', 'exam readiness', 'rapid fire', '7-step protocol']
    },
    // CHAPTER 14: MIDSEM 2026 & CASE VAULT
    {
      ch: 14,
      targetId: 'chapter-14',
      badge: 'DOSSIER 14 // MIDSEM QP',
      title: 'Macroeconomics Mid Term Examination — September 2026',
      subtitle: 'Official TAPMI examination paper: Q1 National Income, Q2 Zephyra GVA, Q3 Loanable Funds',
      keywords: ['midsem', 'midterm', 'examination paper', 'september 2026', 'national statistics office', 'zephyra', 'wheat flour', 'ostara']
    },
    {
      ch: 14,
      targetId: 'ch14-solutions',
      badge: 'DOSSIER 14 // ANSWER KEY',
      title: 'Midsem 2026 Official Answer Key & Step-by-Step Solutions',
      subtitle: 'Triple-check GDP ₹4,700, Double Deflation Real GVA 20%, Loanable funds r=3.04%, Stimulus overshoot ΔG=1312',
      keywords: ['midsem solution', 'midterm answer key', 'double deflation', 'single deflation', 'loanable funds equilibrium', 'stimulus overshoot', '4700']
    },
    {
      ch: 14,
      targetId: 'ch14-cases',
      badge: 'DOSSIER 14 // CASE VAULT',
      title: 'Comprehensive Case Study Vault (10 Cases with 7-Step SOP)',
      subtitle: 'MCA-21, COVID Precautionary Saving, Stimulus Overshoot, OPEC Stagflation, Japan ZLB, Volcker Squeeze',
      keywords: ['case studies', 'case vault', 'mca-21', 'covid savings', 'opec', 'japan liquidity trap', 'volcker disinflation', 'demonetisation case', 'kumbh mela case']
    },
    // CHAPTER 15: ENDSEM SIMULATIONS
    {
      ch: 15,
      targetId: 'ch15-p1',
      badge: 'DOSSIER 15 // PAPER 1',
      title: 'Endsem Simulation Paper 1: Monetary & Fiscal Equilibrium (60 Marks / 2 Hrs)',
      subtitle: 'Section A (4x5M), Section B IS-LM Crowding Out & Automotive GVA (2x10M), Section C Zephyra Crisis Mix (20M)',
      keywords: ['endsem paper 1', 'endsem simulation', '60 marks', 'monetary fiscal equilibrium', 'is-lm crowding out', 'automotive double deflation', 'zephyra 2027']
    },
    {
      ch: 15,
      targetId: 'ch15-p2',
      badge: 'DOSSIER 15 // PAPER 2',
      title: 'Endsem Simulation Paper 2: AD-AS, Expectations & Policy Shocks (60 Marks / 2 Hrs)',
      subtitle: 'Self-correction, Okun law, Sacrifice ratio, Phillips curve stagflation, Keynesian leakages, Dossier Petrolea (20M)',
      keywords: ['endsem paper 2', 'ad-as shock', 'expectations phillips curve', 'sacrifice ratio', 'okuns law', 'petrolea stagflation', 'policy dilemma']
    },
    {
      ch: 15,
      targetId: 'ch15-p3',
      badge: 'DOSSIER 15 // PAPER 3',
      title: 'Endsem Simulation Paper 3: Open Economy, ZLB & Crisis Synthesis (60 Marks / 2 Hrs)',
      subtitle: 'Demonetisation velocity, Twin deficits, Paradox of thrift, Loanable funds deficit offset, Operation Phoenix ZLB (20M)',
      keywords: ['endsem paper 3', 'demonetisation velocity', 'twin deficits', 'paradox of thrift', 'loanable funds offset', 'operation phoenix', 'zero lower bound']
    },
    {
      ch: 15,
      targetId: 'ch15-rubric',
      badge: 'DOSSIER 15 // RUBRIC',
      title: 'Master Marking Scheme & Interactive 60-Mark Score Auditor',
      subtitle: 'TAPMI 5-pillar grading standards, score calculator, and performance feedback',
      keywords: ['marking scheme', 'grading rubric', 'score auditor', '60 marks rubric', 'examiner criteria']
    }
  ];

  let currentSearchResults = [];
  let selectedDropdownIndex = -1;

  // --- ESCAPE HTML HELPER ---
  function escapeHtml(str) {
    return (str || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  // --- HIGHLIGHT MATCHED SUBSTRING ---
  function highlightMatch(text, query) {
    if (!query) return escapeHtml(text);
    const regex = new RegExp('(' + query.replace(/[-/\\^$*+?.()|[\]{}]/g, '\\$&') + ')', 'gi');
    return escapeHtml(text).replace(regex, '<span style="color:#ff4d5a; font-weight:700;">$1</span>');
  }

  // --- REAL-TIME SEARCH INPUT HANDLER ---
  window.handleSearchInput = function(query) {
    const q = (query || '').trim().toLowerCase();
    const clearBtn = document.getElementById('searchClearBtn');
    const dropdown = document.getElementById('searchDropdown');
    const resultsList = document.getElementById('searchResultsList');
    const countBadge = document.getElementById('searchResultCount');

    if (clearBtn) clearBtn.style.display = q ? 'block' : 'none';

    if (!q) {
      currentSearchResults = [];
      selectedDropdownIndex = -1;
      if (resultsList) resultsList.innerHTML = '<div style="padding:12px 16px; font-family:var(--font-mono); font-size:0.68rem; color:var(--text-muted);">Type any concept (e.g. sticky input prices, crowding out, multiplier) to target instantly.</div>';
      if (countBadge) countBadge.textContent = 'READY';
      if (dropdown) dropdown.style.display = 'block';
      return;
    }

    // Match and score across SEARCH_INDEX
    const scored = [];
    SEARCH_INDEX.forEach(item => {
      let score = 0;
      const titleLower = item.title.toLowerCase();
      const subLower = item.subtitle.toLowerCase();

      // Check keywords
      for (const kw of item.keywords) {
        if (kw === q) score += 100;
        else if (kw.includes(q)) score += 50;
        else if (q.includes(kw)) score += 40;
      }
      if (titleLower.includes(q)) score += 30;
      if (subLower.includes(q)) score += 15;

      if (score > 0) {
        scored.push({ item, score });
      }
    });

    // Fallback: search headings in DOM if fewer than 2 matches
    if (scored.length < 2) {
      document.querySelectorAll('.topic-title, .section-subtitle, .chapter-title').forEach(heading => {
        const text = heading.innerText.toLowerCase();
        if (text.includes(q)) {
          const parentCh = heading.closest('.chapter-container, .mission-chapter');
          const chNumMatch = parentCh ? (parentCh.id.match(/\d+/) || [1]) : [1];
          const chNum = parseInt(chNumMatch[0], 10);
          const targetId = heading.id || parentCh.id;
          if (!scored.some(s => s.item.targetId === targetId)) {
            scored.push({
              item: {
                ch: chNum,
                targetId: targetId,
                badge: 'DOSSIER ' + (chNum < 10 ? '0' + chNum : chNum) + ' // TARGET',
                title: heading.innerText,
                subtitle: 'Section target located in Dossier ' + chNum,
                keywords: [q]
              },
              score: 20
            });
          }
        }
      });
    }

    scored.sort((a, b) => b.score - a.score);
    currentSearchResults = scored.slice(0, 7).map(s => s.item);
    selectedDropdownIndex = currentSearchResults.length > 0 ? 0 : -1;

    // Render results
    if (resultsList) {
      if (currentSearchResults.length === 0) {
        resultsList.innerHTML = '<div style="padding:14px 16px; font-family:var(--font-mono); font-size:0.7rem; color:var(--text-muted); text-align:center;">NO EXACT MATCHES FOUND FOR "' + escapeHtml(q) + '". PRESS ENTER TO TARGET FULL TEXT.</div>';
        if (countBadge) countBadge.textContent = '0 MATCHES';
      } else {
        if (countBadge) countBadge.textContent = currentSearchResults.length + ' MATCHES';
        let html = '';
        currentSearchResults.forEach((res, idx) => {
          const isSelected = idx === 0 ? ' selected' : '';
          html += '<div class="search-result-item' + isSelected + '" data-index="' + idx + '" onclick="jumpToTarget(\'' + res.targetId + '\', ' + res.ch + ')">';
          html += '  <div class="search-item-info">';
          html += '    <span class="search-item-badge">' + escapeHtml(res.badge) + '</span>';
          html += '    <span class="search-item-title">' + highlightMatch(res.title, q) + '</span>';
          html += '    <span class="search-item-snippet">' + highlightMatch(res.subtitle, q) + '</span>';
          html += '  </div>';
          html += '  <span class="search-item-action">TARGET ⌖</span>';
          html += '</div>';
        });
        resultsList.innerHTML = html;
      }
    }

    if (dropdown) dropdown.style.display = 'block';
  };

  // --- KEYBOARD ROUTING HANDLER (ENTER / ARROWS / ESC) ---
  window.handleSearchKeyDown = function(event) {
    const dropdown = document.getElementById('searchDropdown');
    const items = document.querySelectorAll('.search-result-item');

    if (event.key === 'ArrowDown') {
      event.preventDefault();
      if (items.length > 0) {
        selectedDropdownIndex = (selectedDropdownIndex + 1) % items.length;
        items.forEach((it, i) => it.classList.toggle('selected', i === selectedDropdownIndex));
        items[selectedDropdownIndex].scrollIntoView({ block: 'nearest' });
      }
      return;
    }

    if (event.key === 'ArrowUp') {
      event.preventDefault();
      if (items.length > 0) {
        selectedDropdownIndex = (selectedDropdownIndex - 1 + items.length) % items.length;
        items.forEach((it, i) => it.classList.toggle('selected', i === selectedDropdownIndex));
        items[selectedDropdownIndex].scrollIntoView({ block: 'nearest' });
      }
      return;
    }

    if (event.key === 'Escape') {
      if (dropdown) dropdown.style.display = 'none';
      return;
    }

    if (event.key === 'Enter') {
      event.preventDefault();
      window.executeSearch();
    }
  };

  // --- SEARCH FOCUS / BLUR ---
  window.handleSearchFocus = function() {
    const input = document.getElementById('globalSearchInput');
    const query = input ? input.value : '';
    window.handleSearchInput(query);
  };

  // --- EXECUTE SEARCH (ON ENTER OR BUTTON CLICK) ---
  window.executeSearch = function() {
    const input = document.getElementById('globalSearchInput');
    const query = input ? input.value.trim().toLowerCase() : '';
    if (!query) return;

    // 1. If an item is selected in dropdown results, jump to it
    if (currentSearchResults.length > 0) {
      const idx = selectedDropdownIndex >= 0 ? selectedDropdownIndex : 0;
      const target = currentSearchResults[idx];
      window.jumpToTarget(target.targetId, target.ch);
      return;
    }

    // 2. Direct keyword mapping lookup
    for (const item of SEARCH_INDEX) {
      if (item.keywords.some(k => query.includes(k) || k.includes(query))) {
        window.jumpToTarget(item.targetId, item.ch);
        return;
      }
    }

    // 3. Fallback scan across all chapters
    for (let i = 1; i <= 13; i++) {
      const el = document.getElementById('chapter-' + i) || document.getElementById('ch' + i);
      if (el && el.innerText.toLowerCase().includes(query)) {
        window.scrollToChapter(i);
        return;
      }
    }
  };

  // --- QUICK JUMP FROM PILL TAGS ---
  window.quickJumpSearch = function(term) {
    const input = document.getElementById('globalSearchInput');
    if (input) input.value = term;
    window.handleSearchInput(term);
    window.executeSearch();
  };

  // --- CLEAR SEARCH ---
  window.clearSearch = function() {
    const input = document.getElementById('globalSearchInput');
    if (input) input.value = '';
    const dropdown = document.getElementById('searchDropdown');
    if (dropdown) dropdown.style.display = 'none';
    const clearBtn = document.getElementById('searchClearBtn');
    if (clearBtn) clearBtn.style.display = 'none';
  };

  // --- PRECISE SECTION-LEVEL TARGET JUMP & RETICLE HIGHLIGHT ---
  window.jumpToTarget = function(targetId, chNum) {
    const dropdown = document.getElementById('searchDropdown');
    if (dropdown) dropdown.style.display = 'none';

    // Find the target element or chapter
    let targetEl = document.getElementById(targetId);
    if (!targetEl && chNum) {
      targetEl = document.getElementById('chapter-' + chNum) || document.getElementById('ch' + chNum);
    }
    if (!targetEl) return;

    // Calculate precise scroll coordinate with 85px header offset
    const rect = targetEl.getBoundingClientRect();
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    const targetY = Math.max(0, rect.top + scrollTop - 85);

    window.scrollTo({
      top: targetY,
      behavior: 'smooth'
    });

    // Update URL hash cleanly without instant jump
    try {
      history.pushState(null, null, '#' + targetId);
    } catch(e) {}

    // Apply authentic James Bond Red Target Reticle Pulse
    targetEl.classList.remove('target-reticle-pulse');
    void targetEl.offsetWidth; // trigger reflow
    targetEl.classList.add('target-reticle-pulse');
    setTimeout(() => {
      targetEl.classList.remove('target-reticle-pulse');
    }, 3200);

    // Update sidebar navigation active state
    if (chNum) {
      document.querySelectorAll('.sidebar-nav .nav-item').forEach((item, idx) => {
        item.classList.toggle('active', (idx + 1) === chNum);
      });
    }

    // Close mobile sidebar if open
    const sidebar = document.getElementById('sidebarNav');
    if (sidebar && sidebar.classList.contains('open')) {
      sidebar.classList.remove('open');
    }
  };

  // --- SMOOTH CHAPTER SCROLL (FOR TRACKING SIDEBAR & HERO LINKS) ---
  window.scrollToChapter = function(chNum) {
    const el = document.getElementById('chapter-' + chNum) || document.getElementById('ch' + chNum);
    if (el) {
      const rect = el.getBoundingClientRect();
      const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      const targetY = Math.max(0, rect.top + scrollTop - 85);

      window.scrollTo({
        top: targetY,
        behavior: 'smooth'
      });

      // Red reticle pulse on chapter
      el.classList.remove('target-reticle-pulse');
      void el.offsetWidth;
      el.classList.add('target-reticle-pulse');
      setTimeout(() => el.classList.remove('target-reticle-pulse'), 2500);

      // Update sidebar nav active state
      document.querySelectorAll('.sidebar-nav .nav-item').forEach((item, idx) => {
        item.classList.toggle('active', (idx + 1) === chNum);
      });

      try {
        history.pushState(null, null, '#chapter-' + chNum);
      } catch(e) {}
    }
  };

  // --- SIDEBAR NAV CLICK HANDLER (100% RELIABLE) ---
  window.navigateToChapter = function(event, chNum) {
    if (event) event.preventDefault();
    window.scrollToChapter(chNum);
  };

  // Compatibility alias
  window.activateNavLink = function(el, chNum) {
    window.scrollToChapter(chNum);
  };

  // Sidebar navigation and collapse controller
  window.toggleSidebarCollapse = function() {
    const sidebar = document.getElementById('sidebarNav');
    const collapseBtn = document.getElementById('sidebarCollapseBtn');
    const collapseIcon = document.getElementById('sidebarCollapseIcon');
    if (!sidebar) return;

    const isCollapsed = sidebar.classList.toggle('collapsed');
    if (collapseIcon) {
      collapseIcon.textContent = isCollapsed ? '▶' : '◀';
    }
    if (collapseBtn) {
      collapseBtn.setAttribute('title', isCollapsed ? 'Expand Intelligence Dossiers' : 'Collapse Intelligence Dossiers');
    }
    try {
      localStorage.setItem('sidebar_collapsed_007', isCollapsed ? '1' : '0');
    } catch(e) {}
  };

  // Mobile drawer and desktop collapse toggle
  window.toggleSidebar = function() {
    if (window.innerWidth > 900) {
      window.toggleSidebarCollapse();
    } else {
      const sidebar = document.getElementById('sidebarNav') || document.getElementById('sidebar');
      if (sidebar) sidebar.classList.toggle('open');
    }
  };

  // Close search dropdown on click outside
  document.addEventListener('click', function(e) {
    const wrap = document.getElementById('headerSearchWrap');
    const dropdown = document.getElementById('searchDropdown');
    if (wrap && dropdown && !wrap.contains(e.target)) {
      dropdown.style.display = 'none';
    }
  });

  // =========================================================================
  // --- TACTICAL RED CROSSHAIR / TARGET AIM FOR EQUILIBRIUM POINTS ---
  // =========================================================================
  function drawTargetCrosshair(ctx, x, y, label) {
    ctx.save();
    // Outer red aim ring
    ctx.strokeStyle = '#d92534';
    ctx.lineWidth = 1.8;
    ctx.beginPath();
    ctx.arc(x, y, 12, 0, 2 * Math.PI);
    ctx.stroke();

    // Inner reticle ring
    ctx.strokeStyle = '#ff4d5a';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.arc(x, y, 5, 0, 2 * Math.PI);
    ctx.stroke();

    // Center aim pip
    ctx.fillStyle = '#ffffff';
    ctx.beginPath();
    ctx.arc(x, y, 2, 0, 2 * Math.PI);
    ctx.fill();

    // 4 Crosshair ticks with scope gap
    ctx.strokeStyle = '#d92534';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    // Top
    ctx.moveTo(x, y - 18);
    ctx.lineTo(x, y - 7);
    // Bottom
    ctx.moveTo(x, y + 7);
    ctx.lineTo(x, y + 18);
    // Left
    ctx.moveTo(x - 18, y);
    ctx.lineTo(x - 7, y);
    // Right
    ctx.moveTo(x + 7, y);
    ctx.lineTo(x + 18, y);
    ctx.stroke();

    // Tactical Target Text label
    if (label) {
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 10px "Space Grotesk", sans-serif';
      ctx.fillText(label, x + 16, y - 8);
    }
    ctx.restore();
  }

  // =========================================================================
  // --- GRAPH ENGINE 1: BUSINESS CYCLE & OUTPUT GAP ANALYZER ---
  // =========================================================================
  window.initBusinessCycleGraph = function() {
    const canvas = document.getElementById('businessCycleCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const slider = document.getElementById('bcTimeSlider');
    const readOutGap = document.getElementById('bcGapReadout');
    const readOutPhase = document.getElementById('bcPhaseReadout');
    const readOutPolicy = document.getElementById('bcPolicyReadout');

    function draw() {
      const w = canvas.width = canvas.parentElement.clientWidth;
      const h = canvas.height = canvas.parentElement.clientHeight;
      ctx.clearRect(0, 0, w, h);

      // Gridlines
      ctx.strokeStyle = 'rgba(213, 219, 228, 0.08)';
      ctx.lineWidth = 1;
      for (let x = 60; x < w; x += 60) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
      }
      for (let y = 30; y < h; y += 40) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
      }

      // Axes
      const originX = 60;
      const originY = h - 40;
      ctx.strokeStyle = '#adb6c4';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(originX, 20);
      ctx.lineTo(originX, originY);
      ctx.lineTo(w - 20, originY);
      ctx.stroke();

      // Axis Labels
      ctx.fillStyle = '#adb6c4';
      ctx.font = '10px "SF Mono", monospace';
      ctx.fillText('REAL GDP (Y)', 10, 25);
      ctx.fillText('TIME (t)', w - 70, originY + 25);

      // Potential GDP Trend (Upward Sloping Line)
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.6)';
      ctx.setLineDash([6, 6]);
      ctx.beginPath();
      const pStart = { x: originX, y: originY - 120 };
      const pEnd = { x: w - 30, y: originY - 240 };
      ctx.moveTo(pStart.x, pStart.y);
      ctx.lineTo(pEnd.x, pEnd.y);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
      ctx.fillText('POTENTIAL OUTPUT (Y*)', w - 170, pEnd.y - 8);

      // Actual GDP Curve (Wave)
      ctx.strokeStyle = '#d92534';
      ctx.lineWidth = 3;
      ctx.beginPath();
      const numPoints = 200;
      const totalWidth = w - 90;
      const points = [];

      for (let i = 0; i <= numPoints; i++) {
        const tRatio = i / numPoints;
        const curX = originX + tRatio * totalWidth;
        // Potential at this x
        const curYp = pStart.y + tRatio * (pEnd.y - pStart.y);
        // Wave deviation
        const wave = Math.sin(tRatio * 2 * Math.PI * 1.5 - Math.PI / 2) * 85;
        const curY = curYp - wave; // canvas Y is inverted
        points.push({ x: curX, y: curY, yp: curYp, wave: wave });
        if (i === 0) ctx.moveTo(curX, curY);
        else ctx.lineTo(curX, curY);
      }
      ctx.stroke();

      // Active Time Position from Slider
      const sliderVal = slider ? parseFloat(slider.value) : 25; // 0 to 100
      const activeIdx = Math.round((sliderVal / 100) * numPoints);
      const activePt = points[activeIdx] || points[0];

      // Draw Output Gap Vertical Bar at active position
      ctx.strokeStyle = activePt.wave >= 0 ? '#10b981' : '#f59e0b';
      ctx.lineWidth = 2;
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(activePt.x, activePt.yp);
      ctx.lineTo(activePt.x, activePt.y);
      ctx.stroke();
      ctx.setLineDash([]);

      // Draw Current Coordinate Point with Red Target Aim Crosshair
      drawTargetCrosshair(ctx, activePt.x, activePt.y, 'TARGET // OPS ' + Math.round(slider.value));

      // Potential Point reference
      ctx.fillStyle = '#828e9f';
      ctx.beginPath();
      ctx.arc(activePt.x, activePt.yp, 4, 0, 2 * Math.PI);
      ctx.fill();

      // Calculate economic readout values
      // wave > 0 means Y > Y* (Inflationary gap), wave < 0 means Recessionary gap
      const gapPercent = ((activePt.wave / 140) * 12).toFixed(2); // normalized percent
      let phase = 'Expansion';
      let policy = 'Neutral stance';

      // Determine phase via slope of wave
      const nextIdx = Math.min(numPoints, activeIdx + 2);
      const prevIdx = Math.max(0, activeIdx - 2);
      const slope = points[nextIdx].wave - points[prevIdx].wave;

      if (activePt.wave > 65) {
        phase = 'Peak';
        policy = 'Contractionary Policy (G↓, T↑, Repo↑) to restrain overheating';
      } else if (activePt.wave < -65) {
        phase = 'Trough';
        policy = 'Expansionary Stimulus (G↑, T↓, Repo↓, CRR↓) to ignite recovery';
      } else if (slope > 0) {
        phase = activePt.wave >= 0 ? 'Boom / Overheating' : 'Recovery';
        policy = activePt.wave >= 0 ? 'Monitor inflationary expectations' : 'Accommodative monetary stance';
      } else {
        phase = activePt.wave >= 0 ? 'Slowdown' : 'Contraction / Recession';
        policy = 'Countercyclical stabilization';
      }

      if (readOutGap) {
        readOutGap.textContent = (gapPercent >= 0 ? '+' : '') + gapPercent + '% (' + (gapPercent >= 0 ? 'Inflationary Gap' : 'Recessionary Gap') + ')';
        readOutGap.style.color = gapPercent >= 0 ? '#10b981' : '#f59e0b';
      }
      if (readOutPhase) readOutPhase.textContent = phase;
      if (readOutPolicy) readOutPolicy.textContent = policy;
    }

    if (slider) {
      slider.addEventListener('input', draw);
    }
    window.addEventListener('resize', draw);
    draw();
  };

  // =========================================================================
  // --- GRAPH ENGINE 2: LOANABLE FUNDS & SAVINGS-INVESTMENT SIMULATOR ---
  // =========================================================================
  window.initLoanableFundsGraph = function() {
    const canvas = document.getElementById('loanableFundsCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const sShiftSlider = document.getElementById('lfSaveShift');
    const iShiftSlider = document.getElementById('lfInvShift');
    const rReadout = document.getElementById('lfRReadout');
    const qReadout = document.getElementById('lfQReadout');
    const reckonerReadout = document.getElementById('lfReckonerReadout');

    function draw() {
      const w = canvas.width = canvas.parentElement.clientWidth;
      const h = canvas.height = canvas.parentElement.clientHeight;
      ctx.clearRect(0, 0, w, h);

      const sShift = sShiftSlider ? parseFloat(sShiftSlider.value) : 0; // -50 to +50
      const iShift = iShiftSlider ? parseFloat(iShiftSlider.value) : 0; // -50 to +50

      // Origin
      const ox = 70;
      const oy = h - 50;

      // Axes
      ctx.strokeStyle = '#adb6c4';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(ox, 20);
      ctx.lineTo(ox, oy);
      ctx.lineTo(w - 30, oy);
      ctx.stroke();

      ctx.fillStyle = '#adb6c4';
      ctx.font = '10px "SF Mono", monospace';
      ctx.fillText('REAL INTEREST RATE r (%)', 10, 20);
      ctx.fillText('LOANABLE FUNDS S, I', w - 140, oy + 25);

      // Base Curves (Midsem Model: S = 1000 + 100r, I = 1600 - 100r)
      // Initial Eq: r = 3%, S = I = 1300
      const scaleX = (w - 120) / 1000; // units
      const scaleY = (oy - 40) / 10;   // percent 0 to 10%

      // Original S curve (blue/silver)
      ctx.strokeStyle = 'rgba(173, 182, 196, 0.4)';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(ox + (1000 - 800) * scaleX, oy - (0) * scaleY);
      ctx.lineTo(ox + (1000 + 100 * 8 - 800) * scaleX, oy - 8 * scaleY);
      ctx.stroke();
      ctx.fillText('S₀', ox + (1800 - 800) * scaleX + 6, oy - 8 * scaleY);

      // Original I curve (blue/silver)
      ctx.beginPath();
      ctx.moveTo(ox + (1600 - 100 * 8 - 800) * scaleX, oy - 8 * scaleY);
      ctx.lineTo(ox + (1600 - 800) * scaleX, oy - 0 * scaleY);
      ctx.stroke();
      ctx.fillText('I₀', ox + (1600 - 800) * scaleX + 6, oy - 0 * scaleY + 12);

      // Shifted S' Curve
      const baseS0 = 1000 + sShift * 5;
      const baseI0 = 1600 + iShift * 5;

      ctx.strokeStyle = '#60a5fa'; // Blue for Saving
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(ox + (baseS0 - 800) * scaleX, oy - 0 * scaleY);
      ctx.lineTo(ox + (baseS0 + 800 - 800) * scaleX, oy - 8 * scaleY);
      ctx.stroke();
      ctx.fillStyle = '#60a5fa';
      ctx.fillText("S'", ox + (baseS0 + 800 - 800) * scaleX + 6, oy - 8 * scaleY);

      // Shifted I' Curve
      ctx.strokeStyle = '#f87171'; // Red for Investment
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(ox + (baseI0 - 800 - 800) * scaleX, oy - 8 * scaleY);
      ctx.lineTo(ox + (baseI0 - 800) * scaleX, oy - 0 * scaleY);
      ctx.stroke();
      ctx.fillStyle = '#f87171';
      ctx.fillText("I'", ox + (baseI0 - 800) * scaleX + 6, oy - 0 * scaleY + 12);

      // New Equilibrium: baseS0 + 100r = baseI0 - 100r => 200r = baseI0 - baseS0
      const newR = (baseI0 - baseS0) / 200;
      const newQ = baseS0 + 100 * newR;

      const eqCanvasX = ox + (newQ - 800) * scaleX;
      const eqCanvasY = oy - newR * scaleY;

      // Draw dashed lines to axes
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(eqCanvasX, oy);
      ctx.lineTo(eqCanvasX, eqCanvasY);
      ctx.lineTo(ox, eqCanvasY);
      ctx.stroke();
      ctx.setLineDash([]);

      // Target Aim Crosshair for Equilibrium Point
      drawTargetCrosshair(ctx, eqCanvasX, eqCanvasY, 'TARGET E* (' + newR.toFixed(1) + '%, ' + Math.round(newQ) + ')');

      // Readouts
      if (rReadout) rReadout.textContent = newR.toFixed(2) + '%';
      if (qReadout) qReadout.textContent = Math.round(newQ) + ' units';

      // Ready Reckoner logic
      let reckoner = 'Baseline Equilibrium';
      if (sShift > 0 && iShift > 0) {
        reckoner = 'Scenario 1 (Both Right): Quantity Determinate (↑), Interest Rate Indeterminate (' + (newR > 3 ? 'r↑ because ΔI > ΔS' : newR < 3 ? 'r↓ because ΔS > ΔI' : 'r unchanged') + ')';
      } else if (sShift < 0 && iShift < 0) {
        reckoner = 'Scenario 2 (Both Left): Quantity Determinate (↓), Interest Rate Indeterminate (' + (newR > 3 ? 'r↑' : 'r↓') + ')';
      } else if (sShift < 0 && iShift > 0) {
        reckoner = 'Scenario 3 (S Left, I Right): Interest Rate Determinate (↑), Quantity Indeterminate';
      } else if (sShift > 0 && iShift < 0) {
        reckoner = 'Scenario 4 (S Right, I Left): Interest Rate Determinate (↓), Quantity Indeterminate';
      }
      if (reckonerReadout) reckonerReadout.textContent = reckoner;
    }

    if (sShiftSlider) sShiftSlider.addEventListener('input', draw);
    if (iShiftSlider) iShiftSlider.addEventListener('input', draw);
    window.addEventListener('resize', draw);
    draw();
  };

  // =========================================================================
  // --- GRAPH ENGINE 3: MULTIPLIER CASCADE RIPPLE ENGINE ---
  // =========================================================================
  window.initMultiplierCascade = function() {
    const mpcSlider = document.getElementById('multMpcSlider');
    const injSlider = document.getElementById('multInjSlider');
    const tableBody = document.getElementById('multiplierRoundsTable');
    const kReadout = document.getElementById('multKReadout');
    const totalYReadout = document.getElementById('multTotalYReadout');

    function update() {
      const mpc = mpcSlider ? parseFloat(mpcSlider.value) : 0.75;
      const inj = injSlider ? parseFloat(injSlider.value) : 100;
      const mps = 1 - mpc;
      const k = 1 / mps;
      const totalDY = inj * k;

      if (kReadout) kReadout.textContent = k.toFixed(2);
      if (totalYReadout) totalYReadout.textContent = '₹' + totalDY.toFixed(1) + ' cr';

      if (!tableBody) return;
      tableBody.innerHTML = '';

      let currentRoundSpending = inj;
      let cumSpending = 0;

      for (let r = 1; r <= 8; r++) {
        let inducedC = r === 1 ? inj : currentRoundSpending * mpc;
        let leakageS = r === 1 ? 0 : currentRoundSpending * mps;
        cumSpending += inducedC;
        currentRoundSpending = inducedC;

        const row = document.createElement('tr');
        row.innerHTML = `
          <td><strong>Round ${r}</strong></td>
          <td>₹${inducedC.toFixed(1)} cr</td>
          <td>₹${leakageS.toFixed(1)} cr</td>
          <td><strong>₹${cumSpending.toFixed(1)} cr</strong></td>
          <td><div style="background:var(--silver-500); height:6px; width:${Math.min(100, (cumSpending/totalDY)*100)}%; border-radius:3px;"></div></td>
        `;
        tableBody.appendChild(row);
      }

      // Add final convergence row
      const finalRow = document.createElement('tr');
      finalRow.style.background = 'rgba(16, 185, 129, 0.1)';
      finalRow.style.fontWeight = 'bold';
      finalRow.innerHTML = `
        <td style="color:#10b981;">Convergence (Round ∞)</td>
        <td style="color:#10b981;">Total ΔY = k × ΔInjection</td>
        <td style="color:#f59e0b;">Total Leakage = ₹${inj.toFixed(1)} cr</td>
        <td style="color:#10b981;">₹${totalDY.toFixed(1)} cr</td>
        <td>100% Complete</td>
      `;
      tableBody.appendChild(finalRow);
    }

    if (mpcSlider) mpcSlider.addEventListener('input', update);
    if (injSlider) injSlider.addEventListener('input', update);
    update();
  };

  // =========================================================================
  // --- GRAPH ENGINE 4: TACTICAL AD–AS SIMULATOR ---
  // =========================================================================
  window.initAdAsGraph = function() {
    const canvas = document.getElementById('adAsCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let currentScenario = 'ad_pos'; // ad_pos, ad_neg, sras_neg, sras_pos, lras_pos, lras_neg
    let mechanism = 'short_run'; // short_run, self_correction, policy_intervention

    window.setAdAsScenario = function(scen, btn) {
      currentScenario = scen;
      document.querySelectorAll('.adas-scen-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      draw();
    };

    window.setAdAsMechanism = function(mech, btn) {
      mechanism = mech;
      document.querySelectorAll('.adas-mech-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      draw();
    };

    function draw() {
      const w = canvas.width = canvas.parentElement.clientWidth;
      const h = canvas.height = canvas.parentElement.clientHeight;
      ctx.clearRect(0, 0, w, h);

      const ox = 70;
      const oy = h - 50;

      // Axes
      ctx.strokeStyle = '#adb6c4';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(ox, 20);
      ctx.lineTo(ox, oy);
      ctx.lineTo(w - 30, oy);
      ctx.stroke();

      ctx.fillStyle = '#adb6c4';
      ctx.font = '10px "SF Mono", monospace';
      ctx.fillText('OVERALL PRICE LEVEL (P)', 10, 20);
      ctx.fillText('REAL OUTPUT (Y)', w - 120, oy + 25);

      const lrasX = ox + (w - ox) * 0.48; // Potential GDP line

      // Initial LRAS (Dashed Vertical)
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.7)';
      ctx.lineWidth = 2;
      ctx.setLineDash([6, 6]);
      ctx.beginPath();
      ctx.moveTo(lrasX, 25);
      ctx.lineTo(lrasX, oy);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillText('LRAS₀ (Y*)', lrasX - 25, 20);

      // Baseline AD0 and SRAS0
      const eqY0 = oy - (oy - 30) * 0.5;

      ctx.strokeStyle = 'rgba(173, 182, 196, 0.35)';
      ctx.lineWidth = 2;

      // AD0
      ctx.beginPath();
      ctx.moveTo(lrasX - 160, eqY0 - 100);
      ctx.lineTo(lrasX + 160, eqY0 + 100);
      ctx.stroke();
      ctx.fillText('AD₀', lrasX + 165, eqY0 + 105);

      // SRAS0
      ctx.beginPath();
      ctx.moveTo(lrasX - 160, eqY0 + 100);
      ctx.lineTo(lrasX + 160, eqY0 - 100);
      ctx.stroke();
      ctx.fillText('SRAS₀', lrasX + 165, eqY0 - 105);

      // Initial Eq Point E0 with Red Target Crosshairs
      drawTargetCrosshair(ctx, lrasX, eqY0, 'TARGET E₀ (100, Y*)');

      // Scenario Shifts calculation
      let newAdX = 0, newSrasY = 0, newLrasX = lrasX;
      let note = '';

      if (currentScenario === 'ad_pos') {
        newAdX = 70; // Shift AD Right
        note = 'Positive Demand Shock (Investment/Consumer boom): AD shifts right to AD₁. Short run: Y > Y*, P rises. Inflationary gap!';
        if (mechanism === 'self_correction') {
          newSrasY = -70; // SRAS shifts left
          note += ' Self-Correction: Tight labor market pushes nominal wages up → SRAS shifts left to SRAS₁ → Economy returns to Y* at higher price level.';
        } else if (mechanism === 'policy_intervention') {
          note += ' Policy Intervention: Central bank / Government implements contractionary policy (Repo↑, G↓) → AD shifts back left to AD₀, restoring potential output without prolonged inflation.';
        }
      } else if (currentScenario === 'ad_neg') {
        newAdX = -70; // Shift AD Left
        note = 'Negative Demand Shock (Recession/Crisis): AD shifts left to AD₁. Short run: Y < Y*, P falls, unemployment rises. Recessionary gap!';
        if (mechanism === 'self_correction') {
          newSrasY = 70; // SRAS shifts right
          note += ' Self-Correction: High unemployment puts downward pressure on wages → SRAS shifts right → Output returns to Y* at lower price level.';
        } else if (mechanism === 'policy_intervention') {
          note += ' Policy Intervention: Expansionary stimulus (G↑, T↓, Repo↓) shifts AD back right to AD₀ rapidly to restore full employment.';
        }
      } else if (currentScenario === 'sras_neg') {
        newSrasY = -70; // SRAS shifts left (oil shock / stagflation)
        note = 'Negative Temporary Supply Shock / Stagflation (Caledonia case): Input prices surge → SRAS shifts left. Output falls below potential while price level rises!';
        if (mechanism === 'self_correction') {
          note += ' Self-Correction: Sustained high unemployment eventually moderates wage demands → SRAS shifts back right to SRAS₀.';
        } else if (mechanism === 'policy_intervention') {
          note += ' Policy Dilemma: Expansionary policy shifts AD right (eliminates recession but worsens inflation); Contractionary policy lowers prices but deepens output loss. Monetary policy cannot simultaneously fix both!';
        }
      } else if (currentScenario === 'sras_pos') {
        newSrasY = 70; // SRAS shifts right (bumper harvest / energy drop)
        note = 'Positive Temporary Supply Shock: Lower production costs shift SRAS right → Output rises above potential and price level falls.';
      } else if (currentScenario === 'lras_pos') {
        newLrasX = lrasX + 70;
        newSrasY = 40; // Technology / infrastructure expansion
        note = 'Permanent Positive Supply Shock (Kumbh Mela / AI diffusion): Productive capacity increases permanently → Both LRAS and SRAS shift right → Higher potential GDP with lower price level.';
      }

      // Draw Shifted Curves
      if (newAdX !== 0 && mechanism !== 'policy_intervention') {
        ctx.strokeStyle = '#60a5fa'; // Shifted AD
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(lrasX - 160 + newAdX, eqY0 - 100);
        ctx.lineTo(lrasX + 160 + newAdX, eqY0 + 100);
        ctx.stroke();
        ctx.fillStyle = '#60a5fa';
        ctx.fillText('AD₁', lrasX + 165 + newAdX, eqY0 + 105);
      }

      if (newSrasY !== 0) {
        ctx.strokeStyle = '#f87171'; // Shifted SRAS
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(lrasX - 160, eqY0 + 100 + newSrasY);
        ctx.lineTo(lrasX + 160, eqY0 - 100 + newSrasY);
        ctx.stroke();
        ctx.fillStyle = '#f87171';
        ctx.fillText('SRAS₁', lrasX + 165, eqY0 - 105 + newSrasY);
      }

      if (newLrasX !== lrasX) {
        ctx.strokeStyle = '#34d399';
        ctx.lineWidth = 2.5;
        ctx.setLineDash([6, 6]);
        ctx.beginPath();
        ctx.moveTo(newLrasX, 25);
        ctx.lineTo(newLrasX, oy);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = '#34d399';
        ctx.fillText('LRAS₁ (Permanent Boost)', newLrasX - 30, 38);
      }

      // Draw Shifted Equilibrium Target Crosshair if shock active
      if (newAdX !== 0 || newSrasY !== 0 || newLrasX !== lrasX) {
        const shiftedEqX = newLrasX !== lrasX ? newLrasX : (lrasX + (newAdX * 0.45));
        const shiftedEqY = eqY0 + (newSrasY * 0.5) - (newAdX * 0.35);
        drawTargetCrosshair(ctx, shiftedEqX, shiftedEqY, 'TARGET E₁');
      }

      const descBox = document.getElementById('adAsDescText');
      if (descBox) descBox.textContent = note;
    }

    window.addEventListener('resize', draw);
    draw();
  };

  // =========================================================================
  // --- GRAPH ENGINE 5: IS–LM TACTICAL SIMULATOR ---
  // =========================================================================
  window.initIsLmGraph = function() {
    const canvas = document.getElementById('isLmCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let isZlb = false;
    let isCoordMix = false;

    const gSlider = document.getElementById('islmGSlider');
    const mSlider = document.getElementById('islmMSlider');
    const yReadout = document.getElementById('islmYReadout');
    const rReadout = document.getElementById('islmRReadout');
    const iReadout = document.getElementById('islmIReadout');

    window.toggleLiquidityTrap = function(btn) {
      isZlb = !isZlb;
      isCoordMix = false;
      if (btn) btn.classList.toggle('active', isZlb);
      const coordBtn = document.getElementById('islmCoordBtn');
      if (coordBtn) coordBtn.classList.remove('active');
      draw();
    };

    window.toggleCoordinatedMix = function(btn) {
      isCoordMix = !isCoordMix;
      isZlb = false;
      if (btn) btn.classList.toggle('active', isCoordMix);
      const zlbBtn = document.getElementById('islmZlbBtn');
      if (zlbBtn) zlbBtn.classList.remove('active');
      draw();
    };

    function draw() {
      const w = canvas.width = canvas.parentElement.clientWidth;
      const h = canvas.height = canvas.parentElement.clientHeight;
      ctx.clearRect(0, 0, w, h);

      const ox = 70;
      const oy = h - 50;

      // Axes
      ctx.strokeStyle = '#adb6c4';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(ox, 20);
      ctx.lineTo(ox, oy);
      ctx.lineTo(w - 30, oy);
      ctx.stroke();

      ctx.fillStyle = '#adb6c4';
      ctx.font = '10px "SF Mono", monospace';
      ctx.fillText('INTEREST RATE r (%)', 10, 20);
      ctx.fillText('NATIONAL INCOME Y', w - 130, oy + 25);

      // Model parameters based on RBI Case Study:
      // IS0: Y = 4000 - 100r => r = 40 - 0.01Y
      // LM0: Y = 2000 + 100r => r = 0.01Y - 20
      // Eq0: r = 10%, Y = 3000, I = 1000 - 40(10) = 600

      let gShift = gSlider ? parseFloat(gSlider.value) : 0; // -600 to +600
      let mShift = mSlider ? parseFloat(mSlider.value) : 0; // -600 to +600

      if (isCoordMix) {
        gShift = -400; // Fiscal contraction IS left
        mShift = 400;  // Monetary expansion LM right
      }

      // Convert equation parameters to canvas coordinates
      const scaleX = (w - 140) / 4000;
      const scaleY = (oy - 40) / 25;

      // Draw Baseline IS0 and LM0 (muted)
      ctx.strokeStyle = 'rgba(173, 182, 196, 0.35)';
      ctx.lineWidth = 2;

      // IS0 (Y from 1500 to 4000)
      ctx.beginPath();
      ctx.moveTo(ox + 1500 * scaleX, oy - (40 - 0.01 * 1500) * scaleY);
      ctx.lineTo(ox + 3800 * scaleX, oy - (40 - 0.01 * 3800) * scaleY);
      ctx.stroke();
      ctx.fillText('IS₀', ox + 3820 * scaleX, oy - (40 - 0.01 * 3800) * scaleY);

      // LM0
      if (!isZlb) {
        ctx.beginPath();
        ctx.moveTo(ox + 2000 * scaleX, oy - 0 * scaleY);
        ctx.lineTo(ox + 3800 * scaleX, oy - (0.01 * 3800 - 20) * scaleY);
        ctx.stroke();
        ctx.fillText('LM₀', ox + 3820 * scaleX, oy - (0.01 * 3800 - 20) * scaleY);
      }

      // Active / Shifted Curves
      let eqR, eqY;

      if (isZlb) {
        // Horizontal LM at r = 1%
        ctx.strokeStyle = '#06b6d4';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(ox, oy - 1 * scaleY);
        ctx.lineTo(w - 30, oy - 1 * scaleY);
        ctx.stroke();
        ctx.fillStyle = '#06b6d4';
        ctx.fillText('LM (Liquidity Trap: Horizontal at ZLB)', ox + 20, oy - 1 * scaleY - 8);

        // IS curve in liquidity trap
        const activeIS_const = 4000 + gShift;
        eqR = 1.0;
        eqY = activeIS_const - 100 * eqR;

        ctx.strokeStyle = '#f87171';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(ox + 1500 * scaleX, oy - ((activeIS_const - 1500)/100) * scaleY);
        ctx.lineTo(ox + 3800 * scaleX, oy - ((activeIS_const - 3800)/100) * scaleY);
        ctx.stroke();
        ctx.fillText('IS', ox + 3820 * scaleX, oy - ((activeIS_const - 3800)/100) * scaleY);

      } else {
        // Standard or Coordinated Mix
        const isConst = 4000 + gShift;
        const lmConst = 2000 + mShift;

        // Equilibrium: isConst - 100r = lmConst + 100r => 200r = isConst - lmConst
        eqR = (isConst - lmConst) / 200;
        eqY = isConst - 100 * eqR;

        // Shifted IS
        ctx.strokeStyle = '#f87171';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(ox + 1500 * scaleX, oy - ((isConst - 1500)/100) * scaleY);
        ctx.lineTo(ox + 3800 * scaleX, oy - ((isConst - 3800)/100) * scaleY);
        ctx.stroke();
        ctx.fillStyle = '#f87171';
        ctx.fillText('IS₁', ox + 3820 * scaleX, oy - ((isConst - 3800)/100) * scaleY);

        // Shifted LM
        ctx.strokeStyle = '#60a5fa';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(ox + lmConst * scaleX, oy - 0 * scaleY);
        ctx.lineTo(ox + 3800 * scaleX, oy - ((3800 - lmConst)/100) * scaleY);
        ctx.stroke();
        ctx.fillStyle = '#60a5fa';
        ctx.fillText('LM₁', ox + 3820 * scaleX, oy - ((3800 - lmConst)/100) * scaleY);
      }

      // Investment calculation: I = 1000 - 40r
      const pInv = 1000 - 40 * eqR;

      // Draw dashed lines and point
      const ptX = ox + eqY * scaleX;
      const ptY = oy - eqR * scaleY;

      ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(ptX, oy);
      ctx.lineTo(ptX, ptY);
      ctx.lineTo(ox, ptY);
      ctx.stroke();
      ctx.setLineDash([]);

      // Target Aim Crosshair for IS-LM Equilibrium
      drawTargetCrosshair(ctx, ptX, ptY, 'TARGET E* (Y=' + Math.round(eqY) + ', r=' + eqR.toFixed(1) + '%)');

      // Readouts
      if (yReadout) yReadout.textContent = Math.round(eqY) + ' units';
      if (rReadout) rReadout.textContent = eqR.toFixed(1) + '%';
      if (iReadout) {
        iReadout.textContent = Math.round(pInv) + ' units';
        if (pInv > 600) iReadout.style.color = '#10b981';
        else if (pInv < 600) iReadout.style.color = '#f87171';
        else iReadout.style.color = '#silver-100';
      }
    }

    if (gSlider) gSlider.addEventListener('input', draw);
    if (mSlider) mSlider.addEventListener('input', draw);
    window.addEventListener('resize', draw);
    draw();
  };

  // =========================================================================
  // --- GRAPH ENGINE 6: PHILLIPS CURVE & DUAL SIMULATOR ---
  // =========================================================================
  window.initPhillipsGraph = function() {
    const canvas = document.getElementById('phillipsCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const uSlider = document.getElementById('pcUSlider');
    const expInfSlider = document.getElementById('pcExpInfSlider');
    const actInfReadout = document.getElementById('pcActInfReadout');
    const nruReadout = document.getElementById('pcNruReadout');
    const tradeOffReadout = document.getElementById('pcTradeoffReadout');

    function draw() {
      const w = canvas.width = canvas.parentElement.clientWidth;
      const h = canvas.height = canvas.parentElement.clientHeight;
      ctx.clearRect(0, 0, w, h);

      const ox = 70;
      const oy = h - 50;

      // Axes
      ctx.strokeStyle = '#adb6c4';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(ox, 20);
      ctx.lineTo(ox, oy);
      ctx.lineTo(w - 30, oy);
      ctx.stroke();

      ctx.fillStyle = '#adb6c4';
      ctx.font = '10px "SF Mono", monospace';
      ctx.fillText('INFLATION RATE π (%)', 10, 20);
      ctx.fillText('UNEMPLOYMENT RATE u (%)', w - 150, oy + 25);

      // Model parameters: Natural rate = 6%, beta = 2, pi = pi_e - 2*(u - 6%)
      const nru = 6.0;
      const uVal = uSlider ? parseFloat(uSlider.value) : 4.0; // 2% to 10%
      const pi_e = expInfSlider ? parseFloat(expInfSlider.value) : 4.0; // 0% to 10%

      const actualPi = pi_e - 2.0 * (uVal - nru);

      const scaleU = (w - 120) / 10;  // 0% to 10%
      const scalePi = (oy - 40) / 14; // 0% to 14%

      // Draw Vertical LRPC at NRU = 6%
      const nruX = ox + nru * scaleU;
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(nruX, 25);
      ctx.lineTo(nruX, oy);
      ctx.stroke();
      ctx.fillText('LRPC (NRU = 6%)', nruX - 45, 20);

      // Draw Downward Sloping SRPC Curve
      // pi = pi_e - 2*(u - 6) => as u goes from 2 to 9
      ctx.strokeStyle = '#60a5fa';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let u = 2.5; u <= 9.5; u += 0.2) {
        const p = pi_e - 2.0 * (u - nru);
        const px = ox + u * scaleU;
        const py = oy - p * scalePi;
        if (u === 2.5) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();
      ctx.fillStyle = '#60a5fa';
      ctx.fillText(`SRPC (πᵉ = ${pi_e}%)`, ox + 8.5 * scaleU, oy - (pi_e - 2*(8.5-nru))*scalePi - 10);

      // Current Point (uVal, actualPi)
      const curX = ox + uVal * scaleU;
      const curY = oy - actualPi * scalePi;

      ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(curX, oy);
      ctx.lineTo(curX, curY);
      ctx.lineTo(ox, curY);
      ctx.stroke();
      ctx.setLineDash([]);

      // Target Aim Crosshair for Phillips Operating Point
      drawTargetCrosshair(ctx, curX, curY, 'TARGET (u=' + uVal.toFixed(1) + '%, π=' + actualPi.toFixed(1) + '%)');

      // Readouts
      if (actInfReadout) actInfReadout.textContent = actualPi.toFixed(1) + '%';
      if (nruReadout) nruReadout.textContent = nru.toFixed(1) + '%';
      if (tradeOffReadout) {
        if (Math.abs(uVal - nru) < 0.1) {
          tradeOffReadout.textContent = 'Long-Run Equilibrium: u = NRU, π = πᵉ. Trade-off vanished.';
          tradeOffReadout.style.color = '#10b981';
        } else if (uVal < nru) {
          tradeOffReadout.textContent = 'Short-Run Boom: u < NRU, Inflation accelerated above expectations.';
          tradeOffReadout.style.color = '#f59e0b';
        } else {
          tradeOffReadout.textContent = 'Short-Run Slump: u > NRU, Disinflationary pressure below expectations.';
          tradeOffReadout.style.color = '#60a5fa';
        }
      }
    }

    if (uSlider) uSlider.addEventListener('input', draw);
    if (expInfSlider) expInfSlider.addEventListener('input', draw);
    window.addEventListener('resize', draw);
    draw();
  };

  // --- FUNCTIONING SIMULATION RESET CONTROLLERS ---
  window.resetBusinessCycleGraph = function() {
    const slider = document.getElementById('bcTimeSlider');
    if (slider) {
      slider.value = 25;
      slider.dispatchEvent(new Event('input', { bubbles: true }));
      slider.dispatchEvent(new Event('change', { bubbles: true }));
    }
  };

  window.resetLoanableFundsGraph = function() {
    const sShiftSlider = document.getElementById('lfSaveShift');
    const iShiftSlider = document.getElementById('lfInvShift');
    if (sShiftSlider) {
      sShiftSlider.value = 0;
      sShiftSlider.dispatchEvent(new Event('input', { bubbles: true }));
      sShiftSlider.dispatchEvent(new Event('change', { bubbles: true }));
    }
    if (iShiftSlider) {
      iShiftSlider.value = 0;
      iShiftSlider.dispatchEvent(new Event('input', { bubbles: true }));
      iShiftSlider.dispatchEvent(new Event('change', { bubbles: true }));
    }
  };

  window.resetMultiplierCascade = function() {
    const mpcSlider = document.getElementById('multMpcSlider');
    const injSlider = document.getElementById('multInjSlider');
    if (mpcSlider) {
      mpcSlider.value = 0.75;
      mpcSlider.dispatchEvent(new Event('input', { bubbles: true }));
      mpcSlider.dispatchEvent(new Event('change', { bubbles: true }));
    }
    if (injSlider) {
      injSlider.value = 100;
      injSlider.dispatchEvent(new Event('input', { bubbles: true }));
      injSlider.dispatchEvent(new Event('change', { bubbles: true }));
    }
  };

  window.resetAdAsGraph = function() {
    const firstScenBtn = document.querySelector('.adas-scen-btn');
    const firstMechBtn = document.querySelector('.adas-mech-btn');
    if (window.setAdAsScenario && firstScenBtn) {
      window.setAdAsScenario('ad_pos', firstScenBtn);
    }
    if (window.setAdAsMechanism && firstMechBtn) {
      window.setAdAsMechanism('short_run', firstMechBtn);
    }
  };

  window.resetIsLmGraph = function() {
    const gSlider = document.getElementById('islmGSlider');
    const mSlider = document.getElementById('islmMSlider');
    const zlbBtn = document.getElementById('islmZlbBtn');
    const coordBtn = document.getElementById('islmCoordBtn');
    if (zlbBtn && zlbBtn.classList.contains('active')) {
      if (window.toggleLiquidityTrap) window.toggleLiquidityTrap(zlbBtn);
    }
    if (coordBtn && coordBtn.classList.contains('active')) {
      if (window.toggleCoordinatedMix) window.toggleCoordinatedMix(coordBtn);
    }
    if (gSlider) {
      gSlider.value = 0;
      gSlider.dispatchEvent(new Event('input', { bubbles: true }));
      gSlider.dispatchEvent(new Event('change', { bubbles: true }));
    }
    if (mSlider) {
      mSlider.value = 0;
      mSlider.dispatchEvent(new Event('input', { bubbles: true }));
      mSlider.dispatchEvent(new Event('change', { bubbles: true }));
    }
  };

  window.resetPhillipsGraph = function() {
    const uSlider = document.getElementById('pcUSlider');
    const expInfSlider = document.getElementById('pcExpInfSlider');
    if (uSlider) {
      uSlider.value = 4.0;
      uSlider.dispatchEvent(new Event('input', { bubbles: true }));
      uSlider.dispatchEvent(new Event('change', { bubbles: true }));
    }
    if (expInfSlider) {
      expInfSlider.value = 4.0;
      expInfSlider.dispatchEvent(new Event('input', { bubbles: true }));
      expInfSlider.dispatchEvent(new Event('change', { bubbles: true }));
    }
  };

  // =========================================================================
  // --- MI6 TACTICAL AUDIO CONTROLLER // "BRIEFING" SOUNDTRACK ---
  // =========================================================================
  function formatAudioTime(seconds) {
    if (isNaN(seconds) || seconds < 0) return '00:00';
    const m = Math.floor(seconds / 60);
    const s = Math.floor(seconds % 60);
    return (m < 10 ? '0' + m : m) + ':' + (s < 10 ? '0' + s : s);
  }

  window.toggleBriefingAudio = function() {
    const audio = document.getElementById('briefingAudioPlayer');
    const playBtn = document.getElementById('briefingPlayBtn');
    const playIcon = document.getElementById('briefingPlayIcon');
    const playLabel = document.getElementById('briefingPlayLabel');
    const spectrum = document.getElementById('briefingSpectrum');
    const satStatusPill = document.getElementById('satStatusPill');
    const satLockText = document.getElementById('satLockText');
    const satSignalBars = document.getElementById('satSignalBars');
    const btnTxState = document.getElementById('btnTxState');
    if (!audio) return;

    if (audio.paused || audio.ended) {
      const playPromise = audio.play();
      if (playPromise !== undefined) {
        playPromise.then(() => {
          if (playBtn) playBtn.classList.add('is-playing');
          if (playIcon) playIcon.textContent = '⏸';
          if (playLabel) playLabel.textContent = 'PAUSE BRIEFING';
          if (spectrum) spectrum.classList.add('active');
          if (btnTxState) btnTxState.textContent = 'TX ACTIVE // 320K LIVE';
          if (satStatusPill) {
            satStatusPill.textContent = 'TRANSMITTING';
            satStatusPill.classList.add('live');
          }
          if (satLockText) satLockText.textContent = 'STREAMING AUDIO // DECRYPTING REAL-TIME';
          if (satSignalBars) satSignalBars.classList.add('active');
        }).catch(err => {
          console.warn('Playback error or policy:', err);
        });
      }
    } else {
      audio.pause();
      if (playBtn) playBtn.classList.remove('is-playing');
      if (playIcon) playIcon.textContent = '▶';
      if (playLabel) playLabel.textContent = 'PLAY BRIEFING';
      if (spectrum) spectrum.classList.remove('active');
      if (btnTxState) btnTxState.textContent = 'STANDBY // KU-BAND 14.2G';
      if (satStatusPill) {
        satStatusPill.textContent = 'UPLINK ONLINE';
        satStatusPill.classList.remove('live');
      }
      if (satLockText) satLockText.textContent = 'CARRIER LOCKED [14.225 GHz KU-BAND]';
      if (satSignalBars) satSignalBars.classList.remove('active');
    }
  };

  window.seekBriefingAudio = function(e) {
    const audio = document.getElementById('briefingAudioPlayer');
    const track = document.getElementById('briefingScrubberTrack');
    if (!audio || !track) return;
    const rect = track.getBoundingClientRect();
    if (rect.width === 0) return;
    const clickX = e.clientX - rect.left;
    const ratio = Math.max(0, Math.min(1, clickX / rect.width));
    const duration = audio.duration || 29.75;
    audio.currentTime = ratio * duration;
  };

  window.toggleBriefingLoop = function() {
    const audio = document.getElementById('briefingAudioPlayer');
    const loopBtn = document.getElementById('briefingLoopBtn');
    if (!audio) return;
    audio.loop = !audio.loop;
    if (loopBtn) {
      if (audio.loop) {
        loopBtn.classList.add('active');
      } else {
        loopBtn.classList.remove('active');
      }
    }
  };

  window.toggleBriefingMute = function() {
    const audio = document.getElementById('briefingAudioPlayer');
    const muteIcon = document.getElementById('briefingMuteIcon');
    if (!audio) return;
    audio.muted = !audio.muted;
    if (muteIcon) {
      muteIcon.textContent = audio.muted ? '🔇' : '🔊';
    }
  };

  window.setBriefingVolume = function(val) {
    const audio = document.getElementById('briefingAudioPlayer');
    const muteIcon = document.getElementById('briefingMuteIcon');
    if (!audio) return;
    const vol = parseFloat(val);
    audio.volume = vol;
    audio.muted = (vol === 0);
    if (muteIcon) {
      muteIcon.textContent = (audio.muted || vol === 0) ? '🔇' : '🔊';
    }
  };

  function initBriefingPlayerEvents() {
    const audio = document.getElementById('briefingAudioPlayer');
    if (!audio) return;

    audio.addEventListener('timeupdate', () => {
      const fill = document.getElementById('briefingScrubberFill');
      const curTime = document.getElementById('briefingCurrentTime');
      const totTime = document.getElementById('briefingTotalTime');
      const duration = audio.duration || 29.75;
      const current = audio.currentTime || 0;
      const pct = (current / duration) * 100;

      if (fill) fill.style.width = Math.min(100, Math.max(0, pct)) + '%';
      if (curTime) curTime.textContent = formatAudioTime(current);
      if (totTime && audio.duration) totTime.textContent = formatAudioTime(duration);
    });

    audio.addEventListener('loadedmetadata', () => {
      const totTime = document.getElementById('briefingTotalTime');
      if (totTime && audio.duration) {
        totTime.textContent = formatAudioTime(audio.duration);
      }
    });

    audio.addEventListener('ended', () => {
      if (!audio.loop) {
        const playBtn = document.getElementById('briefingPlayBtn');
        const playIcon = document.getElementById('briefingPlayIcon');
        const playLabel = document.getElementById('briefingPlayLabel');
        const spectrum = document.getElementById('briefingSpectrum');
        const satStatusPill = document.getElementById('satStatusPill');
        const satLockText = document.getElementById('satLockText');
        const satSignalBars = document.getElementById('satSignalBars');
        const btnTxState = document.getElementById('btnTxState');
        if (playBtn) playBtn.classList.remove('is-playing');
        if (playIcon) playIcon.textContent = '▶';
        if (playLabel) playLabel.textContent = 'PLAY BRIEFING';
        if (spectrum) spectrum.classList.remove('active');
        if (btnTxState) btnTxState.textContent = 'STANDBY // KU-BAND 14.2G';
        if (satStatusPill) {
          satStatusPill.textContent = 'UPLINK ONLINE';
          satStatusPill.classList.remove('live');
        }
        if (satLockText) satLockText.textContent = 'CARRIER LOCKED [14.225 GHz KU-BAND]';
        if (satSignalBars) satSignalBars.classList.remove('active');
      }
    });
  }

  // =========================================================================
  // --- MI6 TOP SECRET ACCESS CLEARANCE GATE (LOCK FEATURE) ---
  // =========================================================================
  const MI6_CORRECT_CREDENTIAL = '007';
  const MI6_CORRECT_PASSWORD = 'Skyfall-Vesper#N19';

  window.handleGateAuthentication = function(e) {
    if (e) e.preventDefault();
    const credInput = document.getElementById('agentCredentialInput');
    const passInput = document.getElementById('agentPasswordInput');
    const feedback = document.getElementById('gateFeedback');
    const overlay = document.getElementById('mi6GateOverlay');
    const submitBtn = document.getElementById('gateSubmitBtn');

    if (!credInput || !passInput) return false;

    const enteredCred = credInput.value.trim();
    const enteredPass = passInput.value;

    if (enteredCred === MI6_CORRECT_CREDENTIAL && enteredPass === MI6_CORRECT_PASSWORD) {
      if (feedback) {
        feedback.className = 'gate-feedback success';
        feedback.innerHTML = '<span class="status-icon">✓</span> CLEARANCE VERIFIED // ACCESS GRANTED TO MISSION: MACRO';
      }
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span>🔓</span> CLEARANCE GRANTED — DECRYPTING...';
      }

      try {
        sessionStorage.setItem('mi6_007_clearance_granted', 'true');
      } catch (err) {}

      setTimeout(() => {
        if (overlay) {
          overlay.classList.add('unlocked');
          setTimeout(() => {
            overlay.style.display = 'none';
            document.body.classList.remove('gate-locked');
          }, 500);
        }
      }, 400);

      return true;
    } else {
      if (feedback) {
        feedback.className = 'gate-feedback error';
        if (enteredCred !== MI6_CORRECT_CREDENTIAL && enteredPass !== MI6_CORRECT_PASSWORD) {
          feedback.innerHTML = '<span class="status-icon">✗</span> ACCESS DENIED: Invalid Agent Credentials & Password';
        } else if (enteredCred !== MI6_CORRECT_CREDENTIAL) {
          feedback.innerHTML = '<span class="status-icon">✗</span> ACCESS DENIED: Unrecognized Agent Credential';
        } else {
          feedback.innerHTML = '<span class="status-icon">✗</span> ACCESS DENIED: Incorrect Security Password';
        }
      }

      const card = document.querySelector('.mi6-gate-card');
      if (card) {
        card.classList.remove('shake');
        void card.offsetWidth;
        card.classList.add('shake');
      }

      passInput.value = '';
      passInput.focus();
      return false;
    }
  };

  window.toggleGatePasswordVisibility = function() {
    const passInput = document.getElementById('agentPasswordInput');
    const eyeOpen = document.getElementById('eyeIconOpen');
    const eyeClosed = document.getElementById('eyeIconClosed');
    if (!passInput) return;
    if (passInput.type === 'password') {
      passInput.type = 'text';
      if (eyeOpen) eyeOpen.style.display = 'none';
      if (eyeClosed) eyeClosed.style.display = 'block';
    } else {
      passInput.type = 'password';
      if (eyeOpen) eyeOpen.style.display = 'block';
      if (eyeClosed) eyeClosed.style.display = 'none';
    }
  };

  window.lockTerminal = function() {
    try {
      sessionStorage.removeItem('mi6_007_clearance_granted');
    } catch(e) {}
    const overlay = document.getElementById('mi6GateOverlay');
    const credInput = document.getElementById('agentCredentialInput');
    const passInput = document.getElementById('agentPasswordInput');
    const feedback = document.getElementById('gateFeedback');
    const submitBtn = document.getElementById('gateSubmitBtn');
    const eyeOpen = document.getElementById('eyeIconOpen');
    const eyeClosed = document.getElementById('eyeIconClosed');

    if (credInput) credInput.value = '';
    if (passInput) {
      passInput.value = '';
      passInput.type = 'password';
    }
    if (eyeOpen) eyeOpen.style.display = 'block';
    if (eyeClosed) eyeClosed.style.display = 'none';
    if (feedback) {
      feedback.className = 'gate-feedback';
      feedback.textContent = '';
    }
    if (submitBtn) {
      submitBtn.disabled = false;
      submitBtn.innerHTML = '<span class="btn-lock-icon">🔒</span> GRANT ACCESS TO "MISSION: MACRO"';
    }
    if (overlay) {
      overlay.style.display = 'flex';
      overlay.classList.remove('unlocked');
      document.body.classList.add('gate-locked');
      if (credInput) setTimeout(() => credInput.focus(), 50);
    }
  };

  window.initGateClearance = function() {
    const overlay = document.getElementById('mi6GateOverlay');
    if (!overlay) return;

    let isGranted = false;
    try {
      isGranted = (sessionStorage.getItem('mi6_007_clearance_granted') === 'true');
    } catch(e) {}

    if (isGranted) {
      overlay.style.display = 'none';
      document.body.classList.remove('gate-locked');
    } else {
      overlay.style.display = 'flex';
      document.body.classList.add('gate-locked');
      const credInput = document.getElementById('agentCredentialInput');
      if (credInput) {
        setTimeout(() => credInput.focus(), 100);
      }
    }
  };

  // --- INITIALIZATION ON DOM READY ---
  document.addEventListener('DOMContentLoaded', () => {
    initGateClearance();
    loadState();
    renderOmegaDials();
    initBriefingPlayerEvents();
    if (typeof window.updateMissionCountdown === 'function') {
      window.updateMissionCountdown();
    }

    // Restore sidebar collapsed state on desktop
    try {
      if (localStorage.getItem('sidebar_collapsed_007') === '1' && window.innerWidth > 900) {
        const sidebar = document.getElementById('sidebarNav');
        const collapseIcon = document.getElementById('sidebarCollapseIcon');
        const collapseBtn = document.getElementById('sidebarCollapseBtn');
        if (sidebar) sidebar.classList.add('collapsed');
        if (collapseIcon) collapseIcon.textContent = '▶';
        if (collapseBtn) collapseBtn.setAttribute('title', 'Expand Intelligence Dossiers');
      }
    } catch(e) {}

    // Init All 6 Interactive Graph Labs
    window.initBusinessCycleGraph();
    window.initLoanableFundsGraph();
    window.initMultiplierCascade();
    window.initAdAsGraph();
    window.initIsLmGraph();
    window.initPhillipsGraph();
  });

})();
"""
