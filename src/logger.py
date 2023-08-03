import os
import logging 
from datetime import datetime
log_filename = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(),'logs')
os.makedirs(logs_path,exist_ok=True)
log_filepath = os.path.join(logs_path,logs_filename)
logging.basicConfig(filename=log_filepath,format="%(asctime)s-%(lineno)d-%(levelname)s-%(message)s",level=logging.INFO)

                                          








































# from src.exception import CustomException 


# import logging 
# import os
# from datetime import datetime

# LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# logs_path=os.path.join(os.getcwd(),"logs")
# os.makedirs(logs_path,exist_ok=True)

# LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO
# )

