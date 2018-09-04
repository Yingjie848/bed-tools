#!/usr/bin/perl
use strict;
use warnings;

if( @ARGV<2 ){
    print "more <bed file> | perl $0 <chr length> <flanking size>\n";
    exit;
}

my $chr_length=shift;
my $flank_size=shift;

my $href_chr_length=loadChr($chr_length);

while(<STDIN>){
    chomp;
    my ($chr,$start,$end)=split;
   
    my $newS=$start;
    my $newE=$end;

    if( $start > $end ){
        $newE=$start;
        $newS=$end;
    }

    $newS=$newS-$flank_size;
    $newE=$newE+$flank_size;

    if( $newS <= 0 ){
        $newS = 1;
    }

    if( $newE > $href_chr_length->{$chr} ){
        $newE = $href_chr_length->{$chr};
    }
    

    print "$chr\t$newS\t$newE\n";
}

sub loadChr{
    my $file=shift;
    my $href={};
    open(IN,$file);
    while(<IN>){
        chomp;
        my ($chr,$length)=split;
        $href->{$chr}=$length;
    }
    return $href;
}

