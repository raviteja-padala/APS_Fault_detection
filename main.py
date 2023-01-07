
from sensor.logger import logging
from sensor.exception import SensorException
import sys,os

def test_logger_and_exception():
     try:
          logging.info("Starting test_logger_and_exception")
          result = 3/0
          print(result)
          logging.info("Starting test_logger_and_exception")
     except Exception as e:
          logging.debug(("Stopping the test logger and excetion"))
          raise SensorException(e, sys)


if __name__=="__main__":
     try:
          test_logger_and_exception()
     except Exception as e:
          print(e)