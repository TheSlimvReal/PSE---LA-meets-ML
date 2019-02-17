#!/usr/bin/env bash
set -e
npm install -g github-wiki-sidebar
mkdir wiki_tmp
cd wiki_tmp
git clone https://github.com/TheSlimvReal/PSE---LA-meets-ML.wiki.git
cd PSE---LA-meets-ML.wiki
rm -rf *
git config push.defaul simple
git config user.name "Wiki Deployment"
git config user.email "Wiki-Deployment@bot.com"
cp ../../wiki/* .
github-wiki-sidebar --silent
git add wiki_tmp/
git commit -m "Deploy wiki with commit: ${TRAVIS_COMMIT}"
git push --force "https://${GH_REPO_TOKEN}@github.com/TheSlimvReal/PSE---LA-meets-ML.wiki.git"
