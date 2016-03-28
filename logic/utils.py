import numpy as np


FEATURE_NAMES = np.load('logic/feature_names.npy')
BUILDER_NAMES = np.load('logic/builder_names.npy')
NET_WEIGHTS = np.load('logic/weights_val_min.npy')

MIN_DICT = np.load('logic/min_dict.npy').reshape(-1)[0]  # 'cause of numpy
MAX_DICT = np.load('logic/max_dict.npy').reshape(-1)[0]  # 'cause of numpy

R = 20
S1 = 35
S2 = 1

w1_cnt = S1 * R
b1_cnt = S1
w2_cnt = S2 * S1
b2_cnt = S2

w1b1_cnt = w1_cnt + b1_cnt
w1b1w2_cnt = w1b1_cnt + w2_cnt
w1b1w2b2_cnt = w1b1w2_cnt + b2_cnt

W1 = NET_WEIGHTS[0:w1_cnt].reshape((S1, R))
b1vec = NET_WEIGHTS[w1_cnt:w1b1_cnt].reshape((S1, 1))
W2 = NET_WEIGHTS[w1b1_cnt:w1b1w2_cnt].reshape((S2, S1))
b2vec = NET_WEIGHTS[w1b1w2_cnt:w1b1w2b2_cnt].reshape((S2, 1))

# S1 = 35
# Training set size:   1110
# Validation set size: 248
# Test set size: 215


def logsig(x):
    return 1. / (1. + np.exp(-x))


def net_response(P):

    N1 = np.dot(W1, P) + b1vec
    A1 = logsig(N1)
    N2 = np.dot(W2, A1) + b2vec

    return N2


def map_to_min1_plus1(val, min, max):

    """
    This function maps the value "val",
    assumed to be on [min, max], onto [-1, 1].
    """

    return -1. + 2. * (val - min) / (max - min)


def form_data_to_net_input(x):

    """
    This function takes the values in x and transforms
    them to [-1, 1].
    """

    feature_names = list(FEATURE_NAMES)
    net_input = np.zeros(x.shape)
    for feature_name in feature_names:

        val = x[feature_names.index(feature_name)]
        min = MIN_DICT[feature_name]
        max = MAX_DICT[feature_name]
        net_input[feature_names.index(feature_name)] = map_to_min1_plus1(
            val,
            min,
            max)

    return net_input


def net_output_to_euros(y):

    """
    This function takes the net output and transforms it
    back to an asking price in euros.
    """

    min = MIN_DICT['asking_price_euros']
    max = MAX_DICT['asking_price_euros']

    ln_eur = 0.5 * (y[0, 0] + 1.) * (max - min) + min
    return np.exp(ln_eur)


def estimate_asking_price_euro(form):

    f_names = list(FEATURE_NAMES)
    b_names = list(BUILDER_NAMES)

    x = np.zeros((len(f_names)+len(b_names), 1))

    for f_name in f_names:
        x[f_names.index(f_name)] = form.cleaned_data[f_name]

    x[len(f_names) + b_names.index(form.cleaned_data['builder'])] = 1.

    x = form_data_to_net_input(x)

    return net_output_to_euros(net_response(x))
