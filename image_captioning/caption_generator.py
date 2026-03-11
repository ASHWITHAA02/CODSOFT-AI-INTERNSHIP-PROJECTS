from transformers import VisionEncoderDecoderModel
from transformers import ViTImageProcessor
from transformers import AutoTokenizer
import torch
from utils import load_image

MODEL_NAME = "nlpconnect/vit-gpt2-image-captioning"

print("Loading AI model...")

model = VisionEncoderDecoderModel.from_pretrained(MODEL_NAME)
feature_extractor = ViTImageProcessor.from_pretrained(MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def generate_caption(image_path):

    image = load_image(image_path)

    if image is None:
        return

    pixel_values = feature_extractor(
        images=image,
        return_tensors="pt"
    ).pixel_values.to(device)

    output_ids = model.generate(
        pixel_values,
        max_length=16,
        num_beams=4
    )

    caption = tokenizer.decode(
        output_ids[0],
        skip_special_tokens=True
    )

    return caption


if __name__ == "__main__":

    path = input("Enter image path: ")

    caption = generate_caption(path)

    print("\nGenerated Caption:")
    print(caption)