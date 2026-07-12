#!/bin/zsh

source "$HOME/.zshrc"
conda activate eeg_rv || exit 1
exec python "/Users/denisemunchen/Documents/EEG_RV/python/test_lsl_sender.py"
