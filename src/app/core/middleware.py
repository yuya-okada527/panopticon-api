from core.config import CORE_SETTINGS
from fastapi.middleware.cors import CORSMiddleware

CORS = {
    "middleware_class": CORSMiddleware,
    "allow_origins": CORE_SETTINGS.fe_domain.split(","),
    "allow_methods": ["*"],
    "allow_headers": ["*"],
    "expose_headers": [],
}
