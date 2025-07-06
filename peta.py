import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io

st.set_page_config(page_title="🗺️ Peta Undangan Pernikahan", layout="wide")
st.title("💒 Buat Peta Undangan Pernikahan")

# Gambar latar peta (pastikan file ada)
bg_image_path = "peta_template.png"
bg_image = Image.open(bg_image_path)

# Opsi mode menggambar
drawing_mode = st.sidebar.selectbox(
    "Mode Menggambar",
    ("freedraw", "line", "rect", "circle", "text", "transform"),
)

stroke_width = st.sidebar.slider("Tebal Gambar", 1, 10, 3)
stroke_color = st.sidebar.color_picker("Warna Garis", "#ff0000")
bg_color = st.sidebar.color_picker("Warna Isi Bentuk", "rgba(255,165,0,0.3)")

# Canvas gambar
canvas_result = st_canvas(
    fill_color=bg_color,
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_image=bg_image,
    update_streamlit=True,
    height=500,
    width=700,
    drawing_mode=drawing_mode,
    key="canvas_undangan"
)

# Menampilkan hasil JSON (opsional untuk keperluan edit lanjutan)
if canvas_result.json_data:
    st.subheader("📝 Data Gambar (opsional)")
    st.json(canvas_result.json_data)

# Tombol download gambar hasil menggambar
if canvas_result.image_data is not None:
    img = Image.fromarray(canvas_result.image_data.astype("uint8"))

    st.subheader("📥 Unduh Gambar Peta")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="📷 Download Peta Undangan",
        data=byte_im,
        file_name="peta_undangan.png",
        mime="image/png"
    )