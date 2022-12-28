Title: The Austrian Language Project
Date: 2022-12-28 11:28
Author: Ewald Enzinger
Tags: speech recognition, Austrian German
Category: Blog
Slug: 


The Austrian Language Project (T-ALP) aims to improve automatic speech recognition of Austrian German. Specifically, it focuses on Austrian German as it is typically spoken in the media such as TV and radio as well as podcasts but, at least at present, does not try to cover the wide dialectal and sociolectal variety of German spoken in Austria. The project was presented at the conference [Building a European Cultural Backbone (ECB2022)](https://cba.fro.at/building-a-european-cultural-backbone) at the Stadtwerkstadt in Linz, Austria.

I initially became involved in this project when I met Alexander Baratsits, one of the founders of the [Cultural Broadcasting Archive (CBA)](https://cba.media/). The CBA aims to promote freedom of expression, media diversity and digital communication by providing free access to a large continuously growing archive of podcasts hosted via independently operated technical infrastructure. There are currently over 140,000 audio contributions in around 50 languages available on the platform, but a large amount of it is spoken in German as it is spoken in Austria.

Adding automatic speech recognition to the platform would enable discovery and recommendation capabilities to users. In addition, recent legislation aimed at improving accessibility requires broadcasters to provide subtitles. Most open-source speech recognition models (and to a large extent commercial ones as well) have difficulty transcribing Austrian German speech, as most models are developed using data from German speakers from Germany who typically use varieties of German which differ from those spoken in Austria on many linguistic levels and in terms of lexicon. In particular, named entities relevant to media discourse in Austria are typically not included in the speech recognition models' vocabularies and are therefore often substituted for other words.[ref]Low-frequency terms are a general problem in automatic speech recognition, not limited to Austrian German, but the issue is exacerbated due to the mismatch in training data and the data the model is being applied on.[/ref]

T-ALP's aim is therefore to collect a substantial amount of training data on the order of 1000 hours of transcribed speech to provide improved automatic speech recognition for Austrian German. Two main data sources were identified:

1. Broadcast film and radio footage with subtitles
2. Recordings of sessions of the Austrian Parliament with stenographic (shorthand) transcriptions

Using footage from broadcast TV and radio and their subtitles for model training has the advantage that the conditions more closely match those of the kind of media the CBA is trying to apply the resulting models on; however, since the footage and subtitles are owned by different legal entities with differing priorities and incentives, it is not straightforward to use them for training a model.[ref]The Austrian Broadcasting Corporation *ORF*, the Austrian national public broadcaster, has a lot of raw material from its productions going back many decades, but due to its organizational structure, it does not necessarily own the subtitles produced for its programs.[/ref]

Sessions of the two chambers of the [Austrian Parliament](https://www.parlament.gv.at/), Nationalrat and Bundesrat, are recorded and available to the public via the online [MediaThek](https://www.parlament.gv.at/MEDIA/) for sessions held from mid 2019 onwards. According to the [terms](https://www.parlament.gv.at/DISC/index.shtml#Nutzungsbedingungen_Videos), the directorate of the parliament owns the rights to these materials and grants their use for non-commercial purposes.

In an initial phase during the development of [OpenAudioSearch](https://github.com/openaudiosearch/openaudiosearch), an open source full-text search engine with automatic speech recognition for podcasts, I developed resources to perform the following steps:

1. Obtaining raw data from sessions of the Austrian Parliament.
2. "Chunking", i.e., segmenting the often many hour long sessions and aligning them with the stenographic transcripts using the tools provided as part of the [Kaldi toolkit](https://github.com/kaldi-asr/kaldi).
3. Training an automatic speech recognition model using [Kaldi](https://github.com/kaldi-asr/kaldi).
4. Evaluate the accuracy of trained models on data.

These are available on [Github](https://github.com/openaudiosearch/speech-recognition) under an open-source license.

---