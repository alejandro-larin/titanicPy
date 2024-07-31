# TitanicPy Project

This is a project created in the Python language, its purpose is to use the functionality of translating the content of the HTML tags into the 3 main Funiber languages.

## Libraries

- deep_translator
- pyperclip

## Use

install the dependences:

`pip i deep_translator, pyperclip`

To use it, it is necessary to change the desired content in the `html_content` variable located in the `main.py` file.

## Features

Here I will talk about the `utils` folder, it has two files `copyFunction.py` and `translator.py`:

### Translator

It collects as parameters the language and the html content where it will go through and translate the content, returning a `string` which would be the html that is completely translated.

### CopyFunction

It collects a string as a parameter whose only usefulness would be to copy it to our clipboard.
