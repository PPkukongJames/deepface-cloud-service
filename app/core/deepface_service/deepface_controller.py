from app.util.log_util import setup_logger
from .deepface_manager import DeepfaceManager
from .domain import DeepfaceRequestCriteria
from fastapi import Response
import json

LOGGER = setup_logger('deepfac_controller')
class DeepfaceController :
    manager = None
    logger = None
    
    def __init__(self):
        self.logger = LOGGER
        self.manager = DeepfaceManager()
        
    def process(self,criteria:DeepfaceRequestCriteria) :
        self.logger.debug("deepface controller")
        
        response = None
        try :
            results = self.manager.process(criteria)
            self.logger.debug(results)
            response = Response(
                content=json.dumps(results),
                status_code=200,
                media_type='application/json'
            )
        except KeyError as e:
            error_message = {'message': str(e)}
            response = Response(
                content=json.dumps(error_message),
                status_code=400,
                media_type='application/json'
            )
        except Exception as e:
            # Handle all other exceptions
            error_message = {'message': str(e)}
            response = Response(
                content=json.dumps(error_message),
                status_code=500,
                media_type='application/json'
            )
            self.logger.error('Exception occurred', exc_info=True)

        return response