# RecipeSpawn

RecipeSpawn is a deep learning project that uses a neural network to generate recipes from images of food.
The application analyzes food images uploaded by the user and suggests recipes based on the ingredients detected in the image. RecipeSpawn uses Convolutional Neural Networks (CNNs) to recognize food items from images and a customized recommendation system to suggest recipes based on the recognized ingredients.

## Requirements

- Python 3.6 or later
- PyTorch 1.7.1 or later
- TorchVision 0.8.2 or later
- Flask 2.0.1 or later
- Numpy 1.19.5 or later
- Pickle 4.0 or later
- Pillow 8.3.1 or later
- Tensorflow 2.5.0 or later (for image preprocessing)
- Matplotlib 3.4.2 or later (for visualizing recipes)

## Installation

1. Clone this repository to your local machine.
2. Install the required packages by running `pip install -r requirements.txt`.

## Usage

1. Start the Flask server by running `python run.py`.
2. Navigate to `http://localhost:5000/` in your web browser.
3. Upload an image of food.
4. Wait for the model to generate the recipe (this may take a few seconds).
5. View the recipe ingredients and instructions on the results page.

## Screenshots

![Screenshot 1](/img_to_recipe/static/images/screenshot/ss.png)

## Contributing

If you would like to contribute to this project, feel free to submit a pull request or open an issue.
