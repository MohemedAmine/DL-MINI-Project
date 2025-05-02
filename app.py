import gradio as gr
import numpy as np
import cv2
from tensorflow.keras.models import load_model

# Load the trained autoencoder model
model = load_model("models/autoencoder_brain_tumor2.keras")  # Ensure this file exists

def preprocess_image(image):
    # Resize image to 64x64 and convert to grayscale
    image = cv2.resize(image, (64, 64))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    image = image.astype('float32') / 255.0
    image = np.expand_dims(image, axis=-1)  # (64, 64, 1)
    image = np.expand_dims(image, axis=0)   # (1, 64, 64, 1)
    return image

def denoise_image(input_img):
    img = preprocess_image(input_img)
    denoised = model.predict(img)[0]  # (64, 64, 1)
    denoised = denoised[:, :, 0]      # Remove last channel dimension
    denoised = (denoised * 255).astype(np.uint8)
    denoised = cv2.resize(denoised, (256, 256), interpolation=cv2.INTER_NEAREST)
    return denoised

# Gradio Interface
interface = gr.Interface(
    fn=denoise_image,
    inputs=gr.Image(type="numpy", label="Noisy Brain MRI"),
    outputs=gr.Image(type="numpy", label="Denoised MRI"),
    title="Brain MRI Denoising using Autoencoder",
    description=(
        "Upload a noisy brain MRI image and this tool will apply an autoencoder-based model "
        "to produce a cleaner, denoised version of the scan. Make sure your image is MRI and square-shaped for best results."
    ),
    allow_flagging="never",
)

# Launch the app
interface.launch()
