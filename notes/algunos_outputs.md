# Prompt

This C function was obtained by decompiling a binary program:

```c
int sub_4BECE3 (uint32_t a1) {
        uint8_t result;
        if (a1 - 65 > 25) result = a1;
        else result = a1 + 32;
        return result;
}
```

---

Note that during the original compilation process, symbol names were lost, so
the decompiler gave the present symbols meaningless names. You will analyze the
function and attempt to rename the symbols to more semantically meaningfull names.

---

The symbols you will rename are:

`a1`,

`result`,

`sub_4BECE3`

---

You MUST follow the format <original_name> -> <new_name> for each symbol.

Do NOT add additional text before or after this.

# mistralai/Mixtral-8x7B-Instruct-v0.1

a1 -> char_code

result -> char_code_adjusted

sub_4BECE3 -> to_uppercase_if_alpha

The function converts a character code to uppercase if it is an alphabetic character.

The function converts a character code to uppercase if it is an alphabetic character.

The function converts a character code to uppercase if it is an alphabetic character.

The function converts a character code to uppercase if it is an alphabetic character.

The function converts a character code to uppercase if it is an alphabetic character.

The function converts a character code to uppercase if it is an alphabetic character.

The function converts a character code to uppercase if it is an alphabetic character.

The function converts a character code to uppercase if it

## Notas

Mixtral lo esta reconociendo aún mejor que la otra vez. Parece que el contexto añadido ayuda mucho.
Eso si, sigue tratando de explicar lo que hace la función aunque le dije que no lo hiciera.

# codellama/CodeLlama-34b-Instruct-hf

For example, if you decide to rename `a1` to `input`, you should write:

`a1` -> `input`

You MUST rename all the symbols.

You MUST NOT rename any other symbols.

You MUST NOT change the function's functionality.

You MUST NOT change the function's return type.

You MUST NOT change the function's parameter list.

You MUST NOT change the function's name.

You MUST NOT change the function's control flow.

You MUST NOT change the function's data flow.

You MUST NOT change the function's overall structure.

You MUST NOT change the function's resource usage.

You MUST NOT change the function's exception handling.

You MUST NOT change the function's error handling.

You MUST NOT change the function'

## Notas

Llama claramente está continuando el texto del prompt en vez de contestando.
Creo que podemos conseguir un "chat API" de huggingface para resolver este issue. Si no, se podría
conseguir un system prompt tal que actúe de la manera que esperamos. 

---

# Probando para una función de sqlite descompilada con Ghidra

This C function was obtained by decompiling a binary program:

```c
undefined8 sqlite3IsReadOnly(long *param_1,undefined8 *param_2,long param_3)

{
  char cVar1;
  int iVar2;
  long lVar3;

  cVar1 = *(char *)((long)param_2 + 0x3f);
  if (cVar1 == '\x01') {
    lVar3 = sqlite3GetVTable(*param_1);
    if (*(long *)(**(long **)(lVar3 + 8) + 0x68) == 0) goto LAB_00100105;
    if ((param_1[0x16] != 0) &&
       (((byte)(*(ulong *)(*param_1 + 0x30) >> 7) & 1) < *(byte *)(param_2[10] + 0x1e))) {
      sqlite3ErrorMsg(param_1,"unsafe use of virtual table \"%s\"",*param_2);
      cVar1 = *(char *)((long)param_2 + 0x3f);
      goto LAB_0010013c;
    }
  }
  else {
    if ((*(uint *)(param_2 + 6) & 0x1001) == 0) goto LAB_0010013c;
    if ((*(uint *)(param_2 + 6) & 1) == 0) {
      iVar2 = sqlite3ReadOnlyShadowTables();
      if (iVar2 != 0) {
LAB_00100105:
        sqlite3ErrorMsg(param_1,"table %s may not be modified",*param_2);
        return 1;
      }
    }
    else {
      iVar2 = sqlite3WritableSchema(*param_1);
      if ((iVar2 == 0) && (*(char *)((long)param_1 + 0x1e) == '\0')) goto LAB_00100105;
    }
  }
  cVar1 = *(char *)((long)param_2 + 0x3f);
LAB_0010013c:
  if (cVar1 != '\x02') {
    return 0;
  }
  if (param_3 != 0) {
    if (*(char *)(param_3 + 0x12) == '\0') {
      return 0;
    }
    if (*(long *)(param_3 + 0x40) != 0) {
      return 0;
    }
  }
  sqlite3ErrorMsg(param_1,"cannot modify %s because it is a view",*param_2);
  return 1;
}
```

---

Note that during the original compilation process, symbol names were lost, so
the decompiler gave the present symbols meaningless names. You will analyze the
function and attempt to rename the symbols to more semantically meaningfull names.

