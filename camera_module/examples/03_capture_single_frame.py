"""
Single Frame Capture Script

Captures a single frame from the camera and saves it as a NumPy array and image file.

Usage:
    python 03_capture_single_frame.py [camera_id] [output_filename]

Default output: captured_frame.png
"""

import sys

import numpy as np
import vmbpy


def capture_frame(camera_id: str = None, output_file: str = "captured_frame.png") -> None:
    """
    Capture a single frame from the camera.

    Args:
        camera_id: Optional camera ID. If None, uses first available camera.
        output_file: Path to save captured image.
    """
    vmb = vmbpy.VmbSystem.get_instance()

    with vmb:
        cameras = vmb.get_all_cameras()

        if not cameras:
            print("No cameras detected.")
            return

        if camera_id:
            camera = vmb.get_camera_by_id(camera_id)
        else:
            camera = cameras[0]
            print(f"Using camera: {camera.get_id()}")

        with camera:
            try:
                frame = camera.get_frame()

                print("\nFrame Information:")
                print(f"  Width:        {frame.get_width()}")
                print(f"  Height:       {frame.get_height()}")
                print(f"  Pixel Format: {frame.get_pixel_format()}")
                print(f"  Frame ID:     {frame.get_id()}")
                print(f"  Timestamp:    {frame.get_timestamp()}")

                frame_data = frame.as_numpy_ndarray()
                print(f"\nNumPy Array Shape: {frame_data.shape}")
                print(f"Data Type: {frame_data.dtype}")

                try:
                    import cv2

                    cv2.imwrite(output_file, frame_data)
                    print(f"\nImage saved to: {output_file}")
                except ImportError:
                    np.save(output_file.replace(".png", ".npy"), frame_data)
                    print(f"\nNumPy array saved to: {output_file.replace('.png', '.npy')}")
                    print("Install OpenCV (cv2) to save as image file.")

            except vmbpy.VmbTimeout:
                print("Error: Frame capture timed out.")
                print("Check that camera is not in use by another application.")


if __name__ == "__main__":
    camera_id = sys.argv[1] if len(sys.argv) > 1 else None
    output_file = sys.argv[2] if len(sys.argv) > 2 else "captured_frame.png"

    try:
        capture_frame(camera_id, output_file)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
