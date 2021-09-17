#!/bin/bash
echo "Deploying..."
echo -e "========================\n"

echo "-> Fetching latest tags..."
git fetch --tags;

git config --global advice.detachedHead false;
if [ -z "$1" ]
then
    latesttag=$(git describe --tags)
    echo checking out ${latesttag}
    git checkout ${latesttag}
    echo -e "-> Finished\n"
else
    git checkout $1;
    echo -e "-> Finished\n"
fi
git config --global advice.detachedHead true

echo "-> Installing requirements..."
sudo apt install ruby ruby-dev build-essential libffi-dev zlib1g-dev liblzma-dev nodejs patch
sudo gem update --system
sudo gem install bundler
sudo bundle install
echo -e "-> Finished\n"

echo "-> Building..."
bundle exec middleman server
echo -e "-> Finished\n"

echo "========================"
echo "Deploy finished"