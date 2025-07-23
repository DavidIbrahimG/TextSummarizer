import os
from src.textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e