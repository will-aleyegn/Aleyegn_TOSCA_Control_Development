# TOSCA Project Status & AI Onboarding

**Last Updated:** 2025-10-22
**Current Phase:** Camera Module Exploration
**Project Status:** Planning → Initial Setup → Camera Testing

---

## Quick Start for New AI Session

1. **Read this file first** - Current project state
2. **Review** `CODING_STANDARDS.md` - Development rules
3. **Check** `docs/DEVELOPMENT_ENVIRONMENT_SETUP.md` - Setup reference
4. **Verify** Git status and latest commits
5. **Continue** from "Next Immediate Tasks" section below

---

## Project Overview

**Name:** TOSCA Medical Laser Control System
**Type:** FDA-Enhanced Documentation Level Medical Device Software
**Compliance:** IEC 62304, Enhanced Documentation Level
**Repository:** https://github.com/will-aleyegn/Aleyegn_TOSCA_Control_Development

**Purpose:** Clinical laser control system with:
- Laser power control (Arroyo TEC Controller)
- Linear actuator (Xeryon) for ring sizing
- Camera system (Allied Vision) for alignment
- GPIO safety interlocks (FT232H)
- Patient management database
- Treatment protocol engine
- Session video recording

---

## Critical Development Rules

**MUST READ:** `CODING_STANDARDS.md`

**Key Principles:**
1. **Minimal code only** - Write only what is explicitly requested
2. **No decorative elements** - No emojis, no extra comments, no flourishes
3. **No placeholder functions** - Only implement what's needed now
4. **Type hints required** - All functions must have type annotations
5. **Safety-critical documentation** - Hardware operations need detailed docstrings
6. **Pre-commit hooks active** - Code must pass Black, Flake8, MyPy, isort

**When installing packages:**
- Always add to `requirements.txt`
- Document in appropriate category

**When creating output files:**
- Use designated output directories
- Never litter repository root
- Add to `.gitignore` if test data

---

## Current Directory Structure

```
TOSCA-dev/
├── .github/                           # GitHub config
│   └── PULL_REQUEST_TEMPLATE.md
├── camera_module/                     # Camera exploration (CURRENT WORK)
│   ├── README.md
│   ├── examples/
│   │   ├── 01_list_cameras.py        # ✓ Working
│   │   ├── 02_camera_info.py         # ✓ Working
│   │   ├── 03_capture_single_frame.py # ✓ Working
│   │   ├── 04_explore_features.py    # ⚠ Needs debugging
│   │   └── 05_continuous_stream.py   # Not tested yet
│   ├── output/                        # Test images (git-ignored)
│   └── docs/
├── docs/
│   ├── architecture/                  # Complete architecture docs
│   └── DEVELOPMENT_ENVIRONMENT_SETUP.md
├── src/                               # Main application (empty structure)
│   ├── main.py
│   ├── config/
│   ├── core/
│   ├── database/
│   ├── hardware/
│   ├── image_processing/
│   ├── ui/
│   └── utils/
├── tests/                             # Test structure created
├── data/                              # Git-ignored
├── venv/                              # Virtual environment
├── CODING_STANDARDS.md                # ⚠ CRITICAL - READ FIRST
├── PROJECT_STATUS.md                  # ⚠ THIS FILE - Keep updated
├── README.md
├── requirements.txt
└── setup.py
```

---

## Completed Work

### ✓ Phase 0: Initial Setup (Complete)

**Repository & Git:**
- [x] GitHub repository created and connected
- [x] `.gitignore` configured for medical device security
- [x] Pre-commit hooks installed (Black, Flake8, MyPy, isort)
- [x] Pull request template with coding standards checklist

**Python Environment:**
- [x] Virtual environment created (Python 3.12.10)
- [x] All dependencies installed (100+ packages)
- [x] Project structure created (`src/`, `tests/`, `data/`)
- [x] Package configuration (`setup.py`, `pyproject.toml`, `pytest.ini`)

**Configuration Files:**
- [x] `.flake8` - Linting rules
- [x] `.pylintrc` - Code analysis rules
- [x] `.pre-commit-config.yaml` - Automated checks
- [x] `.env.example` - Environment variable template

