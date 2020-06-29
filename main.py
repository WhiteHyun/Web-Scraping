from toeic import extract_toeic

MIN_NUM_PROBLEM = 20
MAX_NUM_PROBLEM = 40

word, answer = extract_toeic(1, MIN_NUM_PROBLEM)
print(word)
print(answer)
