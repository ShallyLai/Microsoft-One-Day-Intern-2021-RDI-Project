import json
import random

with open("data_full.json", "r") as input_file:
    json_data = json.load(input_file)

choose_one = random.randint(0, 1540)

#print all article
def list_all_articles(data):
	articles = data["articles"]
	for index, article in enumerate(articles):
		print(f"[{index + 1}] {article['article_title']}")
    
def select_an_article(index, data):
	articles = data["articles"]
	article = articles[index - 1]
	print(
f"""
article_id: {article['article_id']}

article_title: {article['article_title']}

author: {article['author']}

board: {article['board']}

content: {article['content']}

date: {article['date']}

ip: {article['ip']}
"""
	)

def filter_ailishasha(data):
#愛莉莎莎
	articles = data["articles"]
	for index, article in enumerate(articles):
		for key, value in article.items():
			if type(value) is str:
				if "愛莉莎莎"in value:
					print(f"Found 愛莉莎莎 in article index {index}, key {key}, value {value}")
				if type(value) is dict:
					for key_sub, value.sub in value.items():
						if "愛莉莎莎"in value:
							print(f"Found 愛莉莎莎 in article index {index}, key {key}, message include it also {key_sub}") 

def filter_tianshu(data):
#天竺鼠車車
	articles = data["articles"]
	for index, article in enumerate(articles):
		for key, value in article.items():
			if type(value) is str:
				if "天竺鼠車車"in value:
					print(f"Found 天竺鼠車車 in article index {index}, key {key}, value {value}")
				if type(value) is dict:
					for key_sub, value_sub in value.items():
						if "天竺鼠車車"in value:
							print(f"Found 天竺鼠車車 in article index {index}, key {key}, message include it also {key_sub}")


#Components
#list_all_articles(json_data)

select_an_article(choose_one, json_data)

filter_ailishasha(json_data)

filter_tianshu(json_data)
