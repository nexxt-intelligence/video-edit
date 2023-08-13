from gradio_client import Client
import re

CORRECTION_DICT = {"chat GPT": "ChatGPT"}

client = Client("https://sanchit-gandhi-whisper-jax.hf.space/")
result = client.predict(
    "./input_trimmed.mp4",  # str (filepath or URL to file) in 'inputs' Audio component
    "transcribe",  # str in 'Task' Radio component
    True,  # bool in 'Return timestamps' Checkbox component
    api_name="/predict",
)
print(result)

regex = r"\[(\d\d):(\d\d).(\d\d\d) -> (\d\d):(\d\d).(\d\d\d)\]  (.*)"
subst = "00:\\g<1>:\\g<2>,\\g<3> --> 00:\\g<4>:\\g<5>,\\g<6>\\n\\g<7>\n"

output = result[0]
for key in CORRECTION_DICT:
    output.replace(key, CORRECTION_DICT[key])

lines = output.split("\n")

srt_output = "\n".join(
    [
        f"{idx+1}\n{re.sub(regex, subst, line, 0, re.MULTILINE)}"
        for idx, line in enumerate(lines)
    ]
)

with open("transcribed.srt", "w") as f:
    f.write(srt_output)
