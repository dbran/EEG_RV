#!/bin/zsh

source "$HOME/.zshrc"
conda activate eeg_rv || exit 1
exec python "/Users/denisemunchen/Documents/EEG_RV/python/bci_jsonl_to_unity_commands.py" "$@"
