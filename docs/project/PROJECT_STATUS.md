# TOSCA Project Status & AI Onboarding

**Last Updated:** 2025-10-22 22:35
**Current Phase:** GUI Development - Phase 1 Complete
**Project Status:** Initial Setup ✓ → Camera Module ✓ → GUI Shell ✓ → HAL Integration (Next)

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
├── camera_module/                     # Camera exploration ✓ COMPLETE
│   ├── README.md                      # VmbPy API docs (500+ lines)
│   ├── INTEGRATION_FEATURES.md        # Integration spec (736 lines)
│   ├── LESSONS_LEARNED.md             # API quirks documented
│   ├── examples/
│   │   ├── 01_list_cameras.py        # ✓ Working
│   │   ├── 02_camera_info.py         # ✓ Working
│   │   ├── 03_capture_single_frame.py # ✓ Working
│   │   ├── 04_explore_features.py    # ✓ Fixed (223/313 features)
│   │   ├── 05_continuous_stream.py   # ✓ Working (39.4 FPS)
│   │   └── 06_set_auto_exposure.py   # ✓ Working
│   └── output/                        # Test images (git-ignored)
├── docs/
│   ├── architecture/                  # Complete architecture docs
│   ├── project/                       # Project management docs
│   │   ├── WORK_LOG.md               # Current session log
│   │   ├── PROJECT_STATUS.md         # This file
│   │   ├── CODING_STANDARDS.md       # Development rules
│   │   ├── CONFIGURATION.md          # Config reference
│   │   └── archive/                  # Archived work logs
│   └── DEVELOPMENT_ENVIRONMENT_SETUP.md
├── src/                               # Main application (CURRENT WORK)
│   ├── main.py                        # ✓ PyQt6 launcher
│   ├── ui/                            # ✓ GUI shell complete
│   │   ├── main_window.py            # 4-tab layout
│   │   └── widgets/
│   │       ├── patient_widget.py     # Patient selection
│   │       ├── camera_widget.py      # Camera display
│   │       ├── treatment_widget.py   # Treatment controls
│   │       └── safety_widget.py      # Safety interlocks
│   ├── config/
│   ├── core/
│   ├── database/
│   ├── hardware/                      # Next: HAL implementation
│   ├── image_processing/
│   └── utils/
├── tests/                             # Test structure created
├── data/                              # Git-ignored
│   └── logs/                          # Application logs
├── venv/                              # Virtual environment
├── NEW_SESSION_GUIDE.md               # ⚠ START HERE for new sessions
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

### ✓ Camera Module (Complete)

**Allied Vision Camera Integration:**
- [x] VmbPy library installed (v1.1.1)
- [x] Camera module directory structure created
- [x] Camera detected: Allied Vision 1800 U-158c (USB)
- [x] Specifications documented: 1456x1088, RGB8, USB interface
- [x] All 6 test scripts passing
- [x] API quirks documented in LESSONS_LEARNED.md
- [x] Integration specification complete (736 lines)

**Test Scripts - All Working:**
- [x] `01_list_cameras.py` - Camera detection ✓
- [x] `02_camera_info.py` - Camera details ✓
- [x] `03_capture_single_frame.py` - Frame capture with timestamps ✓
- [x] `04_explore_features.py` - Feature exploration (223/313 features) ✓
- [x] `05_continuous_stream.py` - Streaming (39.4 FPS) ✓
- [x] `06_set_auto_exposure.py` - Auto exposure control ✓

**Camera Test Results:**
```
Camera ID: DEV_1AB22C04E780
Model: Allied Vision 1800 U-158c
Resolution: 1456 x 1088 pixels
Format: RGB8 (3 channels)
Exposure: 5ms (manual) or auto-adjust
Frame Rate: 39.4 FPS sustained
Features: 223 of 313 readable
Interface: USB
Status: Fully validated ✓
```

### ✓ GUI Shell - Phase 1 (Complete)

**PyQt6 Main Window:**
- [x] 4-tab layout created (Patient, Camera, Treatment, Safety)
- [x] Status bar with hardware connection indicators
- [x] Main window with proper title and sizing (1400x900)
- [x] Logging integration for all UI actions

**Widget Components:**
- [x] PatientWidget - Patient ID search, session initiation
- [x] CameraWidget - Camera feed placeholder (800x600), controls
- [x] TreatmentWidget - Laser power (0-2000mW), ring size (0-3000µm)
- [x] SafetyWidget - Hardware/software interlocks, E-stop button

**Technical Quality:**
- [x] All methods type annotated (mypy compliant)
- [x] Pre-commit hooks passing (black, flake8, isort, mypy)
- [x] Follows CODING_STANDARDS.md minimal approach
- [x] GUI launches and renders correctly

**Status:** Ready for HAL integration ✓

---

## Known Issues

**None** - All current modules tested and working

**Previously Resolved:**
1. ✓ Camera feature exploration (VmbPy British spelling issue)
2. ✓ Streaming callback signature (3 params required)
3. ✓ Path-independent file operations (using Path(__file__))

---

## Current Work Session Summary

**Session Date:** 2025-10-22
**Total Actions:** 26 major steps completed
**Duration:** ~4 hours

**Completed This Session:**
1. ✓ Camera module exploration (Actions 1-25)
   - 6 test scripts created and validated
   - API quirks documented
   - Integration specification written (736 lines)
   - All tests passing (39.4 FPS streaming)
2. ✓ GUI shell Phase 1 (Action 26)
   - 4-tab PyQt6 interface
   - Patient, Camera, Treatment, Safety widgets
   - Status bar with hardware indicators
   - All type annotations and pre-commit hooks passing

**What's working:**
- Camera: Fully validated with Allied Vision 1800 U-158c
- GUI: Launches and renders all 4 tabs correctly
- Code quality: All pre-commit hooks passing
- Documentation: Work log system with archival

**Current State:**
- Camera module: ✓ Complete
- GUI shell: ✓ Phase 1 complete
- HAL layer: ⏳ Ready to start
- Integration: ⏳ Next step

---

## Next Immediate Tasks

**Priority 1: Hardware Abstraction Layer (Phase 2)**
1. Create `src/hardware/` directory structure
2. Implement `src/hardware/camera_controller.py` (based on camera_module/INTEGRATION_FEATURES.md)
3. Implement `src/hardware/laser_controller.py` stub
4. Implement `src/hardware/actuator_controller.py` stub
5. Wire up CameraWidget "Connect Camera" button
6. Update status bar based on hardware connection state

**Priority 2: Safety System (Phase 3)**
1. Create `src/core/safety.py` - Safety interlock manager
2. Implement interlock state tracking
3. Enable/disable treatment buttons based on safety state
4. Wire up Emergency Stop button
5. Implement safety event logging to SafetyWidget

**Priority 3: Patient Management (Phase 4)**
1. Design database schema for patient records
2. Create `src/database/models.py` with Patient, Session, Treatment tables
3. Implement patient search functionality
4. Wire up PatientWidget search button
5. Implement session start/stop logic

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
22e192c - Archive camera module work log and clean up WORK_LOG.md
73722a2 - Update work log with GUI shell completion (Action #26)
f0faf57 - Create basic GUI shell with PyQt6
0c29b2e - Create integration feature specification (camera module complete)
1c24228 - Implement auto exposure control
1f529e7 - Add timestamps to captured frames
fb3b569 - Fix capture script path issues (use Path(__file__))
0f91ef5 - Establish lessons learned system (camera module)
```

**Full archive:** See WORK_LOG.md and archive/ for complete history

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
