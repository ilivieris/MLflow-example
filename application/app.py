# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Libraries
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

from   fastapi    import FastAPI
from   fastapi    import HTTPException
#
from   pydantic import BaseModel
import mlflow
#
import pickle
import pandas as pd


app = FastAPI(title = 'Irrigation prediction model')

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Parameters
#
class Parameters():
    def __init__( self ):
        self.model_name = "Irrigation prediction model"
        self.model_file = './model.pkl'
        self.version    = "v1.0"
        self.author     = "Ioannis E. Livieris"

        self.target_names = ['Irrigated', 'Drainaged']
args = Parameters()


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Creating a class for the attributes input to the ML model.
#
class Inputs( BaseModel ):
    B11_5:    float = None
    B12_5:    float = None
    B05_5:    float = None
    B06_5:    float = None
    NDVI_5:   float = None
    NDBI_5:   float = None
    LSWI2_5:  float = None
    #
    B11_7:    float = None
    B12_7:    float = None
    B05_7:    float = None
    B06_7:    float = None
    NDVI_7:   float = None
    NDBI_7:   float = None
    LSWI2_7:  float = None
    #
    B11_9:    float = None
    B12_9:    float = None    
    B05_9:    float = None
    B06_9:    float = None
    NDVI_9:   float = None
    NDBI_9:   float = None    
    LSWI2_9:  float = None  
    #
    B11_11:   float = None
    B12_11:   float = None
    B05_11:   float = None
    B06_11:   float = None    
    NDVI_11:  float = None   
    NDBI_11:  float = None
    LSWI2_11: float = None   

{
  "detail": "[ERROR] training data did not have the following fields: B11_5, B12_5, B05_5, B06_5, NDVI_5, NDBI_5, LSWI2_5, B11_7, B12_7, B05_7, B06_7, NDVI_7, NDBI_7, LSWI2_7, B11_9, B12_9, B05_9, B06_9, NDVI_9, NDBI_9, LSWI2_9, B11_11, B12_11, B05_11, B06_11, NDVI_11, NDBI_11, LSWI2_11"
}

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# # Loading the trained model
#
def loadModel():
    
    model = pickle.load(open(args.model_file, 'rb'))
    print('[INFO] Prediction model is loaded')

    return model




# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Methods
#
@app.get("/")
async def main():
    '''
    Base
    '''
    return {'msg': 'Hello World', 'status': 200,}


@app.get("/info")
async def info():
    """Returns model information, version and author"""
    result = dict()

    result['name']    = args.model_name
    result['version'] = args.version
    result['author']  = args.author
    result['status']  = 200

    return result


@app.post('/predict' )
async def get_model_response(data: Inputs):
    '''
    Returns models prediction on input data
    '''
    print( type(data) )
    print( data )

    # Get inputs
    #
    try:
        Instance = {}
        #
        Instance['B11_5']    = [ data.dict()['B11_5']   ]
        Instance['B12_5']    = [ data.dict()['B12_5']   ]
        Instance['B05_5']    = [ data.dict()['B05_5']   ]
        Instance['B06_5']    = [ data.dict()['B06_5']   ]
        Instance['NDVI_5']   = [ data.dict()['NDVI_5']  ]
        Instance['NDBI_5']   = [ data.dict()['NDBI_5']  ]
        Instance['LSWI2_5']  = [ data.dict()['LSWI2_5'] ]
         #
        Instance['B11_7']    = [ data.dict()['B11_7']   ]
        Instance['B12_7']    = [ data.dict()['B12_7']   ]
        Instance['B05_7']    = [ data.dict()['B05_7']   ]
        Instance['B06_7']    = [ data.dict()['B06_7']   ]
        Instance['NDVI_7']   = [ data.dict()['NDVI_7']  ]
        Instance['NDBI_7']   = [ data.dict()['NDBI_7']  ]
        Instance['LSWI2_7']  = [ data.dict()['LSWI2_7'] ]
        #
        Instance['B11_9']    = [ data.dict()['B11_9']   ]
        Instance['B12_9']    = [ data.dict()['B12_9']   ]
        Instance['B05_9']    = [ data.dict()['B05_9']   ]
        Instance['B06_9']    = [ data.dict()['B06_9']   ]
        Instance['NDVI_9']   = [ data.dict()['NDVI_9']  ]
        Instance['NDBI_9']   = [ data.dict()['NDBI_9']  ]
        Instance['LSWI2_9']  = [ data.dict()['LSWI2_9'] ]
        #
        Instance['B11_11']    = [ data.dict()['B11_11']   ]
        Instance['B12_11']    = [ data.dict()['B12_11']   ]
        Instance['B05_11']    = [ data.dict()['B05_11']   ]
        Instance['B06_11']    = [ data.dict()['B06_11']   ]
        Instance['NDVI_11']   = [ data.dict()['NDVI_11']  ]
        Instance['NDBI_11']   = [ data.dict()['NDBI_11']  ]
        Instance['LSWI2_11']  = [ data.dict()['LSWI2_11'] ]
    except Exception as e:
        raise HTTPException(
            status_code = 404, detail = '[ERROR] ' + str(e).split('] ')[-1].strip()
        )  

    # Load model
    #
    try:
        model = loadModel()
    except Exception as e:
        raise HTTPException(
            status_code = 404, detail = '[ERROR] ' + str(e).split('] ')[-1].strip()
        )  
    
    # Load model
    #
    try:
        pred = model.predict( pd.DataFrame(Instance) )[0]
    except Exception as e:
        raise HTTPException(
            status_code = 404, detail = '[ERROR] ' + str(e).split('] ')[-1].strip()
        )  
    

    return {'Prediction':  args.target_names[pred], 'status': 200}