"""
TOSCA Medical Laser Control System - Main Entry Point

This is the primary entry point for the TOSCA application.
Initializes the PyQt6 application and launches the main window.

Safety Notice:
    This is FDA-Enhanced Documentation Level medical device software.
    All safety-critical systems must be verified before clinical use.
"""

import sys
import logging
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent))


def setup_logging():
    """
    Configure application-wide logging.

    Logs are written to:
        - Console (INFO and above)
        - File: data/logs/tosca.log (DEBUG and above)
    """
    log_dir = Path(__file__).parent.parent / "data" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_dir / "tosca.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )

    logger = logging.getLogger(__name__)
    logger.info("=" * 60)
    logger.info("TOSCA Medical Laser Control System Starting")
    logger.info("=" * 60)
    return logger


def main():
    """
    Main application entry point.

    Returns:
        int: Exit code (0 for success, non-zero for error)
    """
    logger = setup_logging()

    try:
        # Import PyQt6 here to ensure logging is set up first
        from PyQt6.QtWidgets import QApplication

        logger.info("Initializing Qt Application")
        app = QApplication(sys.argv)
        app.setApplicationName("TOSCA Laser Control")
        app.setOrganizationName("Aleyegn Medical Devices")

        # TODO: Import and create main window
        # from ui.main_window import MainWindow
        # window = MainWindow()
        # window.show()

        logger.warning("Main window not yet implemented - placeholder mode")
        logger.info("Application ready. Press Ctrl+C to exit.")

        # For now, just show that the app can start
        return_code = 0  # app.exec() when main window is ready

        logger.info("Application shutting down normally")
        return return_code

    except KeyboardInterrupt:
        logger.info("Application interrupted by user")
        return 0

    except Exception as e:
        logger.critical(f"Fatal error during application startup: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
