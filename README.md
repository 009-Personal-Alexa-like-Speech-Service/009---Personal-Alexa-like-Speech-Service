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



How Speech Recognition Works – An Overview

To get a complete overview about the business problem it is necessary to understand how the speech recognition process itself works. 

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
 
- Speech Recognition 
- PyAudio

Speech recognition is for tbd. 
PyAudio is necessary if you want to use audio input from microphones. 


## 3) Findings and achievements
- Detailed description of approach, work, findings, concrete achievements 

1. Problems 
1.1 Installation 

There was a problem to install the package "PyAudio". We found two different solutions for Mac and Windows to solve the shown error. 


1.)For Windows type the following command into the Pycharm console:
- pip install pipwin
- pipwin install pyaudio

After the pip command is installed, the installation of PyAudio should work as well. 

2.)

## 4) Summary
- summary if the targets have been archieved and if not describe reasons 

