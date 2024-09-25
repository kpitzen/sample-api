from fastapi.openapi.utils import get_openapi
from sample_api.serve import app
import json

def generate():
    with open("docs/openapi.json", "w") as f:
        f.write(
            json.dumps(
                get_openapi(
                    title="Sample App",
                    version="3.0.0",
                    openapi_version="3.0.0",
                    routes=app.routes
                )
            )
        )
