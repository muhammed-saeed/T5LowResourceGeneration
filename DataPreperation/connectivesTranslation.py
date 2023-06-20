import argparse
import pandas as pd
import os
import numpy as np
import logging
import sacrebleu
import pandas as pd
import random 
import argparse
from simpletransformers.t5 import T5Model, T5Args
import torch

def main(argss):
    torch.manual_seed(0)
    random.seed(0)

    logging.basicConfig(level=logging.INFO)
    transformers_logger = logging.getLogger("transformers")
    transformers_logger.setLevel(logging.WARNING)

    model_args = T5Args()
    model_args.max_length = 128
    model_args.length_penalty = 1
    model_args.num_beams = 10
    model_args.n_gpu = 1
    model_args.eval_batch_size = 32

    model = T5Model("t5", argss.model_path, args=model_args)

    pdtb_df = pd.read_csv(argss.pdtb_english_path, low_memory=False)


    en2pcm = "translate english to pcm: "
    

    conn1_values = pdtb_df.loc[pd.notnull(pdtb_df['Conn1']), 'Conn1'].tolist()
    conn2_values = pdtb_df.loc[pd.notnull(pdtb_df['Conn2']), 'Conn2'].tolist()
    connective_rawtext_values = pdtb_df.loc[pd.notnull(pdtb_df['Connective_RawText']), 'Connective_RawText'].tolist()



    
    # Perform the translation for each non-null value
    pdtb_df['Conn1_PCM']  = pdtb_df['Conn1']
    conn1_translations = [en2pcm + s for s in conn1_values]
    conn2_translations = [en2pcm + s for s in conn2_values]
    connective_rawtext_translations = [en2pcm + s for s in connective_rawtext_values]


    pdtb_df['Conn2_PCM'] = pdtb_df['Conn2'].copy()
    translation_conn2 = model.predict(conn2_translations)
    pdtb_df.loc[pd.notnull(pdtb_df['Conn2_PCM']), 'Conn2'] = translation_conn2
    pdtb_df.to_csv("data/pcmExplicitConnectives/explicit_df/conn2.csv")


    translation_conn1 = model.predict(conn1_translations)
    pdtb_df.loc[pd.notnull(pdtb_df['Conn1']), 'Conn1'] = translation_conn1
    pdtb_df.to_csv("data/pcmExplicitConnectives/explicit_df/conn1.csv")

    
    pdtb_df['Connective_RawText_PCM'] = pdtb_df['Connective_RawText'].copy()
    translation_raw_text = model.predict(connective_rawtext_translations)
    pdtb_df.loc[pd.notnull(pdtb_df['Connective_RawText_PCM']), 'Connective_RawText'] = translation_raw_text
    pdtb_df.to_csv("data/pcmExplicitConnectives/explicit_df/connectivefullText.csv")
    # Update the DataFrame with the translated values
    
    
    


if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Translate the English pdtb to pidgin")
    parser.add_argument("--model_path", type=str, default="/local/musaeed/BESTT5TranslationModel")
    parser.add_argument("--pdtb_english_path", type=str, default="data/pdtb2.csv")
    parser.add_argument("--pdtb_pcm", type=str, default='data/pdtb2_pcm_connectives.csv')

    args = parser.parse_args()
    main(args)


