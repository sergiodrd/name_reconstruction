import json
import sys

import pyhidra
from numpy.random import default_rng

pyhidra.start()
from ghidra.app.decompiler import DecompileOptions, DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

DECOMP_TIMEOUT = 60
RNG_SEED = 1337


class FunctionName:
    def __init__(self, og: str, obs: str):
        self.original = og
        self.obscured = obs


class SymbolData:
    def __init__(self, func_name: FunctionName, sym: list[str]):
        self.function_name = func_name
        self.symbols = sym

    def all(self) -> list[str]:
        return [self.function_name.obscured] + self.symbols

    def to_dict(self) -> dict:
        return {"function_name": self.function_name.__dict__, "symbols": self.symbols}


class DecompilationData:
    def __init__(self, symbol_data: SymbolData, decompiled_content: str):
        self.symbol_data = symbol_data
        self.decompiled_content = decompiled_content

    def __repr__(self) -> str:
        return f"""Function name: {self.symbol_data.function_name.original}
Obscured name: {self.symbol_data.function_name.obscured}
Symbols found: {self.symbol_data.symbols}
Decompiled contents:
{self.decompiled_content}"""

    def get_prompt(self, base_prompt: str) -> str:
        symbols = "".join(list(map(lambda x: x + ",\n", self.symbol_data.all())))
        prompt = base_prompt.replace("{{ symbols }}", symbols)
        prompt = prompt.replace("{{ function }}", self.decompiled_content)
        return prompt

    def to_dict(self) -> dict:
        return {
            "symbol_data": self.symbol_data.to_dict(),
            "decompiled_content": self.decompiled_content,
        }


def dump_decomp_json(input_files: list[str], output_dir: str) -> list[str]:
    l = []
    for path in input_files:
        with pyhidra.open_program(path) as flat_api:

            class GProgram:
                def __init__(self):
                    self.program = flat_api.getCurrentProgram()

                    self.options = DecompileOptions()
                    self.monitor = ConsoleTaskMonitor()
                    self.decompiler = DecompInterface()

                    self.decompiler.setOptions(self.options)
                    self.decompiler.openProgram(self.program)

                def count_functions(self) -> int:
                    return self.program.getFunctionManager().getFunctionCount()

                def functions(self) -> list:
                    return self.program.getFunctionManager().getFunctions(True)

                def get_decomp_data(self, i: int) -> DecompilationData:
                    func = list(self.functions())[i]
                    results = self.decompiler.decompileFunction(
                        func, DECOMP_TIMEOUT, self.monitor
                    )
                    high_func = results.getHighFunction()
                    func_name = FunctionName(
                        func.getName(), f"sub{func.getEntryPoint().__repr__()}"
                    )
                    data = []
                    for symbol in high_func.getLocalSymbolMap().getSymbols():
                        data.append(symbol.name)
                    decomp = (
                        results.getDecompiledFunction()
                        .getC()
                        .replace(func_name.original, func_name.obscured)
                    )
                    return DecompilationData(SymbolData(func_name, data), decomp)

                def get_all_decomp_data(self) -> list[DecompilationData]:
                    funcs_data = []
                    for i in range(len(list(self.functions()))):
                        funcs_data.append(self.get_decomp_data(i))

                    return funcs_data

            p = f"{output_dir}/{path.split('/')[-1]}.json"
            l.append(p)
            f = open(p, "w")
            json.dump(
                list(map(lambda x: x.to_dict(), GProgram().get_all_decomp_data())), f
            )
            f.close()

    return l


def dump_prompts_from_json(json_path: str, base_prompt_path: str, output_path: str):
    jf = open(json_path, "r")
    pf = open(base_prompt_path, "r")
    out = open(output_path, "w")

    inf: list[dict] = json.load(jf)
    prompt = pf.read()

    def add_prompt_to_dict(data: dict) -> dict:
        s = ""
        length = len(data["symbol_data"]["symbols"])
        for i in range(length):
            s += data["symbol_data"]["symbols"][i] + (",\n" if i + 1 < length else "")

        p = prompt.replace("{{ function }}", data["decompiled_content"])
        p = p.replace("{{ symbols }}", s)

        data["prompt"] = p

        return data

    inf = list(map(add_prompt_to_dict, inf))
    json.dump(inf, out)

    jf.close()
    pf.close()
    out.close()


def sample_n_prompts_to_json(data: list[dict], n: int, out_path: str, size_limit: int):
    data = list(filter(lambda x: len(x["prompt"]) <= size_limit, data))
    rng = default_rng(RNG_SEED)
    samples = rng.choice(data, size=n, replace=False)
    f = open(out_path, "w")
    json.dump(list(samples), f)
    f.close()


def main():
    # paths = dump_decomp_json(sys.argv[1:], "decomp_data")
    # for p in paths:
    #     dump_prompts_from_json(p, "../prompts/cot_base.txt", "test.json")
    f = open("test.json", "r")
    sample_n_prompts_to_json(json.load(f), 10, "test3.json", 1000)


if __name__ == "__main__":
    main()

    # class GProgramPool:
    #     def __init__(self, paths: list[str]):
    #         self.g_programs = list(map(lambda x: GProgram(x), paths))
    #
    #         self.functions = []
    #         for g_program in self.g_programs:
    #             self.functions += g_program.functions()
    #
    #     def random_sample(self, amount: int) -> list[DecompilationData]:
    #         rng = default_rng(RNG_SEED)
    #         indeces = rng.choice(len(self.functions), size=amount, replace=False)
    #         data = []
    #         for i in indeces:
    #             for g_program in self.g_programs:
    #                 if i < g_program.count_functions():
    #                     data.append(g_program.get_decomp_data(i))
    #                     break
    #                 i -= g_program.count_functions()
    #         return data
