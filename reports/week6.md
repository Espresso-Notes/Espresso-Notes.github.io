# Week 6

## Project Structure

### Robert

I spent this week exploring the general project structure when installed on client machines.
This has resulted in an initial directory structure and needed files to support the project.
The top level directory will contain the application, its compilers, and standard .
Each user created project or topic will be structured into a Notebook.
These Notesbooks will contain source files, template files, and output files.
Each output directory will be related to the specific compiler being used, for example the HTML compiler.
The compilers will output their generated documents to here for usage, along with any related files such as CSS files.

An example directory might be:

📦espressonotes

 ┣ 📂notebooks

 ┃ ┣ 📂notebook1

 ┃ ┃ ┣ 📂notes

 ┃ ┃ ┣ 📂out

 ┃ ┃ ┃ ┣ 📂html

 ┃ ┃ ┃ ┃ ┣ 📂css

 ┃ ┃ ┃ ┃ ┃ ┣ 📜clang.css

 ┃ ┃ ┃ ┃ ┃ ┣ 📜markdown.css

 ┃ ┃ ┃ ┃ ┃ ┗ 📜python.css

 ┃ ┃ ┃ ┃ ┗ 📜index.html

 ┃ ┃ ┃ ┗ 📂latex

 ┃ ┃ ┗ 📂templates

 ┃ ┗ 📂notebook2

 ┣ 📜app.exe
 
 ┗ 📜settings.json

## HTML Compiler

### Robert

Work on integrating the Jinja2 engine has begun.
This has revealed a distinct lack of experience with HTML and CSS files.
As a large part of this project is reliant on this compiler specifically, having a solid template base is important.

On the topic of Templates, these will be designed in such a way that users can modify them for their own usage.
There will be a standard set that comes bundled with the 

Work on the Project Structure discussed above has revealed a need for more complex management of the output generated.
The first observation is that Notebooks can contain multiple related Notes documents.
These should be linked together through a project index page, which will get its own generation.
The second observation is that there are a lot of static files that will be copied from the base installation into the specific notebook and output directory.
These static files include templates and CSS files, as examples.

On the topic of CSS files, there will be several that are needed.
For example, there would potentially be one for each of the different languages that are supported.
We are already utilized the same CSS definitions for Markdown that GitHub uses.
These will be extended as necessary for the project, and built in such a way that users can customize them.

## Notes Editor

### Emily

This week, I worked on functions in the text editor.
Now, from the editor, we are able to open the file directory and browse files.
We plan to move on with developing the functions initially stated in the design document.
Currently, we would like to make it so that when the user creates pages, it resembles working in a notebook more as opposed to a Word document.
In the works is the tagging system.
The functional goals for it are to have a directory of tags, for the tags to lead to the designated pages, and for key words and definitions to be highlighted in text.

