
import os
import logging
import sacrebleu
import pandas as pd
from utils import get_all_files, writelines, folderchecker

from simpletransformers.t5 import T5Model, T5Args



logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)


model_args = T5Args()
model_args.max_length = 512
model_args.length_penalty = 1
model_args.num_beams = 10
model_args.evaluation_batch_size=32


model_output_dir="/local/musaeed/BESTT5TranslationModel"
model = T5Model("t5", model_output_dir, args=model_args, use_cuda=False)

 
english_folder_path = "pdtb3Data/rawText/raw"
# Get all folders path inside a main folder
folder_names = [name for name in os.listdir(english_folder_path) if os.path.isdir(os.path.join(english_folder_path, name))]
print(folder_names)
pidgin_parallel_path = "/local/musaeed/NaijaDiscourseClassification/pdtb3Data/rawText/pidgin"

encoding = "latin-1"


# Iterate over each file path and read the contents
for folder_path in folder_names:  
    # Get all file paths inside the folder and its subfolders
    file_paths = get_all_files(os.path.join(english_folder_path,folder_path))
    for file_path in file_paths:
        print(f"currently working with file {file_path}")
        with open(file_path, 'r', encoding= encoding) as file:
            lines = file.readlines()

        # Remove empty lines from the content
        english_non_empty_lines = [line for line in lines if line.strip()]

        pcm_preds = model.predict(english_non_empty_lines)

        folder_list = file_path.split("/")[-5:] 
        
        print(f'the file path split is {file_path.split("/")[-5:]}')
        pcm_folder_path = folderchecker(pidgin_parallel_path, folder_list)

        print(f"file name is {pcm_folder_path}")
        writelines(pcm_folder_path, pcm_preds)


