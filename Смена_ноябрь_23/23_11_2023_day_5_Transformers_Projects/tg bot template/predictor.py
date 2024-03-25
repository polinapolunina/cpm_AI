import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModel


class Model:
    def __init__(self):
        # model.save_pretrained("path/to/model")
        # torch.save(model.state_dict(), path)

        name = "ai-forever/ruBert"  # или путь до вашей сохраненной модели
        name = "ai-forever/ruT5-base"  # или путь до вашей сохраненной модели
        self.tkn = AutoTokenizer.from_pretrained(name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(name)

    def __call__(self, input_seq: str) -> str:
        inputs = self.tkn(input_seq, return_tensors="pt")

        with torch.no_grad():
            # if generate
            out = self.model.generate(inputs.input_ids)
            result = self.tkn.decode(out[0], skip_special_tokens=True)
            # result = model(**tokens)

        return result


model = Model()
