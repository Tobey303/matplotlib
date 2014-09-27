import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

def quad_bezier(ax, vertices, **kwargs):
    """
    Example function to plot quadratic bezier curves.

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    vertices : array
        The vertices for the bezier curves. Each quadratic curve requires 3 vertices

    **kwargs : dict
        Dictionary of kwargs to pass to matplotlib.patches.PathPatch
    """
    assert len(vertices) % 3 == 0, 'Vertex count must be multiple of 3 for quadratic bezier'
    # build code list.
    codes = []
    for idx, v in enumerate(vertices):
        if (idx % 3) == 0:
            codes.append(mpath.Path.MOVETO)
        else:
            codes.append(mpath.Path.CURVE3)
    my_path = mpath.Path(vertices, codes)
    #set default values
    kwargs["fc"]="none"
    kwargs["transform"]=ax.transData
    my_path_patch = mpatches.PathPatch(my_path,**kwargs)
    ax.add_patch(my_path_patch)


fig, ax = plt.subplots()
vertices = [(0.1, 0), (1, 0), (1, 0.5), (1, 0.5), (1,1), (0.1, 0.1)]

# Draw the quadratic bezier curves
quad_bezier(ax, vertices, edgecolor="blue", linestyle="solid")

# Plot the control lines
# Rearrange list of tuples [(x0,y0),(x1,y1),...] into tuple of lists ([x0,x1,..],[y0,y1,..])
line_coords = zip(*vertices)
ax.plot(line_coords[0][:3],line_coords[1][:3],"k:") # first curve
ax.plot(line_coords[0][3:],line_coords[1][3:],"k:") # second curve

#grow axis limits for better display
ax.set_xlim(-0.1,1.1)
ax.set_ylim(-0.1,1.1)
plt.show()


