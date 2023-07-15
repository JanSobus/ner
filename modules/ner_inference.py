from dataclasses import dataclass


import torch
from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline


@dataclass
class Entity:
    entity_group: str
    score: float
    word: str
    start: int
    end: int

    def __post_init__(self):
        entity_types = {"O", "LOC", "PER", "ORG","MISC"}
        if self.entity_group not in entity_types:
            raise ValueError(f"Unrecognized entity type {self.entity_group}")
        self.word = self.word.replace("' ", "'").replace(" '", "'")


class NER_Inference_Simple:
    def __init__(self) -> None:
        self.pipeline = pipeline(
            "ner",
            model="dbmdz/bert-large-cased-finetuned-conll03-english",
            aggregation_strategy="simple",
            ignore_labels=[],
        )

    def predict(self, sequence: str) -> list[Entity]:
        raw_entities = self.pipeline.predict(sequence)

        return [Entity(**re) for re in raw_entities]

# More sophisticated class where you can choose the model and tokenizer - WIP
class NER_Inference_Detailed:
    def __init__(self):
        self.model = AutoModelForTokenClassification.from_pretrained(
            "dbmdz/bert-large-cased-finetuned-conll03-english"
        )
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

    def predict(self, sequence: str):
        inputs = self.tokenizer(sequence, return_tensors="pt")
        tokens = inputs.tokens()
        outputs = self.model(**inputs).logits
        predictions = torch.argmax(outputs, dim=2)

        pred_tuples = [
            (token, self.model.config.id2label[prediction])
            for token, prediction in zip(tokens, predictions[0].numpy())
        ]
        return pred_tuples


if __name__ == "__main__":
    ner = NER_Inference_Simple()
    print(
        ner.predict(
            "Living in New York sure is expensive if you are not Tom Cruise or Micheal Jordan. It's also super challenging."
        )
    )
