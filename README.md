# video-edit

Don't you wish editing videos for Nexxt Intelligence marketing was easy?

Now it is!

Here's how it works:

1. Clone this repo, and make sure you have `gradio_client` Python library installed (`pip install gradio_client`) as well as `ffmpeg`
2. Copy your video file into this folder as `input.mp4`
3. Trim your video, if desired, using some variant of `ffmpeg -ss 00:00:00 -to 00:00:30 -i input.mp4 -c copy input_trimmed.mp4`
4. Generate transcriptions using whisper by running `python transcribe.py` and review `transcribed.srt` output to make sure it looks good! (I recommend using VLC to load the .srt file into the video so that you can playback together and review to make sure everything looks good.)
5. Burn the subtitles into the video so that everyone can see it using this command: `ffmpeg -i input_trimmed.mp4 -vf subtitles=transcribed.srt input_trimmed_subs.mp4`
6. Add the Nexxt Intelligence | inca logo using this command: `ffmpeg -i input_trimmed_subs.mp4 -i nexxt_intelligence_inca_white_blue_small.png -filter_complex "[0:v][1:v] overlay=W-w-30:h+30" -pix_fmt yuv420p -c:a copy output.mp4`

And that gives you `output.mp4` which has our logo, subtitles burned into the video, and is somehow even nicely compressed!

You can also format the `transcribed.srt` file however you like if you want to make use of the raw transcript.
