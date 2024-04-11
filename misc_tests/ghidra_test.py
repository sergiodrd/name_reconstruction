import sys

if len(sys.argv) != 3:
    print("Usage:\n\tpython ghidra_test.py <stripped> <unstripped>")
    exit(1)

st_path = sys.argv[1]
unst_path = sys.argv[2]

import pyhidra

pyhidra.start()
from ghidra.app.decompiler import DecompInterface

with pyhidra.open_program(st_path) as st_flat_api:
    # generate map of addresses to function names using the unstripped binary
    with pyhidra.open_program(unst_path) as unst_flat_api:
        program = unst_flat_api.getCurrentProgram()
        funcs = program.getFunctionManager().getFunctions(True)  # True means 'forward'
        names = map(lambda x: x.getName(), funcs)
        addrs = map(lambda x: x.getEntryPoint(), funcs)
        name_addrs = {name: addr for (name, addr) in zip(names, addrs)}

    print(name_addrs.values())
    program = st_flat_api.getCurrentProgram()
    ifc = DecompInterface()
    ifc.openProgram(program)

    funcs = program.getFunctionManager().getFunctions(True)
    for func in filter(lambda x: x.getName().startswith("FUN"), funcs):
        print(func.getEntryPoint())
        name = "???"
        if func.getEntryPoint() in name_addrs:
            name = name_addrs[func.getEntryPoint()]
        # print(f"{func.getName()} <--> {name}")
        # results = ifc.decompileFunction(func, 0, ConsoleTaskMonitor())
        # print(results.getDecompiledFunction().getC())
