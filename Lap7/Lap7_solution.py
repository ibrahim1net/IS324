import json
import threading
import time
import requests
from bs4 import BeautifulSoup
import datetime

# Exercise 1

# List of tweets
tweetsList = []


# Insert txt file to the list
def insertToList(fileTxt):
    file = open(fileTxt, 'r')
    print(f"Inserting {fileTxt} to the array of lists....")
    line = file.readline()
    while line != '':
        line = line.rstrip("\n")
        y = json.loads(line)
        newStr = f"{str(y['created_at'])}, {str(y['user']['screen_name'])}, {str(y['text'])}"

        # insert every string to the list
        tweetsList.append(newStr)
        line = file.readline()
    file.close()

def save_output(fileName):
    output = open(fileName, 'w', encoding="utf-8")
    for i in tweetsList:
        json_obj = json.dumps(i, indent=1)
        output.write(json_obj + "\n")

    # closing the files
    output.close()

# From starting
start_exercise1 = time.time()

insertToList('TweetsDataPart1.txt')
insertToList('TweetsDataPart2.txt')
insertToList('TweetsDataPart3.txt')
print(f"The total tweets is: {len(tweetsList)}")

save_output('output.txt')

# Ending from the writing file
end_exercise1 = time.time()

result_ex1 = end_exercise1-start_exercise1
print(f"** Total Execution Time for exercise 1 is: {result_ex1} sec(s)")

print("=====================================")

# Exercise 2


start_exercise2 = time.time()
# clear the list
tweetsList = []
files = ['TweetsDataPart1.txt', 'TweetsDataPart2.txt', 'TweetsDataPart3.txt']
thList = []

for f in files:
    i = threading.Thread(target=insertToList, args=(f, ))
    thList.append(i)
    i.start()

for t in thList:
    t.join()

o = threading.Thread(target=save_output, args=('output_usingThread.txt', ))
o.start()
o.join()

print(f"The total tweets is : {len(tweetsList)}")

end_exercise2 = time.time()
result_ex2 = end_exercise2-start_exercise2
print(f"** Total Execution Time is for exercise 2 by using thread is: {result_ex2} sec(s)")

# Report how much this approach is faster than the one in Exercise 1 ?
print(f"Exercise 2 is faster than Exercise 1 {result_ex1-result_ex2 }")

print("=====================================")
# Exercise 3


now = datetime.datetime.now()
now = now.strftime("%d-%m-%Y_%H-%M-%S")
filename = "TS-Stocks("+str(now)+").txt"


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
res = requests.get('https://simplywall.st/stocks/sa/telecom/market-cap-large?page=1',headers=headers)


if res.status_code == 200:
    f = open(filename, 'w', encoding='utf-8')
    soup = BeautifulSoup(res.content, 'html.parser')
    results = soup.find("tbody")
    results = results.find_all("tr")

    for ele in results:
        name = ele.find("span",class_="sc-j5xpw7-10 yAyuW").text
        price = ele.find("span", class_="sc-j2jiwi-0 sc-n7l64u-1 hxrYKN dGQEKd").text
        formateTxt = f"{name} {price}"
        f.write(formateTxt + "\n")

    # closing the file
    f.close()
else:
    print("Website Error must return 200 Ok response")


