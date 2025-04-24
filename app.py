import streamlit as st
import pytesseract
from PIL import Image
from utils import remove_blue_shade_and_enhance

# Set tesseract command path for Streamlit Cloud
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

st.title("Hidden Blue Text Extractor")
st.write("Upload an image with blue shading over text")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.subheader("Extracted Text")
    try:
        processed = remove_blue_shade_and_enhance(image)
        st.image(processed, caption="Processed Image", use_column_width=True)
        text = pytesseract.image_to_string(processed)
        st.text_area("Text", text, height=200)
    except Exception as e:
        st.error("Error extracting text")
        st.exception(e)