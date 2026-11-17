# Test script to generate and verify briefing audio player markup

markup = """
              <!-- MI6 TACTICAL AUDIO BRIEFING CONSOLE (RIGHT BELOW TITANIUM OMEGA SEAMASTER) -->
              <div class="omega-briefing-console-row" id="omegaBriefingRow">
                <div class="briefing-player-card">
                  <!-- Tactical HUD Header -->
                  <div class="briefing-hud-header">
                    <div class="briefing-header-left">
                      <span class="briefing-surveillance-dot"></span>
                      <div class="briefing-title-group">
                        <span class="briefing-hud-badge">MI6 TACTICAL AUDIO CIPHER // OPERATION BRIEFING</span>
                        <span class="briefing-hud-sub">OFFICIAL SOUNDTRACK • "BRIEFING" // 007 INTELLIGENCE FEED</span>
                      </div>
                    </div>
                    <div class="briefing-header-right">
                      <button class="briefing-toggle-btn" id="briefingSizeToggleBtn" onclick="toggleBriefingPlayerSize()" type="button" title="Switch Compact Bar (152px) / Full Card (352px)">
                        <span id="briefingToggleLabel">↕ COMPACT VIEW (152px)</span>
                      </button>
                    </div>
                  </div>

                  <!-- Tactical Equalizer & Frequency Telemetry Strip -->
                  <div class="briefing-telemetry-strip">
                    <div class="briefing-eq-spectrum" id="briefingSpectrum" title="Tactical Audio Frequency Visualizer">
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
                    <div class="briefing-meta-text">
                      <span class="briefing-tag-amber">DIRECT SATELLITE LINK</span>
                      <span class="briefing-track-name">TRACK: "BRIEFING" // HANS ZIMMER</span>
                    </div>
                  </div>

                  <!-- Spotify Official Embed Player -->
                  <div class="briefing-spotify-frame-wrap" id="briefingSpotifyWrap">
                    <iframe id="spotifyBriefingIframe" data-testid="embed-iframe" style="border-radius:12px; width:100%; border:0; display:block;" src="https://open.spotify.com/embed/track/4MR9iW77LJoPPDjwAYbIZZ?utm_source=generator&theme=0&si=dec3429b97424eb6" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
                  </div>

                  <!-- Quick Tactical Footer with Action Controls -->
                  <div class="briefing-hud-footer">
                    <span class="briefing-directive-note">
                      <strong style="color:var(--accent-silver);">OPERATIVE DIRECTIVE:</strong> Stream tactical audio while reviewing examination dossiers. Click play inside the console.
                    </span>
                    <button class="briefing-synth-cue-btn" id="briefingSynthCueBtn" onclick="playTacticalCue()" type="button" title="Play MI6 Cinematic Tone Cue">
                      <span class="synth-btn-icon">▶</span> TACTICAL CHIME
                    </button>
                  </div>
                </div>
              </div>
"""

print("Markup length:", len(markup))
print("Div balance:", markup.count('<div') - markup.count('</div>'))
