from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, TextStreamer, pipeline
import argparse
import sys
import json
from pathlib import Path


model_name_or_path = "Helsinki-NLP/opus-mt-en-de"

generation_params = {
    "do_sample": True,
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "max_new_tokens": 512,
    "repetition_penalty": 1.1
}
    #"return_full_text": False,

def initializeLLM(gpu):
    global tokenizer, model, streamer

    print("Loading LLM (" + model_name_or_path +")")
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)

    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_name_or_path,
        device_map="cuda:" + gpu
    )

    # Using the text streamer to stream output one token at a time
    streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

def translate_caption(caption, gpu):
    device = "cuda:" + gpu

    input_ids = tokenizer.encode(caption, return_tensors="pt").to(device)
    outputs = model.generate(input_ids).to(device)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded.strip()

def translateCommand(filename, gpu):
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
                    new_caption = translate_caption(org_caption, gpu)
                    caption_list[i] = new_caption
                    print("[" + str(r) + " / " + str(len(lines)) + "] " + org_caption + " ===> " + new_caption)
            else:
                #for nTry in range(20):
                org_caption = entry['caption']
                new_caption = translate_caption(org_caption, gpu)
                print("[" + str(r) + " / " + str(len(lines)) + "] " + org_caption + " ===> " + new_caption)
                entry['caption'] = new_caption
                #if not needs_refinining(new_caption, org_caption):
                #    break
            entries.append(entry)
            r=r+1

        # Save the new data
        json_object = json.dumps(entries, indent=4)
        with open(outputName, "w") as outfile:
            outfile.write(json_object)

def testCommand(caption, gpu):
    print("Testing caption translation.")
    initializeLLM(gpu)
    print()
    print("EN: " + caption)
    new_caption = translate_caption(caption, gpu)
    print("DE: " + new_caption)

def main():
    parser = argparse.ArgumentParser(
                    prog='COCO Opus Translator',
                    description='Translates COCO captions to german',
                    epilog='You know - For AI')
    parser.add_argument("command", help='command to execute [translate,test]')
    parser.add_argument("filename", help='source coco caption json file')
    parser.add_argument("gpu", help='GPU ID', type=str, default="0")
    args = parser.parse_args()
    
    if not len(sys.argv) > 1:
       parser.print_help()

    match args.command:
        case "translate":
            translateCommand(args.filename, args.gpu)
        case "test":
            testCommand(args.filename, args.gpu)
        case _:
            print("Unknown command: " + args.command)
            parser.print_help()
    

if __name__ == "__main__":
  main()

