# Weekly Report 2/5/24

## HTML Compiler

Work has progressed on the HTML Compiler. 
Test data is currently being generated using the packages `faker` and `mdgen`.
Currently only Markdown content type is supported.

Here is an example of a generated file and its rendered HTML counterpart:

[Example JSON File](week2-example.json)

[Example HTML Content](week2-example.html)

Upcoming changes:

- Templating Engine
- Support for Code Blocks
- Support for LaTeX Blocks

## Editor

The beginning of the editor needs to be in raw mode to make the text editor due to preset keystroke functions. 
So far, the text editor portion sets up the program so that it can be a usable base for the functions of text editing.
The text editor subsystem can enter raw mode to begin establishing the text editor.

Upcoming changes:

- Viewing Text
- Editing Text from User
- Initializes Default Settings
