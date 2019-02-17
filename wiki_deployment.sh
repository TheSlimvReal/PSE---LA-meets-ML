#!/usr/bin/env bash
set -e
npm install -g  github-wiki-sidebar
mkdir wiki_files
cd wiki_files
git clone https://github.com/TheSlimvReal/PSE---LA-meets-ML.wiki.git
cd PSE---LA-meets-ML.wiki
rm -rf *
git config push.defaul simple
git config user.name "Wiki Deployment"
git config user.email "Wiki-Deployment@bot.com"
cp ../../wiki/* .

git add --all
git commit -m "Deploy wiki with commit: ${TRAVIS_COMMIT}"
git push --force "https://${GH_REPO_TOKEN}@github.com/TheSlimvReal/PSE---LA-meets-ML.wiki.git"
github-wiki-sidebar --git-push --silent