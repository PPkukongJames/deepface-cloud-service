from app.util.log_util import setup_logger
from .deepface_service import DeepfaceService
from .domain import DeepfaceRequestCriteria
import numpy as np
from io import BytesIO
import base64
from PIL import Image
import os

LOGGER = setup_logger('deepfac_manager')
DB_PATH = os.path.join('resource', 'pictures')

class DeepfaceManager :
    manager = None
    logger = None
    
    def __init__(self):
        self.logger = LOGGER
        self.service = DeepfaceService()
        
    def process(self,criteria:DeepfaceRequestCriteria):
        self.logger.debug("deepface manager")
        binary_data = base64.b64decode(criteria.picture)
        img = Image.open(BytesIO(binary_data))  # ใช้ BytesIO เพื่อสร้าง stream จาก byte
        img_np = np.array(img)
        res = self.service.fine_img(img_np)
        
        if res['match'] :
            with open(os.path.join(DB_PATH,res['deepface']['id'],res['deepface']['filename']), 'rb') as f:
                byte_data = f.read()
            res['deepface']['img'] = base64.b64encode(byte_data).decode('utf-8')
            
        return res