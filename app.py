from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES

import os

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        label_image = 'python3 label_image.py --labels=retrained_labels.txt --graph=retrained.pb --image=static/img/' + filename
        os.system(label_image)
        results_file = open("results.txt", "r")
        result = results_file.readline();
        dogBreed = result[:result.find("0")]
        confidence = float(result[result.find("0"):])
        os.remove('static/img/' + filename)
        if confidence >= 0.85:
            return render_template('upload.html', breed=dogBreed)
        else:
            return render_template('upload.html', error='true')
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
