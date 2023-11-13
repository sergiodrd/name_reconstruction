# Name Reconstruction

## Description

This project utilizes two scripts, `llm_test` and `parse_names`, to analyze C
files and generate responses using language models.

### llm_test

The `llm_test` script parses C files and extracts information about functions 
and variables. It uses the pycparser library to create an Abstract Syntax Tree
(AST) of the C code and then prints relevant details such as function names,
arguments, and variables.

#### Usage

```bash
poetry run llm_test <path_to_c_file>
```

### parse_names

The `parse_names` script generates responses using language models (LLMs) based
on a prompt. It uses the transformers library to interact with text generation
models. Multiple LLMs can be specified in a file, and the script generates 
responses for each.

#### Usage

```bash
poetry run parse_names <path_to_llms_file>
```

## Getting Started

1. Clone the repository.

2. Install dependencies using Poetry:

 ```bash
 poetry install
 ```

3. Run `llm_test` on a C file:

 ```bash
 poetry run llm_test <path_to_c_file>
 ```

4. Run `parse_names` on a file containing LLMs:

 ```bash
 poetry run parse_names <path_to_llms_file>
 ```

## Dependencies
- pycparser
- transformers (with pytorch and tensorflow)
