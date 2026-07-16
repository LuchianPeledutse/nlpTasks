# Introduction
This repository is created to solve main nlp tasks for educational puproses. For each task there is a separate notebook that solves this task on a particular dataset. The following problems are solved here: text clasification, token classification, NER, embedding learning, text generation, text translation, summarization. Training artifacts can be found at this [google drive folder](https://drive.google.com/drive/folders/1sB6qpR5yn_is7U1hBhauwLUWmD-kE4Mm?usp=sharing). There are also implementations of NLP-related algorithms in implementations folder.

## Text classification
The dataset that was used for classification task can be found [here](https://huggingface.co/datasets/mteb/emotion). The following models were trained to solve this task: Dummy, TF-IDF + Linear layer, RNN, LSTM, GRU, BERT. BERT training script is located [here](https://colab.research.google.com/drive/1ZEU4bdtIYlJEUvySwG7-ckUcXwxiRTTs?usp=sharing). The results are present in the following table:
<table>
  <tr>
    <th></th>
    <th>Dummy</th>
    <th>TF-IDF + Linear</th>
    <th>RNN(300, 300)</th>
    <th>LSTM(300, 300)</th>
    <th>LSTM(300, 300, bidirectional = True)
    <th>GRU(300, 300)</th>
    <th>BERT-base-uncased</th>
  </tr>
  <tr>
    <th>F1-score</th>
    <td>0.084</td>
    <td>0.716</td>
    <td>0.302</td>
    <td>0.629</td>
    <td>0.620</td>
    <td>0.597</td>
    <td>0.64</td>
  </tr>
</table>

## Token classification
The dataset that was used for russian token classification can be found [here](https://drive.google.com/drive/folders/1yfYMyWkLj98at8OX8lSmjBoGu0_5ep3-?usp=sharing). Here are some examples of dataset:
|Words|tags |
|:----|-----|
|<beg>|<beg>|
|  я  | PRON|
| мою | VERB|
|Окно | NOUN|
|<end>|<end>|

The model was trainined for 6 hours on provided dataset. Here is an example of model inference: 
|Words | Predicted tag|
|:-----|--------------|
|Он    |     PRON     |
|пошел |     VERB     |
|гулять|     VERB     |

## NER task
Here is going to be inforamtion on NER task
