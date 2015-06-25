import HBarPlotter
import matplotlib.pyplot as plt
import numpy as np

met_str = "\\not\mathrel{E}_T"

def get_edm_results():
    edm = []
    # virtual gravtion exchange 
    theo = "ADD n=4"
    edm.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, "$ee+\mu\mu\,\,\, \star$" ),4.14] )
    edm.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, "$ee+\mu\mu\,\,\, \star$" ),4.0] )
    #~ edm.append( ['CMS', r'ADD (j+MET)',3.2] )
    #~ edm.append( ['ATLAS', r'ADD (j+MET)',3.0] )
    #~ edm.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, "jj" ),2.1] )
    #~ edm.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, "jj" ),0.0] )
    
    #http://arxiv.org/pdf/1112.0688v2.pdf
    edm.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, "$\gamma\gamma$" ),1.84] )
    #http://arxiv.org/pdf/1504.05511v1.pdf
    edm.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, "$\gamma\gamma$" ),2.66] )
    
    #http://lanl.arxiv.org/pdf/1408.3583v1.pdf
    edm.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, "$j+%s$"%met_str ),3.56] )
    #http://arxiv.org/pdf/1504.05511v1.pdf
    edm.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, "$j+%s$"%met_str ),3.97] )
    
    #http://arxiv.org/pdf/1410.8812v1.pdf
    edm.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, "$\gamma+%s$"%met_str ),2.2] )
    #http://arxiv.org/pdf/1411.1559v2.pdf
    edm.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, "$\gamma+%s$"%met_str ),2.13] )
    
    theo = "RS $G_{KK}$ $\\tilde{k}$=0.1"#/$\\bar{M}_{Pl}=0.1
    #arXiv:1211.1150
    edm.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, "$ee+\mu\mu\,\,\, \star$" ),2.56] )
    #http://arxiv.org/abs/1405.4123
    edm.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, "$ee+\mu\mu\,\,\, \star$" ),2.68] )
    
    #http://arxiv.org/pdf/1112.0688v2.pdf
    edm.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, "$\gamma\gamma$" ),1.84] )
    #http://arxiv.org/pdf/1504.05511v1.pdf
    edm.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, "$\gamma\gamma$" ),2.66] )
    
    #arxiv 1501.04198
    edm.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, "$jj\,\,\, \star$" ),1.6] )
    edm.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, "$jj\,\,\, \star$" ),0.0] )
    theo = "RS $g_{KK}$ $\\tilde{k}$=1"#/$\\bar{M}_{Pl}=0.1
    edm.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo , r'$tt\,\,\, \star$' ),2.2] ) 
    edm.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo , r"$tt\,\,\, \star$" ),2.8] )
    
    # add on site
    theo = "RS1 $G_{KK}$ $\\tilde{k}$=1"#/$\\bar{M}_{Pl}=0.1
    edm.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo , r'$l \nu qq$' ),0.7] ) 
    edm.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo , r'$l \nu qq$' ),0.0] )
    
    #arXiv:1503.04677;
    edm.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo , r'$ll qq$' ),0.74] ) 
    edm.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo , r'$ll qq$' ),0.0] )
    
    
    
    edm = np.array(edm)
    return edm
    
def get_qbh_results():
    qbh = []
    theo = "CALCHEP RS n=1"
    qbh.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, "$e\mu \,\, \star$" ),3.7] )
    qbh.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, "$e\mu \,\, \star$" ),0.0] )
    theo = "CALCHEP ADD n=6"
    qbh.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, "$e\mu \,\, \star$" ),2.4] )
    qbh.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, "$e\mu \,\, \star$" ),0.0] )
    theo = "BLACKMAX n=6"
    qbh.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, "$jj\,\, \star$" ),0.0] )
    
    qbh.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, "$jj\,\, \star$" ),5.62] )
    
    theo = "$QBH_{GEN}$"
    qbh.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, "$jj\,\, \star$" ),5.8] )
    qbh.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, "$jj\,\, \star$" ),5.66] )
    theo = "$QBH_{GEN} RS$"
    qbh.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, "$ll\,\, \star$" ),0.0] )
    qbh.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, "$ll\,\, \star$" ),2.24] )
    theo = "$QBH_{GEN} ADD$"
    qbh.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, "$ll\, \star$" ),0.0] )
    qbh.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, "$ll\, \star$" ),3.65] )
    return np.array(qbh)
    
