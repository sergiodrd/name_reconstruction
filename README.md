# Name Reconstruction

## Description

This repository contains multiple tests and components to support a research 
project about variable name reconstruction for decompilers. For more information,
see documents.

## Repository structure

- `name_reconstruction/`

This subdirectory corresponds to the python files that make up the components
of the system, as described in the documents. It is currently a work in progress.

- `misc_tests/`

This subdirectory contains scripts that test some functionality that was being
explored. This includes connection with the Ghidra api, parsing C code, and 
interacting with LLMs.

- `batch_jobs/`

This subdirectory contains shell scripts used to run batch jobs on bridges2. 
[For more info, check out the user guide.](https://www.psc.edu/resources/bridges-2/user-guide/#batch-jobs)

- `sources/`

This subdirectory contains C source code for experimentation and benchmarking
purposes. There is a `c_files` subdirectory that contains basic C code, the rest
are git submodules to larger open source projects. These should be compiled as
per each project's building guide, at which point you can work with the produced
binary/binaries while being able to match against the original source code.

- `prompts/`

This subdirectory contains text files to prompts or base prompts that could be
given to an LLM. Base prompts have {{ value placeholders }} that indicate that
some concrete value has to be inserted before usage.

- `documents/`

Here we store research reports and presentations.

- `notes/`

Here we store miscellaneous notes and output logs from tests.

## Getting Started

1. Make sure to have python3 installed.

2. Clone the repository

3. Follow the section of your choice in the following guide.

## Usage

### `name_reconstruction/`

These include the current state of the name reconstruction system. To run:

1. Create a virtual environment with `python3 -m venv <env_name>`.

2. Activate the environment with `source <env_name>/bin/activate`.

3. Install dependencies with `pip install -r requirements.txt`. (Note that this
is the `name_reconstruction/requirements.txt`)

4. Run your component.

#### `prompt_generator.py`

The purpose of this component is to generate prompts from decompiler data, using
the Ghidra API and pyhidra. Currently, it is in a "broken" state, as it is still
being experimented with. See commented code in the main function to see the current
state.

### `misc_tests/`

Some of these tests involve prompting LLMs, those should be run in the appropriate
hardware. We are using bridges2. Others can be run anywhere. In either case, to
run:

1. Create a virtual environment with `python3 -m venv <env_name>`.

2. Activate the environment with `source <env_name>/bin/activate`.

3. Install dependencies with `pip install -r requirements.txt`. (Note that this
is the `misc_tests/requirements.txt`)

4. Run your test.

#### `llm_test.py`

This test takes a single argument, a path to a text file containing a list of 
LLM strings from HuggingFace. It then prompts "hello world" to each LLM and 
writes the responses to an `out.txt` file. This test might crash before writing
to a file, so we recommend using `llm_test2.py`. Feel free to change any parameters
in the code.

#### `llm_test2.py`

This test takes 2 arguments, the first is a LLM string from HuggingFace, and the
second is a path to a text file containing a prompt. The test then prompts the LLM
and prints the result. Feel free to change any parameters in the code.

#### `ghidra_test.py and parse_names.py`

These are no longer relevant to us as we are using different techniques. Feel 
free to look inside and play around with these.
