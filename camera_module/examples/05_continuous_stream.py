"""
Continuous Frame Streaming Script

Captures continuous frames from the camera and displays frame rate.
Press Ctrl+C to stop.

Usage:
    python 05_continuous_stream.py [camera_id] [duration_seconds]

Default duration: 10 seconds
"""

import sys
import time

import vmbpy


def stream_frames(camera_id: str = None, duration: int = 10) -> None:
    """
    Capture continuous frames from camera.

    Args:
        camera_id: Optional camera ID. If None, uses first available camera.
        duration: Duration to capture in seconds.
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
            frame_count = 0
            start_time = time.time()

            print(f"\nStreaming for {duration} seconds...")
            print("Press Ctrl+C to stop early.\n")

            try:
                camera.start_streaming(lambda cam, stream_stats: on_frame_ready(cam, stream_stats))

                while time.time() - start_time < duration:
                    time.sleep(0.1)
                    elapsed = time.time() - start_time
                    if int(elapsed) % 5 == 0 and elapsed > 0:
                        fps = frame_count / elapsed
                        print(f"Elapsed: {elapsed:.1f}s, Frames: {frame_count}, FPS: {fps:.2f}")

                camera.stop_streaming()

            except KeyboardInterrupt:
                print("\nStopping...")
                camera.stop_streaming()

            elapsed = time.time() - start_time
            fps = frame_count / elapsed if elapsed > 0 else 0

            print("\nCapture Complete:")
            print(f"  Duration:  {elapsed:.2f} seconds")
            print(f"  Frames:    {frame_count}")
            print(f"  Avg FPS:   {fps:.2f}")


def on_frame_ready(camera: vmbpy.Camera, stream_stats: vmbpy.StreamStats) -> None:
    """
    Callback function called for each captured frame.

    Args:
        camera: Camera instance
        stream_stats: Streaming statistics
    """
    global frame_count
    frame_count += 1


frame_count = 0


if __name__ == "__main__":
    camera_id = sys.argv[1] if len(sys.argv) > 1 else None
    duration = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    try:
        stream_frames(camera_id, duration)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
