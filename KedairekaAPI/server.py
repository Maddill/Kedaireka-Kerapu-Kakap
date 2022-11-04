from fastapi import FastAPI
from fastapi import UploadFile, File
import uvicorn
from os import path

from segmentation import instance_image, read_image


app = FastAPI()

@app.get('/index')
def hello_world():
    return "Hello World"


@app.post('/api/instance')
def segment_image(file: UploadFile = File(...)):
    
    #read the file
    image = read_image(file)

    #make a instance segmentation
    predictions = instance_image(image)
    print(predictions)
    return predictions

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='0.0.0.0')
