import streamlit as st
import PyPDF2
from gtts import gTTS
from io import BytesIO

def main():
    st.set_page_config(page_title="PragyanAI - VVIET Multimedia Hub", layout="wide")
    st.image()
    st.image("PragyanAI_Transperent.png")
    st.title(" PragyanAI Multi-Functional Media Hub")

    # Create Tabs for Video, YouTube, and PDF
    tab1, tab2, tab3 = st.tabs(["📹 Local Video", "📺 YouTube Player", "📄 PDF to Audio"])

    # --- TAB 1: LOCAL VIDEO PLAYER ---
    with tab1:
        st.header("Upload & Play Local Video")
        video_file = st.file_uploader("Upload MP4/MOV", type=["mp4", "mov", "avi"])
        if video_file:
            st.video(video_file)

    # --- TAB 2: YOUTUBE PLAYER ---
    with tab2:
        st.header("Stream YouTube Content")
        yt_url = st.text_input("Paste YouTube URL here", placeholder="https://www.youtube.com/watch?v=...")
        if yt_url:
            try:
                st.video(yt_url)
                st.caption("Now streaming from YouTube")
            except Exception as e:
                st.error("Please enter a valid YouTube URL.")

    # --- TAB 3: PDF READER & AUDIO --
