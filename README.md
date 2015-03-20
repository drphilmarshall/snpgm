# Supernova Cosmology PGMs

Starting life as a
[hack](https://hackpad.com/CtU2015-Hacks-and-Hackers-8rzvsLPoA89) at
the [Computing the Universe
2015](http://bccp.berkeley.edu/dev/?page_id=2165) workshop, this is now a
repository for testing out ideas for forward-model/hierarchical
supernova cosmology inference.

## About

We're performing inference on Probabalistic Graphical Models (PGMs) like this one:

![PGM](https://github.com/drphilmarshall/snpgm/blob/master/doc/images/snpgm_pjm.png)

It's specific to the SALT2 light curve model, in terms of the parameters that
describe each light curve. Read [this evolving PDF document](https://github.com/drphilmarshall/snpgm/blob/master/doc/details.pdf) for more details.

## People, Credits, Licence etc

Active on this repo are:

* Kyle Barbary (Berkeley)
* Clare Saunders (Berkeley)
* Phil Marshall (SLAC)
* Kara Ponder (Pitt)
* Michael Wood-Vasey (Pitt)
* Josh Meyers (Stanford)

This is astrophysics research in progress: use at your own risk! When referring to this repo in your papers, please cite (Barbary, Ponder et al). The python code is available via the MIT licence: if you feel like playing around, please do introduce yourself by writing us an [issue](https://github.com/kbarbary/snpgm/issues/new).


## Getting Started

Hopefully the following will be enough to get you going on using the code.

**Code Dependencies:**

- astropy
- sncosmo
- emcee
- triangle
- daft

... and the usual numpy/scipy/mpl business.


**Scripts:**

- `gen_pgm.py`: Script to draw the PGM. Generates `snpgm.png`.

- `gen_dataset.py`: Generate a test light curve data set, write each
  light curve to a file in the `testdata` directory. (In all scripts,
  directories are created if they don't already exist.)

- `plot_testdata.py`: Make a plot of the light curve data for each
  file in `testdata`, save to `lcplots` directory. Just to visualize
  the light curve data a bit.

- `naive_sampling.py`: Throw all the SN parameters and global parameters into
  a big MCMC and let it run. That's `4*N_SN + 4` parameters.

Importance sampling is two steps:

- `sample_lcs.py`: Run an MCMC on each light curve in `testdata` individually,
  save samples to `samples` directory as numpy binary files.

- `importance_sampling.py`: Run impotance sampling using the
  individual SN samples already created in previous step.

**Importance sampling papers:**

- Sonnenfeld et al "SL2S Paper 5" (strong lens ensemble)
- Schneider et al: Hierarchical WL