**Documentation:**
- [x] `CODING_STANDARDS.md` - Development rules
- [x] `DEVELOPMENT_ENVIRONMENT_SETUP.md` - Complete setup guide
- [x] Architecture docs in `docs/architecture/`

### ✓ Camera Module (Current)

**Allied Vision Camera Integration:**
- [x] VmbPy library installed (v1.1.1)
- [x] Camera module directory structure created
- [x] Camera detected: Allied Vision 1800 U-158c (USB)
- [x] Specifications documented: 1456x1088, RGB8, USB interface

**Test Scripts Created:**
- [x] `01_list_cameras.py` - Camera detection ✓ Tested
- [x] `02_camera_info.py` - Camera details ✓ Tested
- [x] `03_capture_single_frame.py` - Frame capture ✓ Tested
- [x] `04_explore_features.py` - Feature exploration ⚠ Needs fix
- [x] `05_continuous_stream.py` - Streaming test (not tested)

**Camera Test Results:**
```
Camera ID: DEV_1AB22C04E780
Model: Allied Vision 1800 U-158c
Resolution: 1456 x 1088 pixels
Format: RGB8 (3 channels)
Exposure: ~5ms
Interface: USB
Status: Working ✓
```

---

## Known Issues

1. **Camera Feature Exploration:**
   - Script `04_explore_features.py` finds 313 features but reads 0
   - Features exist but not being accessed correctly
   - Need to debug feature reading logic

2. **Streaming Test:**
   - Script `05_continuous_stream.py` created but not tested
   - Need to verify frame rate and callback functionality

---

## Current Work Session Summary

**What we just did:**
1. Created camera exploration module structure
2. Installed VmbPy library
3. Wrote 5 test scripts for camera operations
4. Successfully tested camera detection, info, and frame capture
5. Documented VmbPy API in `camera_module/README.md`
6. Added output directory for test images
7. Updated `.gitignore` to prevent repository littering

**What's working:**
- Camera detection and connection
- Single frame capture (1456x1088x3 arrays)
- Image saving to `camera_module/output/`

**What needs attention:**
- Feature exploration script debugging
- Streaming test execution
- Feature documentation for TOSCA integration

---

## Next Immediate Tasks

**Priority 1: Complete Camera Module Testing**
1. Debug `04_explore_features.py` to properly read camera features
2. Test `05_continuous_stream.py` for frame rate verification
3. Document key camera features needed for TOSCA (exposure, gain, trigger)
4. Create feature documentation file

**Priority 2: Camera Hardware Abstraction**
1. Create `src/hardware/camera.py` abstraction layer
2. Implement connection, capture, streaming methods
3. Add exposure and gain control
4. Write unit tests

**Priority 3: Actuator Module (Next)**
1. Create `actuator_module/` similar to camera module
2. Research Xeryon API
3. Create test scripts for actuator control
4. Document API and test results

---

## Hardware Status

### Connected & Working:
- **Camera:** Allied Vision 1800 U-158c (USB)
  - Detection: ✓
  - Frame capture: ✓
  - Streaming: Not tested yet

### Not Yet Connected:
- **Laser Controller:** Arroyo TEC Controller (Serial)
- **Actuator:** Xeryon linear stage
- **GPIO:** 2x FT232H breakouts
- **Footpedal:** Not connected
- **Photodiode:** Not connected
- **Smoothing Device:** Not connected

---

## Key Decisions Made

1. **Modular Exploration Approach:**
   - Decided to create separate exploration modules (camera_module, actuator_module)
   - Fully understand APIs before integration
   - Test scripts demonstrate capabilities
   - Prevents polluting main application

2. **Coding Standards Enforcement:**
   - Strict "minimal code only" policy
   - No decorative elements or extra functions
   - Pre-commit hooks enforce quality automatically
   - Type hints required on all functions

3. **Output Organization:**
   - Test outputs go to module-specific output directories
   - Git-ignored to keep repository clean
   - No files in repository root

4. **Documentation First:**
   - README in each module explains API completely
   - Test scripts serve as usage examples
   - Integration plans documented before implementation

---

## Development Workflow

