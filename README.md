# AudioTranscriptionDemo
Simple Whisper-based audio transcription script.

In this activity we will get familiarized with Whisper (https://openai.com/index/whisper/) an automatic speech recognition (ASR) system from OpenAI.

The script can be found in "transcribe.py." There are two simple ways to run it:


- Option 1: Open with gitbug.dev

Note: If you receive the message "You have 1 file with uncommitted changes from a previous edit session... You are 1 commit behind." simply click on "Sync."

1.1) In the menu bar to the left, click on "Terminal" and "New Terminal."

1.2) Then "Continue working on github codespaces."

1.3) Choose "2 cores, 8GB ram, 32 GB storage."

1.4) A new window should open. Click on the "transcribe.py" file.

1.5) Install recommended Python extension. Click on "bash" next to the terminal.   

1.6) run in the terminal:   sudo apt update && sudo apt install ffmpeg -y          (FFmpeg is needed for pydub)

1.7) run in the terminal:   pip install -r requirements.txt

1.8) run python file!                                                              (No need to create a virtual environment!)

1.9) Drag new audio files into the file space to the left. Modify transcribe.py and run again!


- Option 2: Open with Google Colab

2.1) Open Colab https://colab.google/ and click "New Notebook."

2.2) Install Whisper:   !pip install openai-whisper

2.3) Upload audio file; File/Upload File.

2.4) Note: If you try to install Pydub (!pip install pydub) you should get a message that it is already installed.

2.5) Run script "transcribe.py" (copy and paste the Python code)


- Pending to do:

3.1) Does the script work with mp3/mp4 files as is, or does it need to be modified?

3.2) What if the input file is a video, is it possible to substract the transcription only?
