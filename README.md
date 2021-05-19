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
Before we get to the nitty-gritty of doing speech recognition in Python, let’s take a moment to talk about how speech recognition works. A full discussion would fill a book, so I won’t bore you with all of the technical details here. In fact, this section is not pre-requisite to the rest of the tutorial. If you’d like to get straight to the point, then feel free to skip ahead.

Speech recognition has its roots in research done at Bell Labs in the early 1950s. Early systems were limited to a single speaker and had limited vocabularies of about a dozen words. Modern speech recognition systems have come a long way since their ancient counterparts. They can recognize speech from multiple speakers and have enormous vocabularies in numerous languages.

The first component of speech recognition is, of course, speech. Speech must be converted from physical sound to an electrical signal with a microphone, and then to digital data with an analog-to-digital converter. Once digitized, several models can be used to transcribe the audio to text.

Most modern speech recognition systems rely on what is known as a Hidden Markov Model (HMM). This approach works on the assumption that a speech signal, when viewed on a short enough timescale (say, ten milliseconds), can be reasonably approximated as a stationary process—that is, a process in which statistical properties do not change over time.

In a typical HMM, the speech signal is divided into 10-millisecond fragments. The power spectrum of each fragment, which is essentially a plot of the signal’s power as a function of frequency, is mapped to a vector of real numbers known as cepstral coefficients. The dimension of this vector is usually small—sometimes as low as 10, although more accurate systems may have dimension 32 or more. The final output of the HMM is a sequence of these vectors.

To decode the speech into text, groups of vectors are matched to one or more phonemes—a fundamental unit of speech. This calculation requires training, since the sound of a phoneme varies from speaker to speaker, and even varies from one utterance to another by the same speaker. A special algorithm is then applied to determine the most likely word (or words) that produce the given sequence of phonemes.

One can imagine that this whole process may be computationally expensive. In many modern speech recognition systems, neural networks are used to simplify the speech signal using techniques for feature transformation and dimensionality reduction before HMM recognition. Voice activity detectors (VADs) are also used to reduce an audio signal to only the portions that are likely to contain speech. This prevents the recognizer from wasting time analyzing unnecessary parts of the signal.

Fortunately, as a Python programmer, you don’t have to worry about any of this. A number of speech recognition services are available for use online through an API, and many of these services offer Python SDKs.



Some of the factors that make it so difficult are

The complexity of spoken language – In English, many words have multiple meanings depending on the context – for example “red” and “read” sound exactly the same but have completely different meanings.
People talk fast – When we speak, we don’t break our sentences up into individual words – we kind of just blurt it all out in one long string of sounds with few breaks. This makes it difficult to determine where a word ends and the next one begins.
No two people speak in the same way – It’s no good to have a system that needs to be reprogrammed for every individual. A system needs to be able to hear a new voice and understand it immediately.
Background noise – Differentiating the speech from the background noise is very difficult. This is especially true if the background noise is also speech (say at a party).


## 2) Methological approach

install libraries 
- speech recognition 
- PyAudio
-> If you want to use audio input from microphones, PyAudio is also necessary. If not installed, the library will still work, but Microphone will be undefined.

The official PyAudio builds seem to be broken on Windows. As a result, in the installers folder you will find unofficial PyAudio builds for Windows that actually work. Run the installer corresponding to your Python version to install PyAudio.

On Debain-based distributions such as Ubuntu, you can generally install PyAudio by running sudo apt-get install python-pyaudio python3-pyaudio, which will install it for both Python 2 and Python 3.

On other POSIX-based systems, simply use the packages provided on the downloads page linked above, or compile and install it from source.



## 3) Findings and achievements
- Detailed description of approach, work, findings, concrete achievements 

problems with Pyaudio and how to solve 


## 4) Summary
- summary if the targets have been archieved and if not describe reasons 

