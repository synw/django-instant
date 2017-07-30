#!/bin/bash

black='\E[30m'
red='\E[31m'
green='\E[32m'
yellow='\E[33m'
blue='\e[36m'
magenta='\E[35m'
cyan='\E[36m'
white='\E[37m'
normal='\e[0m'
bold='\e[1m'

title() {
		val=$1$bold$2$normal
		val+=' '
		val+=$3
		echo -e $val
	}

ok() {
		val='[ '$1$bold'Ok'$normal' ] '$2
		echo -e $val
	}

option(	) {
	val='[ '$blue$bold'Option'$normal' ] '$1
	echo -e $val		
	}

check() {
	val='['$blue'x'$normal'] '$1
	echo -e $val		
	}

dot	( ) {
	val=$blue$bold'# '$normal$1
	echo -e $val		
	}

important 	( ) {
	val=$cyan$bold' Important '$normal': '$bold$white$1$normal
	echo -e $val		
	}

error 	( ) {
	val='['$red' Error '$normal'] '$1
	echo -e $val		
	}