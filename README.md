# Espresso Notes

Espresso Notes aims to be a Notes taking application targeted for STEM students.
Custom made blocks for content will enable out of the box styling and guidelines for generated notes documents.
These generated documents will initially have support for HTML and LaTeX source formats.

The HTML documents are intended to be a standalone system, able to be viewed on the host machine.
LaTeX source files will need to be compiled elsewhere by the user.


## Weekly Reports

- [Week 3](reports/week1.md)
- [Week 4](reports/week2.md)
- [Week 5](reports/week5.md)
- [Week 6](reports/week6.md)
- [Week 7](reports/week7.md)


## Document Schemas

All application documents will utilize the JSON format with an appropriate [JSON Schema](https://json-schema.org/).

- [Schema Overview](docs/schemas.md)
- [Notes Document](docs/notesdoc.md)
- [Markdown Block](docs/markdownblock.md)
- [Code Block](docs/codeblock.md)
- [Notes Tag](docs/notestag.md)

These schemas are not finalized and subject to change as project continues.


## Document Compilers

All generated files of Espresso Notes will be passed into a compiler to be rendered into a supported output format.
Support is intended for static HTML files and LaTeX source files.

- [HTML Compiler](https://github.com/Espresso-Notes/NotesCompilerHTML)


## Espresso Notes Editor

Users will enjoy a featured Espresso Notes editor custom made to support our content blocks.
This Editor is built utilizing Electron, to make for an easily cross platform desktop app.
This achieves one of our core goals of making this an easy to use, offline application.

The latest editor version can be found [here](https://github.com/Espresso-Notes/espresso_notes_electron/tags).

Installation and usage manual to come at a later date.