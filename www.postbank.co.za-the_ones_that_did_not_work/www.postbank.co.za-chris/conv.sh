#!/bin/sh

cat in.html | sed -e 's:</option>::' | sed -e 's:>: :' | sed -e 's:"::g' | sed -e 's:.*=::'> countries.txt

get_contacts.pl < countries.txt

