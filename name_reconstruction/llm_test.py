from transformers import pipeline
import sys

def prompt_all(prompt: str, llms: list[str], token_limit: int) -> list:
    responses = []
    for llm in llms:
        pipe = pipeline("text-generation", model=llm, max_new_tokens=token_limit)
        responses.append(pipe(prompt))
    return responses

def prompt_one(prompt: str, llm: str, token_limit: int):
    pipe = pipeline("text-generation", model=llm, max_new_tokens=token_limit)
    return pipe(prompt)

def main():
    if len(sys.argv) != 2:
        print("Please provide a llms file path.")
        exit(1)

    f = open(sys.argv[1], 'r')
    llms = f.read().split()
    f.close()

    # responses = prompt_all("hello world", contents)
    responses = prompt_all("hello world", llms, 200)
    f = open("out.txt", 'w')
    for i in range(len(llms)):
        f.write(f"LLM {i+1}: {llms[i]}\n")
        f.write(f"Response: {responses[i]}")
    f.close()
