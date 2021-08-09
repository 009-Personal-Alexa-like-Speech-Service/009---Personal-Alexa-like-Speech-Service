# 009 - Personal Alexa-like Speech Service :loudspeaker:
## Implement an Alexa alike speech service in Python "Natural Language Processing"


- Kim Celine Marzi [843594]
- Melina Bröcker [862393]
- Maximilian Schmitt [872765]
- Thomas Zeutschler

- - - -

# Table of contents
1. [Introduction](#introduction)
2. [Some paragraph](#paragraph1)
    1. [Sub paragraph](#subparagraph1)
3. [Another paragraph](#paragraph2)




## Table of Content

###1. Business Understanding(#introduction)

 1.1 [Determine business objectives ](#subparagraph1)
 
 1.2 [Assess situation](#subparagraph2)
 
 1.3 Determine data mining goals(#subparagraph3)
 
###2. Methological approach(#paragraph1)

###3. Findings and achievements(#paragraph2)

 3.1 Problems(#subparagraph1)
 
 3.2 Achievements(#subparagraph1)
 
###4. Summary(#paragraph3)

###5. Potential future developments(#paragraph4)



## 1) Business Understanding 🧠

*In our Business Understanding the business question and problem is described. The goal and what we intended to archieved is written down in detail.* 


### Use Case 

**Example: program a Speech Regognition**
To start very easy we wrote down the following short use case:

  * Me: HAL, please... Can someone else help me?

  * You: No problem, I'm a Python hero!

**Target** :memo:

Out goal is to develop a voice control system that responds to the command "Hello Hal". After a user starts the speech asistant he should start listening and process the spoked words. Furthermore Hal should be able to give a spoken answer. 
It should contain the follwing features which are mentioned below and give action to that. Moreover we want to create a complete Github repository with our code and a detailed description about our project. 
The project started April 2021 und will be finised in August 2021. It was carried out as a part of our masters degress "Business Analytics".   

**Features**

We want to implement the features listed below:

   * Recognize simple question e. g. "How are you", "What is your name?" or „Hello Hal, tell me a joke“
   * Give information about the weather „Hello Hal, hows the weather today?“  
   * Give information about the time
   * Open a browser (google.com)  
   * Set an alarm     
   * Implement google standard answers  
   * Save document (e. g. speech to text)  
   * Compute two numbers 
   * Implement entities like cities, companies etc. (e. g. "Apple" , "New York")


Now we designed a detailled process: 
<img width="802" alt="image" src="https://user-images.githubusercontent.com/83068247/126769181-02856317-7fe9-441d-88bc-3736bfaf9fa2.png">

[Flowchart.pdf](https://github.com/009-Personal-Alexa-like-Speech-Service/009---Personal-Alexa-like-Speech-Service/files/6868056/Flowchart.pdf)

### Process Flow Chart 

Below we designed a flow chart how our speech recognition works in three steps:
<img width="1044" alt="Bildschirmfoto 2021-06-03 um 18 31 40" src="https://user-images.githubusercontent.com/83067079/120679900-fb4b7980-c499-11eb-87d2-a69cd24ddc16.png">



### Crisp-DM :arrows_counterclockwise:

![Bildschirmfoto 2021-07-22 um 14 42 57](https://user-images.githubusercontent.com/83067079/126640843-1aee7caa-a5a0-4de4-b686-fa84477ad5d7.png)

## Read me specify Business Understanding (CRISP DM) 

**1.1 Determine Business Objectives**

**Background**

&rightarrow; The basic basic steps for how speech recognition technology works are as follow:
* A microphone transmits the vibrations of a person’s voice into a wavelike electrical signal.
* This signal in turn is converted by the system’s hardware—a computer’s sound card, for examples—into a digital signal.
* The speech recognition software analyzes the digital signal to register phonemes, units of sound that distinguish one word from another in a particular language.
* The phenomes are reconstructed into words.

* Speech recognition software works by breaking down the audio of a speech recording into individual sounds, analyzing each sound, using algorithms to find the most probable word fit in that language, and transcribing those sounds into text.

**Business Objectives**
* The goal is to develop a voice control system that responds to the command: "Hello Hal"

**Business Success Criteria**
* Language Support 
* The solution should be capable of multi-language support and detect words/phrases with an high accuracy.


**1.2 Assess Situation**

**Inventory of Resources, Requirements, Assumptions and Constraint**
&rightarrow; Here are the different models used to build a speech recognition system:

* Acoustic: Take the waveform of speech and break it up into small fragments to predict the most likely phonemes in the speech.
* Pronunciation: Take the sounds and tie them together to make words, i.e. associate words with their phonetic representations.
* Language: Take the words and tie them together to make sentences, i.e. predict the most likely sequence of words (or text strings) among several a set of text strings.

**Risks and Contingencies Terminology. Costs and Benefits**
* To further highlight the challenge, speech recognition systems have to be able to distinguish between homophones (words with the same pronunciation but different meanings), to learn the difference between proper names and separate words (“Tim Cook” is a person, not a request for Tim to cook), and more.
* After all, speech recognition accuracy is what determines whether voice assistants become a valuable accessory.

&rightarrow;	Word-error rate has its limitations, though. The data is affected by factors like:
- Background noise
- Crosstalk
- Accents
- Rare words
- Context


**1.3 Determine Data Mining Goals**

**Data Mining Goals**
* General speech recognition (text to speech & speech to text)
* Segmentation of captured speech into words, phrases and sentences
* Function recognition of individual words within a sentence (i.e. subject, verb, object, etc.)
* analysis of sentence context, sentence relationships and entities

**Data Mining Success Criteria**
* Human language is complex and does not always follow logical rules. Words have many variants and meanings, some of which can only be grasped through the context of the content. Thus, it is extremely difficult for programs to recognize subliminal meanings in texts. 
-	This is why it is essential for the software to use an extensive structured database. 
-	The more data available, the better the language models work in recognizing patterns and rules.




### How Speech Recognition Works – An Overview

**To get a complete overview about the business problem it was necessary for us to understand how the speech recognition process itself works.** 

To show the speech recognition process in an easy way we added the figure below. 

![Bildschirmfoto 2021-07-22 um 14 50 18](https://user-images.githubusercontent.com/83067079/126641716-979eb9bd-42e0-4e97-9cf4-ecb88914520a.png)
(Source:https://towardsdatascience.com/speech-recognition-in-python-the-complete-beginners-guide-de1dd7f00726)


**Now we want to give a detailed description of the process:*

The first component of speech recognition is speech. Speech must be **converted from physical sound to an electrical signal** with a microphone, and then to **digital data with an analog-to-digital converter**. Once the speech is digitized, several models can be used to transcribe the audio to text. Most modern speech recognition systems rely on **Hidden Markov Model (HMM).** This approach works on the assumption that a speech signal, when viewed on a short enough timescale, can be reasonably approximated as a stationary process—that is, a process in which statistical properties do not change over time.

One can imagine that this whole process may be computationally expensive. In many modern speech recognition systems, neural networks are used to simplify the speech signal using techniques for feature transformation and dimensionality reduction before HMM recognition. Voice activity detectors (VADs) are also used to reduce an audio signal to only the portions that are likely to contain speech. This prevents the recognizer from wasting time analyzing unnecessary parts of the signal.

While programming, we don't have to worry about about that speech recognition process. There are several speech services/ packages available to help us with that. But we will explained the used packages later on. 
*(Source: https://realpython.com/python-speech-recognition/)*

1. **Configure Microphone**: It is advisable to specify the microphone during the program to avoid any glitches (use laptop microphone or headphones)
2. **Set Chunk Size:** This basically involved specifying how many bytes of data we want to read at once. Typically, this value is specified in powers of 2 such as 1024 or 2048
3. **Set Sampling Rate:** Sampling rate defines how often values are recorded for processing
4. **Set Device ID to the selected microphone:** In this step, we specify the device ID of the microphone that we wish to use in order to avoid ambiguity in case there are multiple microphones. This also helps debug, in the sense that, while running the program, we will know whether the specified microphone is being recognized. During the program, we specify a parameter device_id. The program will say that device_id could not be found if the microphone is not recognized.
5. **Allow Adjusting for Ambient Noise:** Since the surrounding noise varies, we must allow the program a second or too to adjust the energy threshold of recording so it is adjusted according to the external noise level.
6. **Speech to text translation:** This is done with the help of Google Speech Recognition. This requires an active internet connection to work. However, there are certain offline Recognition systems such as PocketSphinx, but have a very rigorous installation process that requires several dependencies. Google Speech Recognition is one of the easiest to use.




### Some of the factors that make programming a speech recognition more difficult are 

* **The complexity of spoken language.** In English, many words have multiple meanings depending on the context – for example “red” and “read” sound exactly the same but have completely different meanings.
* **People talk fast** – When we speak, we don’t break our sentences up into individual words – we kind of just blurt it all out in one long string of sounds with few breaks. This makes it difficult to determine where a word ends and the next one begins.
* **Nobody speak in the same way** – It’s no good to have a system that needs to be reprogrammed for every individual. A system needs to be able to hear a new voice and understand it immediately.
* **Background noise** – Differentiating the speech from the background noise is very difficult. This is especially true if the background noise is also speech (say in a class).



- - - -


## 2) Methological approach

The first step is to install all necessary libraries. 

* **numpy**
 &rightarrow; for working with numerical data 

NumPy (Numerical Python) is an open source Python library used in most scientific and technical fields. It is the standard for working with numerical data in Python. It is used to perform mathematical operations on arrays, such as trigonometric, algebraic and statistical routines. The library contains a lot of mathematical, algebraic and transformation functions.

* **Speech Recognition** 
 &rightarrow; speech to text 

Google has a speech recognition API. This API converts spoken text (microphone) to written text (Python string), called Speech to Text. You can simply speak into the microphone and the Google API will translate it into written text. This program takes the audio from your microphone, sends it to the Speech API, and returns a Python string.

The audio is recorded using a speech recognition module, which is included in the program above. Next, we send the recorded speech to the Google Speech Recognition API and return the output.


* **PyAudio**
 &rightarrow;  for usage of audio input and output

Pyaudio is a Python link for PortAudio, a cross-platform audio input and output library. This basically means that we can use Pyaudio to record and play audio across all platforms and operating systems, such as Windows, Mac and Linux.

![grafik](https://user-images.githubusercontent.com/83067202/124469715-fe889c80-dd9a-11eb-84d3-fbd0e0d544b0.png)


* **spacy**
  &rightarrow; natural language processing 

spaCy is a huge library with many functions. Below we list a few of these function as an overview. It is a open source library for Natural Language Processing (NLP) in Python. Natural Language Processing captures natural language and texts and processes them with the help of algorithms and other rules. 

<img width="515" alt="image" src="https://user-images.githubusercontent.com/83068247/123808167-cb549200-d8f0-11eb-9878-4093c406b6f1.png">


The goal of natural language processing is to make language and texts understandable for computers in order to operate or control them by speech. To extract meaning from speech or texts, it is necessary to understand not only individual words, but also entire sentences, contexts or topics. 

Natural Language Processing starts with tokenisation. In this step, the text is divided into tokens. Tokens are words, spaces or punctuation marks. There are models with their own tokenisation rules for each language. 

Part-of-speech (POS) tagging assigns grammatical properties such as verb, adjective, noun or adverb to the words.

Another step is lemmatisation. Here, the individual words are traced back to their basic forms. 

With the help of Named Entity Recognition, it is possible to assign persons, places, times or other objects like company names to the recognised entities. 
Dependency parsing assigns syntax dependencies to the identified and tagged tokens. Word vectors are used to describe and recognise relationships between words. 


<img width="542" alt="image" src="https://user-images.githubusercontent.com/83068247/123808008-a6601f00-d8f0-11eb-833e-7cd011f4b2f7.png">




* **pyttsx3**
  &rightarrow; text to speech conversion

Is a text-to-speech conversion library used in Python. It works offline and is compatible with Python 2 and 3.
In our case it is used to make the computer talk to us.


### Defined classes 


In the following, we wrote a description of which classes are implemented and what functions they contain. We would like to create an appropriate GitHub repository with our code and a detailled description. 


 **Class: Main** (file main.py) We start our speech assistant Hal in our main-file.
 - The main file actives our Hal class. 
 
**Class: Hal** (file hal.py) Hal is our speech assistant :older_man:
- He starts  to record audio when option 1 in the main menu is chosen
- After three seconds of break he stopps recording 
- If he does not understand the spoken words he gives an error
- If option 2 is chosen he turns off
- And if another input is give, Hal says that he did not understand and asks to repeat the input 

 **Class: Recorder** (file recorder.py) :video_camera:
- The Recorder class imports "speech recognition" as a library. 
- We defined a microphone and that the recording will stopp after three seconds of break. 

 **Class: Listener** (file listener.py) :ear:
 - The Listener class returns the spoken words as a text. 
 
 **Class: Speaker** (file speaker.py) 🔈
- Our speaker class gives Hal the opportunity to speak. For that we initialized a library "pyttsx3" which is explained in 2.0. 

 **Class: Interpreter** (file interpreter.py) ⏳
- The interpreter recognises an input of spoken words and is able to process the correct answer which is defined in each of our recognizer classes.
 
 **Class: Utilities** (file utilities.py) 📂
- We defined the clear screen method in our utilities data. So after every speech recognition command the sceen will be cleared. 
- Furthermore we defined Hals standard answer "Sorry Dave, I'm afraid I can't do this"

 **Class: Recognizer** (file recognizer.py)
 - The recognizer is our main class for natural language processing. It works with inheritance for all the classes listed below and also named "Recognizer..." 
 
 **Class: Recognizertime** (file recognizertime.py)
-  This class returns the current time of the following questions. And returns a standard answer if it's not one of the defined questions.

 **Class: Recognizersimple** (file recognizersimple.py)
 - This class returns in comparison to a default text the correct answer to an input question.

 **Class: Recognizersimplemath** (file recognizersimplemath.py)
 - With an input of numbers, Hal is able to return the correct answer due to the mathematical implementation of the given operators. Which are defined in this 
   class. Also the statistical methods like the interpreter function is able to analyze the syntax for nouns and verbs and finds named entities, phrases and  concepts. The dump function returns for the tokens which are contained in the document which returns token attributes like readable string representations of an attribute. And the isfloat function returns a true for a numeric float or false if it's not the case.

 **Class: Recognizernamedentities** (recognizernamedentities.py)
 - Recognizes named entities like people names, city names etc.


**Process of the classes**

<img width="579" alt="image" src="https://user-images.githubusercontent.com/83068247/126769739-0260daea-d009-4236-b585-61c11eb690f9.png">

[Process of the classes.pdf](https://github.com/009-Personal-Alexa-like-Speech-Service/009---Personal-Alexa-like-Speech-Service/files/6868104/Process.of.the.classes.pdf)



- - - -



## 3) Findings and achievements :construction:
- Detailed description of approach, work, findings, concrete achievements 

:warning: First we will start with problems we had during our project and how we solved these problems :warning:

#### 1. Problems 
##### 1.1 Installation 

There was a problem to install the package "PyAudio". We found two different solutions for Mac and Windows to solve the shown error. 


1.)For **Windows** type the following command into the Pycharm console:
* pip install pipwin
* pipwin install pyaudio :heavy_check_mark:

After the pip command is installed, the installation of PyAudio should work as well. 

2.) For **Mac** type the following command into the Pycharm console:
* "install homebrew"
afterwards use:
* brew install portaudio
* pip install pyaudio 
* *https://www.youtube.com/watch?v=1oolnK1g6jw* &rightarrow; This youtube video explains step by step how to install PyAudio on a Mac :heavy_check_mark:

or

* pip3 install pyaudio :heavy_check_mark:



3.) There was a problem to install the package "Spacy". We found a solution for Mac and Windows. Type the following code in your terminal:


* As a first command: *pip install -U spacy*

* Afterwards this one *python -m spacy download en_core_web_sm* :heavy_check_mark:



##### 1.2 Manual push request

1.) Type in your terminal:

* cd desktop
* And your project path with git push at the end
* Before pushing you need to fetch and merge :heavy_check_mark:

![image](https://user-images.githubusercontent.com/83068247/122056101-91ac6300-cde9-11eb-9ed2-5768d8b7567e.png)


#### 2. Achievements  

In this part we want to give a detailed description how the speech recogntion is used and what features we implemented. 
* To start our speech recognition the "main"-class should be run. You will be asked if the speech assistant Hal should start listening (press button 1) or if Hal should turn off (press button 2). If another input than 1 or 2 is given Hal will tell you it was a "wrong command"
* If number 1 is chosen Hal tells you that he is activated now, starts listening and says that he needs three seconds break before he answers. 
* Now we have various options what to ask and say to Hal:
* 1. What's his name or how old he is (commands: "How old are you?", "What is your age?", "What is your name?"
* 2. How he is feeling today (e. g. command: "How are you?")
* 3. Or ask him for a joke (e. g. command: "Tell me a joke"
* 4. Ask about the current time (e. g. command: "What's the time?")
* 5. Ask for a simple math taks (e. g. "5 * 5")
* In the next step Hal will give you an answer. If he did not undestand what you said, he will ask to repeat. 

- - - -



## 4) Summary :construction:
- summary if the targets have been archieved and if not describe reasons 

All in all it can be said that the task to develop a speech recognition service object oriented was successfully completed. Due to the lack of time we were not able to implement all the features we wanted to add to the speech recognition. We will talk about that in topic 5 "potential future developments". 
Our personal success of this project was to get a much better understanding of object oriented programing and to collect valuable experience for our jobs. We got more used to developer tools such as "GitHub" and working with a Kanban board. 
So nevertheless we were not able to implement all the features we wanted to, the project was a personal success for us. 

## 5) Potential future developments:

We started to interpret easy commands like simple questions (e.g. "How are you Hal?"). Now we can implement further functions like a command to open a browser if the user uses the words "open browser". Also it's possible and necessary to filter out background noises or maybe to just take the loudest voice, when it comes to crosstalk. Also keywords can be selected to helb the NLP to process the language understanding when differnet accents are uswed in different languages.

**Voice-Tech (Healthcare):**
AI-powered chatbots and virtual assistants played a vital role in the fight against COVID-19. So chatbots can help screen and triage patients. Voice and conversational AI have made health services more accessible to everyone who was unable to leave their home during COVID-19 restrictions. Now that patients have a taste for what is possible with voice and healthcare, behaviors are not likely to go back to re-pandemic norms. 

**Voice Cloning:**
Machine learning tech and GPU power development help to create a custom voice  and make the speech more emotional, which makes this computer-generated voice indistinguishable from the real one. You just use a recorded speech and then a voice conversion technology transforms your voice into another. 



**Spacy** &rightarrow;

* If you use all the functions of Spacy, it would be possible for the computer to automatically recognise what a sentence or input is about and then automatically give the appropriate answer. Spacy would then function like a chatbot.
* Furthermore it would be possible to understand a wide range of languages. For example Spanish, German, Chinese and 60 more languages are implemented in Spacy. 
* Test-driven-development

**Implement further libraries** &rightarrow;

* The **PySpark** library is used for machine learning. With the named entity recgnition and the **BERT** language model, which has already been trained with wikipedia articles, you can analyse texts according to structure and content.

* With the **geturl** library you can open urls in python. 

* With **pyowm** (PythonOpenWeatherMap) it is possible to query the weather by location.

* You can also add a wake-up phrase like "hello hal", similar to Siri or Amazon Echo, instead of activating the voice recognition by pressing a button.

