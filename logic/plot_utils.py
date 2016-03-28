from django.conf import settings

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def plot_distributions(x, y):
    
    num_bins = 50
    file_names = []

    print('y = {}'.format(y))

    for i in range(0, 1):

        n, bins, patches = plt.hist(y, num_bins, alpha=0.5)
        plt.plot()
    
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(r'Histogram')
    
        plt.subplots_adjust(left=0.15)
    
        file_name = 'img/histogram_{}.png'.format(i)
        file_path = '{}/{}'.format(settings.MEDIA_ROOT, file_name)

        print(' --- Saving pic to {}'.format(file_path))
        plt.savefig(file_path)
        file_names.append(file_name)
    
    return file_names
    
