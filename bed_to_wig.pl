#!/usr/bin/perl
use strict;
use warnings;

my $bed_file=shift;

open(my $fh,$bed_file);

while(<$fh>){
    chomp;
    my @cols=split;
    for(my $pos=$cols[1];$pos<=$cols[2];$pos++){
        print "$cols[0]\t$pos\t$pos\t1\n";
    }
}
