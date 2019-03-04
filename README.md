# cantera-jupyter

[Cantera](https://cantera.org) examples in the form of [Jupyter](http://jupyter.org)
notebooks. To see the rendered notebooks, browse the directories above or visit the
links in the list of examples below.

**Existing Cantera users**: If you have [Cantera](https://cantera.org) and
[Jupyter](http://jupyter.org) installed on your local machine, simply download
any Jupyter notebook and you should be able to run it.

**New Cantera Users**: If you don't have an exiting Cantera installation, you
can either
[download and install Cantera](https://cantera.org/install/index.html)
or give Cantera a test drive in the cloud. Click on the Binder link below to
launch an interactive environment where you can run these examples. For this,
there is no installation required.

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/cantera/cantera-jupyter)

## Examples

<table align="center">

<tr align="center">
<td> <img src="flames/images/flameSpeed.png" width=250px> <br> Freely Propagating Flame  </td>
<td> <img src="flames/images/twinPremixedFlame.png" width=250px> <br> Strained Flames </td>
</tr>

<tr align="center">
<td> <img src="reactors/images/stirredReactorCartoon.png" width=250px> <br> Continuous Stirred Tank Reactor </td>
<td> <img src="reactors/images/batchReactor.png" width=175px> <br> Batch Reactor </td>
</tr>

<tr align="center">
<td> <img src="electrochemistry/images/SingleParticleBattery.png" width=250px> <br> Li+ Battery OCV Calculation</td>
</tr>

</table>

* Basic Thermodynamics Calculations
  * [Fuel heating value calculator](https://github.com/Cantera/cantera-jupyter/blob/master/thermo/heating_value.ipynb)
  * [Equilibrium flame temperature calculator](https://github.com/Cantera/cantera-jupyter/blob/master/thermo/flame_temperature.ipynb)

* Flame Simulations
  * [Flame speed calculator with sensitivity analysis](https://github.com/Cantera/cantera-jupyter/blob/master/flames/flame_speed_with_sensitivity_analysis.ipynb)
  * [Counter-flow twin premixed flame simulator](https://github.com/Cantera/cantera-jupyter/blob/master/flames/twin_premixed_flame_axisymmetric.ipynb)

* Reactor Models
  * [Batch Reactors: Illustration of ignition delay calculation](https://github.com/Cantera/cantera-jupyter/blob/master/reactors/batch_reactor_ignition_delay_NTC.ipynb)
    * [Batch reactors with non-ideal gases](https://github.com/Cantera/cantera-jupyter/blob/master/reactors/NonIdealShockTube.ipynb)
  * [Continuous Reactors: Simulations at a given residence time](https://github.com/Cantera/cantera-jupyter/blob/master/reactors/stirred_reactor.ipynb)

* Electrochemistry
  * [Open circuit voltage calculations in a Lithium ion battery](https://github.com/Cantera/cantera-jupyter/blob/master/electrochemistry/lithium_ion_battery.ipynb)

## Installation Instructions (for New Users)

### 1. Install Anaconda Distribution

1.   Head on to /www.anaconda.com/distribution/ and download the Anaconda distrubtion according to your OS

2.  Install it on your machine.

### 2. Setting up the conda environment

* Option 1: Create a new environment for Cantera

If you have just installed Anaconda or Miniconda, the following instructions will create a conda environment where you can use Cantera. For this example, the environment is named spam. From the command line (or the Anaconda Prompt on Windows), run:

    conda create --name spam --channel cantera cantera ipython matplotlib
This will create an environment with Cantera, IPython, Matplotlib, and all their dependencies installed. Although Conda can install a large set of packages by default, it is also possible to install packages such as Cantera that are maintained independently. These additional channels from which packages may be obtained are specified by adding the --channel option in the install or create commands. In this case, we want to install Cantera from the cantera channel, so we add --channel cantera and to tell Conda to look at the cantera channel in addition to the default channels.

To use the scripts and modules installed in the spam environment, you must activate it it by running:

    conda activate spam

* Option 2: Install Cantera in an existing environment

First, activate your environment (assumed here to be named baked_beans; if you’ve forgotten the name of the conda environment you wanted to use, the command conda env list can help). This is done by running:

    conda activate baked_beans
Then, install Cantera in the active enironment by running:

    conda install --channel cantera cantera

* Option 3: Install the development version of Cantera

To install a recent development snapshot (i.e., an alpha or beta version) of Cantera in an existing environment, activate the environment and then run:

    conda install --channel cantera/label/dev cantera
If you later want to revert back to the stable version, first remove and then reinstall Cantera:

    conda remove cantera

    conda install --channel cantera cantera

### 3. Notebook Setup
1. Activate the environment having cantera package
```
conda activate spam
```
2. Install the notebook package
```
conda install notebook
```
3.  Run Jupter notebook
```
jupyter notebook
```

## Code of Conduct

This repository follows the same code of conduct as the main Cantera repository.
Cantera adheres to a [code of conduct](https://github.com/Cantera/cantera/blob/master/CODE_OF_CONDUCT.md)
adapted from the [Contributor Covenant code of conduct](https://contributor-covenant.org/).

## Frequently Asked Questions

**How do I use Cantera with Python?**

An introduction to the Cantera Python interface is available
[here](https://cantera.org/tutorials/python-tutorial.html). For more
advanced uses of Cantera, the complete documentation can be found
[here](https://cantera.org/documentation/index.html).

**Can I forgo installing Cantera locally and just use Cantera in the cloud every
time?**

The problem with using Cantera with Binder is that there is no way for you to
save your work. You can upload/download files in a session, but once the session
is over (you close your browser window), you lose all your work. You thus cannot
save your modified Jupyter notebooks.

**I still can't figure something out. Who do I ask?**

If you have more questions, need help with something, or have any suggestions,
please visit the
[Cantera Google Groups Page](https://groups.google.com/forum/#!forum/cantera-users)
and create a post.
