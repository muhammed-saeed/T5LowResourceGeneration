python /home/CE/musaeed/BMGF-RoBERTa/src/preprocess_pdtb.py \
    --csv_file_path /local/musaeed/pdtb2_pidgin_copy.csv \
    --types Implicit \
    --encoder roberta \
    --dataset_file_path /home/CE/musaeed/BMGF-RoBERTa/processed_data/pidgin/train_implicit_roberta.pt \
    --sections 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20

python /home/CE/musaeed/BMGF-RoBERTa/src/preprocess_pdtb.py \
    --csv_file_path /local/musaeed/pdtb2_pidgin_copy.csv \
    --types Implicit \
    --encoder roberta \
    --dataset_file_path /home/CE/musaeed/BMGF-RoBERTa/processed_data/pidgin/valid_implicit_roberta.pt \
    --sections 0,1


python /home/CE/musaeed/BMGF-RoBERTa/src/preprocess_pdtb.py \
    --csv_file_path /local/musaeed/pdtb2_pidgin_copy.csv \
    --types Implicit \
    --encoder roberta \
    --dataset_file_path /home/CE/musaeed/BMGF-RoBERTa/processed_data/pidgin/test_implicit_roberta.pt \
    --sections 21,22


