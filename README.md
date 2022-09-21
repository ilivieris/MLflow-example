# MLFlow-project

This is a custom project, which aims to demonstrate an end-to-end machine learning project using MLFlow, XGBoost, Docker & FastAPI
<br />
<br />

---
## Table of Contents

- [Data](#data)
- [How to run](#how-to-run)
- [Versions](#versions)
- [Contact](#mailbox-contact)
<br />
<br />


---
## Data

The dataset is splited in train/test and contains spectral bands for the Sentinel-2.
<br />
<br />



---
## How to run

For creating/training the prediction model, run
'''
    Model development.ipynb
'''

We can use the Dockerfile to create an image for running our web application inside a container
```
$ docker build --pull --rm -f "Dockerfile" -t mlflowproject:latest "."
```
And now we can test our application using Docker
```
$ docker run -p 8000:8000 mlflowproject
```

To check your application
```
# curl -X GET http://0.0.0.0:8000/
# curl -X GET http://0.0.0.0:8000/info
# curl -X 'POST' 'http://0.0.0.0:8000/predict' -H 'accept: application/json' -H 'Content-Type: application/json' \
  -d '{
  "B11_5": 0.21,
  "B12_5": 0.32,
  "B05_5": 0.123,
  "B06_5": 0.141,
  "NDVI_5": 0.131,
  "NDBI_5": 0.123,
  "LSWI2_5": 0.456,
  "B11_7": 0.456,
  "B12_7": 0.345,
  "B05_7": 0.687,
  "B06_7": 0.234,
  "NDVI_7": 0.012,
  "NDBI_7": 0.123,
  "LSWI2_7": 0.415,
  "B11_9": 0.513,
  "B12_9": 0.561,
  "B05_9": 0.941,
  "B06_9": 0.151,
  "NDVI_9": 0.614,
  "NDBI_9": 0.726,
  "LSWI2_9": 0.724,
  "B11_11": 0.161,
  "B12_11": 0.614,
  "B05_11": 0.613,
  "B06_11": 0.417,
  "NDVI_11": 0.745,
  "NDBI_11": 0.978,
  "LSWI2_11": 0.666
   }'
```

### View on http://0.0.0.0:8000/docs

If you’ve successfully reached until here, you should have your image classifier API up and running on http://0.0.0.0:8000/docs/ and should have a similar looking page!

#### Main page

<p align="center">
<img src=".\images\image1.png" width = "800" alt="" align=center />
</p>

#### Use /predict

<p align="center">
<img src=".\images\image2.png" width = "800" alt="" align=center />
</p>


<br />
<br />



---
## Versions 

- Version 2
    - Deployment
- Version 1
    - Add data
    - Model development
<br />
<br />

---
## :mailbox: Contact

Ioannis E. Livieris (livieris@gmail.com)