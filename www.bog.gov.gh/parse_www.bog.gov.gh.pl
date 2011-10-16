#!/usr/bin/perl -w

use strict;

open (DATA, "temp22") || die;

my ($currRow, $sp1, $name, $sp2, $type, $sp3, $city, $sp4, $address, $sp5, $contact);
my ($nameStart, $typeStart, $cityStart, $addressStart, $contactStart);
my $line;
print join("\t", "name", "type", "city", "address", "contact") . "\n";
while ($line=<DATA>) {
 #   print "$line\n";
    $line =~ s/\r//g;
    $line =~ s/[\r\14]//g;
    last if $line =~ /^\s+SUMMARY OF NBFI/;
    next if $line =~ /^\s+[A-Z\ ]+\s+$/;
    $line =~ s/, Tel/,  Tel/g;
    $line =~ s/Off Tel/Off  Tel/g;
    $line =~ s/ Finance House  /  Finance House  /g;

    if ($line =~ /^(\d+)(\s\s+)(\S.+\S)(\s\s+)(\S.+\S)(\s\s+)(\S.+\S)(\s\s+)(\S.+\S)(\s\s+)(\S.+\S)\s+$/) { 
	process_entry($name, $type, $city, $address, $contact) if $name;   
#	print join("\t", $name, $type, $city, $address, $contact) . "\n" if $name;  #print previous entry (if it exists)
	
	($currRow, $sp1, $name, $sp2, $type, $sp3, $city, $sp4, $address, $sp5, $contact) = ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11);
	$nameStart = length($currRow) + length($sp1);
	$typeStart = $nameStart + length($name) + length($sp2);
	$cityStart = $typeStart + length($type) + length($sp3);
	$addressStart = $cityStart + length($city) + length($sp4);
	$contactStart = $addressStart + length($address) + length($sp5);

	$currRow++;
    }
    elsif ($currRow) {  #add extra text belonging to this block
#	print "2:$line\n";

	my $currPos=0;
	my $fullLength=length($line);
	while ($line =~ m/(\s\s+)(.+)/g) {
	    $currPos += length($1);
	    my $token = $2;
	    $token =~ s/\s\s+.+//g;

	    $line =~ s/\s+$token//g;
#	    print "<$token>\t$currPos\n";

	    #print join("\t", $nameStart, $typeStart, $cityStart, $addressStart, $contactStart, "curr:$currPos", "token:<$token>") . "\n";
	    if    ($currPos >= $nameStart-2 && $currPos <= $nameStart+2)       { $name .= " $token"; }
	    elsif ($currPos >= $typeStart-2 && $currPos <= $typeStart+2)       { $type .= " $token"; }
	    elsif ($currPos >= $cityStart-2 && $currPos <= $cityStart+2)       { $city .= " $token"; }
	    elsif ($currPos >= $addressStart-2 && $currPos <= $addressStart+2) { $address .= " $token"; }
	    elsif ($currPos >= $contactStart-2 && $currPos <= $contactStart+2) { $contact .= " $token"; }
	    else { warn "????<$currPos> <$token>\n"; }
	    $currPos += length($token)+1;
	}
    }
}
process_entry($name, $type, $city, $address, $contact);

sub process_entry {
    my ($name, $type, $city, $address, $contact) = @_;

    if (0) { 
    my $tel="";
    my $web="";
    my $fax="";
    my $email="";
    if    ($address =~ /(tel[:;][\s\-\d\.]+)/i)     { $tel = $1; $address =~ s/$tel//g; }
    if ($address =~ /(website[:;]\s[a-z\.]+)/) { $web = $1; $address =~ s/$web//g; }
    if ($address =~ /(fax[:;][\s\d\-]+)/)      { $fax = $1; $address =~ s/$fax//g; }
    if ($address =~ /(email[:;]\s*\S+\@\S+)/)  { $email = $1; $address =~ s/$email//g; }

    if    ($contact =~ /(tel[;:][\s\-\d\.]+)/i)  { $tel .= $1; $contact =~ s/$tel//g; }
    if ($contact =~ /(website[:;]\s[a-z\.]+)/) { $web .= $1; $contact =~ s/$web//g; }
    if ($contact =~ /(fax[:;][\s\d\-\.]+)/)      { $fax .= $1; $contact =~ s/$fax//g; }
    if ($contact =~ /(email[:;]\s*\S+\@\S+)/)  { $email .= $1; $contact =~ s/$email//g; }

    if ($tel) { $tel =~ s/^\s+//g;  $tel =~ s/\s+tel://gi; }
    if ($web) { $web =~ s/^\s+//g;  $web =~ s/\s+website://gi; }
    if ($fax) { $fax =~ s/^\s+//g;  $fax =~ s/\s+fax://gi; }
    if ($email) { $email =~ s/^\s+//g; $email =~ s/\s+email://gi; }
    print join("\t", $name, $type, $city, $address, $contact, $tel, $web, $fax, $email) . "\n";
    }

    print join("\t", $name, $type, $city, $address, $contact) . "\n";
}
