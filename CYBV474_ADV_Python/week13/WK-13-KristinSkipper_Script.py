'''
Kristin Skipper
CYBV-474
Week 13 Exercise
'''
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

Image.MAX_IMAGE_PIXELS = 200000000  # Handle large images

def calcHueSat(pixel):
    """Calculate the Hue and Saturation of a single pixel."""
    r, g, b = pixel[0], pixel[1], pixel[2]
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == mn:
        hue = 0
    elif mx == r:
        hue = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        hue = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        hue = (60 * ((r - g) / df) + 240) % 360
    if mx == 0:
        sat = 0
    else:
        sat = (df / mx) * 100

    return hue, sat

def extract_features(image, label, stride=5):
    """Extract hue, saturation, and additional features from an image."""
    pix = image.load()
    features = []
    for row in range(0, image.height, stride):
        for col in range(0, image.width, stride):
            r, g, b = pix[col, row]
            hue, sat = calcHueSat((r, g, b))
            brightness = (r + g + b) / 3
            features.append({
                "hue": hue,
                "sat": sat,
                "brightness": brightness,
                "red": r,
                "green": g,
                "blue": b,
                "label": label
            })
    return features

def plot_features(data, title):
    """Plot hue and saturation features."""
    plt.figure(figsize=(10, 6))
    plt.scatter(data['hue'], data['sat'], alpha=0.5, c='blue', edgecolor='k')
    plt.title(title)
    plt.xlabel('Hue')
    plt.ylabel('Saturation')
    plt.show()

def plot_histogram(data, feature, title):
    """Plot histogram for a specific feature."""
    plt.figure(figsize=(10, 6))
    plt.hist(data[feature], bins=50, alpha=0.7, edgecolor='black')
    plt.title(f'{title} - {feature.capitalize()} Distribution')
    plt.xlabel(feature.capitalize())
    plt.ylabel('Frequency')
    plt.show()

if __name__ == "__main__":
    # Input one real and one fake image
    real_image_path = input("\nEnter filename for a Real Image to Extract Features: ")
    fake_image_path = input("\nEnter filename for a Fake Image to Extract Features: ")

    # Process real image
    real_img = Image.open(real_image_path)
    real_features = extract_features(real_img, label="real")

    # Process fake image
    fake_img = Image.open(fake_image_path)
    fake_features = extract_features(fake_img, label="fake")

    # Combine features into a DataFrame
    training_data = real_features + fake_features
    df = pd.DataFrame(training_data)

    # Display the first & last few rows of the training DataFrame
    print("\nTraining Data (First 10 Rows):")
    print(df.head(10))  # Show the first 10 rows
    print("\nTraining Data (Last 10 Rows):")
    print(df.tail(10))  # Show the last 10 rows

    # Save to CSV
    df.to_csv("training_data.csv", index=False)
    print("Training data saved to 'training_data.csv'.")

    # Separate real and fake data
    df_real = df[df['label'] == "real"]
    df_fake = df[df['label'] == "fake"]

    # Plot features
    plot_features(df_real, "Real Image Features")
    plot_features(df_fake, "Fake Image Features")

    # Plot histograms for additional features
    for feature in ["red", "green", "blue", "brightness"]:
        plot_histogram(df_real, feature, "Real Image")
        plot_histogram(df_fake, feature, "Fake Image")
