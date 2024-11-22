from app.util.log_util import setup_logger
from .domain import DeepfaceRequestCriteria
from deepface import DeepFace
import os

LOGGER = setup_logger('deepface_service')
DB_PATH = os.path.join('resource', 'pictures')
class DeepfaceService :
    
    logger = None
    
    def __init__(self):
        self.logger = LOGGER
        
    def fine_img(self,img_np) :
        self.logger.debug("deepface service")
        dfs = DeepFace.find(
            img_path = img_np, 
            db_path = DB_PATH, 
            detector_backend = 'yolov8',
            model_name='Facenet512',
            enforce_detection=False
        )
        self.logger.debug(dfs)
        res = {}
        if len(dfs[0]) != 0 :
            
            temp = dfs[0]['identity'][0].replace('\\','/').split('/')
            res = {
                'match': True,
                'deepface':{
                    'id': temp[-2],
                    'filename': temp[-1]
                }
                
            }
        else :
            res = {
                'match': False,
                'deepface':{}
            }
        
        return res