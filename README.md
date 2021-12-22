This instruction was tested on Windows machines.

# Install Matlab Runtime
* We compiled MATLAB codes (ver MATLAB 2019b) into executables so that you don't need a Matlab license to run GlycoDeNovo2. You need to download and install the free Matlab Runtime 9.8 (https://www.mathworks.com/products/compiler/matlab-runtime.html). If your operating system is Windows, please add Matlab Runtime in environment variables (https://www.mathworks.com/matlabcentral/answers/343074-why-do-i-receive-could-not-find-version-x-x-of-mcr-when-running-my-compiled-app-and-mcr-is-instal). 


# GlycoDeNovo2 (PeakInterpreter2). 
* GlycoDeNovo2.exe is an excutable file compiled from Matlab codes. It mainly implements the PeakInterpreter2 algorithm.
* GlycoDeNovo2.exe requires 'm2c.mat' which contains the mapping from protonated precursor m/z to monosaccharide composition. Make sure both of them are under the same folder. 
* Create an input directory and put all MS/MS spectrum text files in it. Each spechtrum file contains a list of peaks. Create a configuration file 'config.a' specifying the options to be used by GlycoDeNovo2 on each spectrum file. The first column of 'config.a' is the spectrum file name, the second column specifies if the 'gap' search option should be on (i.e., 1) or off (i.e., 0), and the third column specifies if the '-2H' search option should be on (i.e., 1) or off (i.e., 0). Make sure there are no other file in the input directory. This github repository contains one "input" directory as an example, which include the MS/MS spectra of the 29 standard glycans used in the paper. Note: Based on our experience, when analyzing a new spectrum, set both the 'gap' and '-2H' options to off in the first trial. If GlycoDeNovo2 fails to recontruct any topology, turn on the '-2H' option. If GlycoDeNovo2 fails again, turn on the 'gap' option.

* Use command line to run GlycoDeNovo2.exe. **Do not run it by double clicking it.** The command line should be "GlycoDeNovo2.exe [input_directory] [output_directory] [max_branching_number]. For example 
```
GlycoDeNovo2.exe input output 2
```

* It will take a while for GlycoDeNovo2.exe to initialize MATLAB runtime library and toolboxes. GlycoDeNovo2 will run the reconstruction procedure on all spectrum files in the [input_directory] and save the reconstruction results in the [output_directory]. GlycoDeNovo2 saves the reconstruction results of each possible composition in one text file with the ".grec" extension, and finally save the whole reconstruction results of the spectrum into a text file with the ".ALL.grec" extension and a MATLAB data file with the ".mat" extension. If GlycoDeNovo2 is not able to reconstruct any result from a composition, it will not create a result file for that composition. Using the spectrum "Sialyl Lewis A.Na.EED.PM.txt" as an example, there are 3 possible compositions. The reconstruction results of the first two compositions are saved as "Sialyl Lewis A.Na.EED.PM.1.grec" and "Sialyl Lewis A.Na.EED.PM.2.grec", respectively. No topology is reconstructed from the third composition, and hence no result file is created for this composition. "Sialyl Lewis A.Na.EED.PM.1.grec" and "Sialyl Lewis A.Na.EED.PM.2.grec" are combined into the text file "Sialyl Lewis A.Na.EED.PM.ALL.grec" and the MATLAB data file "Sialyl Lewis A.Na.EED.PM.mat".

# GlycanC2T (Composition-to-Topology)
* GlycanC2T.exe creates all possible topologies of a monosaccharide composition with maximum branch number = 2 and saves them into a json file. This is required in generate all topologies to be sampled in calculating p-values.
* List all compositions in a csv file, for example, 'composition.csv' in this github respository. Each line is a composition. 
* Run GlycanMP1.exe using the following command line
  ```
    GlycanC2T.exe composition.csv
  ```
* GlycanC2T.exe reads the composition file and generates one json file for each composition in the same folder where GlycanC2T.exe is located.
