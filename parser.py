import json
import os.path

fileObj = open("names.txt", "r") #opens the file in read mode
words = fileObj.read().splitlines() #puts the file into an array
fileObj.close()
names = 1
while True:
	try:
		with open("chat_history.json", "r") as read_file:
			data = json.load(read_file)
			for i in range(9000000):
				'''#get names
				f = open("names.txt", "a",encoding="utf-8")
				f.write(data["Received Saved Chat History"][i]["From"] + '\n')
				f.close()
				lines_seen = set() # holds lines already seen
				#get unique names
				with open("names.txt", "r+") as f:
					d = f.readlines()
					f.seek(0)
					for i in d:
					    if i not in lines_seen:
					        f.write(i)
					        lines_seen.add(i)
					f.truncate()'''
				if data["Received Saved Chat History"][i]["From"] == words[names-1]:
					f = open("extracted/" + words[names-1]+".html", "a",encoding="utf-8")
					f.write("<p style=\"margin-left:40em;margin-right:40em;white-space: nowrap;\" align=\"Left\">")
					f.write(data["Received Saved Chat History"][i]["Created"].replace(" UTC",""))
					f.write("</p>")
					f.write("<p style=\"background-color:powderblue;width:200px;border: 5px solid #1C6EA4;border-radius: 40px 40px 40px 0px;margin-left:40em;margin-right:40em;padding:5px;\">")
					f.write(data["Received Saved Chat History"][i]["Text"])
					f.write("</p>")
					f.write("\n")
					f.close()
				if data["Sent Saved Chat History"][i]["To"] == words[names-1]:
					f = open("extracted/" + words[names-1]+".html", "a", encoding="utf-8")
					f.write("<p style=\"margin-left:65em;margin-right:65em;white-space: nowrap\">")
					f.write(data["Sent Saved Chat History"][i]["Created"].replace(" UTC",""))
					f.write("</p>")
					f.write("<p style=\"background-color:powderblue;width:200px;border: 5px solid #1C6EA4;border-radius: 40px 40px 0px 40px;margin-right:60em;margin-left:60em;padding:5px;\" align=\"right\">")
					f.write(data["Sent Saved Chat History"][i]["Text"])
					f.write("</p>")
					f.write("\n")
					f.close()
	except IndexError:
		file_exists = os.path.exists("extracted/" + words[names-1]+".html")
		if file_exists is True:
			print(words[names-1] + "'s chat extracted Successful")
		else:
			print(words[names-1] + "'s chat extract Unsuccessful")
		if names < 101:
			names = names + 1
		else:
			exit(0)