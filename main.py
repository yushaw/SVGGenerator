import createPic
from rembg import remove, new_session
from PIL import Image
import os
import subprocess

prompt="seashore"

image_path = "test.png"

image = createPic.generate_pic(prompt+"<lora:SVG:1>")
image.save("createPic.png")

session = new_session("u2net")
image =remove(image, session=session, alpha_matting=False)
image.save(image_path)

def run_vtracer(input_image, output_image):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    if os.name == 'nt':  # nt表示Windows系统
        executable = "vtracer.exe"
    else:
        executable = "vtracer"
    cmd_path = os.path.join(current_dir, executable)
    cmd = f"{cmd_path} --input {input_image} --output {output_image} --segment_length {4} --preset {'poster'} --corner_threshold {145}"
    subprocess.run(cmd, shell=True)

run_vtracer(image_path, "output.svg")
