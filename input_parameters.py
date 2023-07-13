#input parameters
intensity       =      230e10
#bunchLength_ns =       150 #4 sigma in ns
#bunchLength_m	=	    10.67 #1 sigma in m
emittance_x     =       1.4e-6
emittance_y     =       1.4e-6
dpp_rms         =       1.6e-3
#ro             =       # classical radius : default proton change for ions accordingly
bF              =       0.36 # None for Gaussian
Qh		=	6.21    # to estimate detuning and plot
Qv		=	6.24    # to estimate detuning and plot
plot_range  =   [[5.85,6.3],[5.85,6.3]]   # range in Qh & Qv for the plot
plot_order  =   4  # order of resonances to plot
periodicity =   50  # periodicity of ring for the colorcode of the plot
figure		=	'figure.png'
twiss_file  =   'twiss_files/twiss_PS'
harmonic    =   7
#b  =   # relativistic beta  :  if desired energy different than in twiss file
#g  =   # relativistic gamma :  if desired energy different than in twiss file
