import random
import json
import pyttsx3
engine = pyttsx3.init() # object creation
engine.setProperty('rate', 125)

"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1


"""VOICE"""

voices = ["englisg+f1","english+f2","english+m1","english+m3","english+m2","english_rp+m2"]

d = {
	"zen101":[
		{"title":"A cup of tea",
		"story":[
			{"voice":"1","text":"Nan-in, a Japanese master during the Meiji era (1868-1912) received a university professor who came to inquire about Zen."},
			{"voice":"1","text":"Nan-in saved tea. He poured his visitor's cup full, and then kept on pouring."},
			{"voice":"1","text":"The professor watched the overflow until he no longer could restrain himself."},
			{"voice":"2","text":"It is overfull. No more will go in"},
			{"voice":"3","text":"Like this cup,You are full of your own opinions and speculations. How can I show you Zen unless you first empty your cup?"},
			]
		},
		{"title":"Is That So?",
		"story":[
			{"voice":"1","text":"The Zen master Hakuin was praised by his neighbors as one living a pure life."},
			{"voice":"1","text":"A beautiful Japanese girl whose parents owned a food store lived near him. Suddenly, without any warning her parents discovered she was with child."},
			{"voice":"1","text":"This made her parents angry. She would not confess who the man was, but after much harassment at last named Hakuin."},
			{"voice":"1","text":"In great anger the parents went to the master. 'Is that so?' was all he would say."},
			{"voice":"1","text":"After the child was born it was brought to Hakuin. By this time he had lost his reputation, which did not trouble him, but good care of the child. He obtained milk from his neighbors and everything else the little one needed."},
			{"voice":"1","text":"A year later the girl-mother could stand it no longer. She told her parents the truth - that the real father of the child was a in the fish market."},
			{"voice":"1","text":"The mother and father of the girl at once went to Hakuin to ask his forgiveness, to apologize at length, and to get the child back again."},
			{"voice":"1","text":"Hakuin was willing. In yielding the child, all he said was"},
			{"voice":"2","text":"Is that so?"}
			]
		},
		{"title":"The Moon cannot be Stolen",
		"story":[
			{"voice":"1","text":"Ryokan, a Zen master, lived the simplest kind of life in a little hut at the foot of a mountain. One evening a thief visited the hut only to discover there was nothing in it to stea1."},
			{"voice":"1","text":"Ryokan returned and caught him."},
			{"voice":"2","text":"You may have come a long way to visit me and you should not return empty-handed. Please take my clothes as a gift."},
			{"voice":"1","text":"The thief was bewildered. He took the clothes and slunk away.Ryokan sat naked, watching the moon."},
			{"voice":"2","text":"Poor fellow, I wish I could give him this beautiful moon."},
			{"voice":"1","text":"No one can steal your beautiful heart"}
			]
		},
		{"title":"Muddy Road",
		"story":[
			{"voice":"1","text":"Tanzan and Ekido were once traveling together down a muddy road. A heavy rain was still falling."},
			{"voice":"1","text":"Coming around a bend, they met a lovely girl in a silk kimono and sash, unable to cross the intersection."},
			{"voice":"2","text":"Come on, girl"},
			{"voice":"1","text":"said Tanzan at once. Lifting her in his arms, he carried her over the mud."},
			{"voice":"1","text":"Ekido did not speak again until that night when they reached a lodging temple. Then he no longer could restrain himself."},
			{"voice":"3","text":"We monks don't go near females, especially not young and lovely ones. It is dangerous. Why did you do that?"},
			{"voice":"2","text":"I left the girl there, Are you still carrying her?"}
			]
		},
		{"title":"Learning to be Silent",
		"story":[
			{"voice":"1","text":"The pupils of the Tendai School used to study meditation before Zen entered Japan. Four of them who were intimate friends promised one another to observe seven days of silence."},
			{"voice":"1","text":"On the first day all were silent Their meditation had begun auspiciously, but when night came and the oil-lamps were growing dim one of the pupils could not help exclaiming to a servant"},
			{"voice":"2","text":"Fix those lamps"},
			{"voice":"1","text":"The second pupil was surprised to hear the first one talk."},
			{"voice":"3","text":"We are not supposed to say a word"},
			{"voice":"4","text":"You two are stupid. Why did you talk?"},
			{"voice":"1","text":"asked the third"},
			{"voice":"5","text":"I am the only one who has not talked"},
			{"voice":"1","text":"muttered the fourth pupil."}
			]
		}
		]
	}


# with open("zenstories.json", "w") as write_file:
#     json.dump(d, write_file, indent=4)
# print("Done writing PrettyPrinted JSON data into file with indent=4")

# print (len(d["zen101"]))
n = random.randint(0,4)
print(d["zen101"][n]["title"])
lines = d["zen101"][n]["story"]
# print(lines)
for i in range(len(lines)):
	x = int(lines[i]["voice"])
	# print(voices[x])
	engine.setProperty('voice',voices[x]) 
	engine.say(lines[i]["text"])

engine.runAndWait()
engine.stop()

# For ubuntu
# 1 install pyttsx3
# 2 install espeak