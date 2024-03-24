
from ipywidgets import interact, widgets
from IPython.display import display, Video
from gtts import gTTS
from moviepy.editor import *
from translate import Translator
#LAST CHANGE - BELOW STATEMENT
import os
import math


from flask import Flask, request, jsonify, send_file
#from moviepy.editor import TextClio
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define a list of Indian languages and their codes
indian_languages = {
    'English': 'en',
    'Hindi': 'hi',
    'Bengali': 'bn',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Marathi': 'mr',
    # Add more languages as needed
}

@app.route('/convert', methods=['POST'])

# Function to handle video generation
#def generate_video():
    # Translate the text using the `translate` module
    #data = request.get_json()
    #text = data['text']
    #translator = Translator(to_lang=indian_languages[target_language])
    #translated_text = translator.translate(text)


def convert_text_to_video():
    data = request.get_json()
    text = data['text']
    target_language = data['lang']
    translator = Translator(to_lang=indian_languages[target_language])
    translated_text = translator.translate(text)
    #print("This is the text: " + translated_text)

    tts = gTTS(translated_text, lang=indian_languages[target_language])
    #tts = gTTS(translated_text, lang=indian_languages[target_language])
    tts.save('generated_audio.mp3')

    gif_clip = VideoFileClip('train.gif')
    gifclip_duration = gif_clip.duration
    
    clip = TextClip(text, 
                    fontsize=30, 
                    color='white', 
                    # stroke_color='white',
                    bg_color='transparent', 
                    size=(300, 400), 
                    method='caption')
    # clip = clip.set_position(("center", "middle"))

    # Create a TextClip as shown earlier
    #clip = TextClip(text, fontsize=40, color='white')
    
    clip = clip.set_fps(30)

    audio_clip = AudioFileClip('generated_audio.mp3')
    audioclip_duration = audio_clip.duration
    background_clip = gif_clip.loop(n=math.ceil(audioclip_duration/gifclip_duration))
    clip = clip.set_duration(background_clip.duration)

    #Setting audio to text clip
    video_clip = clip.set_audio(audio_clip)

    # Position the text in the center of the video
    video_clip = video_clip.set_position("center")
    
    # Overlay the text on top of the background GIF
    final_clip = CompositeVideoClip([background_clip, video_clip])
    #final_clip = CompositeVideoClip([audio_clip])

    #output_filename = f"output_video_{target_language}.mp4"
    #final_clip.write_videofile(output_filename, codec='libx264', fps=24)
    
    # Save the video as a file
    video_path = 'output.mp4'
    final_clip.write_videofile(video_path, codec='libx264')
    #video_clip.write_videofile(video_path, codec='libx264')

    # Send the video file as a response
    return send_file(video_path)

#if __name__ == '__main':
app.run()
