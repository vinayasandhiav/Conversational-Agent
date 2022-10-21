
# coding: utf-8

# In[2]:


import pandas as pd
import pyttsx3
import speech_recognition as sr
import joblib


# In[6]:


df=pd.read_csv("Corpus_to_test.csv",encoding='latin-1')
df.head()


# In[7]:


questions=df['Question'].values.tolist()
questions


# In[8]:


labels=df['S.No'].values.tolist()


# In[9]:


answers=df['Answers'].values.tolist()
answers


# In[3]:


bow_vectorizer=joblib.load("bow_vectorizer.joblib")
classifier=joblib.load("model_MNB.joblib")


# In[13]:

#rec_user=0
#rec_bot=0
class ChatBot:
	exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later", "stop")
	def start_chat(self):
		engine = pyttsx3.init()
		engine.say("Hi, I'm a bot,How can i help you")
		engine.runAndWait()
		r = sr.Recognizer()
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source, duration=0.5)
			print("user response recording started...")
			audio = r.listen(source)
			print("finished recording")
			try:
				user_response = r.recognize_google(audio)
				print("user: ",user_response)
			except:
				print("could not understand audio")
				user_response="repeat"
        #user_response = input("Hi, I'm a bot,How can i help you?\n")
		self.chat(user_response)
  
	def chat(self, reply):
		rec_bot=0
		rec_user=0
		while not self.make_exit(reply):
			qns=self.generate_response(reply)
			print("BOT:",qns)
			engine = pyttsx3.init()
			engine.say(str(qns))
			engine.save_to_file(qns, 'bot/rec_bot{}.mp3'.format(str(rec_bot)))
			rec_bot+=1
			engine.runAndWait()
			r = sr.Recognizer()
			with sr.Microphone() as source:
				r.adjust_for_ambient_noise(source, duration=0.5)
				print("user response recording started...")
				audio = r.listen(source)
				print("finished recording hh")
				with open("user/rec_user{}.wav".format(str(rec_user)), "wb") as f:
					f.write(audio.get_wav_data())
					rec_user+=1
			try:
				reply = r.recognize_google(audio)
				print("user: ",reply)
			except:
				print("could not understand audio")
				user_response="repeat"
				reply="repeat"
            #print(qns+"\n")
            #reply = input(qns+"\n")
		return
  
	def generate_response(self, ans):
		input_vector = bow_vectorizer.transform([ans])
		predict = classifier.predict(input_vector)
		index = int(predict[0])
		#print("Accurate:",str(classifier.predict_proba(input_vector)[0][index-1] * 1000)[:5] + "%")
		return answers[index-1]
		print()
	def make_exit(self, reply):
		for exit_command in self.exit_commands:
			if exit_command in reply:
				engine = pyttsx3.init()
				engine.say("Ok, have a great day!")
				engine.runAndWait()
				print("Ok, have a great day!")
				return True
		return False

# In[17]:


#etcetera = ChatBot()
#etcetera.start_chat()

