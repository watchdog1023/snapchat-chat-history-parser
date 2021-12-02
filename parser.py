import json
import os.path

g = open("messagers.html","a")
g.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">")
g.write("<body style=\"background-color:#FAEBD7\">")
g.close()

with open("chat_history.json", "r") as read_file:
	data = json.load(read_file)
	sent = len(data["Sent Saved Chat History"])
	rec = len(data["Received Saved Chat History"])
	if sent > rec:
		mx = sent
	else:
		mx = rec
	for i in range(0,mx):
		if i < rec:
			current = data["Received Saved Chat History"][i]["From"]
			previous = data["Received Saved Chat History"][i-1]["From"]
		if i == 0:
			pass
		if current == previous:
			if i < rec:
				f = open("messagers.html", "a")
				f.write("<p style=\"margin-left:40em;margin-right:40em;white-space: nowrap;\" align=\"Left\">")
				f.write(data["Received Saved Chat History"][i]["Created"].replace(" UTC",""))
				f.write("</p>")
				f.write("<p style=\"background-color:powderblue;width:200px;border: 5px solid #1C6EA4;border-radius: 40px 40px 40px 0px;margin-left:40em;margin-right:40em;padding:5px;\">")
				f.write(data["Received Saved Chat History"][i]["Text"])
				f.write("</p>")
				f.write("\n")
				f.close()
			if i < sent:
				f = open("messagers.html", "a")
				f.write("<p style=\"margin-left:65em;margin-right:65em;white-space: nowrap\">")
				f.write(data["Sent Saved Chat History"][i]["Created"].replace(" UTC",""))
				f.write("</p>")
				f.write("<p style=\"background-color:powderblue;width:200px;border: 5px solid #1C6EA4;border-radius: 40px 40px 0px 40px;margin-right:60em;margin-left:60em;padding:5px;\" align=\"right\">")
				f.write(data["Sent Saved Chat History"][i]["Text"])
				f.write("</p>")
				f.write("\n")
				f.close()
		else:	
			f = open("messagers.html", "a")
			f.write("<p style=\"font-size: large;margin-left:40em;margin-right:40em;\"><b>")
			f.write(data["Received Saved Chat History"][i]["From"])
			f.write("<div style=\"margin-left:40em;margin-right:40em;width: 600px;height: 4px;border-bottom: 3px solid black;position: relative;\"></div></b><br /></p>")
			f.close()
		
h = open("messagers.html","a")
h.write("<p>")
h.write("<div style=\"margin-left:40em;margin-right:40em;width: 600px;height: 4px;border-bottom: 3px solid black;position: relative;\">")
h.write("</p>")
h.write("</body>")
h.close()
file_exists = os.path.exists('messagers.html')
if file_exists is True:
	print("Messages extracted Successful")
else:
	print("Messages extracted Unsuccessful")
