from fastapi import APIRouter
from app.util.log_util import setup_logger
from .deepface_controller import DeepfaceController
from .domain import DeepfaceRequestCriteria


router = APIRouter()
logger = setup_logger('deepface_init')
@router.post('/search-deepface')
def process(criteria: DeepfaceRequestCriteria):
    controller = DeepfaceController()
    logger.debug('deepface init')
    return controller.process(criteria)