import requests
from bs4 import BeautifulSoup


def extract_problem(html):
    word = html.find("p", {"class": "word"}).string
    answer = html.find("span", {"class": "af_answer"}).string
    word = word[word.find(' ') + 1:]
    return {word: answer}


# TOEIC Scraping
def extract_toeic(day, question):
    URL = f"https://www.hackers.co.kr/?c=s_toeic/new_voca_toeic_testpaper/toeic_study/new_paper&level=1&level_type=1&lang_text=2&question={question}&day1={day}&day2={day}"
    toeic_result = requests.get(URL)
    toeic_soup = BeautifulSoup(toeic_result.text, "html.parser")
    list_box = toeic_soup.find("ul", {"class": "list-box"}).find_all("li")
    toeic_problem = []
    for problem in list_box:
        toeic_problem.append(extract_problem(problem))
    return toeic_problem
