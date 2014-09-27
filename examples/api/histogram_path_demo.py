"""
This example shows how to use a path patch to draw a bunch of
rectangles.  The technique of using lots of Rectangle instances, or
the faster method of using PolyCollections, were implemented before we
had proper paths with moveto/lineto, closepoly etc in mpl.  Now that
we have them, we can draw collections of regularly shaped objects with
homogeous properties more efficiently with a PathCollection.  This
example makes a histogram -- its more work to set up the vertex arrays
at the outset, but it should be much faster for large numbers of
objects
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

def histogram_path_demo(ax, hist, bin_edges, **kwargs):
    """
    Example function to plot a histogram

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    hist : array
        The values of the histogram.

    bin_edges : array
        The bin_edges (length(hist)+1).

    **kwargs : dict
        Dictionary of kwargs to pass to matplotlib.patches.PathPath
    """

    # get the corners of the rectangles for the histogram
    left   = np.array(bin_edges[:-1])
    right  = np.array(bin_edges[1:])
    bottom = np.zeros(len(left))
    top = bottom + hist
    # we need a (numrects x numsides x 2) numpy array for the path helper
    # function to build a compound path
    XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T

    # get the Path object
    barpath = path.Path.make_compound_path_from_polys(XY)
    # make a patch out of it
    patch = patches.PathPatch(barpath, **kwargs)
    ax.add_patch(patch)
    # update the view limits
    ax.set_xlim(left[0], right[-1])
    ax.set_ylim(bottom.min(), top.max())


fig, ax = plt.subplots()
data = np.random.randn(1000)
n, bins = np.histogram(data, 50)
histogram_path_demo(ax,n,bins, facecolor="blue", edgecolor="black", alpha=0.4)
plt.show()

