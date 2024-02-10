import gc 
import torch
from happytransformer import HappyGeneration
from happytransformer import GENTrainArgs 

#model = "./model_e42"
model = "./finetune-tinystories/finetuned/checkpoint-8000"
happy_gen = HappyGeneration("GPT-NEO", model)

result = happy_gen.generate_text("A picture of: ")
print(result)
print(result.text)

# Cleanup
try:
    del happy_gen
except:
    pass

gc.collect()
torch.cuda.empty_cache()
