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

    FULLTEXT  = pdtb_df["FullRawText"].tolist()
    FullText_to_preds = [en2pcm + s for s in FULLTEXT]
    print(f"{FullText_to_preds[:5]}")

    ARG1 = pdtb_df["Arg1_RawText"].tolist()
    ARG1_to_preds = [en2pcm + s for s in ARG1]
    print(f"{ARG1_to_preds[:5]}")

    ARG2 = pdtb_df["Arg2_RawText"].tolist()
    ARG2_to_preds = [en2pcm + s for s in ARG2]
    print(f"{ARG2_to_preds[:5]}")

    connective_raw_text = pdtb_df['Connective_RawText'].tolist()
    connective_to_pred = [en2pcm + str(s) for s in connective_raw_text]
    print(f"{connective_to_pred[:5]}")

    
    
    
    ARG1_pcm_preds = model.predict(ARG1_to_preds)
    pdtb_df["ARG1_RawText_PCM"] = ARG1_pcm_preds
    pdtb_df.to_csv("data/sample/arg1_raw_text_pcm.csv")

    ARG2_pcm_preds = model.predict(ARG2_to_preds)
    pdtb_df["ARG2_RawText_PCM"] = ARG2_pcm_preds
    pdtb_df.to_csv("data/sample/arg2_raw_text_pcm.csv")


    FullRawText_pcm_preds = model.predict(FullText_to_preds)
    pdtb_df["FullRawText_PCM"] = FullRawText_pcm_preds
    pdtb_df.to_csv("data/sample/full_text_pcm.csv")


    # ConnectiveFullText_pcm_preds = model.predict(connective_to_pred)
    
    # pdtb_df["Connective_RawText"] = ConnectiveFullText_pcm_preds
    # pdtb_df.to_csv("data/sample/connective_RawText.csv")
    conn1_values = pdtb_df.loc[pd.notnull(pdtb_df['Conn1']), 'Conn1'].tolist()
    conn2_values = pdtb_df.loc[pd.notnull(pdtb_df['Conn2']), 'Conn2'].tolist()
    connective_rawtext_values = pdtb_df.loc[pd.notnull(pdtb_df['Connective_RawText']), 'Connective_RawText'].tolist()

    # Perform the translation for each non-null value
    conn1_translations = [en2pcm + s for s in conn1_values]
    conn2_translations = [en2pcm + s for s in conn2_values]
    connective_rawtext_translations = [en2pcm + s for s in connective_rawtext_values]

    translation_conn1 = model.predict(conn1_translations)
    pdtb_df["Conn1_PCM"] = pdtb_df["Conn1"].copy()
    pdtb_df.loc[pd.notnull(pdtb_df['Conn1_PCM']), 'Conn1'] = translation_conn1
    pdtb_df.to_csv("data/pcmExplicitConnectives/explicit_df/conn1_pcm.csv")

    translation_conn2 = model.predict(conn2_translations)
    pdtb_df['Conn2_PCM'] = pdtb_df['Conn2'].copy()
    pdtb_df.loc[pd.notnull(pdtb_df['Conn2_PCM']), 'Conn2'] = translation_conn2
    pdtb_df.to_csv("data/pcmExplicitConnectives/explicit_df/conn2_pcm.csv")

    translation_raw_text = model.predict(connective_rawtext_translations)
    pdtb_df['Connective_RawText_PCM'] = pdtb_df["Connective_RawText"].copy()
    pdtb_df.loc[pd.notnull(pdtb_df['Connective_RawText']), 'Connective_RawText'] = translation_raw_text
    pdtb_df.to_csv("data/pcmExplicitConnectives/explicit_df/connectivefullText_pcm.csv")
 
    pdtb_df.to_csv(argss.pdtb_pcm)
    



if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Translate the English pdtb to pidgin")
    parser.add_argument("--model_path", type=str, default="/local/musaeed/BESTT5TranslationModel")
    parser.add_argument("--pdtb_english_path", type=str, default="data/pdtb2.csv")
    parser.add_argument("--pdtb_pcm", type=str, default='data/pdtb2_pcm.csv')

    args = parser.parse_args()
    main(args)
