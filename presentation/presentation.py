import argparse
import pandas as pd

def main(args):
    pdtb_df = pd.read_csv(args.pcm_input_file, low_memory=False)
    pcm_df = pdtb_df[['Relation', 'Connective_RawText_PCM', 'Conn1_PCM',  'Conn2_PCM','ARG1_RawText_PCM', 'ARG2_RawText_PCM', 'FullRawText_PCM',  'Connective_RawText_PCM']]
    pcm_df.to_csv(args.pcm_output_file)
    en_df = pdtb_df[['Relation', 'Connective_RawText','Conn1',        'Conn2','Arg1_RawText', 'Arg2_RawText', 'FullRawText',  'Connective_RawText']]
    en_df.to_csv(args.en_output_file)
    



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Creating Sample for presentation')
    parser.add_argument("--pcm_input_file", type=str, default = "data/pdtb2_pcm.csv", help="Path to the pidgin PDTB ")
    parser.add_argument("--pcm_output_file", type=str, default="presentation/data/pdtb2_pcm_presentation.csv", help="Path to the output of the presentation file")
    parser.add_argument("--en_output_file", type=str, default="presentation/data/pdtb2_en_presentation.csv", help="Path to the english presentation")
    args = parser.parse_args()
    main(args)