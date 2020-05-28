#!/usr/bin/perl -w
use strict;

my @array_name = qw /Cflo Csol Dall Fari Mcin Mdem Nvit Oabi Tpre/ ;
my %hash_a;

opendir DIR, "group_trimal" or die "Can't open dir!";
while (my $file = readdir DIR) {
	next if $file=~/^\./;
	open File, "group_trimal/".$file or die "Can't open file!";
	my %hash;
	my $id;
	while (<File>) {
		chomp();
		if (/^>(\S+)\|.*$/) {
			$id = $1;
		} else {
			$hash{$id} .= $_;
		}
	}
	foreach (@array_name) {
		$hash_a{$_} .=$hash{$_}; 
	}
}
closedir DIR;

foreach (@array_name) {
	print ">".$_."\n".$hash_a{$_}."\n";
}