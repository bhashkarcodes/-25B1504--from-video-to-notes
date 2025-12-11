from youtube_transcript_api import YouTubeTranscriptApi

ytt_api = YouTubeTranscriptApi()
srt = ytt_api.fetch("2LOh_01i8Is")  # video ID

with open("face.txt" , 'w') as f:
    for line in srt:
        f.write(f"{line}\n") 