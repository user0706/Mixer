<p align="center"> 
<img src="https://raw.githubusercontent.com/user0706/Mixer/master/ignore/MixerCover.png" height=150px/>
</p>

## About Mixer

Mixer is a small and adaptive program for training and testing sentence classification models inspired by Cloud AutoML. It is completely offline and the speed of loading the dataset and training time directly depends on the performance of the computer

## Language Independence
The mixer is a multilingual program, ie language independent. All font types that UTF-8 supports are also supported by the Mixer.

## How Mixer Works
The mixer is based on the Python programming language with the intention of being a compromise between the model training speed and the classification results. Before each loading of the database, it is necessary to set the desired filter parameters, if desired. The number of different classes is not limited. It would be desirable if the number of sentences for each of the classes is approximately identical.

The trained model will not be saved until the user exports it. The exported model has a built-in complete loaded database with all accompanying information, as well as a model on the basis of which class prediction is performed.

Instead of a database, it is possible to load a trained model. But it is not possible to apply additional filters or re-export to the model.

## Process flow diagram
<p align="center"> 
<img src="https://raw.githubusercontent.com/user0706/Mixer/master/ignore/ProcessFlowing.png"/>
</p>

## Requirements
The Mixer was created in the Python 3.6.0 programming language. The GUI was created in QtDesigner and PyQt5 v.5.14.2.

## Screenshots
![](https://raw.githubusercontent.com/user0706/Mixer/master/ignore/mixer.gif)

