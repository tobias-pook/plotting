import numpy as np
import matplotlib.pyplot as plt
# Set up some better defaults for matplotlib
from matplotlib import rcParams
import brewer2mpl
import operator as o
import matplotlib.cm as cm

texcolormap = {  'blue':np.array((0, 84, 159)) / 255. ,
                 'darkblue':np.array((0, 59, 111)) / 255. ,
                 'lightblue':np.array((142, 186, 229)) / 255. ,
                 'verylightblue':np.array((242, 241, 250)) / 255. ,
                 'red':np.array((204, 7, 30)) / 255. ,
                 'lightred':np.array((250, 235, 227)) / 255. ,
                 'green':np.array((0, 128, 0)) }
              
class HbarPlotter():
    
    #The object constructor
    #
    #@param self The object pointer
    #@param results A dict structure {label , values, category, subcategory}
    #@param aspect_width for plot figure [default 3]
    #@param aspect_height for plot figure [default 8]
    #@param space space between each set of bars [default 0.3]
    def __init__(self, aspect_width = 4 ,
                       aspect_height = 8 ,
                       space = 0.4,
                       sortoption = 'mean'):
        
        # set aspect ratio for plots
        self.aspect_width = aspect_width
        self.aspect_height = aspect_height
        self.space = space
        self.sortoption = sortoption
        # set some style settings
        #colorbrewer2 Dark2 qualitative color table
        #~ dark2_colors = brewer2mpl.get_map('Dark2', 'Qualitative', 6).mpl_colors
        dark2_colors = brewer2mpl.get_map('Set2', 'Qualitative', 3).mpl_colors
        bg_color = texcolormap['verylightblue']
        rcParams['figure.figsize'] = (aspect_width, aspect_height)
        rcParams['figure.dpi'] = 150
        rcParams['figure.facecolor'] = bg_color
        rcParams['figure.edgecolor'] = bg_color
        rcParams['savefig.facecolor'] = bg_color
        rcParams['savefig.edgecolor'] = bg_color
        rcParams['axes.color_cycle'] = dark2_colors
        rcParams['axes.facecolor'] = bg_color
        rcParams['lines.linewidth'] = 2
        #~ rcParams['axes.facecolor'] = 'white'
        rcParams['font.size'] = 14
        rcParams['patch.edgecolor'] = 'white'
        #~ rcParams['patch.facecolor'] = dark2_colors[0]
        rcParams['patch.facecolor'] = texcolormap['verylightblue']
        #~ rcParams['font.family'] = 'StixGeneral'
        rcParams['font.family'] = 'sans-serif'
        rcParams['text.usetex'] = True
        rcParams['font.sans-serif'] = 'Helvetica'
        rcParams['text.latex.unicode']=True
        
    def makeHbarPlot(self,
                     ax,
                     dpoints,
                     condition_colormap = None, 
                     xlabel = None,
                     ylabel = None ,
                     axLabelSize = 22,
                     tickLabelSize = 18,
                     addLegend = False):
        '''
        Create a barchart for data across different categories with
        multiple conditions for each category. 
    
        @param self: The Object pointer
        @param ax: The plotting axes from matplotlib.
        @param dpoints: The data set as an (n, 3) numpy array (category, condition, value)
        '''  
        
        # Aggregate the conditions and the categories according to their
        # mean values
        conditions = [(c, np.mean(dpoints[dpoints[:,0] == c][:,2].astype(float))) 
                      for c in np.unique(dpoints[:,0])]
        for c in np.unique(dpoints[:,1]):
            print dpoints[dpoints[:,1] == c][0][1]
        if self.sortoption == 'mean':
            categories = [(c, np.mean(dpoints[dpoints[:,1] == c][:,2].astype(float))) 
                          for c in np.unique(dpoints[:,1])]
        elif self.sortoption == 'alphabetical':
            categories = [(c, dpoints[dpoints[:,1] == c][0][1]) 
                          for c in np.unique(dpoints[:,1])]
        print categories
        
        # sort the conditions, categories and data so that the bars in
        # the plot will be ordered by category and condition
        conditions = [c[0] for c in sorted(conditions, key=o.itemgetter(1))]
        categories = [c[0] for c in sorted(categories, key=o.itemgetter(1),reverse=True)]
        
        dpoints = np.array(sorted(dpoints, key=lambda x: categories.index(x[1])))
        # the space between each set of bars
        n = len(conditions)
        width = (1 - self.space) / (len(conditions))
        
        # Create a set of bars at each position
        for i,cond in enumerate(conditions):
            indeces = range(1, len(categories)+1)
            vals = dpoints[dpoints[:,0] == cond][:,2].astype(np.float)
            pos = [j - (1 - self.space) / 2. + i * width for j in indeces]
            # check if condition specific numbers present
            if not condition_colormap == None:
                barcolors = condition_colormap[cond]
            else:
                barcolors = cm.Accent(float(i) / n)
            ax.barh(pos, vals, height=width, label=cond, 
                   color= barcolors)
                   
        ax.set_yticks(indeces)

        ax.set_yticklabels(categories, ha = 'left')
        ax.tick_params(axis='both', which='major', labelsize=tickLabelSize)
        ax.tick_params(axis='both', which='minor', labelsize=tickLabelSize)
        # Add the axis labels
        if not ylabel == None: 
            ax.set_ylabel(ylabel)
        if not xlabel == None: 
            ax.set_xlabel(xlabel, fontsize = 22)
        handles, labels = ax.get_legend_handles_labels()
        # Add a legend
        if addLegend:
            
            ax.legend(handles[::-1], labels[::-1], loc='upper center',
                        bbox_to_anchor=(0.5, 1.11), ncol = 2, frameon=False)
        return handles, labels
        
    @property
    def nCategories(self):
        return len( self.results.keys() )
        
    def remove_border(self, axes=None, top=False, right=False, left=True, bottom=True):
        '''
        Minimize chartjunk by stripping out unnecesasry plot borders and axis ticks
        
        The top/right/left/bottom keywords toggle whether the corresponding plot border is drawn
        '''
        ax = axes or plt.gca()
        ax.spines['top'].set_visible(top)
        ax.spines['right'].set_visible(right)
        ax.spines['left'].set_visible(left)
        ax.spines['bottom'].set_visible(bottom)
        
        #turn off all ticks
        ax.yaxis.set_ticks_position('none')
        ax.xaxis.set_ticks_position('none')
        
        #now re-enable visibles
        if top:
            ax.xaxis.tick_top()
        if bottom:
            ax.xaxis.tick_bottom()
        if left:
            ax.yaxis.tick_left()
        if right:
            ax.yaxis.tick_right()
    

