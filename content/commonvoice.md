Title: Kaldi recipe for Mozilla's Common Voice corpus
Date: 2018-01-10 11:15
Author: Ewald Enzinger
Tags: speech recognition, mozilla, common voice, corpus
Category: Blog
Slug: 

**Note:** This is about a recipe for the original, English-only Common Voice corpus released in 2018. Subsequent releases with data for various languages are not compatible with this recipe.

Recently, Mozilla published a first version of their [Common Voice corpus](https://voice.mozilla.org/data). It consists of speech prompts from an unknown number of speakers (no speaker IDs are provided due to privacy concerns, see this [forum thread](https://discourse.mozilla.org/t/speaker-ids-for-speaker-recognition/22747)). About 254 hours have been validated by multiple listeners. The data has been split into pre-defined training, development and test sets. 

I created an initial Kaldi recipe for the corpus as a research exercise. 
It has since been [merged](https://github.com/kaldi-asr/kaldi/pull/2057) into the Kaldi master branch. 
Using the pre-defined split into training, development, and test sets, and without any tuning of parameters, a system using a time-delay neural network (TDNN) based acoustic model and a 3-gram language model achieved a WER of 4.27% on the test set; however, given the near-complete overlap in spoken utterances between the training, development, and test sets, these results are not very meaningful in terms of generalization to other datasets. 
See [this issue](https://github.com/kaldi-asr/kaldi/issues/2141) for an ongoing discussion on how the data collection effort could be improved. 
