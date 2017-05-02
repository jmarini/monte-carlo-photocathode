# Monte Carlo Scripts

This is a collection of scripts for analysis and plotting of monte carlo data. It is collected into folders depending on the program or runtime used.

## File Listing

###  gnuplot

To run any gnuplot script use the following command

    gnuplot -c SCRIPT ARG1 ARG2 ...


``make_gif.txt`` - ARG1 = output type to plot (i.e. potential), ARG2 = step to end at, defaults to 100. Plots 2d gif of output type from step 1 to speficied end.

``make_3d_gif.txt`` - ARG1 = output type to plot (i.e. potential), ARG2 = step to end at, defaults to 100. Plots 3d gif of output type from step 1 to speficied end.

``make_energy_gif.txt`` - ARG1 = step to end at, defaults to 100. Plots gif of average electron energy overlaid on the band structure from step 1 to specified end.

``make_energy_gif2.txt`` - ARG1 = step to end at, defaults to 100. Plots gif of electron energy overlaid on the band structure from step 1 to specified end.

``plot_energy.txt`` - ARG1 = step to plot, defaults to 0. Plots electron energy overlaid on the band structure for specified step.

``make_histogram.txt`` - Plots histogram of emitted electrons.

## Python

``band_tracking.py`` - Deprecated, uses old output format. Outputs electron path overlaid on band structure.

``band_tracking_binary.py`` - Outputs electron path overlaid on band structure as png images as well as summary info on each particle such as number of times scattered and average distance between scattering events.

``distance.py`` - Output scatter plot of emitted electrons - starting location vs excess energy above vacuum.

``max_qe.py`` - Output emitted particle histogram overalid on band structure. Also prints summary info.

``mcanalyze.py`` - Initial work on auto-analysis of results from mcautomate. Right now takes a UUID as input and unzips the result file.

``process_data.py`` - Processes output from Sentaurus to align to required input standards for monte carlo. Use ``monte_carlo.tcl`` file to output in the proper format for this script. Note that all device dimensions must match between sentaurus and monte carlo, but meshing does not need to match.

``surface_bb.py`` - Outputs near-surface band structure of tsv file output from ``process_data.py``.

``tracking.py`` - Example script for reading binary tracking files.

``validation.py`` - Plots histogram of emitted particles.

``valley_occupation.py`` - Plots valley occupation over time.

## IPython

Note that these files require jupyter notebook to view. In a pinch you can open the files in a text editor and see the raw code.

``00-distribution.ipynb`` - Plot various distributions of emitted particles. Also includes analysis of QE vs electron affinity for earlier experiments for validation.

``01-errors.ipynb`` - Attempts to fit emitted particle distribution and validation of specific particles that gave strange results - mostly used for fixing errors.

``02-tracking.ipynb`` - Early attempts at creating the particle tracking outputs. Relies on the old tracking (non-binary) outputs so does not work any more.

``03-tracking-binary.ipynb`` - Work towards creating the particle tracking outputs using the new binary format.

``04-summary.ipynb`` - Plotting some summary data on emitted particles and histograms showing number of times scattered, mean distance travelled, etc.

``poisson.ipynb`` - Analytic calculation of band structure for a given surface band bending. Verification prior to implementation of new surfacebb feature.

``probability.ipynb`` - Attempts to pull out analytic equations of QE based on monte carlo simulation results. Modeled average distance travelled between scattering events using exponential distribution. Multiple scattering events are modeled using a poisson distribution with parameterized on k, defined as the number of scattering events to bring particle below vacuum energy. Very preliminary exploration.
