import requests
from bs4 import BeautifulSoup


# TOEIC Scraping
def extract_toeic(day, question):
    URL = f"https://www.hackers.co.kr/?c=s_toeic/new_voca_toeic_testpaper/toeic_study/new_paper&level=1&level_type=1&lang_text=2&question={question}&day1={day}&day2={day}"
    toeic_result = requests.get(URL)
    toeic_soup = BeautifulSoup(toeic_result.text, "html.parser")
    list_box = toeic_soup.find("ul", {"class": "list-box"})
    words_list = list_box.find_all("p", {"class": "word"})
    answers_list = list_box.find_all("span", {"class": "af_answer"})

    word = []
    answer = []
    for n in words_list:
        temp = n.string
        temp = temp[temp.find(' ') + 1:]
        word.append(temp)

    for n in answers_list:
        answer.append(n.string)
    return (word, answer)
