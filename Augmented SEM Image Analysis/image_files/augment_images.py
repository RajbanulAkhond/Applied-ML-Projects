import os
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
from pathlib import Path

def add_white_noise(image, noise_intensity=45):
    """Add white noise to an image."""
    image_array = np.array(image, dtype=np.float32)
    noise = np.random.normal(0, noise_intensity, image_array.shape)
    noisy_image = np.clip(image_array + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(noisy_image)

def blur_image(image, radius=10):
    """Apply Gaussian blur to an image."""
    return image.filter(ImageFilter.GaussianBlur(radius=radius))

def increase_contrast(image, factor=2.0):
    """Increase the contrast of an image."""
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def augment_folder(input_folder, output_base_name):
    """Augment all images in a folder with three different augmentations."""
    base_path = Path("/Users/akhond/Library/CloudStorage/OneDrive-IndianaUniversity/PhD/Courses/Applied ML (P-556)/H3_Q2")
    
    # Create output folders
    blurred_folder = base_path / f"{output_base_name}_blurred"
    noisy_folder = base_path / f"{output_base_name}_noisy"
    contrast_folder = base_path / f"{output_base_name}_contrast"
    
    blurred_folder.mkdir(exist_ok=True)
    noisy_folder.mkdir(exist_ok=True)
    contrast_folder.mkdir(exist_ok=True)
    
    input_path = base_path / input_folder
    
    # Process all images in the folder
    image_files = [f for f in os.listdir(input_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]
    
    print(f"\nProcessing {input_folder}...")
    print(f"Found {len(image_files)} images")
    
    for idx, filename in enumerate(image_files, 1):
        try:
            image_path = input_path / filename
            image = Image.open(image_path)
            
            # Convert to RGB if necessary (e.g., RGBA)
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Apply blur augmentation
            blurred = blur_image(image, radius=15)
            blurred.save(blurred_folder / filename)
            
            # Apply white noise augmentation
            noisy = add_white_noise(image, noise_intensity=25)
            noisy.save(noisy_folder / filename)
            
            # Apply contrast augmentation
            contrasted = increase_contrast(image, factor=2.0)
            contrasted.save(contrast_folder / filename)
            
            if idx % 10 == 0:
                print(f"  Processed {idx}/{len(image_files)} images...")
        
        except Exception as e:
            print(f"  Error processing {filename}: {str(e)}")
    
    print(f"  ✓ Completed {input_folder}")
    print(f"    - Saved {len(image_files)} blurred images to {blurred_folder.name}")
    print(f"    - Saved {len(image_files)} noisy images to {noisy_folder.name}")
    print(f"    - Saved {len(image_files)} contrast-enhanced images to {contrast_folder.name}")

if __name__ == "__main__":
    print("=" * 70)
    print("Image Augmentation Script")
    print("=" * 70)
    
    # Process all three folders
    folders = [
        ("Fibres", "Fibres"),
        ("Films_Coated_Surface", "Films_Coated_Surface"),
        ("Porous_Sponge", "Porous_Sponge")
    ]
    
    for input_folder, output_name in folders:
        augment_folder(input_folder, output_name)
    
    print("\n" + "=" * 70)
    print("Augmentation complete!")
    print("=" * 70)
