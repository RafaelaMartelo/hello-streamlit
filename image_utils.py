from PIL import Image
import tempfile

def save_uploaded_file(uploaded_file):
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp:
            tmp.write(uploaded_file.getvalue())
            tmp.flush()
            return tmp.name
    return None

def display_image(column, image_path, caption):
    image = Image.open(image_path)
    column.image(image, caption=caption, use_column_width=True)
