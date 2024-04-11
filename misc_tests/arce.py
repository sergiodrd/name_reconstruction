from transformers import AutoTokenizer
# llm = "mistralai/Mistral-7B-v0.1"
# llm = "codellama/CodeLlama-13b-Instruct-hf"
# llm = "codellama/CodeLlama-7b-Instruct-hf"
# llm = "bigcode/starcoder"

# llm = "Salesforce/codegen25-7b-multi"
llm = "mistralai/Mixtral-8x7B-Instruct-v0.1"

tokenizer = AutoTokenizer.from_pretrained(llm, padding_side="left")
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained(llm, device_map="auto", load_in_4bit=True)


myPrompt = "int countOdds(int arr[], int size)"
myPrompt = '''Consider the following C++ function.\n
int foo(int arr[], int size) {  \n    int i = 0;  \n    int var_0x45 = 0; \n    for ( i = 0; i < size; i++) {  \n     var_0x45 += arr[i];  \n } \n return var_0x45; \n } \n A better name for var_0x45 would be'''

myPrompt = '''Consider the following C++ function.\n
int foo(int arr[], int size) {  \n    int i = 0;  \n    int var_0x45 = 0; \n    for ( i = 0; i < size; i++) {  \n    if (arr[i] >= '0' && arr[i] <= '9') var_0x45++;  \n } \n return var_0x45; \n } \n A better name for var_0x45 would be'''

myPrompt = '''Consider the following C++ function.\n
int compare_strings(uint8_t* string1, uint8_t* string2){ uint8_t *string1_pointer, *string2_pointer; uint8_t string2_char, string1_char; // ... do{ string1_char = sub_4BECE3(*string1_pointer); string2_char = sub_4BECE3(*string1_pointer); if(string1_char == 0) break; ++string1_pointer; ++string2_pointer; }while (string1_char == string2_char); return string1_char – string2_char; \n A better name for sub_4BECE3 would be '''

myPrompt = '''
Can you help me guess some information for the following decompiled C function from a binary program? The following is the decompiled C function:
int sub_4BECE3 (uint32_t a1){ uint8_t result; if (a1 - 65 > 25) result = a1; else result = a1 + 32; return result; }
In the above function, what are good names for `a1`, `result`, and `sub_4BECE3`, respectively? You MUST follow the format <original_name> -> <new_name>
'''


myPrompt2 = '''
Can you help me guess some information for the following decompiled C function from a binary program? The following is the decompiled C function:
static Idx __attribute__((pure))
re_node_set_contains(const re_node_set *set, Idx elem) {
__re_size_t idx, var_0xbaca1a0, mid;
if (set->nelem <= 0)
return 0;
/* Binary search the element. */
idx = 0;
var_0xbaca1a0 = set->nelem - 1;
while (idx < var_0xbaca1a0) {
mid = (idx + var_0xbaca1a0) / 2;
if (set->elems[mid] < elem)
idx = mid + 1;
else
var_0xbaca1a0 = mid;
}
return set->elems[idx] == elem ? idx + 1 : 0;
}
In the above function, what is a good name for `var_0xbaca1a0`?
'''



model_inputs = tokenizer([myPrompt], return_tensors="pt").to("cuda")
generated_ids = model.generate(**model_inputs, max_new_tokens=200)
print(tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0])