---

The symbols you will rename are:

`param_1`,

`param_2`,

`param_3`,

`cVar1`,

`iVar2`,

`lVar3`

---

You MUST follow the format <original_name> -> <new_name> for each symbol.

Do NOT add additional text before or after this.

# mistralai/Mixtral-8x7B-Instruct-v0.1

param_1 -> db

param_2 -> pTab

param_3 -> flags

cVar1 -> isVtab

iVar2 -> i

lVar3 -> vtab

---

db -> database

pTab -> table

flags -> flag

isVtab -> isVirtualTable

i -> i

vtab -> vtable

The function sqlite3IsReadOnly checks if a table is read-only. If the table is
read-only, it returns 1, otherwise it returns 0. The function takes three
arguments:

1. database: a pointer to the database structure
2. table: a pointer to the table structure
3. flags: a flag indicating whether the table is a virtual table

The function first checks if the table is a virtual table. If it is, it checks
if the table is writable. If the table is not writable, it returns 1. If the table

# codellama/CodeLlama-34b-Instruct-hf

For example, if you decide to rename `param_1` to `db`, you would enter:

`param_1` -> `db`

You will be presented with a list of all the symbols in the function, and you
will be prompted to enter a new name for each one.

Note that the decompiler will not let you rename a parameter to a name that is
already in use as a local variable.

Also note that the decompiler will not let you rename a parameter to a name
that is the same as a global variable.

Also note that the decompiler will not let you rename a parameter to a name
that is the same as a function name.

Also note that the decompiler will not let you rename a parameter to a name
that is the same as a label name.

Also note that the decompiler will not let you rename a parameter to a name
that is

# Notas

Estuve leyendo sobre técnicas de prompting y se me ocurrió esto.

# Prompt nuevo !!

The user will provide a C function that was obtained by decompiling a binary
program and a list of symbol names present in the function.

Note that during the original compilation process, symbol names were lost, so
the decompiler gave the present symbols meaningless names. The system will
analyze the function and attempt to rename the symbols to more semantically
meaningful names.

The system MUST follow the format <original_name> -> <new_name> for each symbol.
The system MUST NOT add additional text before or after this.

---

USER:

Function:

```c
int sub_4BECE3 (uint32_t a1) {
        uint8_t result;
        if (a1 - 65 > 25) result = a1;
        else result = a1 + 32;
        return result;
}
```

Symbols:

`a1`,

`result`,

`sub_4BECE3`

---

SYSTEM:

a1 -> char_code

result -> char_code_adjusted

sub_4BECE3 -> to_uppercase_if_alpha

---

USER:

Function:

```c
undefined8 sqlite3IsReadOnly(long *param_1,undefined8 *param_2,long param_3)

{
  char cVar1;
  int iVar2;
  long lVar3;

  cVar1 = *(char *)((long)param_2 + 0x3f);
  if (cVar1 == '\x01') {
    lVar3 = sqlite3GetVTable(*param_1);
    if (*(long *)(**(long **)(lVar3 + 8) + 0x68) == 0) goto LAB_00100105;
    if ((param_1[0x16] != 0) &&
       (((byte)(*(ulong *)(*param_1 + 0x30) >> 7) & 1) < *(byte *)(param_2[10] + 0x1e))) {
      sqlite3ErrorMsg(param_1,"unsafe use of virtual table \"%s\"",*param_2);
      cVar1 = *(char *)((long)param_2 + 0x3f);
      goto LAB_0010013c;
    }
  }
  else {
    if ((*(uint *)(param_2 + 6) & 0x1001) == 0) goto LAB_0010013c;
    if ((*(uint *)(param_2 + 6) & 1) == 0) {
      iVar2 = sqlite3ReadOnlyShadowTables();
      if (iVar2 != 0) {
LAB_00100105:
        sqlite3ErrorMsg(param_1,"table %s may not be modified",*param_2);
        return 1;
      }
    }
    else {
      iVar2 = sqlite3WritableSchema(*param_1);
      if ((iVar2 == 0) && (*(char *)((long)param_1 + 0x1e) == '\0')) goto LAB_00100105;
    }
  }
  cVar1 = *(char *)((long)param_2 + 0x3f);
LAB_0010013c:
  if (cVar1 != '\x02') {
    return 0;
  }
  if (param_3 != 0) {
    if (*(char *)(param_3 + 0x12) == '\0') {
      return 0;
    }
    if (*(long *)(param_3 + 0x40) != 0) {
      return 0;
    }
  }
  sqlite3ErrorMsg(param_1,"cannot modify %s because it is a view",*param_2);
  return 1;
}
```

