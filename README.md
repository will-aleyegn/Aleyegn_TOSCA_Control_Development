# Medical Laser Control System

**Project Status:** Planning Phase
**Date:** 2025-10-15
**Application Type:** Clinical Medical Device

## Overview

This is a comprehensive medical laser control system designed for clinical use. The system integrates:

- **Laser Control** - Arroyo Instruments TEC Controller (serial communication)
- **Linear Actuator** - Xeryon actuator for ring size control
- **Camera System** - Allied Vision camera with VmbPy SDK for alignment and monitoring
- **GPIO Safety Interlocks** - Adafruit FT232H breakouts for footpedal, smoothing device, and photodiode monitoring
- **Patient Management** - SQLite database for longitudinal patient tracking
- **Treatment Protocols** - Configurable treatment plans with power ramping and ring sizing
- **Video Recording** - Complete session recording and event logging

## Key Features

### Safety-First Design
- **Footpedal Deadman Switch** - Active requirement for laser operation
- **Hotspot Smoothing Device Interlock** - Signal health monitoring
- **Photodiode Feedback** - Real-time power verification
- **Multiple Software Interlocks** - E-stop, power limits, session validation
- **Comprehensive Event Logging** - Complete audit trail

### Treatment Capabilities
- Pre-defined protocol templates
- Custom protocol builder with multi-step sequences
- Power ramping (constant, linear, logarithmic, exponential)
- Adjustable ring size via actuator control
- Real-time protocol adjustments
- In-treatment monitoring and recording

### Image Processing
- Laser ring detection (circle finding algorithm)
- Focus quality measurement
- Live video feed with overlays
- Session video recording
- Snapshot capture

### Patient Management
- Anonymized patient profiles
- Multi-session longitudinal tracking
- Technician/operator authentication
- Complete treatment history

## Architecture Documentation

Comprehensive technical documentation is available in `docs/architecture/`:

### 1. [System Overview](docs/architecture/01_system_overview.md)
- Complete system architecture
- Technology stack
- Hardware components
- Software layers
- Development phases

### 2. [Database Schema](docs/architecture/02_database_schema.md)
- Complete SQLite schema
- Entity relationships
- Table definitions
- Common queries
- Migration strategy

### 3. [Safety System](docs/architecture/03_safety_system.md)
- Safety philosophy and principles
- Hardware interlocks (footpedal, smoothing device, photodiode)
- Software interlocks (e-stop, power limits)
- Safety state machine
- Fault handling procedures
- Testing requirements

### 4. [Treatment Protocols](docs/architecture/04_treatment_protocols.md)
- Protocol data model and JSON schema
- Example protocols (constant power, ramping, multi-step)
- Protocol execution engine
- Ring size control and calibration
- Protocol builder UI

### 5. [Image Processing](docs/architecture/05_image_processing.md)
- Camera system integration
- Ring detection algorithm (Hough Circle Transform)
- Focus measurement (Laplacian variance)
- Video recording
- Calibration procedures

## Project Directory Structure

```
laser-control-system/
├── src/                        # Source code
│   ├── main.py                 # Application entry point
│   ├── config/                 # Configuration files
│   ├── ui/                     # PyQt6 user interface
│   ├── core/                   # Business logic
│   ├── hardware/               # Hardware abstraction layer
│   ├── image_processing/       # Computer vision
│   ├── database/               # Database operations
│   └── utils/                  # Utilities
├── data/                       # Application data
│   ├── laser_control.db        # SQLite database
│   ├── sessions/               # Per-session recordings
│   └── logs/                   # Application logs
├── docs/                       # Documentation
│   ├── architecture/           # Technical architecture docs
│   ├── user_manual.md          # User guide (TBD)
│   └── installation.md         # Installation guide (TBD)
├── tests/                      # Test suite
│   ├── test_hardware/
│   ├── test_core/
│   ├── test_safety/
│   └── test_integration/
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Technology Stack

### Core
- **Python 3.10+**
- **PyQt6** - GUI framework
- **SQLite** - Database
- **OpenCV (cv2)** - Image processing
- **NumPy** - Numerical operations

### Hardware Libraries
- **pyserial** - Arroyo laser communication
- **Xeryon API** - Linear actuator control
- **VmbPy** - Allied Vision camera SDK
- **adafruit-blinka** - FT232H GPIO/ADC

### Supporting Libraries
- **pyqtgraph** - Real-time plotting
- **sqlalchemy** - Database ORM
- **alembic** - Database migrations
- **pydantic** - Configuration validation

## Hardware Requirements

### Components
1. **Laser Controller:** Arroyo Instruments TEC Controller
2. **Linear Actuator:** Xeryon linear stage
3. **Camera:** Allied Vision camera (USB 3.0 / GigE)
4. **GPIO Controllers:** 2x Adafruit FT232H Breakout (USB-C)
5. **Footpedal:** Normally-open momentary switch
6. **Hotspot Smoothing Device:** With digital signal output
7. **Photodiode:** With voltage output (0-5V range)

### Computer
- **OS:** Windows 10
- **Form Factor:** Mini PC
- **Minimum Specs:**
  - Intel i5 or equivalent
  - 8GB RAM
  - 256GB SSD
  - Multiple USB 3.0 ports

## Installation

**Note:** Installation procedures will be documented once development begins.

### Prerequisites
```bash
# Python 3.10 or higher
python --version

# Virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

### Dependencies
```bash
pip install -r requirements.txt
```

## Development Phases

### Phase 1: Foundation (Hardware + Safety) - Weeks 1-4
- [ ] Hardware abstraction layer for all devices
- [ ] Safety interlock system implementation
- [ ] Basic GUI shell (PyQt6)
- [ ] Database schema and CRUD operations
- [ ] Hardware connection and self-test routines

### Phase 2: Core Treatment Features - Weeks 5-8
- [ ] Patient selection and session management
- [ ] Treatment protocol engine
- [ ] Manual treatment control (constant power)
- [ ] Basic event logging
- [ ] Camera integration and live feed display

### Phase 3: Advanced Features - Weeks 9-12
- [ ] Ring detection and focus measurement
- [ ] Video recording and playback
- [ ] Protocol builder UI
- [ ] Advanced ramping protocols
- [ ] Calibration tools

### Phase 4: Polish & Validation - Weeks 13-16
- [ ] Comprehensive testing (unit, integration, safety)
- [ ] User manual and documentation
- [ ] Calibration procedures documentation
- [ ] Performance optimization
- [ ] Bug fixes and refinement

## Safety & Compliance

**CRITICAL:** This is a medical device intended for clinical use.

Before deployment:
1. **Risk Analysis** - Perform comprehensive FMEA
2. **Safety Testing** - Document all safety system tests
3. **Validation** - Independent safety review
4. **Regulatory Review** - Consult with regulatory experts
5. **User Training** - Complete operator training program
6. **Maintenance Protocol** - Regular safety verification schedule

## Development Guidelines

### Safety First
- All safety-critical code must have unit tests
- Safety interlocks cannot be bypassed in production builds
- Any safety event must be logged immutably
- Regular code reviews for safety-related modules

### Code Quality
- Follow PEP 8 style guidelines
- Type hints for all functions
- Comprehensive docstrings
- Unit tests for all modules (target: 80%+ coverage)

### Documentation
- Keep architecture docs updated
- Document all hardware interfaces
- Maintain change log
- User-facing docs must be clear and comprehensive

## Testing Strategy

### Unit Tests
- Hardware abstraction layer
- Protocol engine
- Image processing algorithms
- Database operations

### Integration Tests
- Hardware communication
- Safety interlock coordination
- UI to backend integration

### Safety Tests
- Footpedal response time
- Photodiode monitoring accuracy
- E-stop effectiveness
- Watchdog timer functionality
- Multi-fault scenarios

### User Acceptance Testing
- Clinical workflow validation
- Operator feedback
- Usability assessment

## Contributing

**This is a medical device project.** All contributions must:
1. Pass safety review
2. Include comprehensive tests
3. Not compromise any safety features
4. Be thoroughly documented

## License

**TBD** - To be determined based on deployment requirements

## Contact

**Project Lead:** [To be assigned]
**Safety Engineer:** [To be assigned]
**Clinical Advisor:** [To be assigned]

## Acknowledgments

- Arroyo Instruments for laser controller documentation
- Xeryon for actuator API
- Allied Vision for VmbPy SDK
- Adafruit for FT232H libraries

---

## Quick Start (Once Development Complete)

```bash
# Clone repository
git clone <repository-url>
cd laser-control-system

# Install dependencies
pip install -r requirements.txt

# Initialize database
python -m src.database.init_db

# Run application
python src/main.py
```

## Documentation

**Project Management:** `docs/project/`
- START_HERE.md - New AI session quick start
- PROJECT_STATUS.md - Current project state
- WORK_LOG.md - Real-time session tracking
- CODING_STANDARDS.md - Development rules
- CONFIGURATION.md - Config file reference

**Architecture:** `docs/architecture/`

1. **01_system_overview.md** - Start here for complete system architecture
2. **02_database_schema.md** - Database design and schema
3. **03_safety_system.md** - Critical safety architecture
4. **04_treatment_protocols.md** - Protocol design and execution
5. **05_image_processing.md** - Camera and image processing

Additional docs (to be created):
- **user_manual.md** - End-user guide
- **installation.md** - Setup and installation
- **maintenance.md** - Calibration and maintenance procedures
- **troubleshooting.md** - Common issues and solutions

---

**Last Updated:** 2025-10-15
**Project Status:** Planning - Architecture Complete, Ready for Implementation
