This instruction was only tested on Windows machines.

# Install Matlab Runtime
* Download and install Matlab Runtime 9.8 (https://www.mathworks.com/products/compiler/matlab-runtime.html). If your operating system is Windows, please add Matlab Runtime in environment variables (https://www.mathworks.com/matlabcentral/answers/343074-why-do-i-receive-could-not-find-version-x-x-of-mcr-when-running-my-compiled-app-and-mcr-is-instal).


# GlycoDeNovo2 (PeakInterpreter2). 
* GlycoDeNovo2.exe requires 'm2c.mat'. Make sure both of them are under the same folder.
* Create an input directory and put all MS/MS spectrum text files in it. In addition, create a configuration file 'config.a' specifying the options to be used by GlycoDeNovo2 on each spectrum file. The first column of 'config.a' is the spectrum file name, the second column specifies if the 'gap' search option should be on (i.e., 1) or off (i.e., 0), and the third column specifies if the '-2H' search option should be on (i.e., 1) or off (i.e., 0). This Github contains one "input" directory as an example. Make sure there are no other txt files.

* Use command line to run GlycoDeNovo2.exe. **Do not run it by double clicking it.** The command line should be "GlycoDeNovo2.exe [input_directory] [output_directory] [max_branching_number]. For example 
```
>GlycoDeNovo2.exe Desktop\a\input Desktop\a\output 2
```

* It will take a while for GlycoDeNovo2.exe to initialize MATLAB runtime library and toolboxes. GlycoDeNovo2 will run the reconstruction procedure on all spectrum files in the [input_directory] and save the reconstruction results in the [output_directory]. 

# GlycanMP (Composition-to-Topology)
* GlycanMP1.exe creates all possible topologies of a monosaccharide composition and saves them into a json file. This is required in generate all topologies to be sampled in calculating p-values.
* List all compositions in a csv file, for example, 'composition.csv' in this github respository. Each line is a composition. 
* Run GlycanMP1.exe using the following command line
  ```
    >GlycanMp1.exe composition.csv
  ```
* GlycanMP.exe reads the composition file and generates one json file for each composition in the same folder where GlycanMP1.exe is located.
