# 009 - Personal Alexa-like Speech Service
## Implement an Alexa alike speech service in Python "Natural Language Processing"


- Kim Celine Marzi [843594]
- Melina Bröcker [862393]
- Maximilian Schmitt [872765]
- Thomas Zeutschler

- - - -

## 1) Business Understanding 
- Description and understanding of the business question or problem
- Goal: What was the task to be accomplished? What was intended to achieve?

### Use Case 

**Example: program a Speech Regognition**

  * Me: HAL, please... Can someone else help me?

  * You: No problem, I'm a Python hero!

**Target**
  * &rightarrow; The goal is to develop a voice control system that responds to the command: "Hello Hal"
  * &rightarrow; It should contain the follwing features which are mentioned below and give action to that. 

**Features**

We want to implement the features listed below:

   * &rightarrow; Give information about the weather „Hello Hal, hows the weather today?“  
   * &rightarrow; Open Browser (google.com)  
   * &rightarrow; Set Alarm  
   * &rightarrow; Turn on music  
   * &rightarrow; „Hello Hal, tell me a joke“  
   * &rightarrow; Implement google standard answers  
   * &rightarrow; Save document (e. g. speech to text)  
   * &rightarrow; Compute two numbers 

### Process Flow Chart 

Below we designed a flow chart how our speech recognition works in three steps:
<img width="1044" alt="Bildschirmfoto 2021-06-03 um 18 31 40" src="https://user-images.githubusercontent.com/83067079/120679900-fb4b7980-c499-11eb-87d2-a69cd24ddc16.png">


### Crisp-DM

