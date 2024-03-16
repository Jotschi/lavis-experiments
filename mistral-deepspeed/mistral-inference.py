from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline
import torch
import sys

model_name = sys.argv[1]

#    bnb_4bit_use_double_quant=True,
#    bnb_4bit_quant_type="nf4",

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
)

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(
        model_name,
        load_in_4bit=True,
        quantization_config=quantization_config,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )


pipe = pipeline(
    "text-generation", 
    model=model, 
    tokenizer = tokenizer, 
    torch_dtype=torch.bfloat16, 
    device_map="auto"
)

prompts = ["Ein Mann und eine Frau stehen", "Ein Haus steht", "Das Auto ist", "Ein Teller mit", "Das Kind hat", "Der opa wirft", "Ein Ball", "Eine Frau, die einen großen" ]

for prompt in prompts:
    sequences = pipe(
        prompt,
        do_sample=True,
        max_new_tokens=100, 
        temperature=0.7, 
        top_k=50, 
        top_p=0.95,
        num_return_sequences=1,
    )
    print("--------------")
    print(prompt)
    print(sequences[0]['generated_text'])