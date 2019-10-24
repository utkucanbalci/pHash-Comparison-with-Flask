from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2
import os
from PIL import Image
import imagehash

app = Flask(__name__)

UPLOAD_FOLDER = ''
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def hamming_distance(s1, s2):#https://en.wikipedia.org/wiki/Hamming_distance
    s1 = str(s1)
    s2 = str(s2)

    return sum(el1 != el2 for el1, el2 in zip(s1, s2))

@app.route("/api/computeImage",methods=["POST"])
def computeImage():#calculates phash of an image
    try:

        image = request.files["image"]
        filename = image.filename
        image_path=UPLOAD_FOLDER+"/"+filename

        image.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))

        image_phash = imagehash.phash(Image.open(image_path))

        response = {'pHash': '{}'.format(image_phash)}

        response_pickled = jsonpickle.encode(response)
        if os.path.exists(image_path):
            os.remove(image_path)
        return Response(response=response_pickled, status=200, mimetype="application/json")
    except Exception as e:
        response = {'Error': '{}'.format(e)}

        response_pickled = jsonpickle.encode(response)

        return Response(response=response_pickled, status=400, mimetype="application/json")

@app.route("/api/computePath",methods=["POST"])
def computePath():#calculates phash from image path
    try:

        dir = request.args.get("im1", None )

        if os.path.exists(dir):
            image_phash = imagehash.phash(Image.open(dir))

            response = {'pHash': '{}'.format(image_phash)
                        }

            response_pickled = jsonpickle.encode(response)

            return Response(response=response_pickled, status=200, mimetype="application/json")
        else:
            response = {'Error': '{} is not an existing file.'.format(dir)}

            response_pickled = jsonpickle.encode(response)

            return Response(response=response_pickled, status=404, mimetype="application/json")
    except Exception as e:
        response = {'Error': '{}'.format(e)}

        response_pickled = jsonpickle.encode(response)

        return Response(response=response_pickled, status=400, mimetype="application/json")

@app.route("/api/compareImages",methods=["POST"])
def compareImages():#compares two images
    try:

        image1 = request.files["image1"]
        image2 = request.files["image2"]

        image1.save(os.path.join(app.config["UPLOAD_FOLDER"],image1.filename))
        image2.save(os.path.join(app.config["UPLOAD_FOLDER"],image2.filename))

        image_path1=UPLOAD_FOLDER+"/"+image1.filename
        image_path2=UPLOAD_FOLDER+"/"+image2.filename

        image_phash1 = imagehash.phash(Image.open(image_path1))
        image_phash2 = imagehash.phash(Image.open(image_path2))

        cmp = hamming_distance(image_phash1, image_phash2)

        response = {'pHash1': '{}'.format(image_phash1), 'pHash2': '{}'.format(image_phash2), 'hamming_distance': '{}'.format(str(cmp))
                    }

        response_pickled = jsonpickle.encode(response)

        if os.path.exists(image_path1):
            os.remove(image_path1)
        if os.path.exists(image_path2):
            os.remove(image_path2)
        return Response(response=response_pickled, status=200, mimetype="application/json")
    except Exception as e:
        response = {'Error': '{}'.format(e)}

        response_pickled = jsonpickle.encode(response)

        return Response(response=response_pickled, status=400, mimetype="application/json")

@app.route("/api/comparePaths",methods=["POST"])
def comparePaths():#compares two image filepaths
    try:
        dir1 = request.args.get("im1", None )
        dir2 = request.args.get("im2", None )
        check_dir1=  os.path.exists(dir1)
        check_dir2=  os.path.exists(dir2)
        if check_dir1 and check_dir2:

            image_phash1 = imagehash.phash(Image.open(dir1))
            image_phash2 = imagehash.phash(Image.open(dir2))
            cmp = hamming_distance(image_phash1, image_phash2)

            response = {'pHash1': '{}'.format(image_phash1), 'pHash2': '{}'.format(image_phash2), 'hamming_distance': '{}'.format(str(cmp))
                        }

            response_pickled = jsonpickle.encode(response)

            return Response(response=response_pickled, status=200, mimetype="application/json")
        else:
            status1 = ""
            status2 = ""
            if check_dir1:
                status1 = "Exists"
            else:
                status1 = "Does not exists"

            if check_dir2:
                status2 = "Exists"
            else:
                status2 = "Does not exists"


            response = {'Error': '{} {} and {} {}'.format(dir1,status1, dir2, status2)}

            response_pickled = jsonpickle.encode(response)

            return Response(response=response_pickled, status=404, mimetype="application/json")
    except Exception as e:
        response = {'Error': '{}'.format(e)}

        response_pickled = jsonpickle.encode(response)

        return Response(response=response_pickled, status=400, mimetype="application/json")


app.run(host="localhost", port=5000, debug=True)
