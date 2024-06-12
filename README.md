# GP-legal-chatbot
QA answering system for Egyption law **Personal Status law** (قانون الاحوال الشخصية)

## Introduction
if you have any question related to law you have to google it first and **this is hard** or call some legal advisor/ laywer which is **expensive**

so we came out with this solution **Legal QA Chatbot**

## Dataset
to train a model or finetune a model first we must have a dataset which wasn't exist. so we created it 

### EgyLaw SQUAD Dataset
this dataset was generted by our team depending on Egyption legal books. the dataset is available on **huggingface** [from here](https://huggingface.co/datasets/BoodyAhmedHamdy/EgyLaw-Squad)


you can use it via the **datasets** library

```python
from datasets import load_dataset

dataset = load_dataset("BoodyAhmedHamdy/EgyLaw-Squad")
```

this dataset has some features:
- the **first dataset** in the field of egyption law
- **Specialized** in Personal Status egyption law
- **SQUAD-like** structure 
- small but good to start with **800+ rows**


## Finetuned Model
using our dataset we have to finetune a model for QA task so we used **AraElectra**.

we didn't start from zero but we used a finetuned model on a SQUAD dataset as our base model. you can check our base model from [here](https://huggingface.co/ZeyadAhmed/AraElectra-Arabic-SQuADv2-QA)


after finetuning the model we published it on Huggingface. you can use it via **transformers library**

```python
# Load model directly
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

tokenizer = AutoTokenizer.from_pretrained("BoodyAhmedHamdy/AraElectra-QA-EgyLaw-Squad")
model = AutoModelForQuestionAnswering.from_pretrained("BoodyAhmedHamdy/AraElectra-QA-EgyLaw-Squad")
```

or using **Pipeline**
```python
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("question-answering", model="BoodyAhmedHamdy/AraElectra-QA-EgyLaw-Squad")
```

### Code for Finetuning
you can find the notebook that contains code for finetuning process on **Kaggle** from [here](https://www.kaggle.com/code/boodyahmedhamdy/araelectra-finetuning-huggingface-clone)



