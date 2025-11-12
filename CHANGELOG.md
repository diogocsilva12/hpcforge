# 🧾 CHANGELOG

> All notable changes to **HPCTools** will be documented in this file.  
> This project adheres to **Semantic Versioning** (https://semver.org).

---

## [0.1.0] – 2025-11-11  
### 🚀 Initial Public Release

**Highlights**
- 🎯 First stable release of the `hpctools` CLI
- Unified **interactive menu** system for HPC workflow automation
- Compatible with **Linux**, **macOS**, and **Windows**

**Added**
- `hpctools make` → Generate Makefiles (manual or from templates)
- `hpctools slurm` → Generate SLURM job scripts
- `hpctools all` → Combined Makefile + SLURM generation
- `hpctools templates` → Interactive template viewer with syntax-highlighted preview
- Default templates:
  - `make_default.mk`
  - `slurm_default.sh`
- Template quick-apply generator (`⚡ Apply → Generate in current folder`)
- ETA estimation with Rich progress spinner (`⏱ Estimated runtime`)
- SLURM time-limit verification (`⚠️ exceeds SLURM time limit`)
- `clear_console()` for clean UI across OSes
- Auto-detection of compiler modules via `module avail`
- Autocomplete path input (`questionary.path`)
- Colorized console outputs with **Rich**
- Deucalion mode preset (automatic account + partition defaults)
- Modular utilities (`utils.py`) for I/O, templates, timestamps, and commands

**Changed**
- CLI prompts redesigned with rich colors and structured defaults  
- Simplified blank-account handling for non-Deucalion clusters  
- Improved cross-platform support for file saving and output directories  
- Consistent icons and visual cues across all commands  

**Fixed**
- Bug where blank SLURM account defaulted incorrectly in non-Deucalion mode  
- Template preview not respecting `.sh` syntax highlighting  
- Minor layout issues in Windows CMD  

**Developer Experience**
- Added modular command clearing (`clear_console()`)
- Added `detect_modules()` helper in `utils.py`
- Improved code readability and reusability between commands

---

## [0.1.1] – (Planned)
### 🔮 Upcoming Enhancements

**To Be Added**
- 🧬 `hpctools doctor` → environment diagnostics (detect GCC, Score-P, Perf)
- 💾 Persistent user configuration (`~/.config/hpctools/config.json`)
- 🧩 Smart flag suggestions (Performance / Debug / Safe modes)
- ⚙️ Cluster presets (`--preset deucalion`, `--preset search`, `--preset local`)
- 📦 `hpctools init <project>` → project scaffolding command
- 📊 Benchmark report exporter (`results/report.html`)
- 🧱 Auto shell-completion installer for Bash/Zsh/Fish
- 🧠 Smart ETA calibration from historical runs
- Smarter Helper for Makefile flags

---

## [0.2.0] – (Future milestone)
### 🌐 Distribution & Cloud Sync

- Publish on **PyPI** (`pip install hpctools`)
- Add **Homebrew tap** support (`brew install hpctools`)
- Cloud sync for templates/configs (`hpctools sync`)
- Integrated HTML/Markdown reporting engine
- Preset templates for common HPC clusters (Deucalion, SeARCH, MareNostrum)
- Cross-platform packaging improvements

---

## 🧠 Notes

- Each minor version focuses on **UX refinement + automation depth**.
- Every new cluster preset or template should be version-tagged separately.

---

**Maintained by:** Diogo Silva
**License:** MIT  
**Repository:** [github.com/diogocsilva12/hpctools](https://github.com/diogocsilva12/hpctools)