def get_prime_results():
    prime = []
    theo = "$Z^\prime$"
    #arxiv 1412.6302
    prime.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, "$ee+\mu\mu\,\,\, \star$" ),2.9] )
    
    prime.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, "$ee+\mu\mu\,\,\, \star$" ),2.9] ) 
    #1501.04198
    #Z' 0 boson (Z' 0 )qq[1.2,1.7]
    #~ prime.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, r'$jj$' ),1.7] )
    #prime.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, r'bb' ),0.0] ) 
    #prime.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, r"bb" ),2.9] )
    
    #~ prime.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo , r'$tt$' ),0.] ) 
    #~ prime.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo , r"$tt$" ),2.4] )
    
    prime.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo , r'$e\mu\,\,\, \star$' ),2.5] ) 
    prime.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo , r"$e\mu\,\,\, \star$" ),0.0] )
    prime.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo , r'$e\tau\,\,\, \star$' ),2.2] ) 
    prime.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo , r"$e\tau\,\,\, \star$" ),0.0] )
    prime.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo , r'$\mu\tau\,\,\, \star$' ),2.2] ) 
    prime.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo , r"$\mu\tau\,\,\, \star$" ),0.0] )
    
    
    theo = "$Z^{\prime}_{TC2}$"
    prime.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo , r'$tt\,\,\, \star$' ),2.0] ) 
    prime.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo , r"$tt\,\,\, \star$" ),0.0] )
    
    theo = "$W^{\prime}_{R}$"
    prime.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, r'$tb$' ),2.05] )
    prime.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, r'$tb$' ),1.92] )
   
    theo = "$W^{\prime}_{L}$"
    prime.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, r'$tb$' ),2.05] )
    prime.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, r'$tb$' ),1.8] )
    theo = "$W^\prime$"
    #1408.2745
    prime.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, r'$l+%s\,\,\, \star$' % met_str ),3.28] )
    #1407.7494
    prime.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, r'$l+%s\,\,\, \star$' % met_str ),3.24] ) 
    #1501.04198
    #W' boson (W' )qq [1.2,1.9] + [2.0,2.2]
    prime.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, r'$jj\,\,\, \star$' ),2.2] )
    #1407.1376
    prime.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, r'$jj\,\,\, \star$' ),2.45] ) 
    
    theo = "$W^\prime_{EGM}$"
    # added on site
	#EPJC 75 (2015) 209
    prime.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, r'$jj$' ),1.5] )
    # arXiv:1405.1994
    prime.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, r'$jj$' ),1.7] )     
    
    prime.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, r'$l \nu qq$' ),0.0] )
    # arXiv:1503.04677
    prime.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, r'$l \nu qq$' ),1.5] ) 
        
    prime.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, r'$llqq$' ),0.0] )
    # arXiv:1409.619
    prime.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, r'$llqq$' ),1.5] ) 
        
    prime.append( ['CMS', r'{0:<8}: {1:<8}'.format( theo, r'$l \nu ll$' ),0.0] )
    # ATLAS-CONF-2014-015
    prime.append( ['ATLAS', r'{0:<8}: {1:<8}'.format( theo, r'$l \nu ll$' ),1.7] )     
    
    return np.array(prime)
    
