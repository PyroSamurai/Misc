#!/usr/bin/sh

sudo apt-get install -y uncrustify

mkdir -p ~/.local/share/gedit/plugins

cp -R ./uncrustify ~/.local/share/gedit/plugins

echo "\nGedit Uncrustify Plugin installation complete!"