![image](https://user-images.githubusercontent.com/83068247/122058489-f4066300-cdeb-11eb-9eb3-748da4dc36f1.png)






### How Speech Recognition Works – An Overview

<img width="1151" alt="Bildschirmfoto 2021-06-10 um 10 44 41" src="https://user-images.githubusercontent.com/83067079/121494423-055d0300-c9d9-11eb-8d8d-4617f08a481a.png">
(Source:https://towardsdatascience.com/speech-recognition-in-python-the-complete-beginners-guide-de1dd7f00726)


To get a complete overview about the business problem it is necessary to understand how the speech recognition process itself works.

1. **Configure Microphone**: It is advisable to specify the microphone during the program to avoid any glitches.
2. **Set Chunk Size:** This basically involved specifying how many bytes of data we want to read at once. Typically, this value is specified in powers of 2 such as 1024 or 2048
3. **Set Sampling Rate:** Sampling rate defines how often values are recorded for processing
4. **Set Device ID to the selected microphone:** In this step, we specify the device ID of the microphone that we wish to use in order to avoid ambiguity in case there are multiple microphones. This also helps debug, in the sense that, while running the program, we will know whether the specified microphone is being recognized. During the program, we specify a parameter device_id. The program will say that device_id could not be found if the microphone is not recognized.
5. **Allow Adjusting for Ambient Noise:** Since the surrounding noise varies, we must allow the program a second or too to adjust the energy threshold of recording so it is adjusted according to the external noise level.
6. **Speech to text translation:** This is done with the help of Google Speech Recognition. This requires an active internet connection to work. However, there are certain offline Recognition systems such as PocketSphinx, but have a very rigorous installation process that requires several dependencies. Google Speech Recognition is one of the easiest to use.

The first component of speech recognition is speech. Speech must be **converted from physical sound to an electrical signal** with a microphone, and then to **digital data with an analog-to-digital converter**. Once the speech is digitized, several models can be used to transcribe the audio to text.

Most modern speech recognition systems rely on **Hidden Markov Model (HMM).** This approach works on the assumption that a speech signal, when viewed on a short enough timescale, can be reasonably approximated as a stationary process—that is, a process in which statistical properties do not change over time.

In a typical HMM, the speech **signal is divided into 10-millisecond fragments.** The power spectrum of each fragment, which is essentially a plot of the signal’s power as a function of frequency, is mapped to a vector of real numbers known as cepstral coefficients. The dimension of this vector is usually small—sometimes as low as 10, although more accurate systems may have dimension 32 or more. The final output of the HMM is a **sequence of these vectors.**

To decode the **speech into text,** groups of vectors are matched to one or more phonemes—a fundamental unit of speech. This calculation requires training, since the sound of a phoneme varies from speaker to speaker, and even varies from one utterance to another by the same speaker. A special algorithm is then applied to determine the most likely word (or words) that produce the given sequence of phonemes.

One can imagine that this whole process may be computationally expensive. In many modern speech recognition systems, neural networks are used to simplify the speech signal using techniques for feature transformation and dimensionality reduction before HMM recognition. Voice activity detectors (VADs) are also used to reduce an audio signal to only the portions that are likely to contain speech. This prevents the recognizer from wasting time analyzing unnecessary parts of the signal.

While programming, we don't have to worry about about that speech recognition process. There are several speech services/ packages available to help us with that. But we will explained the used packages later on. 

*(Source: https://realpython.com/python-speech-recognition/)*




### Some of the factors that make programming a speech recognition more difficult are 

* the complexity of spoken language. In English, many words have multiple meanings depending on the context – for example “red” and “read” sound exactly the same but have completely different meanings.
* People talk fast – When we speak, we don’t break our sentences up into individual words – we kind of just blurt it all out in one long string of sounds with few breaks. This makes it difficult to determine where a word ends and the next one begins.
* Nobody speak in the same way – It’s no good to have a system that needs to be reprogrammed for every individual. A system needs to be able to hear a new voice and understand it immediately.
* Background noise – Differentiating the speech from the background noise is very difficult. This is especially true if the background noise is also speech (say in a class).


## 2) Methological approach

The first step is to install all necessary libraries. 
 
- Speech Recognition &rightarrow; speech to text  
- PyAudio &rightarrow;  for usage of audio input and output
- wave &rightarrow;  read & write wav files
- spacy &rightarrow; natural language processing

spaCy is a huge library with many function. Below we listed a few of these function as an overview. 

spaCy is a free, open-source library for advanced Natural Language Processing (NLP) in Python.

spaCy comes with pretrained pipelines and currently supports tokenization and training for 60+ languages. It features state-of-the-art speed and neural network models for tagging, parsing, named entity recognition, text classification and more, multi-task learning with pretrained transformers like BERT, as well as a production-ready training system and easy model packaging, deployment and workflow management. spaCy is commercial open-source software, released under the MIT license.

<img width="515" alt="image" src="https://user-images.githubusercontent.com/83068247/123808167-cb549200-d8f0-11eb-9878-4093c406b6f1.png">


**1. Tokenization ** 

Word tokens are the basic units of text that appear in any NLPlabeling task. The first step in processing text is to break it into tokens.
Import the Spacy language class to create an NLP object of this class with the code shown in the following code. Then process your document using the NLP object and put some text data or your text file into it to process it. Select the token you want to print and then print the output using the "Token and Text" function to get the value in text form.

<img width="542" alt="image" src="https://user-images.githubusercontent.com/83068247/123808008-a6601f00-d8f0-11eb-833e-7cd011f4b2f7.png">


**2. Labeling of word types**

When we learn basic grammar, we understand the difference between nouns, verbs, adjectives, and adverbs, and while it may seem pointless at the time, it turns out to be a crucial element of natural language processing.

Spacy provides convenient tools to break sentences into word lists and then assign each word to a specific part of speech based on the context.

**3. Name entity recognition**

One of the most common labeling problems is finding entities in the text. Typically, name entity recognition represents the names of politicians, actors, and famous places, as well as organizations and products available in that organization's market.

Simply import the Spacy and Load model and process the text with nlp, then iterate over each entity and print its label.

**4. Dependency parsing**

The main concept of dependency parsing is that each linguistic unit (words) is connected by a directed linkage. These links are called dependencies in linguistics.

**5. Matcher**

The Matcher is very powerful and allows you to start many NLP-based tasks, such as entity extraction, finding patterns that match in the text or document.

Import the Spacy, Matcher and initialize the matcher with the document and define a pattern you want to find in the document. Then add the pattern to the matcher. Then print the matches in the matcher documents.


- pyttsx3 &rightarrow; text to speech conversion
- numpy






In the following, we wrote a description of which classes are implemented and what functions they contain. 
* **Class: Main** (file main.py) We start our speech assistant Hal in our main-file.
* **Class: Hal** (file hal.py) Hal is our speech assistant
** He starts  to record audio when option 1 in the main menu is chosen
** After three seconds of break he stopps recording 
** If he does not understand the spoken words he gives an error
* **Class: Listener**
* **Class: Speaker**
* **Class: Interpreter**
* **Class: Utilities**
* **Class: Recognizer**


## 3) Findings and achievements
- Detailed description of approach, work, findings, concrete achievements 

First we will start with our problems we had during our project:

#### 1. Problems 
##### 1.1 Installation 

There was a problem to install the package "PyAudio". We found two different solutions for Mac and Windows to solve the shown error. 


1.)For **Windows** type the following command into the Pycharm console:
- pip install pipwin
- pipwin install pyaudio

After the pip command is installed, the installation of PyAudio should work as well. 

2.) For **Mac** type the following command into the Pycharm console:
- "install homebrew"
afterwards use:
- brew install portaudio
- pip install pyaudio
- *https://www.youtube.com/watch?v=1oolnK1g6jw* &rightarrow; This youtube video explains step by step how to install PyAudio on a Mac

or

- pip3 install pyaudio


##### 1.2 Manual push request

1.) Type in your terminal:

- cd desktop
- And your project path with git push at the end
- Before pushing you need to fetch and merge.

![image](https://user-images.githubusercontent.com/83068247/122056101-91ac6300-cde9-11eb-9ed2-5768d8b7567e.png)







## 4) Summary
- summary if the targets have been archieved and if not describe reasons 




