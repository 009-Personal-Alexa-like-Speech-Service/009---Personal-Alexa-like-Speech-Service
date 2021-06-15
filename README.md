# 009 - Personal Alexa-like Speech Service
## Implement an Alexa alike speech service in Python. natural language processing.


- Kim Celine Marzi [843594]
- Melina Bröcker [862393]
- Maximilian Schmitt [872765]
- Thomas Zeutschler

- - - -

## 1) Business Understanding 
- Description and understanding of the business question or problem
- Goal: What was the task to be accomplished? What was intended to achieve?

## Use Case 

- Example: program a Speech Regognition

  Me: HAL, please... Can someone else help me?

  You: No problem, I'm a Python hero!

- Target
  --> The goal is to develop a voice control system that responds to the command: "Hello Hal"
  --> It should contain the follwing features which are mentioned below.

- Features:

   --> weather „Hello Hal, hows the weather?“ Wetterdatenbank einfügen  
   --> Open Browser (play a youtube video)  
   --> Set Alarm  
   --> Turn on music  
   --> „Hello Hal, tell me a joke“  
   --> Implement google standard answers  
   --> Save document (e. g. speech to text)  

## Process Flow Chart 
<img width="1044" alt="Bildschirmfoto 2021-06-03 um 18 31 40" src="https://user-images.githubusercontent.com/83067079/120679900-fb4b7980-c499-11eb-87d2-a69cd24ddc16.png">



## How Speech Recognition Works – An Overview

<img width="1151" alt="Bildschirmfoto 2021-06-10 um 10 44 41" src="https://user-images.githubusercontent.com/83067079/121494423-055d0300-c9d9-11eb-8d8d-4617f08a481a.png">
(Source:https://towardsdatascience.com/speech-recognition-in-python-the-complete-beginners-guide-de1dd7f00726)


To get a complete overview about the business problem it is necessary to understand how the speech recognition process itself works.

1. Configure Microphone (for external microphones): It is advisable to specify the microphone during the program to avoid any glitches.
2. Set Chunk Size: This basically involved specifying how many bytes of data we want to read at once. Typically, this value is specified in powers of 2 such as 1024 or 2048
3. Set Sampling Rate: Sampling rate defines how often values are recorded for processing
4. Set Device ID to the selected microphone: In this step, we specify the device ID of the microphone that we wish to use in order to avoid ambiguity in case there are multiple microphones. This also helps debug, in the sense that, while running the program, we will know whether the specified microphone is being recognized. During the program, we specify a parameter device_id. The program will say that device_id could not be found if the microphone is not recognized.
5. Allow Adjusting for Ambient Noise: Since the surrounding noise varies, we must allow the program a second or too to adjust the energy threshold of recording so it is adjusted according to the external noise level.
6. Speech to text translation: This is done with the help of Google Speech Recognition. This requires an active internet connection to work. However, there are certain offline Recognition systems such as PocketSphinx, but have a very rigorous installation process that requires several dependencies. Google Speech Recognition is one of the easiest to use.


 

The first component of speech recognition is speech. Speech must be converted from physical sound to an electrical signal with a microphone, and then to digital data with an analog-to-digital converter. Once the speech is digitized, several models can be used to transcribe the audio to text.

Most modern speech recognition systems rely on Hidden Markov Model (HMM). This approach works on the assumption that a speech signal, when viewed on a short enough timescale, can be reasonably approximated as a stationary process—that is, a process in which statistical properties do not change over time.

In a typical HMM, the speech signal is divided into 10-millisecond fragments. The power spectrum of each fragment, which is essentially a plot of the signal’s power as a function of frequency, is mapped to a vector of real numbers known as cepstral coefficients. The dimension of this vector is usually small—sometimes as low as 10, although more accurate systems may have dimension 32 or more. The final output of the HMM is a sequence of these vectors.

To decode the speech into text, groups of vectors are matched to one or more phonemes—a fundamental unit of speech. This calculation requires training, since the sound of a phoneme varies from speaker to speaker, and even varies from one utterance to another by the same speaker. A special algorithm is then applied to determine the most likely word (or words) that produce the given sequence of phonemes.

One can imagine that this whole process may be computationally expensive. In many modern speech recognition systems, neural networks are used to simplify the speech signal using techniques for feature transformation and dimensionality reduction before HMM recognition. Voice activity detectors (VADs) are also used to reduce an audio signal to only the portions that are likely to contain speech. This prevents the recognizer from wasting time analyzing unnecessary parts of the signal.

While programming, we don't have to worry about about that speech recognition process. There are several speech services/ packages available to help you with that. But we will talk about the packages later on. 

(Source: https://realpython.com/python-speech-recognition/) 


Some of the factors that make programming more difficult are 

- the complexity of spoken language. In English, many words have multiple meanings depending on the context – for example “red” and “read” sound exactly the same but have completely different meanings.
- People talk fast – When we speak, we don’t break our sentences up into individual words – we kind of just blurt it all out in one long string of sounds with few breaks. This makes it difficult to determine where a word ends and the next one begins.
- Nobody speak in the same way – It’s no good to have a system that needs to be reprogrammed for every individual. A system needs to be able to hear a new voice and understand it immediately.
- Background noise – Differentiating the speech from the background noise is very difficult. This is especially true if the background noise is also speech (say in a class).


## 2) Methological approach

The first step is to install all necessary libraries. 
 
- Speech Recognition ->speech to text  
- PyAudio ->for usage of audio input and output
- wave ->read & write wav files
- spacy -> natural language processing
- pyttsx3 ->text to speech conversion
- numpy


## 3) Findings and achievements
- Detailed description of approach, work, findings, concrete achievements 

1. Problems 
1.1 Installation 

There was a problem to install the package "PyAudio". We found two different solutions for Mac and Windows to solve the shown error. 


1.)For Windows type the following command into the Pycharm console:
- pip install pipwin
- pipwin install pyaudio

After the pip command is installed, the installation of PyAudio should work as well. 

2.) For Mac type the following command into the Pycharm console:
- https://www.youtube.com/watch?v=1oolnK1g6jw --> install homebrew

afterwards use:
- brew install portaudio
- pip install pyaudio

or

- pip3 install pyaudio

## 4) Summary
- summary if the targets have been archieved and if not describe reasons 