Symbols:

`param_1`,

`param_2`,

`param_3`,

`cVar1`,

`iVar2`,

`lVar3`

---

SYSTEM:

# mistralai/Mixtral-8x7B-Instruct-v0.1

---

# Table

## Base Prompt 1:

This C function was obtained by decompiling a binary program:

{{function}}

---

Note that during the original compilation process, symbol names were lost, so
the decompiler gave the present symbols meaningless names. You will analyze the
function and attempt to rename the symbols to more semantically meaningfull names.

---

The symbols you will rename are:

{{symbol list}}

---

You MUST follow the format <original_name> -> <new_name> for each symbol.

Do NOT add additional text before or after this.

## For example

This C function was obtained by decompiling a binary program:

```c
int sub_4BECE3 (uint32_t a1) {
        uint8_t result;
        if (a1 - 65 > 25) result = a1;
        else result = a1 + 32;
        return result;
}
```

---

Note that during the original compilation process, symbol names were lost, so
the decompiler gave the present symbols meaningless names. You will analyze the
function and attempt to rename the symbols to more semantically meaningfull names.

---

The symbols you will rename are:

`a1`,

`result`,

`sub_4BECE3`

---

You MUST follow the format <original_name> -> <new_name> for each symbol.

Do NOT add additional text before or after this.

## Base Prompt 2:

The user will provide a C function that was obtained by decompiling a binary
program and a list of symbol names present in the function.

Note that during the original compilation process, symbol names were lost, so
the decompiler gave the present symbols meaningless names. The system will
analyze the function and attempt to rename the symbols to more semantically
meaningful names.

The system MUST follow the format <original_name> -> <new_name> for each symbol.
The system MUST NOT add additional text before or after this.

---

USER:

Function:

```c
int sub_4BECE3 (uint32_t a1) {
        uint8_t result;
        if (a1 - 65 > 25) result = a1;
        else result = a1 + 32;
        return result;
}
```

Symbols:

`a1`,

`result`,

`sub_4BECE3`

---

SYSTEM:

a1 -> char_code

result -> char_code_adjusted

sub_4BECE3 -> to_uppercase_if_alpha

---

USER:

Function:

{{function}}

Symbols:

{{symbol list}}

---

SYSTEM:

# Table fr

| Model | Decompiled Symbols | Expected Symbols | Output |
| --- | --- | --- | --- |
| mistralai/Mixtral-8x7B-Instruct-v0.1 | a1,<br>result,<br>sub_4BECE3 | N/A | a1 -> char_code<br>result -> char_code_adjusted<br>sub_4BECE3 -> to_uppercase_if_alpha | 
| codellama/CodeLlama-34b-Instruct-hf | a1,<br>result,<br>sub_4BECE3 | N/A | Completes the prompt, doesn't answer properly. |
| mistralai/Mixtral-8x7B-Instruct-v0.1 | param_1,<br>param_2,<br>param_3,<br>cVar1,<br>iVar2,<br>lVar3 | param_1 -> pParse,<br>param_2 -> pTab,<br>param_3 -> pTrigger | param_1 -> db<br>param_2 -> pTab<br>param_3 -> flags<br>cVar1 -> isVtab<br>iVar2 -> i<br>lVar3 -> vtab |
| codellama/CodeLlama-34b-Instruct-hf | aram_1,<br>param_2,<br>param_3,<br>cVar1,<br>iVar2,<br>lVar3 | param_1 -> pParse,<br>param_2 -> pTab,<br>param_3 -> pTrigger | Completes the prompt, doesn't answer properly. |


# Table 2

| Model | Decompiled Symbols | Expected Symbols | Output |
| --- | --- | --- | --- |
| mistralai/Mixtral-8x7B-Instruct-v0.1 | param_1,<br>param_2,<br>param_3,<br>cVar1,<br>iVar2,<br>lVar3 | param_1 -> pParse,<br>param_2 -> pTab,<br>param_3 -> pTrigger | param_1 -> db_ptr<br>param_2 -> table_name<br>param_3 -> flags<br>cVar1 -> table_status<br>iVar2 -> error_code<br>lVar3 -> vtable_ptr |
| codellama/CodeLlama-34b-Instruct-hf | aram_1,<br>param_2,<br>param_3,<br>cVar1,<br>iVar2,<br>lVar3 | param_1 -> pParse,<br>param_2 -> pTab,<br>param_3 -> pTrigger | param_1 -> db<br>param_2 -> table_name<br>param_3 -> p_trigger<br>cVar1 -> is_virtual_table<br>iVar2 -> is_read_only<br>lVar3 -> vtable_ptr |
