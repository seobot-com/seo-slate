#!/bin/bash
sudo apt install ruby ruby-dev build-essential libffi-dev zlib1g-dev liblzma-dev nodejs patch
sudo gem update --system
sudo gem install bundler
sudo bundle install

bundle exec middleman server
