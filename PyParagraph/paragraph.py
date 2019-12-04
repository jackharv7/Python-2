import re

sent_count = -1
letter_count = 0
count = 0
with open("paragraph2.txt") as inputfile: 
    text = inputfile.read()
    for letters in text:
        if not letters.isalpha():
            continue
        for letter in letters:
            letter_count +=1
    split_words = re.split(" ", text)
    for words in split_words:
        count += 1
    split_sent = re.split("(?<=[.!?])", text)
    for sents in split_sent:
        sent_count += 1
    avg_sent_length = count/sent_count
    avg_letter_count = letter_count/count

text_summary = """
    Paragraph Analysis
--------------------------
Approximate Word Count: {count}
Approximate Sentence Count: {sent_count}
Average Letter Count: {avg_letter_count:.2f}
Average Sentence Length: {avg_sent_length:.2f}""".format(count=count,sent_count=sent_count,avg_sent_length=avg_sent_length,avg_letter_count=avg_letter_count)

print(text_summary)