from transformers import AutoTokenizer, AutoModelForSequenceClassification
#transformer gives me accessed to pre-trained models
#autotokenizer converts human text to model readable langauge
#automodelforsequnce classification is what takes the input and gives us the result
import torch #framework the model runs on

MODEL_NAME = "cross-encoder/nli-deberta-v3-base" #specific model we are using

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME) #tokenizer for this specific model
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME) #neural network model? Already trained with valid weights
model.eval() #turn model from training to evaluating
#until here, it is run during the import statement, so early on

#TODO: consider lazy loading to speed up startup
#TODO: consider batched inference for performance

LABEL_MAP = {0: "opposing", 1: "supporting", 2: "neutral"}



def classify_stance(premise: str, hypothesis: str) -> tuple[str, float]:
    #premis is what the source says, hypothesis is the claim we are checking
    #we return stance and confidence

    inputs = tokenizer( #converts the text to numbers (tokens) that machine can read
        premise,
        hypothesis,
        return_tensors="pt",
        truncation=True, #loses the info if it goes over the max length, adjust if this causes the issue later
        max_length=512,
    )
    with torch.no_grad(): #don't track gradient of neural network cuz we are not doing any training
        outputs = model(**inputs) #unpacts the dictioaary and actaully get the output
    probs = torch.softmax(outputs.logits, dim=1)[0] #convert returned raw scores into probability of each verdict
    predicted_idx = probs.argmax().item() #find max prob
    confidence = probs[predicted_idx].item() #get confidnece of that
    return LABEL_MAP[predicted_idx], confidence


