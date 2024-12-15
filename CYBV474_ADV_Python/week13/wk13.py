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


def extract_features(image, label):
    """Extract hue, saturation, and additional features from an image."""
    pix = image.load()
    features = []

    for row in range(image.height):
        for col in range(image.width):
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
    # Prepare DataFrame for training data
    training_data = []

    # Collect real image features
    for _ in range(3):
        photoSelection = input("\nEnter filename for a Real Image to Extract Features: ")
        img = Image.open(photoSelection)
        training_data.extend(extract_features(img, label="real"))

    # Collect fake image features
    for _ in range(3):
        photoSelection = input("\nEnter filename for a Fake Image to Extract Features: ")
        img = Image.open(photoSelection)
        training_data.extend(extract_features(img, label="fake"))

    # Create DataFrame
    df = pd.DataFrame(training_data)

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
        plot_histogram(df_real, feature, "Real Images")
        plot_histogram(df_fake, feature, "Fake Images")
