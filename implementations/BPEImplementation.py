from typing import List
from tqdm import tqdm

def encode_corpus(corpus: List[str], size = 200, special_tokens = ["<pad>", "<unk>"]):
    current_vocabulary = {k: special_tokens[k] for k in range(len(special_tokens))}
    unique_characters = set()
    # Create initial unique tokens
    for text in corpus:
        tokens = text.split()
        for token in tokens:
            unique_characters.update(list(token.lower()))
    # Updating dictionary with unique characters
    if len(list(current_vocabulary.keys())) != 0:
        last_key = list(current_vocabulary.keys())[-1] + 1
    else:
        last_key = 0
    for char in unique_characters:
        current_vocabulary[last_key] = char
        last_key += 1
    # Updating the dictionary by learning the merges
    while len(current_vocabulary) <= size:
        merged_counted = {}
        for voc_token in current_vocabulary.values():
            for text in corpus:
                for word in text.lower().split():
                    id_start = word.find(voc_token)
                    # check if pattern found
                    if id_start != -1:
                        id_end = id_start + len(voc_token) + 1
                        try:
                            merged = word[id_start : id_end]
                        except IndexError:
                            continue
                        try:
                            if merged not in list(current_vocabulary.values()):
                                merged_counted[merged] += 1
                        except KeyError:
                            merged_counted[merged] = 1
                    else:
                        continue
        if len(merged_counted) != 0:
            # Get last key of vocabulary
            if len(list(current_vocabulary.keys())) != 0:
                last_key = list(current_vocabulary.keys())[-1] + 1
            else:
                last_key = 0
            # Get item to be moved
            current_key = None
            current_count_value = 0
            for merged_key in merged_counted:
                if merged_counted[merged_key] > current_count_value:
                    current_count_value = merged_counted[merged_key]
                    current_key = merged_key
            current_vocabulary[last_key] = current_key
        else:
            break
    return current_vocabulary
    # finding the most frequent pair and updating




corpus = [
    "This is the Hugging Face Course.",
    "This chapter is about tokenization.",
    "This section shows several tokenizer algorithms.",
    "Hopefully, you will be able to understand how they are trained and generate tokens.",
    "This algorithm just don't want to work, Hopefully it will work"
]
    





if __name__ == "__main__":
    result = encode_corpus(corpus, size = 200, special_tokens = ["<pad>", "<unk>"])
    print(result)