# Pig Latin Translater Microservice

The goal of this challenge is to build a microservice that takes english text and translates it into Pig Latin. This microservice should expose an HTTP endpoint that developers can submit their strings to which will return the translation. The translation should have matching capitalization and punctionation.

For example, this sentence-

> Hello, my name is Alice.

Should tranlate to-

> Ellohay, ymay amenay isay Aliceay.


## Pig Latin Rules

1. For words that begin with a consonant, all letters before the initial vowel are placed at the end of the word sequence. Then, "ay" is added.

* pig => igpay
* latin => atinlay
* banana => ananabay

2. When words begin with consonant clusters (multiple consonants that form one sound), the whole sound is added to the end when speaking or writing.

* smile => ilesmay
* string => ingstray
* glove => oveglay

3. For words that begin with vowels, one just adds "ya" to the end. Examples are:

* eat => eatay
* omelet => omeletay
* are => areay

These rules are a simplified version of the ones from Wikipedia. https://en.wikipedia.org/wiki/Pig_Latin


## Considerations

* You can use any language you want as long as the project can be run on an OSX machine or using Docker or Vagrant.


## Deliverables

* A readme describing in detail how to build and launch your service on a local computer, including installing any dependencies.
* A client script that can be used to send requests to your application.
