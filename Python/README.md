

# Downloading Python 3.7 version of Anaconda and OpenCV
---

## Windows
```bash
md AnacondaBinary
cd  AnacondaBinary
wget https://repo.anaconda.com/archive/Anaconda3-2019.07-Windows-x86_64.exe
```

## Mac
```bash
mkdir AnacondaBinary
cd  AnacondaBinary
wget https://repo.anaconda.com/archive/Anaconda3-2019.07-MacOSX-x86_64.pkg
```


## Linux
```bash
mkdir AnacondaBinary
cd  AnacondaBinary
wget https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh
```
Go to this link https://repo.anaconda.com/archive/ and search for the latest packges
Based on you operating system, after successful download, execute the binary and follow the instructions in the GUI.  


After you Anaconda installation ensure to update your packages
```bash
# First update conda package installer itself.
conda update conda -y

# Update all packages here.
conda update --all -y
```

# Jupyter Notebook
My preference for testing would be Jupyter Notebook
You can use **GUI** to open Jupyter Notebook or from the **command prompt** using the syntax below:
```bash
jupyter-notebook
```

## Jupyter Notebook Browser
Jupyter Notebook Homepage ![alt text](https://git.txstate.edu/v-s191/MachineLearning/blob/master/images/Screen%20Shot%202019-09-08%20at%2010.01.20%20AM.png?raw=true)

## Open a new Notebook
Click on the **New** drop down box and Choose **Python3**

New Jupyter Notebook ![alt text](https://git.txstate.edu/v-s191/MachineLearning/blob/master/images/Screen%20Shot%202019-09-08%20at%209.40.28%20AM.png?raw=true)


## Jupyter Notebook Editor

Jupyter Notebook ![alt text](https://git.txstate.edu/v-s191/MachineLearning/blob/master/images/Screen%20Shot%202019-09-08%20at%209.43.12%20AM.png?raw=true)

## Save your Notebook for later usage
Double click on the **Untitled** text beside the Jupyter Logo.
> By default auto save will be enabled

Saving Your Work ![alt text](https://git.txstate.edu/v-s191/MachineLearning/blob/master/images/Screen%20Shot%202019-09-08%20at%209.48.34%20AM.png?raw=true)

## Working with Notebook
Type in Python syntax and press ``` Shift Enter ```

Working with Notebook ![alt text](https://git.txstate.edu/v-s191/MachineLearning/blob/master/images/Screen%20Shot%202019-09-08%20at%209.51.09%20AM.png?raw=true)


For more details refer to 
Jupyter Notebook Documentation ![alt text](https://jupyter.readthedocs.io/en/latest/running.html?raw=false)


# Installing OpenCV after the installation of Anaconda
---
Open a command prompt (for windows) or open a shell (Linux/MacOS)

```bash
  conda install -c conda-forge opencv
```

or if you wish to install a specific version follow the instructions below
```bash
  conda install -c conda-forge opencv=3.4.1
```





