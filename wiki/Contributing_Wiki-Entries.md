This project has a special build process for the wiki.
In the project you find a folder called `wiki`.
This folder contains wiki pages and the `options.json` file.
This file contains configurations for the generated sidebar.
On each build process of the master, travis will run the file `wiki_deployment.sh`.

This script copies all wiki entries into the git of the GitHub wiki and builds the sidebar using the [GitHub Wiki Sidebar](https://github.com/adriantanasa/github-wiki-sidebar).
To ensure this build works successfully you need to follow some guidelines.

* only add files to the `wiki` folder, that are supported by the GitHub-Wiki
* If you want to make a subsection, prepend the name of the parent section followed by an underscore (e.g. parent section `Setup.md` &rarr; subsection `Setup_Remote-Interpreter.md`)
* `-` in the file name will be translated into spaces
* If you add a file, make sure to also update the order of the files in the `options.json` file. Therefore you just need to insert your filename at the correct location.
* don't write wiki entries directly on the GitHub website, these will be deleted on the next build process