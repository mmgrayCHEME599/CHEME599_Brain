# -*- coding: utf-8 -*-
"""butterworth_filter

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10hBZydW61SnPzlAHlGY5KqfFRmV0aQ7x
"""

def butterwoth_filter(im, order, D0, hipass):

  ''' Performs butterworth filtering of an image in the frequency domain 
      

    Parameters
    ----------
    im : a grayscale image
        color images should be converted using rgb2gray
    order : the order of butterworth filter to use
    D0: cutoff frequency
    hipass: (0 or 1) whether to use highpass (1) or lowpass (0) butterworth filter

    Returns
    -------
    imB
        an ubyte image that represents `im` filtered in the frequency domain
        using butterword filter as defined by parameters
    A comparison plot of the original `im` and filtered `imB` images
      
    Notes
    -----
      Is dependent on frequency_filter function

    Examples
    --------
    #filter grayscale cameraman image
    from skimage import data
    im=data.camera() # load cameraman image
    imB=butterwoth_filter(im, 2, 10, 0) # perform second order lowpass 
    filtering with cutoff frequency 10Hz 
    with kernel width 1/2 image
  

    #frequency filter color image 
    from skimage import data, color
    im=sk.data.chelsea()
    im=sk.color.rgb2gray(im) 
    imB=butterwoth_filter(im, 2, 10, 0)# perform second order lowpass 
    filtering with cutoff frequency 10Hz 
    with kernel width 1/4 image
  '''


  
  n, D0= order, D0
  # initialize the filter
  xi=np.linspace(0,im.shape[1]-1,im.shape[1])
  yi=np.linspace(0,im.shape[0]-1,im.shape[0])
  x,y=np.meshgrid(xi,yi) # need to make sure filter is same shape as image

  #define the filter
  D=np.sqrt((x-im.shape[1]/2)**2+(y-im.shape[0]/2)**2)
  if hipass==0:
    bfilt=1-1/(1+(D/D0)**(2*n))
  else:
    bfilt=1/(1+(D/D0)**(2*n))
  
  imB=frequency_filter(im, bfilt) #perform filter

  #visualize
  fig, ax = plt.subplots(ncols=2, figsize=(10, 10))
  ax[0].imshow(im, cmap='gray')
  ax[0].set_title('Original Image')
  ax[0].axis('off')
  ax[1].imshow(imB, cmap='gray')
  ax[1].set_title('Butterworth Filtered Image')
  ax[1].axis('off')

  return imB