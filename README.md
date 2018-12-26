# Dog-Breed-Detector

This project is a Flask web application that creates a webpage for a user to submit a dog photo and get the results of it's breed.

The project uses a trained inceptionv3 model and tensorflow's label_image.py to label the dog images.

Results.txt is created when the image is labeled, and is used by flask to get the dog's breed and show it on the HTML.

The page being loaded is upload.html.

## Running the app

Make sure you have a python 3 version installed, including the flask, tensorflow, numpy, and jinja2 dependencies.

To run, create an environment variable called FLASK_APP and set it = to app.py. Then to run, type flask run. This will host the project on localhost:5000, which you can visit in your browser.
