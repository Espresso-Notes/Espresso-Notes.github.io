# Week 7

## HTML Compiler

### Robert

I've managed to get compiling working with the Jinja2 templating engine.
This allows me to easily develop the templates for the various output files utilized.
An example of the current template file for Notes HTML documents can be found [here](week7/templates.md).

Alongside this came the development of a test environment.
This completely sets up a notebook environment with the currently discussed structure, as was detailed in a previous week.
It generates the test data and then compiles it.
Upcoming will be the inclusion of automated downloading of static files such as the templates and CSS files.

Upcoming work on the HTML Compiler for next two weeks:
- Update to the newest Notes Document Standard Schemas
- Add Validation of the Schemas
- Default Static Files added to Website for easy downloads
- Additions to Templates for Code, Latex content blocks

Having multiple files generated all from the same project now means that an index page tying them together must be developed.
This will be a fairly simple file, but work on the UI of it is upcoming.

After the rest of the content blocks are added and updated with support for default templates and CSS files, support for Notes Tags will be added.
These will require an expansion of the templating files to include a search feature for the content in that file.

#### Examples

3 test files were generated and rendered as HTML, which can be found below.

- Example: [JSON](week7/test_notes1.json) [HTML](week7/test_notes1.html)
- Example: [JSON](week7/test_notes2.json) [HTML](week7/test_notes2.html)
- Example: [JSON](week7/test_notes3.json) [HTML](week7/test_notes3.html) 