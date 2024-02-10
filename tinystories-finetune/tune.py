import gc 
import torch
from happytransformer import HappyGeneration
from happytransformer import GENTrainArgs 

model = "EleutherAI/gpt-neo-125M"
# model_to_use = "EleutherAI/gpt-neo-1.3B",
   
happy_gen = HappyGeneration("GPT-NEO", model)

#result = happy_gen.generate_text("Artificial intelligence will ")
#print(result)
#print(result.text)
args = GENTrainArgs(learning_rate =1e-5, num_train_epochs = 1)

happy_gen.train("train.csv", args)
try:
    del happy_gen
except:
    pass

gc.collect()
torch.cuda.empty_cache()
