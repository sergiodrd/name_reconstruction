from sys import argv
from transformers import AutoTokenizer
import os

if len(argv) != 3: exit()
llm = argv[1]
prompt = open(argv[2], "r").read()

tokenizer = AutoTokenizer.from_pretrained(llm, padding_side="left")
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained(llm, device_map="auto", load_in_4bit=True)
model_inputs = tokenizer([prompt], return_tensors="pt").to("cuda")
generated_ids = model.generate(**model_inputs, max_new_tokens=200)

print(tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0])
