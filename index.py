# Built with python 3, dependencies installed with pip 
# library to generate images - Pillow 
# https://pillow.readthedocs.io/en/stable/installation.html
from PIL import Image

# library to work with arrays 
# https://numpy.org/
import numpy as np

#extra added for flask
from flask import Flask, jsonify, make_response
from flask.helpers import make_response
app = Flask(__name__)


# lib for api calls using pinata
import requests

# lib for making readable stream of file for pinata
import io
#lib for getting random number
import random

# library to interact with the operating system
import os

# library to generate random integer values
from random import seed
from random import randint

# gets path to be used in image creation mechanism, using os
dirname = os.path.dirname(__file__)

# sets final image dimensions as 480x480 pixels
# the original 24x24 pixel image will be expanded to these dimensions
dimensions = 640, 640

# tells how many times to iterate through the following mechanism
# which equals the number of birds
# e.g. 
# for x in range(0-200) 
# would generate 201 birds numbered 0-200

def makeImposter():
    for x in range(0, 1):

        # using ETH block number as starting random number seed
        
        b = random.randrange(0,1190029)
        print(b)
        seed(x+b)

        #head color - randomly generate each number in an RGB color
        hd = (randint(0, 256), randint(0, 256), randint(0, 256))


        e = randint(0, 1000)
        seed(e)
        #eye "white" color
        # if random number between 1-1000 is 47 or less - Crazy Eyes!
        if e > 47:
            # normal eyes are always the same color
            jc = (0, 0, 0)
        else:
            # crazy eyes have the same (154, 0, 0) pupil and a random 'eye white' color
            jc = (randint(0, 256), randint(0, 256), randint(0, 256))
            
        



        # background color
        bg = (238, 238, 238)
        # outline color
        ol = (0, 0, 0)

        yl = (255, 255, 102)  # yellow color
        rd = (204, 0, 0)  # red color
        dk = (randint(0, 256), randint(0, 256),
            randint(0, 256))  # goggle color crazy
        ew = (240, 248, 255)  # surrounding pupil color
        ey = (0, 0, 0)  # pupil color
        #jc = (0, 0, 0) #jettpack color
        gc = (179, 217, 255)  # goggle color basic


        # jettpack color
        f = randint(0, 1000)

        if f > 500:
            # if random number is 501-1000 >> grey jettpack
            jc = (152, 152, 152)
        elif 500 >= f > 47:
            # 48-500 >> gold jettpack
            jc = (204, 172, 0)
        elif 47 >= f > 7:
                # 8 >> 47 >> red jettpack
            jc = (204, 0, 0) 
        else:
        # random number is 7 or less >> black jettpack
            jc = (0, 0, 0) 
        

        

        Basic_Imposter = [

            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ol, gc, gc, gc, gc, gc, gc, gc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, ol, gc, gc, gc, gc, gc, gc, gc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, jc, ol, hd, hd, hd, ol, gc, gc, gc, gc, gc, gc, gc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, jc, jc, ol, hd, hd, hd, ol, gc, gc, gc, gc, gc, gc, gc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, jc, jc, ol, hd, hd, hd, ol, gc, gc, gc, gc, gc, gc, gc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, jc, jc, ol, hd, hd, hd, ol, gc, gc, gc, gc, gc, gc, gc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, jc, jc, ol, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, jc, jc, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, jc, jc, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, jc, jc, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, jc, jc, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, jc, jc, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, jc, jc, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ol, ol, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ol, bg, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ol, bg, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ol, bg, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, ol, ol, bg, ol, hd, hd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]

        
        ]  




        l = randint(0,1000)
        type = "will decide"
        if l > 750:
            # shoes
            type = "shoe"

            td = randint(0,1000)
            if td >= 500:
                print("red shoes")
            elif 500 > td >= 100:
                print("blue shoes")
            elif 100 > td >= 25:
                print("green shoes")
            elif 10 > td >= 0:
                print("golden shoes")

        elif 750 >= l > 500:
            # clothes
            type = "cloth"

            td = randint(0,1000)
            if td >= 500:
                print("red shoes")
            elif 500 > td >= 100:
                print("blue shoes")
            elif 100 > td >= 25:
                print("green shoes")
            elif 10 > td >= 0:
                print("golden shoes")

        elif 500 >= l > 250:
            # hat
            type = "hat"

            td = randint(0,1000)
            if td >= 500:
                print("red shoes")
            elif 500 > td >= 100:
                print("blue shoes")
            elif 100 > td >= 25:
                print("green shoes")
            elif 10 > td >= 0:
                print("golden shoes")

        elif 250 >= l:
            # hands    
            type = "hand"

            td = randint(0,1000)
            if td >= 500:
                print("red shoes")
            elif 500 > td >= 100:
                print("blue shoes")
            elif 100 > td >= 25:
                print("green shoes")
            elif 10 > td >= 0:
                print("golden shoes")


        
                     

        g = randint(0,1000)
        pixels = Basic_Imposter
            

        # convert the pixels into an array using numpy
        array = np.array(pixels, dtype=np.uint8)

        # use PIL to create an image from the new array of pixels
        new_image = Image.fromarray(array)
        new_image = new_image.resize(dimensions, resample=0)
        imgname = dirname + '/bird/' + (str(x)) + '.png'
        

        image_file = io.BytesIO()
        
        new_image.save(image_file, format='PNG')
        im = Image.open(image_file)
        imagedata = image_file.getvalue()


        pinataApiKey = "a770d310d147135d5ec4" 
        pinataSecretApiKey = "076b05a1c38c2910d32a8079e1007d52b8c02264990e0af61fa0e544cd760c78"
        url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
        jsonUrl = "https://api.pinata.cloud/pinning/pinJSONToIPFS"

        headers = {
            'pinata_api_key': "a770d310d147135d5ec4",
            'pinata_secret_api_key': "076b05a1c38c2910d32a8079e1007d52b8c02264990e0af61fa0e544cd760c78",
        }

        res = requests.post(url=url,files={'file':imagedata}, headers=headers)

        data = res.json()
        
        return data


@app.route('/')
def home():
    gg = makeImposter()
    res = make_response(jsonify(gg), 200)
    return res


if __name__ == '__main__':
    app.run(debug=True)
