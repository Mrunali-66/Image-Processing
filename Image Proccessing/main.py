from PIL import Image, ImageFilter, ImageEnhance
import os

def load_image(file_path):
    """Load an image from file"""
    return Image.open(file_path)

def resize_image(image, width, height):
    """Resize image to specified dimensions"""
    return image.resize((width, height))

def rotate_image(image, degrees):
    """Rotate image by specified degrees"""
    return image.rotate(degrees)

def apply_filter(image, filter_type):
    """Apply different image filters"""
    filters = {
        'blur': ImageFilter.BLUR,
        'contour': ImageFilter.CONTOUR,
        'detail': ImageFilter.DETAIL,
        'edge_enhance': ImageFilter.EDGE_ENHANCE,
        'sharpen': ImageFilter.SHARPEN
    }
    return image.filter(filters.get(filter_type, ImageFilter.BLUR))

def adjust_brightness(image, factor):
    """Adjust image brightness"""
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def adjust_contrast(image, factor):
    """Adjust image contrast"""
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def convert_to_grayscale(image):
    """Convert image to grayscale"""
    return image.convert('L')

def crop_image(image, box):
    """Crop image using a tuple (left, upper, right, lower)"""
    return image.crop(box)

def main():
    # Example usage
    try:
        # Load an image
        image_path = 'example.jpg'  # Replace with your image path
        original_image = load_image(image_path)

        # Create output directory if it doesn't exist
        os.makedirs('output', exist_ok=True)

        # Resize image
        resized = resize_image(original_image, 300, 200)
        resized.save('output/resized_image.jpg')

        # Rotate image
        rotated = rotate_image(original_image, 45)
        rotated.save('output/rotated_image.jpg')

        # Apply blur filter
        blurred = apply_filter(original_image, 'blur')
        blurred.save('output/blurred_image.jpg')

        # Adjust brightness
        brightened = adjust_brightness(original_image, 1.5)
        brightened.save('output/brightened_image.jpg')

        # Convert to grayscale
        grayscale = convert_to_grayscale(original_image)
        grayscale.save('output/grayscale_image.jpg')

        # Crop image
        cropped = crop_image(original_image, (100, 100, 400, 400))
        cropped.save('output/cropped_image.jpg')

        print("Image processing completed successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()