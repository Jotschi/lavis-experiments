from PIL import Image
import torch

raw_image = Image.open("aral.jpg").convert("RGB")

# setup device to use
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model, vis_processors, txt_processors = load_model_and_preprocess(name="blip_vqa", model_type="vqav2", is_eval=True, device=device)
vis_processors.keys()
txt_processors.keys()

question = "What is visible?"

# use "eval" processors for inference
image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
question = txt_processors["eval"](question)

samples = {"image": image, "text_input": question}

print(model.predict_answers(samples=samples, inference_method="generate"))


## rank answer candidates by their likelihood and return the best answer
#answer_candidates = ["Singapore", "London", "Palo Alto", "Tokyo"]
#
#model.predict_answers(samples, answer_list=answer_candidates, inference_method="rank")
#
#
#batch_size = 3
#
## create a batch of samples, could be multiple images or copies of the same image
#image_batch = image.repeat(batch_size, 1, 1, 1)
#
## create a batch of questions, make sure the number of questions matches the number of images
#question_1 = txt_processors["eval"]("Which city is this photo taken?")
#question_2 = txt_processors["eval"]("What time is this during the day?")
#question_3 = txt_processors["eval"]("Is it Singapore or London?")
#
#question_batch = [question_1, question_2, question_3]
#
#model.predict_answers(samples={"image": image_batch, "text_input": question_batch}, inference_method="generate")