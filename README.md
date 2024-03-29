# RecipeSpawn

RecipeSpawn is a deep learning project that uses a neural network to generate recipes from images of food.
The application analyzes food images uploaded by the user and suggests recipes based on the ingredients detected in the image. RecipeSpawn uses Convolutional Neural Networks (CNNs) to recognize food items from images and a customized recommendation system to suggest recipes based on the recognized ingredients.

## Installation

1. Clone this repository to your local machine.
2. Install the required packages by running `pip install -r requirements.txt`.

## Usage

1. Start the Flask server by running `python run.py`.
2. Navigate to `http://localhost:5000/` in your web browser.
3. Upload an image of food.
4. Wait for the model to generate the recipe (this may take a few seconds).
5. View the recipe ingredients and instructions on the results page.

## Screenshot

![Screenshot 1](/img_to_recipe/static/images/screenshot/ss.png)
