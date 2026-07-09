# Introduction
This repository is created to solve main nlp tasks for educational puproses. For each task there is a separate notebook that solves this task on a particular dataset. The following problems are solved here: text clasification, token classification, NER, embedding learning, text generation, text translation, summarization. Training artifacts can be found at this [google drive folder](https://drive.google.com/drive/folders/1sB6qpR5yn_is7U1hBhauwLUWmD-kE4Mm?usp=sharing)

## Text classification
The dataset that was used for classification task can be found [here](https://huggingface.co/datasets/mteb/emotion). The following model were trained to solve this task: Dummy, TF-IDF + Linear layer, RNN, LSTM, GRU, BERT. Results are present in the following table:

<table>
  <tr>
    <th></th>
    <th>Dummy</th>
    <th>TF-IDF + Linear</th>
    <th>RNN(300, 300)</th>
    <th>LSTM(300, 300)</th>
    <th>GRU(300, 300)</th>
    <th>BERT-base-uncased</th>
  </tr>
  <tr>
    <th>F1-score</th>
    <td>0.084</td>
    <td>0.716</td>
    <td>0.302</td>
    <td>Data 4</td>
    <td>Data 5</td>>
    <td>Data 6</td>
  </tr>
</table>
