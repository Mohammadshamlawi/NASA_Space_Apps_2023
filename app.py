import streamlit as st
import random
from PIL import Image, ImageOps
import numpy as np

import warnings
warnings.filterwarnings("ignore")


st.set_page_config(
    page_title="Team Name",
    layout="wide"
)

st.set_option('deprecation.showfileUploaderEncoding', False)
st.write("""
         # Fine-Tuned Burn Scar Detection
         """
         )

file = st.file_uploader("", type=["jpg", "png"])
left, right = st.columns(2, gap="medium")

st.write("##")
left.title("Input")

right.title("Output")

if file is not None:
    image = Image.open(file)
    left.image(image, use_column_width=True)
    right.image(image, use_column_width=True)