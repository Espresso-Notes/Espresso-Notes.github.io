# Week 11 (4/1)

## Cody

This week was mostly spend transferring the existing code over to a slightly different framework called [electron-vite](https://electron-vite.org/). While this framework still maintains all the same functionality as the default version of Electron, it comes with a few important differences that are greatly helpful for the app we are building. The biggest of these differences are:
1. A pre-configured project structure, allowing for a more organized scaffolding of assets used for the project.
2. Built in support for TypeScript, allowing for more readable code, and ReactJS, a library specifically built for designing a pleasant front-end experience
3. Compatibility with many useful third-party plugins and libraries, some of which we make use of in our project.

While it was time consuming to essentially recreate the project with a slightly altered structure, it was worth it to create a more efficient foundation to continue from for the remainder of our work.

The same basic functionality that was previously present in our application has successfully been implemented in this new framework, and additionally, work has begun to create a user interface that appears much more modern and pleasant than the very primative layout we used previously. The implementation of this new UI has proved much easier using electron-vite.
