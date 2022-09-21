<p align="center">
<img src=".\images\MLFlow.png" width = "300" alt="" align=left/>
</p>

<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />

# MLFlow-project

This is a custom project, which aims to demonstrate an end-to-end machine learning project using MLFlow, XGBoost, Docker & FastAPI. The hyperparameter optimization is performed using Sequental Optimization.

Additionally, the best model is locally deployed
- using FastAPI & Docker
- using MLFlow serving

For creating the optimized prediction model run ```01. Model development.ipynb```

**Notice:** That for tracking the experiments launch ``$ mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 0.0.0.0 --port 5000``
<br />
<br />

---
## Table of Contents

- [Data](#data)
- [Deployment using FastAPI & Docker](#deployment-using-fastapi--docker)
- [Deployment using MLFlow serving](#mlflow-serving-model)
- [Versions](#versions)
- [Contact](#mailbox-contact)
<br />
<br />


---
## Data

The dataset is splited in train/test and contains spectral bands for the Sentinel-2.

```
Data
|── Irrigation_train.csv
└── Irrigation_test.csv
```

<br />
<br />



---
## Deployment using FastAPI & Docker

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

<br />

**Main page**

<p align="center">
<img src=".\images\image1.png" width = "800" alt="" align=center />
</p>

<br />

**Use predict**

<p align="center">
<img src=".\images\image2.png" width = "800" alt="" align=center />
</p>


<br />
<br />

---
## MLFlow serving model

1. Launch ```$ mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 0.0.0.0 --port 5000```

2. Got to http://0.0.0.0:5000

3. Pick the best model, register with Model Registry as ```Irrigation_Model```

4. Choose second best model and create version 2 in the Model Registry
    - Transition the best model into Production
    - Transition the second best model into Staging

5. Open and run ```MLFlow serving model.ipynb```

**Notice**
- Set environment variable for the tracking URL where the Model Registry resides
```
export MLFLOW_TRACKING_URI=http://0.0.0.0:5000
```

- Serve the production model from the model registry
```
mlflow models serve -m "models:/Irrigation_model/Production" --no-conda --port 1983
```
<br />
<br />



---
## Versions 

- Version 2.1
    - Model deployment using MLFlow serving
- Version 2
    - Deployment using FastAPI
- Version 1
    - Add data
    - Model development
<br />
<br />

---
## :mailbox: Contact

Ioannis E. Livieris (livieris@gmail.com)