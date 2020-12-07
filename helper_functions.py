import numpy as np
from sklearn.decomposition import PCA
from math import ceil
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import itertools

def get_label(array):
    """
    Returns String Label of Class
    """
    if array[0] ==1:
        return 'MildDemented'
    elif array[1] ==1:
        return 'ModerateDemented'
    elif array[2] ==1:
        return 'NonDemented'
    elif array[3] ==1:
        return 'VeryMildDemented'

def find_mean_img(full_mat, ax, title, size = (224, 224)):
    """
    Returns mean images given array of images
    """
    # calculate the average
    mean_img = np.mean(full_mat, axis = 0)
    # reshape it back to a matrix
    #mean_img = mean_img.reshape(size)
    ax.imshow(mean_img, vmin=0, vmax=255, cmap='Greys_r')
    ax.set_title(f'Average {title}')
    ax.axis('off')
    return mean_img

def find_std_img(full_mat, ax, title, size = (224, 224)):
    """
    Returns the standard deviation of images given array of images
    """
    # calculate the average
    std_img = np.std(full_mat, axis = 0)
    # reshape it back to a matrix
    #mean_img = mean_img.reshape(size)
    ax.imshow(std_img, vmin=0, vmax=255, cmap='Greys_r')
    ax.set_title(f'Standard Dev {title}')
    ax.axis('off')
    return std_img

def eigenimages(full_mat, title, n_comp = 0.7):
    """
    Performs Principal Component Analysis
    """
    # fit PCA to describe n_comp * variability in the class
    size = (full_mat.shape[0],(224*224*3))
    array = np.reshape(full_mat, size)
    pca = PCA(n_components = n_comp, whiten = True)
    pca.fit(array)
    print('Number of PC: ', pca.n_components_)
    return pca

def plot_pca(pca):
    """
    plot eigenimages in a grid from a pca
    """
    n = pca.n_components_
    fig = plt.figure(figsize=(30, 10))
    r = int(n**.5)
    c = ceil(n/ r)
    for i in range(n):
        ax = fig.add_subplot(r, c, i + 1, xticks = [], yticks = [])
        ax.imshow(pca.components_[i].reshape(224,224*3), 
                  cmap='viridis')
    plt.axis('off')
    plt.show()

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion Matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=90)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')