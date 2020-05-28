#!/usr/bin/perl -w
use strict;

#用法：perl 程序.pl all.fasta 1_1_1_group_sorted.txt
#读所有物种的序列；

my $genename;
my %hash_1;

open my $fasta1, "<", $ARGV[0] or die "Can't open file!";
while (<$fasta1>) {
	chomp();
	if (/^>(.*)$/){
		$genename = $1;
	} else {
		$hash_1{$genename} .= $_;
	}
}
close $fasta1;

#把group里面的基因名换成对应的序列，mafft比对，trimal取保守序列；
`mkdir group`; #新建一个文件夹。
`mkdir group_mafft`;
`mkdir group_trimal`;
open my $Group, "<", $ARGV[1] or die "Cant't open file!";
while (<$Group>) {
	chomp();
	my @array1 = split /\t/, $_;
	my $group_nogood = shift @array1;
	my @array2 = split /:/, $group_nogood;
	my $group = $array2[0];
	open OUT, ">","$group.fasta";
	foreach (@array1) {
		print OUT ">".$_."\n".$hash_1{$_}."\n";
	}
	close OUT;
	`mv $group.fasta group`;
	`mafft --auto group/$group.fasta >$group.mafft.fasta`;
	`mv $group.mafft.fasta group_mafft`;
	`trimal -in group_mafft/$group.mafft.fasta -out $group.trimal.fasta -automated1`;
	`mv $group.trimal.fasta group_trimal`;
}
close $Group;