**Starting a Session:**
```bash
cd C:\Users\wille\Desktop\TOSCA-dev
venv\Scripts\activate
git pull origin main
```

**Before Writing Code:**
```bash
# Review coding standards
cat CODING_STANDARDS.md
```

**Testing:**
```bash
# Run specific test script
python camera_module/examples/01_list_cameras.py

# Run all tests
pytest
```

**Before Committing:**
```bash
# Pre-commit hooks run automatically on commit
git add .
git commit -m "message"  # Hooks will validate code
git push origin main
```

---

## Important File Locations

**Critical Documents:**
- `PROJECT_STATUS.md` - This file (session state)
- `CODING_STANDARDS.md` - Development rules
- `docs/DEVELOPMENT_ENVIRONMENT_SETUP.md` - Setup guide

**Architecture:**
- `docs/architecture/01_system_overview.md` - System design
- `docs/architecture/02_database_schema.md` - Database design
- `docs/architecture/03_safety_system.md` - Safety requirements
- `docs/architecture/04_treatment_protocols.md` - Protocol specs
- `docs/architecture/05_image_processing.md` - Image processing specs

**Camera Module:**
- `camera_module/README.md` - VmbPy API documentation
- `camera_module/examples/` - Test scripts
- `camera_module/output/` - Test images

**Configuration:**
- `.env.example` - Environment variables template
- `requirements.txt` - Python dependencies
- `.pre-commit-config.yaml` - Code quality hooks

---

## Questions to Ask at Session Start

1. **What are we working on?**
   - Continue camera module?
   - Start actuator module?
   - Begin hardware abstraction layer?

2. **Any issues with current code?**
   - Review git status
   - Check for uncommitted changes
   - Review latest commits

3. **New hardware connected?**
   - Update "Hardware Status" section
   - Add to this document

4. **Any decisions made?**
   - Document in "Key Decisions Made"
   - Update relevant sections

---

## Git Commit History Summary

**Latest commits:**
```
5b61058 - Add output directory for test images and update gitignore
a33e263 - Fix type hint in feature exploration script
25b883c - Add Allied Vision camera exploration module with VmbPy API
3737a93 - Configure strict coding standards and quality enforcement
acb6bd7 - Initialize Python project structure and development environment
6550878 - Initial commit: TOSCA Medical Laser Control System documentation
```

---

## Environment Details

**Python:** 3.12.10
**Virtual Environment:** `venv/` (activated with `venv\Scripts\activate`)
**OS:** Windows 10

**Key Packages:**
- PyQt6 6.10.0 (GUI)
- OpenCV 4.12.0 (Image processing)
- NumPy 2.2.6 (Arrays)
- VmbPy 1.1.1 (Camera)
- SQLAlchemy 2.0.44 (Database)
- pytest 8.4.2 (Testing)

**Development Tools:**
- Black (formatting)
- Flake8 (linting)
- MyPy (type checking)
- Pylint (analysis)
- Pre-commit (hooks)

---

## MCP Configuration

**GitHub Token:** Configured in `.mcp.json` (git-ignored)
**MCP Servers Active:**
- github: GitHub API integration
- memory: Knowledge graph
- context7: Documentation lookup

---

## Session Handoff Template

**When ending a session, update this section:**

**Date:** YYYY-MM-DD
**What was completed:**
- Item 1
- Item 2

**What needs attention:**
- Issue 1
- Issue 2

**Next session should:**
- Task 1
- Task 2

**Notes:**
- Any important context

---

## Notes for AI Assistant

**User Preferences:**
1. **Minimal code** - Only what's requested, no extras
2. **No decorative elements** - No emojis, clean code only
3. **Ask before adding** - Don't assume features needed
4. **Document as you go** - Keep this file updated
5. **Test outputs in designated directories** - No littering

**When user requests new work:**
1. Review this file first
2. Check CODING_STANDARDS.md
3. Verify current git status
4. Continue from documented state

**Update this file when:**
- Completing major tasks
- Making architectural decisions
- Changing directory structure
- Adding new modules
- Discovering issues
- Connecting new hardware

---

**End of Project Status Document**
**Remember: Update this file as work progresses!**
