import numpy as np
from django import forms


FEATURE_NAMES = np.load('logic/feature_names.npy')
BUILDER_NAMES = np.load('logic/builder_names.npy')
AVERAGES = np.load('logic/averages.npy').reshape(-1)[0]  # 'cause of numpy

MIN_DICT = np.load('logic/min_dict.npy').reshape(-1)[0]  # 'cause of numpy
MAX_DICT = np.load('logic/max_dict.npy').reshape(-1)[0]  # 'cause of numpy


def make_hr(builder_name):

    if builder_name == 'None':
        return 'Other'

    return builder_name.title()


class EstimateBoatForm(forms.Form):

    CHOICES = ((b, make_hr(b)) for b in BUILDER_NAMES)

    def __init__(self, *args, **kwargs):

        super(EstimateBoatForm, self).__init__(*args, **kwargs)

        for feature_name in FEATURE_NAMES:
            if not self.fields.get(feature_name, None):

                min = MIN_DICT[feature_name]
                max = MAX_DICT[feature_name]

                help_text = 'Range: {} to {}'.format(min, max)

                self.fields[feature_name] = forms.FloatField(
                    required=False,
                    help_text=help_text)

    def clean(self):

        for feature_name in FEATURE_NAMES:

            if not self.cleaned_data.get(feature_name, None):
                avg = AVERAGES[feature_name]
                self.cleaned_data[feature_name] = avg

            else:
                val = self.cleaned_data[feature_name]
                min = MIN_DICT[feature_name]
                max = MAX_DICT[feature_name]

                if val < min or val > max:
                    msg = 'Value must be in range '
                    msg += '[{}, {}]'.format(min, max)
                    self.add_error(feature_name, msg)

        return self.cleaned_data

    builder = forms.ChoiceField(choices=CHOICES)
