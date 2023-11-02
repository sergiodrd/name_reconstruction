from transformers import pipeline
import sys

def prompt_all(prompt: str, llms: list[str], token_limit: int, file, f = id) -> list:
    responses = []
    for llm in llms:
        try:
            pipe = pipeline("text-generation", model=llm, max_new_tokens=token_limit)
            res = pipe(prompt)
            responses.append(res)
            f(res, file)
        except Exception:
            pass
    return responses

def prompt_one(prompt: str, llm: str, token_limit: int):
    try:
        pipe = pipeline("text-generation", model=llm, max_new_tokens=token_limit)
        return pipe(prompt)
    except Exception:
        pass

def output_response(r, file):
    file.write(r)

def main():
    if len(sys.argv) != 2:
        print("Please provide a llms file path.")
        exit(1)

    f = open(sys.argv[1], 'r')
    llms = f.read().split()
    f.close()

    f = open("out.txt", 'a')
    _ = prompt_all("hello world", llms, 200, f, output_response)
    f.close()
