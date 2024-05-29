from sys import argv
from transformers import AutoTokenizer
import os
import json
os.environ['HF_HOME'] = '.cache/transformers/'

f = open(argv[1], "r")
prompt_json = json.load(f)
out_json = prompt_json
f.close()
llms = argv[2:]

for i, obj in enumerate(prompt_json):
    for llm in llms:
        tokenizer = AutoTokenizer.from_pretrained(llm, padding_side="left")
        from transformers import AutoModelForCausalLM

        model = AutoModelForCausalLM.from_pretrained(llm, device_map="auto", load_in_4bit=True)
        model_inputs = tokenizer([obj["prompt"]], return_tensors="pt").to("cuda")
        generated_ids = model.generate(**model_inputs, max_new_tokens=200)

        out_json[i]["output"] = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        f = open("output.json", "w")
        json.dump(out_json, f)
        f.close()
        print(out_json[i]["output"])
