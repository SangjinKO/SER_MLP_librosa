# SER_MLP_librosa
 
Speech Emotion Recognition System using MLP (Multilayer Perception)

Dependencies: librosa, numpy, sklearn

Corpos: RAVDESS (English, 1500 audios from 24 people)

Train (Features): librosa features sets*
* flatness, zerocr, meanMagnitude, maxMagnitude, meancent, stdcent,
maxcent, stdMagnitude, pitchmean, pitchmax, pitchstd,
pitch_tuning_offset, meanrms, maxrms, stdrms,
mfccs, mfccsstd, mfccmax, chroma, mel, contrast

Parameter seeting: alpha = 1.9, max_iter = 700

Result: Accuracy: 76.4%

*MEMO: Files (corpus) should be categorized and stored in different folders by labels (emotions)
