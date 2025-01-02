from rembg import remove
from PIL import Image
import streamlit as st
import io

st.title("Background Remover App")




uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    input_image = Image.open(uploaded_file)
    st.image(input_image, caption="Original Image", use_container_width=True)

    input_bytes = io.BytesIO()
    input_image.save(input_bytes, format="PNG")
    input_bytes = input_bytes.getvalue()

    output_bytes = remove(input_bytes)

    output_image = Image.open(io.BytesIO(output_bytes))
    st.image(output_image, caption="Image without Background", use_container_width=True)

    download_button = st.download_button(
        label="Download Image without Background",
        data=output_bytes,
        file_name="output_image.png",
        mime="image/png"
    )
