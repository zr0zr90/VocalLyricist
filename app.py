from flask import Flask, request, jsonify
from google.cloud import texttospeech
import os

app = Flask(__name__)

# Initialize Google TTS client
client = texttospeech.TextToSpeechClient()

def synthesize_speech(text, artist_voice):
    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name=artist_voice  # Example: "en-US-Wavenet-D"
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    return response.audio_content

@app.route('/create_song', methods=['POST'])
def create_song():
    data = request.json
    text = data.get('text')
    artist_voice = data.get('artist_voice')

    if not text or not artist_voice:
        return jsonify({"error": "Invalid input"}), 400

    audio_content = synthesize_speech(text, artist_voice)

    output_filename = "output.mp3"
    with open(output_filename, "wb") as out:
        out.write(audio_content)

    return jsonify({"message": "Song created successfully", "file": output_filename})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
