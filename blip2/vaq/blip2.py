from PIL import Image

#from lavis.models import load_model_and_preprocess
#from lavis.processors import load_processor
from transformers import Blip2Processor, Blip2ForConditionalGeneration
import torch


image = Image.open("test.jpg").convert("RGB")

device = torch.device("cuda") if torch.cuda.is_available() else "cpu"

#model, vis_processors, text_processors = load_model_and_preprocess("blip2_image_text_matching", "pretrain", device=device, is_eval=True)

processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b")
model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b", torch_dtype=torch.float16)
model.to(device)

# use "eval" processors for inference
#image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
#question = text_processors["eval"](question)

#samples = {"image": image, "text_input": question}

prompt = "Describe the scene."

inputs = processor(images=image, text=prompt, return_tensors="pt").to(device, torch.float16)


generated_ids = model.generate(**inputs)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()
print(generated_text)

#print(model.predict_answers(samples=samples, inference_method="generate"))
#model.generate({"image": image, "prompt": "Question: which city is this? Answer:"})


#caption = "company logo"
#img = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
#txt = text_processors["eval"](caption)
#
#
#itm_output = model({"image": img, "text_input": txt}, match_head="itm")
#itm_scores = torch.nn.functional.softmax(itm_output, dim=1)
#print(f'The image and text are matched with a probability of {itm_scores[:, 1].item():.3%}')
#
#itc_score = model({"image": img, "text_input": txt}, match_head='itc')
#print('The image feature and text feature has a cosine similarity of %.4f'%itc_score)