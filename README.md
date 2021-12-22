# GlycoDeNovo2. 
This instruction was only tested on Windows machines.

## Install
* Download GlycoDeNovo2.exe and m2c.mat. Make sure both of them are under the same folder.

* Install Matlab Runtime 9.8 (https://www.mathworks.com/products/compiler/matlab-runtime.html). If your operating system is Windows, please add Matlab Runtime in environment variables (https://www.mathworks.com/matlabcentral/answers/343074-why-do-i-receive-could-not-find-version-x-x-of-mcr-when-running-my-compiled-app-and-mcr-is-instal).

## How to use
* Create an input directory and put all MS/MS spectrum text files in it. In addition, create a configuration file ''config.a'' specifying the options to be used by GlycoDeNovo2 on each spectrum file. This Github contains one "input" directory as an example. Make sure there are no other txt files.

* Use command line to run GlycoDeNovo2.exe. **Do not run it by double clicking it.** The command line should be "GlycoDeNovo2.exe [input_directory] [output_directory] [max_branching_number]. For example 
```
>GlycoDeNovo2.exe Desktop\a\input Desktop\a\output 2
```

* It will take a while for GlycoDeNovo2.exe to initialize MATLAB runtime library and toolboxes. GlycoDeNovo2 will collect all spectrum files in the [input_directory] and list them . After that, the command line shows a list of glycan files and their correspond reconstruct settings.  ![](1.PNG)
To set if to use gap and to use minus 2H while reconstructing a glycan, first input the index before the glycan name. For example, let __Lewis B.Na.EED.PN.txt__ use minus2H, first input its index 13 and press enter. Then input if to use gap (0 or 1). We don't want to use gap so we type 0 and press enter. Finally set if to use minus2H. In this example we set it as 1. **Inputs other than 0 and 1 are not accepted.**
* Once you've finished setting each glycans, you can type in **save** to generate a config file. Type in **load** to load the config file so that you don't neet to set each glycan next time.
* Type **done** to start GlycoDeNovo2. The reconstructed spectrum data is stored in the output folder.

# GlycanMP
* GlycanMP1.exe creates all possible topologies of a monosaccharide composition and saves them into a json file.
## How to use
* List all compositions in a csv file, for example, 'composition.csv' in this github respository. Each line is a composition. 
* Run GlycanMP1.exe using the following command line
  ```
    >GlycanMp1.exe composition.csv
  ```
* GlycanMP.exe reads the composition file and generates one json file for each composition in the same folder where GlycanMP1.exe is located.
