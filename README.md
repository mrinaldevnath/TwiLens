# TwiLens: Analyzing Public Sentiment with Emotion Classification and Summarization

TwiLens is an innovative project that combines emotion classification and abstractive summarization techniques to analyze public sentiment from social media data, particularly Twitter. By leveraging advanced natural language processing (NLP) models, TwiLens aims to provide stakeholders with actionable insights derived from large volumes of tweets.

## Features

- **Emotion Classification**: TwiLens utilizes state-of-the-art transformer-based models, including ALBERT, BERT, DistilBERT, and RoBERTa, to classify tweets into positive, neutral, and negative emotions. These models are fine-tuned using transfer learning techniques on labeled sentiment analysis datasets to optimize performance for the Twitter data domain.

- **Abstractive Summarization**: TwiLens employs cutting-edge summarization models, such as BART, PEGASUS, and T5, to generate concise summaries of the filtered tweets. These models are pre-trained on large-scale datasets and fine-tuned on the filtered tweet dataset to adapt to the specific characteristics of Twitter data.

- **Real-Time Analysis**: TwiLens integrates with the Twitter API, allowing users to provide hashtags of interest and retrieve top tweets in real-time. The pipeline automatically processes the retrieved tweets through the fine-tuned sentiment analysis and summarization models, generating insights on-the-fly.

- **Data Preprocessing**: TwiLens employs comprehensive data preprocessing techniques to ensure the quality and consistency of the input data. This includes text cleaning, normalization, removal of special characters, hashtags, mentions, and URLs, as well as stopword removal.

- **Performance Evaluation**: TwiLens evaluates the performance of the sentiment analysis models using metrics such as accuracy and F1-score, while the quality and coherence of the generated summaries are assessed using standard metrics like ROUGE scores.

## Applications

TwiLens has a wide range of potential applications, including:

- **Understanding Public Complaints**: TwiLens can be used to analyze the reasons behind public complaints by identifying negative sentiment in tweets and generating summaries of the key issues raised.

- **Evaluating Entity Performance**: TwiLens can help evaluate the performance of entities like regions or companies by analyzing public sentiment expressed in tweets related to those entities.

- **Trend Analysis**: By monitoring public sentiment over time, TwiLens can identify emerging trends and shifts in public opinion, providing valuable insights for decision-making processes.

- **Marketing and Brand Monitoring**: TwiLens can be employed to monitor brand perception and track the effectiveness of marketing campaigns by analyzing sentiment in tweets related to specific brands or products.

## Getting Started

To get started with TwiLens, follow these steps:

1. Clone the TwiLens repository: `git clone https://github.com/mrinaldevnath/TwiLens.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up your Twitter API credentials in the configuration file.
4. Run the TwiLens pipeline: `FinalModel.ipynb`

Note: Due to size contrains, the model weights could not be uploaded. Therefore, finetune the models using the code given in FineTune folder
