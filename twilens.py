from transformers import pipeline


class TwiLens:
    def __init__(self) -> None:
        self.classifiermodel = pipeline(
            "sentiment-analysis", model="ClassifierModels/BERT", device=0
        )
        self.summarizermodel = pipeline(
            "summarization", model="SummarizerModels/PEGASUS", device=0
        )

    def get_labels(self, pred):
        label_map = {
            "LABEL_0": "negative",
            "LABEL_1": "positive",
            "LABEL_2": "neutral",
        }
        return label_map[pred["label"]]

    def classifier(self, dataset):
        if type(dataset) != list:
            dataset = dataset.tolist()
        preds = self.classifiermodel(dataset)
        preds = [self.get_labels(pred) for pred in preds]
        return preds

    def summarizer(self, dataset):
        text = " ".join(text for text in dataset)
        summary = self.summarizermodel(text)
        return summary

    def SentimentSummary(self, dataset, sentiment):
        sentiment = sentiment.lower()
        preds = self.classifier(dataset)
        filtered_text = [
            text for text, pred in zip(dataset, preds) if pred == sentiment
        ]
        if len(filtered_text) == 0:
            print(
                f"There are no tweets of {sentiment} sentiment among the ones provided as input."
            )
        else:
            summary = self.summarizer(filtered_text)
            return summary[0]["summary_text"]
