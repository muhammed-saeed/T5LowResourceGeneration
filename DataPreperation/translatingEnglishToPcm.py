import argparse
import pandas as pd
import os
import logging
import sacrebleu
import pandas as pd
import random 
import argparse
from simpletransformers.t5 import T5Model, T5Args
import torch

def main(args):
    torch.manual_seed(0)
    random.seed(0)

    logging.basicConfig(level=logging.INFO)
    transformers_logger = logging.getLogger("transformers")
    transformers_logger.setLevel(logging.WARNING)

    model_args = T5Args()
    model_args.max_length = 128
    model_args.length_penalty = 1
    model_args.num_beams = 5
    model_args.eval_batch_size = 32

    model = T5Model("t5", args.model_path, args=model_args)

    eval_df = pd.read_csv(args.pdtb, sep="\t").astype(str)

    
    en2pcm = "translate english to pcm: "
    to_pcm_ = [en2pcm + s for s in to_pcm]
    pcm_preds = model.predict(to_pcm_)




if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Translate the English pdtb to pidgin")
    parser.add_argument("--model_path", type=str, default="../BESTT5TranslationModel")
    parser.add_argument("--pdtb_english_path", type=str, default="data/pdtb2.csv")
    parser.add_argument("--pdtb_pcm", type=str, default='data/pdtb2_pcm.csv')

    args = parser.parse_args()
    main(args)
