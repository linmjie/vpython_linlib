<!--TOC-->
# Installation
- You should always use virtual environments when dealing with Python modules
- Below has instructions for you to start using these virtual environments
- If you don't care about this, you can skip to the local installation for this Python module [here](#installing-this-library)

<!--TOC-->
## Using miniconda virtual environments
Miniconda is my preferred virtual environment manager, this guide will teach you the very basics of using it. For more comprehensive documentation, see the [official anaconda guide](https://www.anaconda.com/docs/getting-started/working-with-conda/conda-intro-tutorial)
- Install miniconda on [Windows](#windows-installation), [macOS](#macos-installation), or [Linux](linux-installation)
- Make sure you ran the proper conda init command, otherwise you will not be able to create and use virtual environments
- You can run 'conda' or 'conda --help' in your terminal to get a list of conda commands
- Create a virtual environment with conda create, placing the name of your virtual environment after the -n flag
```shell
conda create -n MY_ENVIRONMENT_NAME
```
- Any arguments after will automatically be installed into that environment
```shell
conda create -n ENVIRONMENT_WITH_SOME_LIBRARIES module1 module2 module3
```
- Here's some example environments you can use
  - Virtual environment for vpython:
    ```shell
    conda create -n vpython vpython
    ```
  - Virtual environment for data science:
    ```shell
    conda create -n datascience numpy pandas matplotlib
    ```
- Once you create your environment, it'll give you some instructions on how to use it, notably how to activate and deactivate it
- To activate:
```shell
conda activate ENVIRONMENT_NAME
```
- To deactivate (you do not need to supply the argument for which environment to deactivate):
```shell
conda deactivate
```
- You can see what environment you are in to the left of you terminal prompt (base is your standard environment, do not touch your base environment)

<!--TOC-->
## Windows installation
- Install Window's package manager, [Scoop](https://scoop.sh/)(make sure you run this in Powershell, not terminal, switch to your terminal once you downloaded Scoop)
- Install git via Scoop for repository cloning for buckets
```powershell
scoop install git
```
- Install the 'extras' bucket that contains miniconda
```powershell
scoop bucket add extras
```
- Install miniconda
```powershell
scoop install miniconda3
```
- Activate miniconda in your terminal by running this command:
```powershell
conda init powershell
```
- Restart your terminal after, miniconda will now work for future terminal sessions

<!--TOC-->
## macOS installation
- Install macOS's package manager, [HomeBrew](https://brew.sh/). [MacPorts](https://www.macports.org/install.php) may work better on Intel Macs
- Install miniconda via homebrew
```shell
brew install --cask miniconda
```
- Activate miniconda in your terminal by running this command:
```shell
conda init zsh
```
- If your Mac is really old, you may run bash. Replace zsh in the command with bash
  - You can check which shell your terminal runs via this command:
    ```shell
    which $SHELL
    ```
- Restart your terminal after, miniconda will now work for future terminal sessions

<!--TOC-->
## Linux installation
- Install miniconda, either following the [website](https://www.anaconda.com/docs/getting-started/miniconda/install/linux-install)'s instructions, or installing via your favorite package manager (package is typically called miniconda3)
- Activate miniconda in your terminal by running this command:
```shell
conda init bash
```
- If you use zshell, just replace bash with zsh
- Restart your terminal after, miniconda will now work for future terminal sessions
<!--TOC-->
## Installing this library
<p>This is supposed to work with vpython, make sure your environment has vpython installed</p>

Cloning the repo:
```
git clone https://github.com/linmjie/vpython_linlib.git
```
Manual pip installation (use python3/pip3 if necessary)
```
pip install -e .
```
<p>
  Note: '.' can be replaced with whatever path takes you to the vpython_linlib directory
</p>
