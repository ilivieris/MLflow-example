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
    # Get inputs
    #
    Instance = []
    Instance.append( data.dict()['B11_5']   )
    Instance.append( data.dict()['B12_5']   ) 
    Instance.append( data.dict()['B05_5']   )
    Instance.append( data.dict()['B06_5']   )
    Instance.append( data.dict()['NDVI_5']  )
    Instance.append( data.dict()['NDBI_5']  )
    Instance.append( data.dict()['LSWI2_5'] )
    #
    Instance.append( data.dict()['B11_7']   )
    Instance.append( data.dict()['B12_7']   ) 
    Instance.append( data.dict()['B05_7']   )
    Instance.append( data.dict()['B06_7']   )
    Instance.append( data.dict()['NDVI_7']  )
    Instance.append( data.dict()['NDBI_7']  )
    Instance.append( data.dict()['LSWI2_7'] )    
    #
    Instance.append( data.dict()['B11_9']   )
    Instance.append( data.dict()['B12_9']   ) 
    Instance.append( data.dict()['B05_9']   )
    Instance.append( data.dict()['B06_9']   )
    Instance.append( data.dict()['NDVI_9']  )
    Instance.append( data.dict()['NDBI_9']  )
    Instance.append( data.dict()['LSWI2_9'] )    
    #
    Instance.append( data.dict()['B11_11']   )
    Instance.append( data.dict()['B12_11']   ) 
    Instance.append( data.dict()['B05_11']   )
    Instance.append( data.dict()['B06_11']   )
    Instance.append( data.dict()['NDVI_11']  )
    Instance.append( data.dict()['NDBI_11']  )
    Instance.append( data.dict()['LSWI2_11'] )    
    
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
        pred = model.predict( [Instance] ).tolist()[0]
    except Exception as e:
        raise HTTPException(
            status_code = 404, detail = '[ERROR] ' + str(e).split('] ')[-1].strip()
        )  
    

    return {'Prediction':  args.target_names[pred], 'status': 200}