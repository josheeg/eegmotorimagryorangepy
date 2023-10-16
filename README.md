# eegmotorimagryorangepy

Motor imaging EEG signal recognition is an important and challenging research problem in human-computer interaction. 

A motor imagery-based brain-computer interface (MI-BCI) creates a path through which the brain interacts with the external environment by recording and processing electroencephalograph (EEG) signals made by imagining the movement of a particular limb.

As the relevant rhythmic signals during motor imagery are divided into μ rhythm signal of 8–12 Hz and β rhythm signal of 13–30 Hz 

Deep Learning (DL) models have gained popularity for EEG classification as they provide a solution for automatic extraction of spatio-temporal features in the signals. 

https://www.youtube.com/watch?v=XIowcswb1Hg

Short Term Fourier transform can be applied to signals to make them more significant to unsupervised training.
Lables may have to be coppied over if Time and number of records same... 
Neuronetwork seems to be the best model.
The Data comes in and out of the widget as a row signal and can be concatinated to many rows then transposed for many columns to train on

samples 100000 to output . array x= 202 , y= 501  stft nperseg=1000 fs =10e3 = 1000 202 time  y 501 freq n val amp
transpose to have sample time be on y axis and frequency power be x 

201 points in time 500 samples to 1 out? labeling may be manual

256 samples defalt 100000 samples /256 390.625 *2 781   783 samples found out so 2x? 

Once the STFT and moving transforms are run on the data that gives features the neuronetwork can be trained on and models saved. The models can be used to predict what new data after it has STFT and moving transform features calculated what imagined motor movement happened and its acuracy. 

That can be used as a mouse or keyboard interface...

eeg motor imagry orange python data mining neuronetwork 
