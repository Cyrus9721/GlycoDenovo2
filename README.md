This instruction was only tested on Windows machines.

# Install Matlab Runtime
* We compiled MATLAB codes into executables so that you don't need a Matlab license to run GlycoDeNovo2. You need to download and install the free Matlab Runtime 9.8 (https://www.mathworks.com/products/compiler/matlab-runtime.html). If your operating system is Windows, please add Matlab Runtime in environment variables (https://www.mathworks.com/matlabcentral/answers/343074-why-do-i-receive-could-not-find-version-x-x-of-mcr-when-running-my-compiled-app-and-mcr-is-instal). 


# GlycoDeNovo2 (PeakInterpreter2). 
* GlycoDeNovo2.exe is an excutable compiled from Matlab codes. 
* GlycoDeNovo2.exe requires 'm2c.mat' which contains the mapping from protonated precursor m/z to monosaccharide composition. Make sure both of them are under the same folder. 
* The raw glycan MS data is under the input folder, along with a config file. The reconstructed topologies will be saved in the output folder.

* Use command line to run GlycoDeNovo2.exe. **Do not run it by double clicking it.** The command line should be "GlycoDeNovo2.exe [input_directory] [output_directory] [max_branching_number]. For example 
```
GlycoDeNovo2.exe input output 2
```

* It will take a while for GlycoDeNovo2.exe to initialize MATLAB runtime library and toolboxes. GlycoDeNovo2 will run the reconstruction procedure on all spectrum files in the [input_directory] and save the reconstruction results in the [output_directory]. 

# GlycanMP (Composition-to-Topology)
* GlycanMP1.exe creates all possible topologies of a monosaccharide composition and saves them into a json file. This is required in generate all topologies to be sampled in calculating p-values.
* List all compositions in a csv file, for example, 'composition.csv' in this github respository. Each line is a composition. 
* Run GlycanMP1.exe using the following command line
  ```
    GlycanC2T.exe composition.csv
  ```
* GlycanMP.exe reads the composition file and generates one json file for each composition in the same folder where GlycanMP1.exe is located.
