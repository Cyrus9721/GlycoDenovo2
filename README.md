# GlycoDeNovo2. 
This instruction was only tested on Windows machines.
## Install
* Download GlycoDeNovo2.exe and m2c.mat. Make sure both of them are under the same folder.
* Install Matlab Runtime 9.8. If your operating system is Windows, please add Matlab Runtime in environment variables. [Link](https://www.mathworks.com/matlabcentral/answers/343074-why-do-i-receive-could-not-find-version-x-x-of-mcr-when-running-my-compiled-app-and-mcr-is-instal)
## How to use
* Put all MS/MS spectrum text files in one folder. Make sure there are no other txt files.
* Use command line to run GlycoDeNovo2.exe. **Do not run it by double clicking it.** The command line should be "GlycoDeNovo2.exe [input_directory] [output_directory] [max_branching_number]. For example 
```
>GlycoDeNovo2.exe Desktop\a\input Desktop\a\output 3
```
* After that, the command line shows a list of glycan files and their correspond reconstruct settings.  ![](1.PNG)
To set if to use gap and to use minus 2H while reconstructing a glycan, first input the index before the glycan name. For example, let __Lewis B.Na.EED.PN.txt__ use minus2H, first input its index 13 and press enter. Then input if to use gap (0 or 1). We don't want to use gap so we type 0 and press enter. Finally set if to use minus2H. In this example we set it as 1. **Inputs other than 0 and 1 are not accepted.**
* Once you've finished setting each glycans, you can type in **save** to generate a config file. Type in **load** to load the config file so that you don't neet to set each glycan next time.
* Type **done** to start GlycoDeNovo2. The reconstructed spectrum data is stored in the output folder.

# GlycanMP
## How to use
* GlycanMP.exe maps a composition into a json file, which contains all of the possible glycan topologies.
* The input of GlycanMP.exe is a csv file of compositions. GlycanMP.exe reads the csv and generates json files for each composition.
* **Similar to GlycoDeNovo2.exe, GlycanMP.exe should be started from command line**, followed by the path of the csv file. Example:
  ```
    >GlycanMp1.exe temp1.csv
  ```
* The generated json files will be in the same folder as GlycanMP.exe.
