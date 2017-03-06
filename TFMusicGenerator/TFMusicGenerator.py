import numpy as np
import pandas as pd
import tensorflow as tf
from tqdm import tqdm # for progress bar during training
import rtmidi as midi_manipulation

# Hyperparameters

lowest_note = midi_manipulation.MidiIn(