# How to Start a New Claude Code Session

**Purpose:** Exact steps to get a new AI instance up to speed on TOSCA project

---

## Step 1: Copy-Paste This Prompt

```
I'm working on the TOSCA Medical Laser Control System - an FDA-Enhanced Documentation Level medical device project.

Please read these files in order:
1. docs/project/START_HERE.md
2. docs/project/PROJECT_STATUS.md
3. docs/project/CODING_STANDARDS.md
4. docs/project/WORK_LOG.md

After reading, tell me:
- What we were last working on
- Current project status
- What you recommend as next steps

Critical rules:
- Minimal code only (no extras, no decorative elements, no emojis)
- Always add new packages to requirements.txt
- Test outputs go to designated directories only
- Update docs/project/WORK_LOG.md after each significant action
- All code must pass pre-commit hooks (Black, Flake8, MyPy, isort)

Repository: https://github.com/will-aleyegn/Aleyegn_TOSCA_Control_Development
Working Directory: C:\Users\wille\Desktop\TOSCA-dev
```

---

## Step 2: Wait for AI to Read and Summarize

The AI will:
- Read all 4 files
- Summarize current project state
- Tell you what was last being worked on
- Suggest next steps

---

## Step 3: Give Your Direction

Examples:
- "Continue with that work"
- "Actually, I want to work on [specific task]"
- "Let's start the actuator module"
- "Debug the camera feature exploration issue"

---

## That's It!

The AI now has:
- Complete project context
- Development standards
- Recent work history
- All documentation locations

---

## Alternative: If AI Doesn't Auto-Read

If the AI doesn't automatically read the files, you can be more explicit:

```
Please use the Read tool to read these files:
- docs/project/START_HERE.md
- docs/project/PROJECT_STATUS.md
- docs/project/CODING_STANDARDS.md
- docs/project/WORK_LOG.md

Then summarize what we were working on and ask what I want to do next.
```

---

## Key Files Reference

If you need to reference specific docs during session:

- **START_HERE.md** - Quick 5-step setup
- **PROJECT_STATUS.md** - Complete project state (472 lines)
- **CODING_STANDARDS.md** - Development rules (minimal code philosophy)
- **WORK_LOG.md** - Real-time action tracking
- **CONFIGURATION.md** - All 11 config files explained
- **SESSION_PROMPT.md** - Template prompt (what Step 1 is based on)

Architecture Documentation:
- `docs/architecture/01_system_overview.md` - Complete system architecture
- `docs/architecture/02_database_schema.md` - Database design
- `docs/architecture/03_safety_system.md` - Safety system (critical)
- `docs/architecture/04_treatment_protocols.md` - Protocol engine
- `docs/architecture/05_image_processing.md` - Camera and vision

---

## Tips for Smooth Sessions

1. **Always update WORK_LOG.md** - Tell the AI to update after each significant action
2. **Reference PROJECT_STATUS.md** - Have AI update it when major milestones complete
3. **Point to CODING_STANDARDS.md** - If AI generates extra code, remind it of minimal code rule
4. **Check git status frequently** - Keep commits organized and meaningful

---

**Last Updated:** 2025-10-22
**Location:** docs/project/NEW_SESSION_GUIDE.md
