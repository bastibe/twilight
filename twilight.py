from matplotlib.colors import LinearSegmentedColormap

"""Circular colormap for white-blue-black-red-white.

The colors begin with off-white, ranges through blue to off-black,
then to red and back to off-white. Perceptual lightness contrast and
color contrast are uniform over the whole value range. The colormap
prints as perfect white-black-white, and works equally well with color
blindness.

"""

__all__ = ['twilight', 'sunlight']

cm_data = [[ 0.94398606,  0.92379568,  0.95378996],
           [ 0.85892107,  0.86872657,  0.88695835],
           [ 0.77269523,  0.81634245,  0.83579016],
           [ 0.68533652,  0.76613997,  0.79772199],
           [ 0.60236827,  0.71573565,  0.77098912],
           [ 0.5274876 ,  0.66399818,  0.75223302],
           [ 0.46359466,  0.61032341,  0.73828579],
           [ 0.41370521,  0.55419069,  0.72601024],
           [ 0.37983056,  0.49526679,  0.7117918 ],
           [ 0.36081731,  0.43368071,  0.69150687],
           [ 0.35152678,  0.37030575,  0.66086667],
           [ 0.3445333 ,  0.30701653,  0.61602877],
           [ 0.33265951,  0.24679286,  0.55464881],
           [ 0.31070656,  0.19315868,  0.47748529],
           [ 0.27638729,  0.14834521,  0.3896227 ],
           [ 0.23050045,  0.11117814,  0.29911839],
           [ 0.17580591,  0.07748523,  0.21275973],
           [ 0.11491149,  0.04258091,  0.13280069],
           [ 0.18656241,  0.07511247,  0.18347702],
           [ 0.25991705,  0.10194022,  0.22785959],
           [ 0.33525555,  0.12498945,  0.26461781],
           [ 0.41174556,  0.14684434,  0.29138527],
           [ 0.48682898,  0.1721968 ,  0.30589243],
           [ 0.55587942,  0.20747459,  0.30945052],
           [ 0.61462227,  0.25585313,  0.30990235],
           [ 0.66220035,  0.31464171,  0.31675699],
           [ 0.69991239,  0.37982659,  0.3360442 ],
           [ 0.72935439,  0.44867407,  0.3709017 ],
           [ 0.7523454 ,  0.51935505,  0.42268891],
           [ 0.77148669,  0.59036483,  0.49107153],
           [ 0.79050926,  0.66038803,  0.57386822],
           [ 0.81391727,  0.72850756,  0.66721417],
           [ 0.84574284,  0.79454985,  0.76622981],
           [ 0.8870694 ,  0.85986781,  0.86433525],
           [ 0.94398606,  0.92379568,  0.95378996]]

twilight = LinearSegmentedColormap.from_list('twilight', cm_data)
sunlight = LinearSegmentedColormap.from_list('sunlight', [*cm_data[len(cm_data)//2:],
                                                          *cm_data[:len(cm_data)//2]])

# for viscm:
test_cm = twilight

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    try:
        from pycam02ucs.cm.viscm import viscm
        viscm(test_cm)
    except ImportError:
        print("pycam02ucs not found, falling back on simple display")
        plt.imshow(np.linspace(0, 100, 256)[None, :], aspect='auto',
                   cmap=test_cm)
    plt.show()
