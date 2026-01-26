# import sys
# import os

# import certifi
# ca = certifi.where()

# from dotenv import load_dotenv
# load_dotenv()
# mongo_db_url = os.getenv("MONGODB_URL_KEY")


# print(mongo_db_url)

# import pymongo
# from networksecurity.exception.exception import NetworkSecurityException
# from networksecurity.logging.logger import logging
# from networksecurity.pipeline.training_pipeline import TrainingPipeline


# from fastapi.middleware.cors import CORSMiddleware
# from fastapi import FastAPI, File, UploadFile,Request
# from uvicorn import run as app_run
# from fastapi.responses import Response
# from starlette.responses import RedirectResponse
# import pandas as pd

# from networksecurity.utils.main_utils.utils import load_object

# from networksecurity.utils.ml_utils.model.estimator import NetworkModel



# client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

# from networksecurity.constant.training_pipeline import DATA_INGESTION_COLLECTION_NAME
# from networksecurity.constant.training_pipeline import DATA_INGESTION_DATABASE_NAME

# database = client[DATA_INGESTION_DATABASE_NAME]
# collection = database[DATA_INGESTION_COLLECTION_NAME]


# app = FastAPI()
# origins = ["*"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# from fastapi.templating import Jinja2Templates
# templates = Jinja2Templates(directory="./templates")

# @app.get("/", tags=["authentication"])
# async def index():
#     return RedirectResponse(url="/docs")


# @app.get("/train")
# async def train_route():
#     try:
#         train_pipeline=TrainingPipeline()
#         train_pipeline.run_pipeline()
#         return Response("Training is successful")
#     except Exception as e:
#         raise NetworkSecurityException(e,sys)
    
# @app.post("/predict")
# async def predict_route(request: Request,file: UploadFile = File(...)):
#     try:
#         df=pd.read_csv(file.file)

#         #print(df)
#         preprocesor=load_object("final_model/preprocessor.pkl")
#         final_model=load_object("final_model/model.pkl")
#         network_model = NetworkModel(preprocessor=preprocesor,model=final_model)
#         print(df.iloc[0])
#         y_pred = network_model.predict(df)
#         print(y_pred)
#         df['predicted_column'] = y_pred
#         print(df['predicted_column'])
#         #df['predicted_column'].replace(-1, 0)
#         #return df.to_json()
#         df.to_csv('prediction_output/output.csv')
#         table_html = df.to_html(classes='table table-striped')
#         #print(table_html)
#         return templates.TemplateResponse("table.html", {"request": request, "table": table_html})
        
#     except Exception as e:
#             raise NetworkSecurityException(e,sys)


# if __name__=="__main__":
#     app_run(app,host="0.0.0.0",port=8000)


import sys
import os
from pathlib import Path

import certifi
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import Response
from starlette.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import pymongo

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.pipeline.training_pipeline import TrainingPipeline
from networksecurity.utils.main_utils.utils import load_object
from networksecurity.utils.ml_utils.model.estimator import NetworkModel
from networksecurity.constant.training_pipeline import (
    DATA_INGESTION_COLLECTION_NAME,
    DATA_INGESTION_DATABASE_NAME,
)

# ------------------------
# ENV SETUP
# ------------------------

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

if not MONGO_DB_URL:
    raise RuntimeError("MONGO_DB_URL environment variable not set")

ca = certifi.where()

client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)


database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]

BASE_DIR = Path(__file__).resolve().parent

MODEL_DIR = BASE_DIR / "final_model"
PREDICTION_DIR = BASE_DIR / "prediction_output"
PREDICTION_DIR.mkdir(exist_ok=True)

# ------------------------
# FASTAPI APP
# ------------------------

app = FastAPI(title="Network Security ML API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", tags=["root"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train", tags=["training"])
async def train_route():
    try:
        pipeline = TrainingPipeline()
        pipeline.run_pipeline()
        return Response("Training completed successfully ✅")
    except Exception as e:
        raise NetworkSecurityException(e, sys)


@app.post("/predict", tags=["prediction"])
async def predict_route(
    request: Request,
    file: UploadFile = File(...)
):
    try:
        df = pd.read_csv(file.file)

        preprocessor = load_object(MODEL_DIR / "preprocessor.pkl")
        model = load_object(MODEL_DIR / "model.pkl")

        network_model = NetworkModel(
            preprocessor=preprocessor,
            model=model,
        )

        predictions = network_model.predict(df)

        df["prediction"] = predictions

        output_path = PREDICTION_DIR / "output.csv"
        df.to_csv(output_path, index=False)

        table_html = df.to_html(classes="table table-striped")

        return templates.TemplateResponse(
            "table.html",
            {"request": request, "table": table_html},
        )

    except Exception as e:
        raise NetworkSecurityException(e, sys)
