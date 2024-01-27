# eegmotorimagryorangepy

Motor imaging EEG signal recognition is an important and challenging research problem in human-computer interaction. 

A motor imagery-based brain-computer interface (MI-BCI) creates a path through which the brain interacts with the external environment by recording and processing electroencephalograph (EEG) signals made by imagining the movement of a particular limb.

As the relevant rhythmic signals during motor imagery are divided into μ rhythm signal of 8–12 Hz and β rhythm signal of 13–30 Hz 

Deep Learning (DL) models have gained popularity for EEG classification as they provide a solution for automatic extraction of spatio-temporal features in the signals. 

Convolutional neural network

https://en.wikipedia.org/wiki/Convolutional_neural_network

https://www.youtube.com/watch?v=XIowcswb1Hg

Electroencephalogram Signal Classification for action identification
EEG Modeling of data and a CNN
https://keras.io/examples/timeseries/eeg_signal_classification/

For less acurat rnn Short Term Fourier transform can be applied to signals to make them more significant to unsupervised training.

The Short Term Fourier Transform (STFT) is a method used to decompose a signal into short-duration frequency components. In EEG signal processing, this can be useful for highlighting the relevant and significant frequencies of motor imagery signals, making them more suitable for unsupervised Deep Learning training. 

Convolution Neuronetwork:
This allows DL models to learn the EEG Signals directly and important spatio-temporal features of the EEG signals, leading to improved accuracy in motor imagery detection.

Electroencephalogram Signal Classification for action identification
https://keras.io/examples/timeseries/eeg_signal_classification/

Datasets:

keywords: keras eeg bci ml mi

Datasets collected with labels are important for machene learning a button trigger on the ganglion labled prog can do that D17.

https://docs.openbci.com/Cyton/CytonExternal/

CNN EEG signal clasification in python tensorflow keras.
The data set is from 15 subjects at the same time 500 samples long or 15 or 16 channel eeg.
https://keras.io/examples/timeseries/eeg_signal_classification/

Saving these biosignal models is important they can take a lot of time to train and smaller processor to use to predict. 
model.save('path/to/location.keras')  # The file needs to end with the .keras extension

https://keras.io/guides/serialization_and_saving/

"Make Predictions with Keras"

https://machinelearningmastery.com/how-to-make-classification-and-regression-predictions-for-deep-learning-models-in-keras/

Structured data classification from scratch
https://keras.io/examples/structured_data/structured_data_classification_from_scratch/

References:
...
Li, H., Ding, M., Zhang, R., & Xiu, C. (2022). Motor imagery EEG classification algorithm based on CNN-LSTM feature fusion network. Biomedical signal processing and control, 72, 103342.

Wang, P., Jiang, A., Liu, X., Shang, J., & Zhang, L. (2018). LSTM-based EEG classification in motor imagery tasks. IEEE transactions on neural systems and rehabilitation engineering, 26(11), 2086-2095.

Khademi, Z., Ebrahimi, F., & Kordy, H. M. (2022). A transfer learning-based CNN and LSTM hybrid deep learning model to classify motor imagery EEG signals. Computers in biology and medicine, 143, 105288.

Garcia-Moreno, F. M., Bermudez-Edo, M., Rodríguez-Fórtiz, M. J., & Garrido, J. L. (2020, July). A CNN-LSTM deep Learning classifier for motor imagery EEG detection using a low-invasive and low-Cost BCI headband. In 2020 16th international conference on intelligent environments (IE) (pp. 84-91). IEEE.

Xu, F., Xu, X., Sun, Y., Li, J., Dong, G., Wang, Y., ... & Yin, S. (2022). A framework for motor imagery with LSTM neural network. Computer methods and programs in biomedicine, 218, 106692.
