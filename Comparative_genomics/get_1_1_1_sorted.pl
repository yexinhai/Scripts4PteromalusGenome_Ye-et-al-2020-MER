#!/usr/bin/perl -w
use strict;
#usage: perl get_1_1_1_sorted.pl groups.txt
# Ye Xinhai, yexinhai@zju.edu.cn

my @array_name = qw /Acep Aech Amel Aros Bimp Cafl Cflo Ccin Cobs Csol Dall Fari Hsal Lhum Mcin Mdem Mrot Nvit Oabi Pbar Pdom Sinv Tcas Tpre/; #物种简称；


open my $group, "<", $ARGV[0] or die "Cannot find the file!";
open OUT1, ">", "numbers.txt";
while (<$group>) {
	chomp();
	my @array=split/\s+/,$_;
	my $group=shift @array;
	my @array_a;
	foreach (@array) {
		 my @a = split /\|/,$_;
		push @array_a, $a[0]; 
	}
	my %hash;
	foreach(@array_a){
		$hash{$_}=0 unless exists $hash{$_};
		$hash{$_}+=1;
	}
	my @out;
	foreach(@array_name){
		$hash{$_}=0 unless exists $hash{$_};
		push @out,$hash{$_};
	}
	my $result = join "\t", @out;
	print OUT1 $group."\t".$result."\n";	
}
close $group;
close OUT1;

my %hash;
open $group, "<", $ARGV[0] or die "Cannot find the file!";
while (<$group>) {
	chomp();
	if (/(Group\S+:)\s+(.*)/){
		$hash{$1} = $2;
	}
}
close $group;


my @out;
open my $numbers, "numbers.txt" or die "Can't open numbers.txt";
while (<$numbers>) {
	chomp();
	my @array = split /\t/, $_;
	my $group = shift @array;
	my $num = 0;
	for (my $i = 0; $i <= $#array; $i++) {
		if ($array[$i]==1){
			$num++;
		}
	}
	if ($num == 24) { #物种数目；
		push @out, $group;
	}
}
close $numbers;

open OUT2, ">", "1_1_1_group.txt";
foreach (@out) {
	print OUT2 "$_ $hash{$_}\n";
}
close OUT2;

open my $file, "1_1_1_group.txt" or die "Can't open 1_1_1_group.txt";
open OUT3, ">", "1_1_1_group_sorted.txt";
while (<$file>) {
	chomp();
	my @array = split /\s+/, $_;
	my $group = shift @array;
	my @array_sorted = sort @array;
	my $result = join "\t",@array_sorted;
	print OUT3 $group."\t".$result."\n";
}
close $file;
close OUT3;


