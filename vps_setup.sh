#!/usr/bin/bash

LINUX_DISTRO=`cat /etc/os-release | awk -F= '/^ID=/ { print $2 }'`

print_welcome() {
	printf ' ██▒   █▓ ██▓███    ██████      ██████ ▓█████▄▄▄█████▓ █    ██  ██▓███\n'
      	printf '▓██░   █▒▓██░  ██▒▒██    ▒    ▒██    ▒ ▓█   ▀▓  ██▒ ▓▒ ██  ▓██▒▓██░  ██▒\n'
	printf ' ▓██  █▒░▓██░ ██▓▒░ ▓██▄      ░ ▓██▄   ▒███  ▒ ▓██░ ▒░▓██  ▒██░▓██░ ██▓▒\n'
	printf '  ▒██ █░░▒██▄█▓▒ ▒  ▒   ██▒     ▒   ██▒▒▓█  ▄░ ▓██▓ ░ ▓▓█  ░██░▒██▄█▓▒ ▒\n'
	printf '   ▒▀█░  ▒██▒ ░  ░▒██████▒▒   ▒██████▒▒░▒████▒ ▒██▒ ░ ▒▒█████▓ ▒██▒ ░  ░\n'
	printf '   ░ ▐░  ▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░   ▒ ▒▓▒ ▒ ░░░ ▒░ ░ ▒ ░░   ░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░\n'
	printf '   ░ ░░  ░▒ ░     ░ ░▒  ░ ░   ░ ░▒  ░ ░ ░ ░  ░   ░    ░░▒░ ░ ░ ░▒ ░     \n'
	printf '     ░░  ░░       ░  ░  ░     ░  ░  ░     ░    ░       ░░░ ░ ░ ░░       \n'
	printf '      ░                 ░           ░     ░  ░           ░              \n'
	printf '     ░                                                                  \n'
	printf '\n'
}

main() {
	SECONDS=0

	clear
	print_welcome
	read -t 3 -p "Starting proccess of setup your Linux ..."
	printf '\n'
	
	if [ $LINUX_DISTRO == 'ubuntu' ];
	then

		sudo apt-get update && sudo apt upgrade -y
		sudo apt install software-properties-common -y
		sudo add-apt-repository ppa:deadsnakes/ppa -y
		sudo apt-get install -y vim tmux htop git curl wget unzip zip gcc build-essential make nginx postgresql postgresql-contrib python3.10 python3.10-dev python3.10-venv libpq-dev python3-pip
		sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" ----keep-zshrc
		sudo localedef uk_UA.UTF-8 -i uk_UA -fUTF-8;export LANGUAGE=uk_UA.UTF-8;export LANG=uk_UA.UTF-8;export LC_ALL=uk_UA.UTF-8 ;sudo locale-gen uk_UA.UTF-8 ;sudo dpkg-reconfigure locales
		sudo echo '\nexport LANGUAGE=uk_UA.UTF-8\nexport LANG=uk_UA.UTF-8\nexport LC_ALL=uk_UA.UTF-8' >> /etc/profile
		sudo systemctl start postgresql.service; sudo systemctl enable postgresql
		sudo systemctl start nginx; sudo systemctl enable nginx

		echo '\nalias zshconfig="vim ~/.zshrc"\nalias ohmyzsh="mate ~/.oh-my-zsh"\nalias cp="cp -i"\nalias df='df -h'\nalias free='free -m'\nalias np='nano -w PKGBUILD'\nalias more=less\nalias upd='sudo apt update;sudo apt upgrade -y'\nalias ll='ls -all'\nalias ls='ls --color=auto'\nalias ..='cd ..'\nalias ...='cd ../../../'\nalias ....='cd ../../../../'\nalias .....='cd ../../../../'\nalias .4='cd ../../../../'\nalias .5='cd ../../../../..'\nalias bc='bc -l'\nalias ping='ping -c 5'\nalias ports='netstat -tulanp'\nalias psmem='ps auxf | sort -nr -k 4'\nalias psmem10='ps auxf | sort -nr -k 4 | head -10'\nalias pscpu='ps auxf | sort -nr -k 3'\nalias pscpu10='ps auxf | sort -nr -k 3 | head -10'\nalias rsync='rsync --progress -avrxH  --delete'\nalias ip='curl 2ip.ua'\n' >> ~/.zshrc; source ~/.zshrc
	
	elif [ $LINUX_DISTRO == 'manjaro' ];
	then
		printf 'Manjaro\n'
	else
		printf "This script valid only for Ubuntu"
	fi

	#clear
	duration=$SECONDS
	printf 'Setup is finished! '
	printf "$(($duration / 60)) min. $(($duration % 60)) sec. elapsed.\n"
	
}

main
