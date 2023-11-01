from transformers import pipeline
import sys

def prompt_all(prompt: str, llms: list[str]) -> list:
    responses = []
    for llm in llms:
        pipe = pipeline("text-generation", model=llm)
        responses.append(pipe(prompt))
    return responses

def prompt_one(prompt: str, llm: str):
    pipe = pipeline("text-generation", model=llm)
    return pipe(prompt)

def main():
    if len(sys.argv) != 2:
        print("Please provide a llms file path.")
        exit(1)

    f = open(sys.argv[1], 'r')
    contents = f.read().split()
    f.close()

    # responses = prompt_all("hello world", contents)
    responses = prompt_one("hello world", contents[0])
    print(responses)
