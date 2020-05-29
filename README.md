# MIXER <img src="https://raw.githubusercontent.com/user0706/Mixer/master/MixerLogo.png" alt="drawing" width="25"/>
Mixer is a small and adaptive program for training and testing sentence classification models inspired by Cloud AutoML. It is completely offline and the speed of loading the dataset and training time directly depends on the performance of the computer.

## Introductions
The mixer initially uses a non-advanced algorithm in an attempt to keep training time as short as possible. The goal of the initial classification algorithm is for the classification results to be consistent with a trade-off between training time and guessing accuracy.
<br>By combining filter options, it is possible to see how filters affect the reliability of guessing.

If someone wants, non-advanced algorithms can be relatively easily replaced by advanced ones, by modifying certain parts of the source code.

## Legend
The mixer contains four tabs (main, results, filters and initialization) and on the right is an overview of the files of the exported models.

### Main
**Bassic overview** is located in the upper left part of the main tab. As the name suggests, it serves to review general information about the loaded database.
<br>Here you can find information on how many sentences there are in total, the number of different labels, then how many labeled sentences there are, as well as the number of non-labeled sentences.

**Labels overview** is below the bassic overview group. This group provides information on the number of sentences for each label.

**Dataset overview** is located in the right part of the main tab, ie in the central part of the program itself. It has a simple task, to display the loaded database.

The **Main button area** is the area located in the lower middle part of the main tab. This area consists of two buttons, Load File and Train.

### Results
Results, or perhaps it would be more appropriate to say Test tab, can be divided into several parts.

At the top is a section that displays **information** about the trained model. It has the ability to display information about accuracy (optional), the time required to train the model, the date and time when the model was trained, as well as the number of sentences tested for accuracy (also optional - related to accuracy).

Below the information part is the **input part**, ie the part for entering the desired sentence that will be analyzed.

In the central part of the results tab, there is an area for displaying the **results** of the classification of the input test sentence.

As with the main tab, there is also a **results button area** at the bottom. In this case, it is a single button, the Export button. With it, it is possible to export an already trained model with all the accompanying information.

### Filters
The filter tab has only one part, a part with filters and as a sub part, a part for accuracy. If the accuracy checkbox is activated, 10% of the total database will initially be tested, provided that the input field, below the checkbox, is empty. By entering a value, the value is set as a percentage of how many sentences will be tested.

### Initialization
In addition to having a built-in Stop Word database, the Mixer also provides the ability to load an external Stop Word database.

All models are initially exported to a folder called "MixerModelDataBackup" which is located in the Documents ie to the `C:\Users\Public\Documents\MixerModelDataBackup` location.

In case you need to return to the initial settings, the Default button is located in the lower middle part.

## Shortcuts
|Comand|Function  |
|--|--|
| `Ctr+O` | Load File |
| `Ctr+M` | Load Model|
| `Ctr+E`| Export Model|

## Dataset
|Sentence|Label  |
|--|--|
| Hello | Neutral |
| Hello. I'm so glad you called me. | Positiv|
| Yes, but not to me.| Negativ|

> The dataset should be headerless.

>Dataset must be CSV UTF-8 (comma delimited)

## Screenshots
![](https://raw.githubusercontent.com/user0706/Mixer/master/ignore/mixer.gif)

