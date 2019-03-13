#!/usr/bin/env bash
# install the GitHub Wiki Sidebar (https://github.com/adriantanasa/github-wiki-sidebar)
npm install -g github-wiki-sidebar
mkdir wiki_tmp
cd wiki_tmp
# clone the wiki's git
git clone https://github.com/TheSlimvReal/PSE---LA-meets-ML.wiki.git
cd PSE---LA-meets-ML.wiki
# remove all old entries
rm -rf *
# makes the automated push process simpler
git config push.defaul simple
# pretend to be a user called `Wiki Deployment`
git config user.name "Wiki Deployment"
git config user.email "Wiki-Deployment@bot.com"
# copy all files from the wiki folder into the cloned wiki git
cp ../../wiki/* .
# build the sidebar using the options.json
github-wiki-sidebar --silent
# commit and push changes of the wiki
git add .
# the environment variable TRAVIS_COMMIT will be available during runtime on the travis build
git commit -m "Deploy wiki with commit: ${TRAVIS_COMMIT}"
# the GH_REPO_TOKEN will also be available during runtime and grants the permissions to push on the git repo
git push --force "https://${GH_REPO_TOKEN}@github.com/TheSlimvReal/PSE---LA-meets-ML.wiki.git"
