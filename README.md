# Espresso Notes

Espresso Notes aims to be a Notes taking application targeted for STEM students.
Custom made blocks for content will enable out of the box styling and guidelines for generated notes documents.


## Weekly Reports

- [Week 2](reports/week1.md)
- [Week 3](reports/week2.md)
- [Week 5](reports/week5.md)


## Document Schemas

All application documents will utilize the JSON format with an appropriate [JSON Schema](https://json-schema.org/).

- [Notes Document](docs/notesdoc.md)
- [Markdown Block](docs/markdownblock.md)
- [Code Block](docs/codeblock.md)
- [Notes Tag](docs/notestag.md)

These schemas are not finalized and subject to change as project continues.


## Document Compilers

All generated files of Espresso Notes will be passed into a compiler to be rendered into a supported output format.
Support is intended for static HTML files and LaTeX source files.

- [HTML Compiler](https://github.com/Espresso-Notes/NotesCompilerHTML)