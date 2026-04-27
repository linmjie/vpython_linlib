<!--TOC-->
# Installation
- You should always use virtual environments when dealing with Python modules
- Below has instructions for you to start using these virtual environments
- If you don't care about this, you can skip to the local installation for this Python module [here](#installing-this-library)
<!--TOC-->
## Using miniconda virtual environments
<p>
  Miniconda is my preferred virtual environment manager
</p>

### Windows installation
- Install Window's package manager, [Scoop](https://scoop.sh/), running the command on the website (make sure it is in Powershell, not terminal)
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