def plotSummary( resultList, outputName ,yshift = 0.4, left_margin =0.43):
    #get colors
    mycolors = HBarPlotter.texcolormap
    # add data for extra dimensions, heavy gauge bosons and compositness
    temp = np.array( resultList[:,2], 'd' )
    plotter =  HBarPlotter.HbarPlotter(aspect_width = 6 ,
                                       aspect_height = 8,
                                       space = 0.2,
                                       sortoption = 'alphabetical')
    #~ fig, (ax_edm, ax_prime) = plt.subplots(2, 1, sharey=True)
    fig, ax_edm = plt.subplots(1, 1, sharey=True)
    #~ ax_edm.set_axisbelow(True)
    # set number of xticks
    xticks = np.arange(max( np.array( resultList[:,2], 'd') ) )
    ax_edm.set_xticks( xticks )
    #~ grid = ax_edm.grid(axis = 'x', color ='white', linestyle='-', linewidth = 1.4)
    exp_colors = {'CMS':mycolors['lightblue'], 'ATLAS':mycolors['darkblue']}
    grid = ax_edm.grid( axis = 'x',
                        color = mycolors['verylightblue'],
                        linestyle='-',
                        linewidth = 2)
    handles, labels = plotter.makeHbarPlot( ax_edm,
                                            resultList, 
                                            xlabel = r'Mass limit [TeV]',
                                            condition_colormap = exp_colors)
    plotter.remove_border(ax_edm, top=False, right=False, left=False, bottom=False)
#~ 
    #~ fig.tick_params(axis='both', which='major', labelsize=10)
    #~ fig.tick_params(axis='both', which='minor', labelsize=8)
    plt.draw()
    yax = ax_edm.get_yaxis()
    # find the maximum width of the label on the major ticks
    # from http://stackoverflow.com/questions/15882249/matplotlib-aligning-y-ticks-to-the-left
    pad = max(T.label.get_window_extent().width for T in yax.majorTicks)
    yax.set_tick_params(pad=pad * yshift)

    plt.subplots_adjust(left= left_margin, right=0.93, top=0.95, bottom=0.1)
    # Add global legend
    plt.figlegend(handles[::-1], labels[::-1], loc='upper center', ncol = 2, frameon=False)
    # Save figure to file
    plt.savefig('Figures/barh_%s.pdf' % outputName)      
    
def main():
    plotSummary( get_edm_results(), 'edm',0.55,0.58)
    plotSummary( get_prime_results(), 'prime',0.65,0.35)
    plotSummary( get_qbh_results(), 'qbh',0.57,0.59)
    #~ #get colors
    #~ mycolors = HBarPlotter.texcolormap
    #~ # add data for extra dimensions, heavy gauge bosons and compositness
    #~ edm = get_edm_results()
    #~ temp = np.array(edm[:,2], 'd')
    #~ plotter =  HBarPlotter.HbarPlotter(aspect_width = 6 ,
                                       #~ aspect_height = 8,
                                       #~ space = 0.2,
                                       #~ sortoption = 'alphabetical')
    #~ fig, ax_edm = plt.subplots(1, 1, sharey=True)
    #~ # set number of xticks
    #~ xticks = np.arange(max( np.array(edm[:,2], 'd') ) )
    #~ ax_edm.set_xticks( xticks )
    #~ ##~ grid = ax_edm.grid(axis = 'x', color ='white', linestyle='-', linewidth = 1.4)
    #~ exp_colors = {'CMS':mycolors['lightblue'], 'ATLAS':mycolors['darkblue']}
    #~ grid = ax_edm.grid( axis = 'x',
                        #~ color = mycolors['verylightblue'],
                        #~ linestyle='-',
                        #~ linewidth = 1.4)
    #~ handles, labels = plotter.makeHbarPlot( ax_edm,
                                            #~ edm, 
                                            #~ xlabel = r'Mass limit [TeV]',
                                            #~ condition_colormap = exp_colors)
    #~ plotter.remove_border(ax_edm, top=False, right=False, left=False, bottom=False)
#~ 
#~ 
    #~ plt.draw()
    #~ yax = ax_edm.get_yaxis()
    #~ # find the maximum width of the label on the major ticks
    #~ # from http://stackoverflow.com/questions/15882249/matplotlib-aligning-y-ticks-to-the-left
    #~ pad = max(T.label.get_window_extent().width for T in yax.majorTicks)
    #~ print pad
    #~ yax.set_tick_params(pad=pad *0.5)
#~ 
    #~ plt.subplots_adjust(left=0.3, right=0.93, top=0.95, bottom=0.1)
    #~ # Add global legend
    #~ plt.figlegend(handles[::-1], labels[::-1], loc='upper center', ncol = 2, frameon=False)
    #~ # Save figure to file
    #~ plt.savefig('Figures/edm.pdf')
    
    
if __name__ == '__main__':
    main()
