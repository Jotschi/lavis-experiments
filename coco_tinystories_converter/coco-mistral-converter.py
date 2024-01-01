from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer
from transformers import pipeline
import argparse
import sys
import json
from pathlib import Path


generation_params = {
    "do_sample": True,
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "return_full_text": False,
    "max_new_tokens": 512,
    "repetition_penalty": 1.1
}

model_name_or_path = "TheBloke/Mistral-7B-Instruct-v0.2-AWQ"

def initializeLLM(gpu):
    global tokenizer, model, streamer

    print("Loading LLM (" + model_name_or_path +")")
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_name_or_path,
        device_map="cuda:" + gpu
    )

    # Using the text streamer to stream output one token at a time
    streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

def convert_caption(caption):
    # TinyStories Example Prompt taken from https://arxiv.org/abs/2305.07759
    #Write a short story (3-5 paragraphs) which only uses very simple words that a 3 year old child would likely understand. The story should use the verb ”decorate”, the noun ”thunder” and the adjective ”ancient”. The story
    #should have the following features: the story should contain at least one dialogue, the story has a bad ending.
    #Remember to only use simple words!

    prompt = "Rewrite the sentence '" + caption +"' for a 3 to 4 year old child. Give only one simple sentence. Don't use the word see. Give only a single answer."
    #prompt = "Rewrite only the sentence '" + caption +"' for a very young child. Don't any more info."
    prompt_template=f'''<s>[INST] {prompt} [/INST]
'''

    tokens = tokenizer(
        prompt_template,
        return_tensors='pt'
    ).input_ids.cuda()


    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        **generation_params
    )

    pipe_output = pipe(prompt_template)[0]['generated_text']
    return pipe_output.strip()

def convert_caption_with_retry(coco_caption):
    new_caption = "***FAILED***"
    for nTry in range(20):
        new_caption = convert_caption(coco_caption)
        print("[" + str(nTry) + "] N: " + new_caption)
        if not needs_refinining(new_caption, coco_caption):
            break
    return new_caption;

            


def captionCommand(filename, gpu):
    print("Loading captions from " + filename + " using GPU " + gpu)
    Path("output").mkdir(parents=True, exist_ok=True)
    outputName = "output/" + Path(filename).stem + ".json"

    initializeLLM(gpu)

    with open(filename, 'r') as f:
        lines = f.readlines()
        entries = []
        r=0
        for line in lines:
            entry = json.loads(line)
            if isinstance(entry['caption'], list):
                caption_list = entry['caption']
                for i, s in enumerate(caption_list):
                    org_caption = s.strip()
                    new_caption = convert_caption_with_retry(org_caption)
                    caption_list[i] = new_caption
                    print("[" + str(r) + " / " + str(len(lines)) + "] " + org_caption + " ===> " + new_caption)
            else:
                for nTry in range(20):
                    org_caption = entry['caption']
                    new_caption = convert_caption(org_caption)
                    print("[" + str(r) + " / " + str(len(lines)) + "] " + org_caption + " ===> (" + str(nTry) + ") " + new_caption)
                    entry['caption'] = new_caption
                    if not needs_refinining(new_caption, org_caption):
                        break
            entries.append(entry)
            r=r+1

        # Save the new data
        json_object = json.dumps(entries, indent=4)
        with open(outputName, "w") as outfile:
            outfile.write(json_object)

def needs_refinining(caption, coco_caption):
    length = caption.count('\n')
    if length >= 1:
        return True
    if caption.count("(") >= 1:
        return True
    if caption.count(")") >= 1:
        return True
    if caption.count("]") >= 1:
        return True
    if caption.count("[") >= 1:
        return True
    if caption.count("___") >= 1:
        return True
    if caption.count("***") >= 1:
        return True
    if caption.count("simplified") >= 1:
        return True
    if caption.count("Children:") >= 1:
        return True
    if caption.count("child:") >= 1:
        return True
    if caption.count("simple sentence") >= 1:
        return True
    if caption.count("simple way to") >= 1:
        # simple way to explain/describe
        return True

    return False

def testCommand(caption, gpu):
    print("Testing caption generation.")
    initializeLLM(gpu)
    print()
    print("O: " + caption)
    for nTry in range(20):
        new_caption = convert_caption(caption)
        check_result = needs_refinining(new_caption, caption)
        print("N(" + str(nTry) + "|" + str(check_result) +"): " + new_caption)

def refineCommand(filename, gpu):
    print("Invoking refine of " + filename + " using GPU " + gpu)
    Path("refine").mkdir(parents=True, exist_ok=True)
    outputName = "refine/" + Path(filename).stem + ".json"

    initializeLLM(gpu)

    # Load the original coco captions (needed for refining the bad quality caption)
    coco_captions = {}
    with open("vg_caption.json", 'r') as f:
        data = json.load(f)
        for entry in data:
            coco_captions[entry['image_id']] = entry['caption']

    # Read the mistralized caption file
    with open(filename, 'r') as f:
        data = json.load(f)
        
        # Check how many captions need refininig
        pending=0
        for entry in data:
            id = entry['image_id'] 
            mistral_caption = entry['caption'].strip()
            coco_caption = coco_captions[id].strip()
            if needs_refinining(mistral_caption, coco_caption):
                pending=pending+1

        # Refine the captions
        for entry in data:
            id = entry['image_id'] 
            mistral_caption = entry['caption'].strip()
            coco_caption = coco_captions[id].strip()
            if needs_refinining(mistral_caption, coco_caption):
                print("----------")
                print("[" + id + " / " + str(pending) + "] C: " + mistral_caption)
                print("[" + id + " / " + str(pending) + "] O: " + coco_caption)
                pending = pending-1
                for nTry in range(20):
                    new_caption = convert_caption(coco_caption)
                    entry['caption'] = new_caption
                    print("[" + id + " / " + str(pending) + "] N(" + str(nTry) + "): " + new_caption)
                    if not needs_refinining(new_caption, coco_caption):
                        break
                       

        # Save the updated caption file to the refine folder
        with open(outputName, "w") as outfile:
            json_object = json.dumps(data, indent=4)
            outfile.write(json_object)


def main():
    parser = argparse.ArgumentParser(
                    prog='COCO Mistral 7B Converter',
                    description='Converts coco captions to simplified english',
                    epilog='You know - For AI')
    parser.add_argument("command", help='command to execute [caption,test, refine]')
    parser.add_argument("filename", help='source coco caption json file')
    parser.add_argument("gpu", help='GPU ID', type=str, default="0")
    args = parser.parse_args()
    
    if not len(sys.argv) > 1:
       parser.print_help()

    match args.command:
        case "caption":
            captionCommand(args.filename, args.gpu)
        case "refine":
            refineCommand(args.filename, args.gpu)
        case "test":
            testCommand(args.filename, args.gpu)
        case _:
            print("Unknown command: " + args.command)
            parser.print_help()
    


#def main2():
#    caption="A woman hitting a tennis ball with the racquet she's holding in her hand."
#    print(convertCaption(caption))

if __name__ == "__main__":
  main()

