#!/usr/sh
# https://gist.github.com/vidavidorra/548ffbcdae99d752da02 for more information about this script
set -e

mkdir code_docs
cd code_docs

git clone -b gh-pages https://git@$GH_REPO_REF
cd $GH_REPO_NAME

git config --global push.defaul simple

git config user.name "Tavis CI"
git config user.email "travis@travis-ci.org"

rm -rf *

echo "" > .nojekyll

doxygen %DOXYFILE 2>%1 | tee doxygen.log

if [ -d "html" ] && [ -f "html/index.html" ]; then

    git add --all
    git commit -m "Deploy code docs to GitHub Pages Travis build: ${TRAVIS_BUILD_NUMBER}" -m "Commit: ${TRAVIS_COMMIT}"
    git push --force "https://{GH_REPO_TOKEN}@${GH_REPO_REF}" > /dev/null 2>&1

else

    echo '' >&2
    echo 'Warning: no documentation /html) files have been found!' >&2
    echo 'Warning: Not going to push the documentation to GitHub!' >&2
    exit 1

fi
