import subprocess
import os

# ✅ Add watermark to video/file (Simple example)
def add_watermark(input_file):
    output_file = f"wm_{os.path.basename(input_file)}"
    watermark_text = os.getenv("WATERMARK_TEXT", "© AutoRenameBOT")

    # Simple ffmpeg drawtext filter
    cmd = [
        "ffmpeg", "-i", input_file, "-vf",
        f"drawtext=text='{watermark_text}':x=10:y=H-th-10:fontsize=24:fontcolor=white",
        "-codec:a", "copy", output_file, "-y"
    ]
    subprocess.run(cmd)

    return output_file
