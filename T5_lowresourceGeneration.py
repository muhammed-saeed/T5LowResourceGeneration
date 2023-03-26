from transformers import T5Tokenizer, T5ForConditionalGeneration, TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments

# 1. Gather a large corpus of text in the new language
corpus_file = "/local/musaeed/ROBERTA-base-en/Mono_lingual_data/pcm_entire_mono.txt"

# 2. Preprocess the text by cleaning and tokenizing it
tokenizer = T5Tokenizer.from_pretrained("t5-small")
max_length = 512

# 3. Convert the preprocessed text into a format suitable for T5 pretraining
dataset = TextDataset(tokenizer=tokenizer, file_path=corpus_file, block_size=max_length)

# 4. Train the T5 model on the preprocessed data
model = T5ForConditionalGeneration.from_pretrained("t5-small")
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)


data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
training_args = TrainingArguments(
    output_dir="/local/musaeed/new_language_t5_pretraining",
    num_train_epochs=10,
    per_device_train_batch_size=4,
    logging_steps=100,
    save_steps=5000,
    learning_rate=3e-4,
    report_to="wandb",
    run_name="T5 for LowResource"
)
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    data_collator=data_collator
)
trainer.train()
