import sqlite3
from datadict import keyword_dict

# conn = sqlite3.connect('complaint_data.db')
# c = conn.cursor()


# top 10 keywords from a given dept(user selected)[dict]
# top 10 tweets in that dept [list]

def top_by_dept(dept_name):
	'''
	Returns top 10 most frequent keywords by dept.
	params:
	dept_name : string
	'''
	conn = sqlite3.connect('complaint_data.db')
	c = conn.cursor()
	counts = []
	keyword = []

	for word in keyword_dict[dept_name]:
		keyword.append(word)
		c.execute(f'''SELECT COUNT(Category) FROM complaints WHERE Subcategory LIKE '%{word}%';''' )
		cnt = c.fetchone()[0]
		counts.append(cnt)

	freq = dict(zip(keyword, counts))
	freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

	if len(freq) < 10:
		return freq

	return freq[:10]

	conn.commit()
	conn.close()



def top_tweets(keyword_name):
	'''
		Returns a list of top 10 tweets in the given dept.
		params:
		dept_name : string
	'''
	conn = sqlite3.connect('complaint_data.db')
	c = conn.cursor()

	tweets = []
	c.execute(f'''SELECT Subcategory FROM complaints WHERE Subcategory LIKE '%{keyword_name}%' ORDER BY Date LIMIT 10;''')
	text = c.fetchall()
	for t in text:
		tweets.append(t)

	return tweets




