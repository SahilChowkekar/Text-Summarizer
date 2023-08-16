from src.textsummarization.config.configuration import ConfigurationManager
from src.textsummarization.components.data_transformation import DataTransformation
from src.textsummarization.logging import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()