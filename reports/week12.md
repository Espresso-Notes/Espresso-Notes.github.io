# Week 12 (4/8)

## Cody

This week, the full markdown support we were hoping to achieve has been implemented into the application. The markdown formatting that has been implemented includes the following:
- Bold, italic, and underlined text
- Differently sized headings
- External links
- Ordered and unordered lists
- Quote blocks
- Code blocks with support for code formatting
All of these types of formatting are able to be accessed through a toolbar on the interface or with keyboard shortcuts.

These features were able to be implemented thanks to a third-party component for ReactJS, [MDXEditor](https://mdxeditor.dev/). This component includes more streamlines methods for creating many of the features one would expect in a text editor, with basic functionality built in but an extreme freedom in allowing customization of its features.

MDXEditor has been used in tandem with [TailwindCSS](https://tailwindcss.com/), a library for CSS which makes creating and altering visual interfaces much quicker and more intuitive. Combining the power of these two, the editor has been able to be presented in a much more sleek way while also allowing necessary features to be created with less hassle.

Two features which were not able to be implemented with these tools are support for the LATEX language or optical character recognition allowing photographs to be converting into text. Although they have been more tricky to successfully implement, work will continue on finding other ways to make these features function within our current project framework.
